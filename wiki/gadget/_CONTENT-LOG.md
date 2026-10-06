---
sensitivity: private
entity_type: system
name: Content Log
last_updated: 2026-08-22
---

# Content Log — what has already been published

**Check this before drafting anything.** Emmanuel asked "hope we haven't done this topic before" on 2026-08-22 and the only way to answer was to list a folder and reason from filenames. That is not a record, and it is exactly how a topic gets repeated.

One row per piece. Add the row when the piece is **rendered**, not when it is posted, because a drafted-and-forgotten topic gets re-drafted just as easily as a posted one.

---

## Carousels

| Date | Slug | Topic | Slides | Posted? |
|---|---|---|---|---|
| 2026-08-10 | `idm-icm-ibm` | IDM / ICM / IBM. Non-genuine replaced parts, where to find them, what they cost you. Real screenshots on slide 04. | 7 | unconfirmed |
| 2026-08-13 | `carrier-lock` | What an eSIM is, why "locked" is the real problem, the Carrier Lock row, and the model-number check. | 7 | unconfirmed |
| 2026-08-22 | `buy-now-or-wait` | iPhone 18 launch timing. The split launch, and what a generation of age actually costs, measured from our own ladder. | 6 | unconfirmed |

## Daily checks

| Date | The check |
|---|---|
| 2026-08-08 | Battery boosting — a health percentage can be faked |
| 2026-08-09 | Parts and Service History — has this phone been opened |
| 2026-08-11 | Activation Lock — is the last owner still signed in |
| 2026-08-13 | *(needs confirming — file exists, topic not recorded)* |

## Openers

Presence posts, no topic. 2026-08-10, 08-11, 08-13.

## Product posts

| Date | Unit |
|---|---|
| 2026-08-08 | iPhone 12 128GB (several design iterations) |
| 2026-08-10 | Pixel Watch 3 · iPhone 17 Air · iPhone Air lineup · iPhone 14 Plus 512GB |

---

## Topics still unused

Do not draft one of these without checking the table above first.

- **Model number ending in /A** — which region the phone was actually built for. Partly covered as slide 07 of the carrier-lock carousel, so a standalone post would need a different angle.
- **MDM / corporate lock** — a company can wipe that phone remotely
- **The NCC device register** — stolen and cloned phones being cut off the network
- **Charge cycles vs battery health** — the number that is harder to fake
- **What "UK used" actually means** — the term has no standard
- **Storage: which size to actually buy** — a buying-decision post
- **iPhone 14 Pro vs 15** — near-identical price in our ladder, genuinely non-obvious

---

## The real gap this exposed

`analytics.py` has a `content` table and **zero rows in it**. Every piece so far was rendered and never logged, so the OS cannot answer "what have we posted", "what got engagement", or "which angle works" — the whole learning loop for content is dead.

Log each piece when it goes out:

```
python scripts/analytics.py --log-content '{"platform":"whatsapp","angle":"buyer-protection","sku":"","format":"carousel","notes":"carrier-lock"}'
```

Until that happens this file is the only record, and it is maintained by hand.
