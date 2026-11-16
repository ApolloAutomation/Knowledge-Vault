# Freshdesk AI Support Plan

Status: proposal · 2026-11-15
Research behind this plan: [vault audit](research/vault-audit-2026-11-15.md) · [Freshdesk API brief](research/freshdesk-api-brief-2026-11-15.md) · [AI support practices](research/ai-support-practices-2026-11-15.md)

## Goal

Claude reads new Freshdesk tickets and answers them from the `Apollo-Knowledge/` vault. Replies start as **private notes that an agent reviews**. Only once the numbers show it is safe does Claude **auto-send for narrow categories**. When a ticket hits something the vault doesn't cover, that gap becomes a reviewed vault update. Past tickets are mined into FAQ notes so the vault keeps getting better.

Rough timeline: shadow mode by week 6, first auto-send category by weeks 10–12.

## Where the vault stands today

The vault is a good base, but it doesn't yet hold the knowledge most tickets need:

- **41 notes**: 20 products, 5 accessories, 16 components, 965 lines in all. The structure is consistent, but the notes use plain `Label:` lines instead of headings, and no note has a title in its body.
- **142 "Not stated on site" placeholders.** About 110 of them are battery or power fields on USB- or PoE-powered devices. The real answer there is "N/A, no battery", but as written the AI would say "we don't know".
- **Q&A sections:** 19 of 20 are empty. The two MSR-2 answers ("Reflash from website", "Put in boot mode") have no link and no steps.
- **Missing entirely:** setup and onboarding (Improv Wi-Fi, fallback hotspot, adopting the device in HA), flashing and boot mode per device, OTA updates, troubleshooting, warranty, returns and RMA, shipping, preorders, contact hours and escalation, and a URL allowlist.
- **Small fixes:** `ld2450.md` should be `LD2450`. Some backlinks are missing (TEMP-1 → its probes, ESK-1 → the Breakout Module). Stock status is buried in description text.

**Takeaway:** writing the Setup, Troubleshooting and Company notes matters more than the code.

## Architecture

```
Freshdesk ──poll every 2 min──▶ support-ai (small VPS, SQLite state)
                                   │
          sanitize ─▶ deterministic escalation rules ─▶ route (small model)
                                   │
          draft (Claude Sonnet-class, whole vault in prompt, cited, NO tools)
                                   │
          verify (citations, URL allowlist, numbers match note, no promises)
                                   │
Freshdesk ◀── private note / tags / custom fields (later: public reply)
```

Key choices:

- **Custom Claude build instead of Freddy.** Freddy can't read a private git vault, charges per session (~$49 per 100), and gives you little control. If you later want a self-service portal, you can sync the public notes into Freshdesk Solutions.
- **No vector database yet.** The whole vault is about 20k tokens, so it goes into every prompt with prompt caching and citations. Revisit this once it grows past about 80k tokens.
- **Polling instead of webhooks.** This needs no public endpoint, and Freshdesk webhooks aren't signed anyway. A 2-minute delay is fine for email.
- **Guarantees come from code, not prompts.** The Freshdesk client only exposes `get`, `list`, `add_private_note` (private hard-coded) and `update_ai_fields`. Reply code doesn't exist until Phase 5. Hard escalations (refunds, RMA, safety, legal, "talk to a human") are matched by deterministic phrase rules **before** the LLM sees the ticket.
- **Customer email is untrusted input.** It's wrapped as data, the drafter has no tools, and the output is checked against an allowlist.

Repo layout (one repo):

```
Apollo-Knowledge/      content only — everything here is customer-quotable unless `audience: internal`
  Products/ Accessories/ Components-Sensors/   (existing)
  Setup/ Troubleshooting/ Company/ Safety/ FAQ/<Product>/ Legacy/
  _meta/schema.md  _meta/taxonomy.yml  Links.md (URL allowlist)
support-ai/            code, prompts, escalation.yaml, autosend.yml (CODEOWNERS-protected)
evals/                 scrubbed test cases + scorecards
docs/                  this plan and research
```

Raw ticket exports and state live **outside git**, in `~/apollo-support-data/`. Worktrees get cleaned up, and PII must never be committed.

## Phases

### Phase 0: Access and a cheap validation (week 1)

1. **Freshdesk API access.** Create a dedicated agent called "Apollo AI Assistant". Give it permission to view tickets, add notes and edit tags and fields, with no reply, delete or admin rights. Its API key is under *Profile → View API key* and works as the basic-auth username (`curl -u KEY:X https://<domain>.freshdesk.com/api/v2/tickets`). Keep the key in 1Password and never in the repo. Check:
   - whether your plan has custom roles (they may be Pro or Enterprise only)
   - what the bot seat costs
   - your real rate limit, from the `X-RateLimit-*` response headers (Growth is ~100 per minute, shared with every app)
2. **Anthropic API key** with a monthly spend cap, plus a separate low-limit key for CI.
3. **Freshdesk setup:**
   - custom fields `cf_ai_status`, `cf_ai_category`, `cf_ai_language`
   - tags `ai-drafted`, `ai-escalate-<reason>`, `ai-kb-gap`, `ai-off` (per-ticket kill switch), `ai-sent`
4. **Metadata-only crawl.** Pull subjects, tags and status only, no message bodies, and rank the top 20 contact reasons. This decides what to write first and whether order-status questions dominate.
5. **Zero-code pilot (~2 hours).** Paste 20–30 real tickets, with personal details removed by hand, into a Claude Project that holds the vault, and grade the answers. This shows the real gaps before anything is built.

### Phase 1: Make the vault answerable (weeks 1–3, mostly writing)

1. Add `_meta/schema.md`. Every note gets frontmatter for `title`, `aliases`, `type`, `audience`, `status` (in stock / preorder / sold out / legacy), `power_source` and `last_verified`, plus an H1 title.
2. Make one scripted migration across all 41 notes. Each placeholder becomes one of three things: a real value, "N/A", or "Unknown — escalate". The same migration fixes links, moves stock status into frontmatter, and turns facts buried in the text into Q&As. For example: the AIR-1 temperature offset, the MTR-1 smart-charger issue, BTN-1 wake behaviour, and the MiCS-4514 being present/absent only.
3. Write the missing notes in the order the Phase 0 report sets. Claude drafts each one from the site and wiki, and you correct it:
   - **Setup/**: Improv Wi-Fi, fallback hotspot, adopting in HA, web flasher and boot mode per device, OTA updates, PoE.
   - **Troubleshooting/**: won't connect, device unavailable, USB not detected, temperature reads high, radar ghosts and still presence, CO2 calibration, battery drain.
   - **Company/**: contact and hours, warranty, returns and RMA, shipping, preorders, order changes.
   - **Safety/**, **Links.md**.
4. Add a `vault-lint` check in CI. It fails on broken links, leftover placeholders, URLs not on the allowlist, and personal-data patterns.

### Phase 2: Mine historical tickets (weeks 2–5, read-only)

1. **Export:**
   - `GET /api/v2/tickets?updated_since=…&per_page=100`, walking date windows because of the 300-page cap.
   - `GET /api/v2/tickets/{id}/conversations` for each ticket.
   - Use at most ~40% of the rate limit, off-hours, backing off on `Retry-After`.
   - Archived tickets need an Admin → Account export.
2. **Scrub before any LLM sees the text.** Remove emails, phone numbers, addresses, order numbers, MAC and IP addresses, HA and Nabu Casa URLs, and Wi-Fi passwords or API keys inside pasted YAML. Also strip names, signatures and quoted history. Check 50 tickets by hand.
3. **Filter** to resolved tickets whose final public reply came from an agent and that weren't reopened.
4. **Extract and cluster.** Claude labels each ticket with product, topic, customer wording, resolution steps, and whether the vault already covers it. Topics with 3 or more tickets are distilled into `FAQ/<Product>/<topic>.md`, each with 2–4 customer phrasings and numbered steps. These arrive as **pull requests that a person reviews**; raw transcripts are never added to the vault. Contradictions go to `conflicts.md`.
5. **Build the eval set:**
   - ~200 scrubbed past tickets, with the agent's real answer as the gold reply
   - 30 or more adversarial cases (prompt injection, refunds, safety, questions the vault can't answer)
   - 30 or more "false escalation traps", where normal setup language contains trigger words: "hotspot", "charger", "IP address", "lost connection"

### Phase 3: Drafter and offline evaluation (weeks 3–6)

Build `support-ai/` as roughly 300–500 lines of Python. The pipeline runs sanitize → escalate → route → draft → verify → write note.

- **Escalate** on refunds, RMA, warranty claims, order changes, safety, legal, requests for a human, reopened tickets, and image attachments (v1). An escalated ticket gets a triage note instead of a draft.
- **Verify:**
  - every claim cites a note
  - URLs are on the allowlist
  - numbers and part numbers appear in the cited note
  - no promises, prices, dates or stock claims
  - otherwise the ticket escalates

Run the evals in CI on every vault or prompt PR, so a knowledge edit has to show it helps.

**Gate to Phase 4:**

- 100% recall on hard escalations, and at least 80% escalation precision
- at least 95% faithfulness
- at least 65% resolution match
- clean results on the injection suite

### Phase 4: Shadow, then agent-assist (weeks 6–10)

- **Shadow, then assist.** The bot posts private notes headed **"AI DRAFT — NOT SENT"**, each with its category, citations, any vault gaps, and the draft. Agents copy and edit it. Run this as shadow for 2 weeks, then use it in daily work.
- **Duplicate and loop guards:**
  - Process each new customer message only once.
  - Re-check the ticket just before writing, and skip it if an agent already replied.
  - Ignore out-of-office replies and bounces.
  - Only one poller runs at a time.
- **Feedback.** Agents tag drafts 👍/✏️/👎. A nightly job stores draft-vs-sent pairs, and a daily digest reports volume, escalations, verify failures, cost and cache hit rate.
- **Gate to Phase 5:**
  - at least 300 drafts
  - at least 70% accepted
  - no harmful drafts and no missed hard escalations in the last 2 weeks

### Phase 5: Narrow auto-send (week 10 onward)

- **Turn on replies.** Grant the bot the reply permission and add `reply.py` behind `AUTO_SEND=true` and an allowlist of categories.
- **When a category qualifies:** at least 85% of its drafts usable, over 40 or more tickets and 3 or more weeks, with no corrected facts. Auto-send covers the first response only, and English only. Likely first categories: Wi-Fi onboarding, flashing and boot mode, OTA how-to, temperature offset.
- **Every auto-reply:**
  - says it was AI-assisted and tells the customer to reply to reach a person
  - sets the ticket to Pending, never Resolved
  - turns off Freshdesk's duplicate acknowledgement email
- **Audit and pause.** Audit 100% of auto-replies in week 1, then 10%. A category pauses automatically if its reopen rate climbs 5 points above the human baseline.
- **After hours.** This is where auto-send pays off most. Escalated tickets get a fixed "a person will reply on Monday" template.
- **5b, optional: Shopify order status.** A read-only Shopify app looks up orders by the requester's email and fills a fixed template with the tracking link. No LLM is involved in the factual part.

### Ongoing: feedback loop

- **Weekly:** Claude clusters agent edits and vault gaps into a "Weekly KB update" PR with an eval scorecard. A person merges it, and each correction becomes a regression test.
- **Monthly:** review `last_verified`, check which notes keep getting corrected, and review escalations.
- **On product launches:** updating the vault note is on the release checklist.

## Cost (estimates, to check against current pricing)

| Item | Estimate |
|---|---|
| Drafting, Sonnet-class with caching | ~1–5¢ per ticket → low tens of $/month at 300–600 tickets |
| One-time mining of 2–5k tickets (Batch API) | tens of $ |
| Eval CI | a few $ per run |
| VPS | $5–10/month |
| Freshdesk bot agent seat | probably the largest item; check your plan |

## Decisions for you

| # | Decision | Recommendation |
|---|---|---|
| D1 | Custom Claude build or Freddy AI | Custom |
| D2 | Freshdesk plan / bot seat / custom roles | Check in week 1 |
| D3 | Where it runs | Small VPS, one named owner for alerts |
| D4 | Data policy: Anthropic API terms, privacy-policy line, raw data kept 30 days | Yes |
| D5 | Hard-escalation list | Refunds, RMA, warranty claims, order changes, safety, legal, "human please" |
| D6 | May the AI state warranty or return policy? | Not in v1; revisit in Phase 5 |
| D7 | May the AI state stock, prices or ship dates? | Never; link the store page |
| D8 | Disclose that replies are AI-assisted? | Yes, plus "reply to reach a person" |
| D9 | Automate Shopify order status? | Yes, if the Phase 0 crawl puts it in the top 3 |
| D10 | After-hours behaviour | Fixed holding template plus a holiday calendar |
| D11 | Non-English tickets | Drafts in assist mode; auto-send English only |
| D12 | Who reviews vault PRs and approves auto-send per category | One support lead, about 2 hours a week |

## Out of scope for now

Discord, phone and chat tickets, product reviews, and image understanding (vision).

## Not yet verified

- Custom-role availability on your Freshdesk plan
- Whether the reply and note permissions can be granted separately
- The bot seat price
- Whether webhooks count against the rate limit (not needed while polling)
- All dollar figures
- Whether order status really is the top contact reason
