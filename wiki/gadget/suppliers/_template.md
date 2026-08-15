---
sensitivity: private
entity_type: company
name: "[Supplier name]"
slug: "[supplier-slug]"
last_updated: "YYYY-MM-DD"

supplier_type: "[market-vendor|importer|distributor|agent|individual]"
location: "[Computer Village Ikeja | Shenzhen | UK | ...]"
status: "prospect"      # prospect | sampling | active | probation | blacklisted
first_contact: "YYYY-MM-DD"

# Reliability — from scripts/analytics.py supplier log
reliability_score: null     # 0-100 composite
orders_placed: 0
orders_on_time: 0
orders_with_defects: 0
avg_lead_time_days: null
moq: null
payment_terms: null
sole_source_for: []         # SKUs where this is the ONLY supplier — supplier gate reads this

categories: []
relationships: []
---

# [Supplier Name]

## Who They Are

[Two sentences. What they actually supply, how they operate, how the relationship started.]

---

## Contact

| Field | Value |
|---|---|
| Primary contact | [name] |
| Phone / WhatsApp | |
| Alternative contact | [second person at the same supplier — see rule below] |
| Location / address | |
| Online presence | |
| Introduced by | |

**A supplier with one contact is a supplier with one point of failure.** Get a second name and number at the same operation before the second order. When the primary contact travels, changes number, or falls out with the business, a single-contact supplier disappears completely.

---

## Reliability Scorecard

Recomputed after every order. Log orders with:
`python scripts/analytics.py --log-order '{"supplier":"[slug]","sku":"...","units":N,"on_time":true,"defects":0}'`

| Dimension | Weight | Score | Evidence |
|---|---|---|---|
| **Delivery reliability** — arrives when promised | 30% | — | [N of M orders on time] |
| **Quality consistency** — units match description | 30% | — | [defect rate across orders] |
| **Price stability** — quotes hold, no surprises at collection | 15% | — | |
| **Communication** — responds, tells you about problems early | 15% | — | |
| **Terms flexibility** — MOQ, payment, returns on defects | 10% | — | |
| **Composite** | | **—** | |

| Band | Meaning |
|---|---|
| 80–100 | Core supplier. Safe to scale volume. |
| 65–79 | Working supplier. Keep a second source on anything important. |
| 50–64 | Probation. Small orders only. Fix or replace. |
| <50 | Blacklist. Document why so the mistake is not repeated in six months. |

**Under 4 orders, no band applies — the supplier reads as `unproven` regardless of score.** A flawless record over one order is not evidence. Calling such a supplier "core" is how sole-source concentration happens by accident, which is precisely what the supplier gate exists to prevent.

---

## Commercial Terms

| Term | Value |
|---|---|
| MOQ | |
| Lead time (quoted / actual) | / |
| Payment terms | |
| Currency | |
| Defect policy | [what happens when a unit is bad — the answer "nothing" is itself the answer] |
| Price list validity | |
| Volume breaks | |

**The defect question is the one that matters and it must be asked before the first order, not after the first bad unit.** A supplier who will not answer it has answered it.

---

## Order History

| Date | SKU | Units | Unit cost | Lead time (q/a) | On time | Defects | Notes |
|---|---|---|---|---|---|---|---|

---

## Sole-Source Exposure

**Gate: never sole-source a top-5 product.**

| SKU | Is this the only supplier? | Backup supplier | Status |
|---|---|---|---|

Any row with no backup on a top-5 SKU is an open risk. It goes in `_QUEUE.md` as a `supplier` item until a second source exists. The cost of finding a backup supplier is a few conversations. The cost of not having one is discovering it during a stockout, when there is no leverage and no time.

---

## Relationship Notes

*Append-only, dated. The things that do not fit a table.*

### YYYY-MM-DD
[What happened. What was learned. What was promised by whom.]

---

## Red Flags Observed

- [ ] Quoted price changed at collection
- [ ] Unit did not match the description
- [ ] Went silent mid-order
- [ ] Pushed for full payment upfront on a first order
- [ ] Refused or dodged an IMEI check
- [ ] Vague about where stock comes from
- [ ] Pressure tactics — "someone else is buying it today"

Any two of these together means probation. An IMEI dodge alone is an immediate blacklist — it is the only red flag here that can end the business rather than cost it money.

---

## Linked

[[gadget-index]] · [[gadget-pricing]] · [[yemi]]
