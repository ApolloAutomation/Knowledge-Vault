---
title: Vault schema
type: meta
audience: internal
last_verified: 2026-11-15
---
# Vault schema

Every note in `Products/`, `Accessories/` and `Components-Sensors/` follows this schema. `scripts/vault_lint.py` enforces it in CI. Files under `_meta/` describe the vault itself and are never shown to customers.

## Rules for every note

1. **Frontmatter is required.** The keys each type needs are listed below.
2. **The body starts with `# <title>`.** It must match the `title` frontmatter exactly. This lets any chunk of text be traced back to its product.
3. **Sections are `##` headings.** Do not use plain `Label:` lines.
4. **Each spec value is one of three things:**
   - **A real value**, e.g. `5V 3A via USB-C`.
   - **`N/A — <reason>`**, when the field doesn't apply, e.g. `N/A — USB-C powered, no battery`.
   - **`Unknown — escalate to support`**, when we don't know yet.

   Never write "Not stated on site".
5. **Write as Apollo, speaking to the customer.** Do not use hedges like "per the site", "Site note:" or "wording unclear on site". Facts that come only from customer reviews do not belong in customer-facing notes.
6. **Keep chip-maker figures separate.** Datasheet figures go under `## Datasheet figures (chip manufacturer, not an Apollo rating)`, with a `Source:` line. They must never be mixed into Apollo's own specs.
7. **Keep fast-changing facts out of prose.** Stock and preorder status belong in the `status` frontmatter, never in the description. Prices and ship dates are never stated in the vault.
8. **Wikilinks must match a filename exactly, including case.** Plain text is fine for things that have no note.
9. **Write Q&As as real customer questions.** Format each as `### <question>` followed by the answer. The answer may only use facts that already appear in the note or in a linked note.

## Frontmatter

| Key | Applies to | Values |
|---|---|---|
| `title` | all | Canonical name, same as the filename without `.md` (e.g. `MSR-2`) |
| `aliases` | all | List of other names customers or the site use (e.g. `[MSR 2, HLK-LD2450]`). Use `[]` if there are none |
| `type` | all | `product`, `accessory`, `component` |
| `audience` | all | `customer` (may be quoted to customers) or `internal` |
| `source` | product, accessory | Official store URL |
| `status` | product, accessory | `available`, `preorder`, `sold-out`, `discontinued` |
| `status_checked` | product, accessory | Date `status` was last confirmed (YYYY-MM-DD) |
| `power_source` | product | List from: `usb-c`, `battery`, `poe`, `mains`, `dc`, `wago`, `host-board` |
| `used_in` | component | List of wikilinks to products |
| `last_verified` | all | Date the note's facts were last checked (YYYY-MM-DD) |

Add `sold_as_product: true` and `source` to a component that is also sold on its own in the store, e.g. LD2412.

## Section order

**Product**

```
# <title>
## Description
## Features
## Specs
## Components
## Options and add-ons
## What's in the box
## Common questions and answers
```

**Accessory**

```
# <title>
## Description
## Features
## Specs
## Compatible with
## What's in the box
## Common questions and answers
```

**Component**

```
# <title>
## Description
## Used in
## Specs
## Datasheet figures (chip manufacturer, not an Apollo rating)   (optional)
```

If a Q&A section has no entries yet, write `_None yet._` under it.

## Battery fields

Products have six standard spec fields:

- Battery life
- Operating temperature
- Waterproof
- Power consumption awake
- Power consumption sleeping
- What battery works with it

If `power_source` does not include `battery`, then "Battery life" and "What battery works with it" must be `N/A — <reason>`. "Power consumption sleeping" must also be `N/A` unless the device has a sleep mode.
