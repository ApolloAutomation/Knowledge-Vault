#!/usr/bin/env python3
"""Lint the Apollo knowledge vault against _meta/schema.md."""
import re
import sys
from pathlib import Path

import yaml

VAULT = Path(__file__).resolve().parent.parent / "Apollo-Knowledge"
NOTE_DIRS = {
    "Products": "product", "Accessories": "accessory", "Components-Sensors": "component",
    "Setup": "guide", "Troubleshooting": "troubleshooting",
}
GUIDE_KEYS = ["title", "aliases", "type", "audience", "applies_to", "sources", "review_status", "last_verified"]
REVIEW_STATUSES = {"draft", "reviewed"}
URL = re.compile(r"https?://[^\s)>\]]+")

REQUIRED = {
    "product": ["title", "aliases", "type", "audience", "source", "status", "status_checked", "power_source", "last_verified"],
    "accessory": ["title", "aliases", "type", "audience", "source", "status", "status_checked", "last_verified"],
    "component": ["title", "aliases", "type", "audience", "used_in", "last_verified"],
    "guide": GUIDE_KEYS,
    "troubleshooting": GUIDE_KEYS,
}
SECTIONS = {
    "product": ["Description", "Features", "Specs", "Components", "Options and add-ons", "What's in the box", "Common questions and answers"],
    "accessory": ["Description", "Features", "Specs", "Compatible with", "What's in the box", "Common questions and answers"],
    "component": ["Description", "Used in", "Specs"],
    "guide": ["Summary", "Applies to", "Before you start", "Steps", "If it doesn't work", "Customer phrasings"],
    "troubleshooting": ["Summary", "Applies to", "Symptoms", "Quick checks", "Fix", "When to escalate", "Customer phrasings"],
}
DATASHEET = "Datasheet figures (chip manufacturer, not an Apollo rating)"
STATUSES = {"available", "preorder", "sold-out", "discontinued"}
POWER = {"usb-c", "battery", "poe", "mains", "dc", "wago", "host-board"}
AUDIENCES = {"customer", "internal"}
HEDGES = [
    r"not stated on site", r"per the site", r"site note", r"note on site", r"on the site",
    r"wording unclear", r"as high as tested", r"customer reviews", r"site says", r"the site",
]
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
VALUE_LINE = re.compile(r"^([A-Z][^:\n]{1,80}):\s*(.*)$")


def parse(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return yaml.safe_load(text[4:end]) or {}, text[end + 5:]


def as_date(v):
    return str(v) if v is not None else ""


def allowed_hosts():
    links = VAULT / "Links.md"
    if not links.exists():
        return None
    return {re.sub(r"^www\.", "", u.split("/")[2].lower()) for u in URL.findall(links.read_text(encoding="utf-8"))}


def url_allowed(url, hosts):
    host = re.sub(r"^www\.", "", url.split("/")[2].lower())
    return host in hosts


def lint_note(path, kind, names, errors, hosts=None):
    rel = path.relative_to(VAULT)
    err = lambda m: errors.append(f"{rel}: {m}")
    fm, body = parse(path)
    if fm is None:
        err("missing YAML frontmatter")
        return

    for key in REQUIRED[kind]:
        if key not in fm:
            err(f"frontmatter missing '{key}'")
    if fm.get("type") != kind:
        err(f"type should be '{kind}', got {fm.get('type')!r}")
    if fm.get("title") != path.stem:
        err(f"title {fm.get('title')!r} must equal filename '{path.stem}'")
    if not isinstance(fm.get("aliases", []), list):
        err("aliases must be a list")
    if fm.get("audience") not in AUDIENCES:
        err(f"audience must be one of {sorted(AUDIENCES)}")
    for key in ("last_verified", "status_checked"):
        if key in fm and not DATE.match(as_date(fm[key])):
            err(f"{key} must be YYYY-MM-DD")
    if "status" in fm and fm["status"] not in STATUSES:
        err(f"status must be one of {sorted(STATUSES)}")
    if kind == "product":
        ps = fm.get("power_source") or []
        if not isinstance(ps, list) or not ps or set(ps) - POWER:
            err(f"power_source must be a non-empty list from {sorted(POWER)}")
    if kind in ("guide", "troubleshooting"):
        if fm.get("review_status") not in REVIEW_STATUSES:
            err(f"review_status must be one of {sorted(REVIEW_STATUSES)}")
        for key in ("applies_to", "sources"):
            if not isinstance(fm.get(key), list) or not fm.get(key):
                err(f"{key} must be a non-empty list")
    if hosts is not None:
        for u in URL.findall(body) + [x for x in (fm.get("sources") or []) if isinstance(x, str)]:
            if not url_allowed(u, hosts):
                err(f"URL host not in Links.md allowlist: {u}")
    if kind == "component":
        if fm.get("sold_as_product") and "source" not in fm:
            err("sold_as_product requires source")
        used = fm.get("used_in") or []
        if not isinstance(used, list):
            err("used_in must be a list")

    lines = body.strip("\n").splitlines()
    if not lines or lines[0].strip() != f"# {path.stem}":
        err(f"body must start with '# {path.stem}'")

    headings = [l[3:].strip() for l in lines if l.startswith("## ")]
    expected = SECTIONS[kind]
    core = [h for h in headings if h != DATASHEET]
    if core != expected:
        err(f"sections {core} != expected {expected}")
    if DATASHEET in headings and kind != "component":
        err("datasheet section only allowed on components")

    low = body.lower()
    for h in HEDGES:
        if re.search(h, low):
            err(f"hedge/placeholder phrase found: '{h}'")
    for m in re.finditer(r"Unknown(?! — escalate to support)", body):
        line = body[: m.start()].count("\n") + 1
        ctx = body.splitlines()[line - 1]
        if re.match(r"^[^:]+:\s*Unknown", ctx):
            err(f"body line {line}: use 'Unknown — escalate to support'")

    for target in WIKILINK.findall(body + "\n" + str(fm.get("used_in", "")) + str(fm.get("applies_to", ""))):
        if target.strip() not in names:
            err(f"broken or wrong-case wikilink [[{target}]]")

    sections = split_sections(lines)
    if "Common questions and answers" in sections:
        qa = [l for l in sections["Common questions and answers"] if l.strip()]
        if qa and qa != ["_None yet._"] and not any(l.startswith("### ") for l in qa):
            err("Q&A entries must be '### <question>' headings")

    if kind == "product":
        specs = {}
        for l in sections.get("Specs", []):
            m = VALUE_LINE.match(l.lstrip("- "))
            if m:
                specs[m.group(1).strip().lower()] = m.group(2).strip()
        if "battery" not in (fm.get("power_source") or []):
            for key in ("battery life", "what battery works with it"):
                if key in specs and not specs[key].startswith("N/A"):
                    err(f"'{key}' must be N/A when power_source has no battery")


def split_sections(lines):
    out, cur = {}, None
    for l in lines:
        if l.startswith("## "):
            cur = l[3:].strip()
            out[cur] = []
        elif cur:
            out[cur].append(l)
    return out


def main():
    errors = []
    notes = [(p, kind) for d, kind in NOTE_DIRS.items() for p in sorted((VAULT / d).glob("*.md"))]
    names = {p.stem for p in VAULT.rglob("*.md") if ".obsidian" not in p.parts}
    hosts = allowed_hosts()
    for path, kind in notes:
        lint_note(path, kind, names, errors, hosts)
    for e in errors:
        print(e)
    print(f"\n{len(notes)} notes checked, {len(errors)} problem(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
