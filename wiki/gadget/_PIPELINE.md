---
sensitivity: private
entity_type: system
name: Product Pipeline
last_updated: 2026-08-08
---

# Product Pipeline — Gadget OS

Every product the business touches, at every stage, in one table. Read by `scripts/heartbeat.py` for stale-stage detection and by `scripts/pulse.py` for pipeline value.

---

## The Stages

```
idea ──► researching ──► qualified ──► sampling ──► sourcing ──► listing_draft
                │             │            │            │              │
                ▼             ▼            ▼            ▼              ▼
              killed        killed      rejected     killed        approved
                                                                       │
                                                                       ▼
                                                    live ──► selling ──► retired
                                                                │
                                                                ▼
                                                            dead_stock
```

| Stage | What it means | Max days before heartbeat flags it |
|---|---|---|
| `idea` | Someone mentioned it. Not researched. | 30 |
| `researching` | Demand and competition being checked. | 7 |
| `qualified` | Passed `/product-qualify` with score ≥65. | 14 |
| `sampling` | Sample ordered, not yet inspected. | 21 |
| `sourcing` | Sample passed. Negotiating bulk PO. | **14** |
| `listing_draft` | Stock inbound or landed. Copy being written. | 7 |
| `approved` | Listing signed off, not published yet. | **7** |
| `live` | Published, no sales yet. | 21 |
| `selling` | Published and moving units. | — |
| `retired` | Deliberately discontinued. | — |
| `dead_stock` | Live 60+ days, under 2 units sold. Capital trapped. | — |
| `killed` / `rejected` | Did not pass a gate. Kept for the pattern log. | — |

The two bolded thresholds are the ones the operator actually loses money on: capital sitting in `sourcing` limbo, and finished listings that never get published.

---

## Active Pipeline

<!-- MACHINE-READABLE BLOCK — parsed by scripts/heartbeat.py and scripts/pulse.py. Keep it valid JSON. -->
```json
[]
```

**Row schema** — every product entry uses these fields:

```json
{
  "sku": "iphone-13-128-uk-used",
  "name": "iPhone 13 128GB — UK Used, Grade A",
  "category": "phones",
  "stage": "sourcing",
  "stage_entered": "2026-08-08",
  "score": 78,
  "supplier": "supplier-slug-or-null",
  "units_held": 0,
  "unit_cost_ngn": 0,
  "target_price_ngn": 0,
  "gross_margin_pct": 0,
  "capital_committed_ngn": 0,
  "channel": ["whatsapp", "instagram"],
  "notes": "One line. What is actually true right now."
}
```

Field notes:
- `capital_committed_ngn` — money already spent or hard-committed on this SKU. This is what `pulse.py` sums for pipeline exposure. Deposits count.
- `gross_margin_pct` — `(target_price - unit_cost) / target_price × 100`. Landed cost, not invoice cost: include freight, clearing, courier, and the FX rate actually paid.
- `supplier` — must match a node slug in `suppliers/active/`. `null` is allowed only before the sourcing stage.
- `score` — composite from `qualify.py`. Required from `qualified` onward.

---

## Pipeline Rules

1. **One SKU, one row.** Colour and storage variants of the same model are one row unless their margins differ by more than 10 points — then split them.
2. **`stage_entered` is updated on every stage change.** This field is the entire basis of stale detection. A row whose `stage_entered` never moves is a row the OS can no longer see.
3. **Nothing enters `sourcing` without a supplier node.** The supplier gate is enforced here, not at PO time.
4. **Nothing enters `live` without a published listing in `outputs/listings/`.**
5. **`dead_stock` is a decision, not an insult.** When a SKU hits it, run `/pricing-strategy` for a clearance number, then either liquidate or retire. Capital trapped in dead stock is the single most expensive mistake this business can make — it is not a loss until it is sold, which is exactly why it gets ignored.
6. **Killed products stay in the file.** Move them to the archive block below with the reason. Three kills for the same reason is a pattern — write it to `market/patterns/dead-stock.md`.

---

## Archive — Killed / Retired

```json
[]
```
