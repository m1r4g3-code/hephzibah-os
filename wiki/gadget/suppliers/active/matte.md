---
sensitivity: private
entity_type: company
name: "Matte — Ikeja"
slug: "matte"
last_updated: "2026-08-08"

supplier_type: "market-vendor"
location: "Ikeja / Computer Village, Lagos"
status: "active"
first_contact: "unknown — predates the OS"

reliability_score: null
orders_placed: 0
orders_on_time: 0
orders_with_defects: 0
avg_lead_time_days: null
moq: 1
payment_terms: "unknown — CONFIRM"
sole_source_for: []

categories: ["phones"]
relationships:
  - target: "[[identity]]"
    type: known_by
    strength: 9
    first_seen: "2026-08-08"
    last_reinforced: "2026-08-08"
  - target: "[[gadget-index]]"
    type: supplies
    strength: 8
    first_seen: "2026-08-08"
    last_reinforced: "2026-08-08"
---

# Matte — Ikeja

## Who They Are

Emmanuel's own vendor at Ikeja, independent of [[yemi-group]]. Works for a boss at Computer Village **and** trades on his own account — which is the important detail: the units he sells Emmanuel personally are his own book, not his boss's.

Personally close to Emmanuel — described as *"like a brother."* That is an asset and an exposure at the same time, and the section below says why.

---

## Contact

| Field | Value |
|---|---|
| Primary contact | Matte |
| Phone / WhatsApp | **MISSING — fill in** |
| Alternative contact | **MISSING** — see note |
| Location / address | Ikeja / Computer Village |
| Online presence | unknown |
| Introduced by | — (direct relationship) |
| Works for | a boss at Computer Village (name unknown) — also trades independently |

**The second contact here is unusual.** Normally the backup is another person at the same operation. Matte *is* the operation for his own trades, so there is no second name to take. What matters instead is knowing **which hat he is wearing on a given unit** — his boss's stock or his own. Those have different prices, different availability, and different consequences when something goes wrong. Ask, per unit.

---

## Reliability Scorecard

Nothing logged yet. Every order goes through:
`python scripts/analytics.py --log-order '{"supplier":"matte","sku":"...","units":N,"on_time":true,"defects":0}'`

| Dimension | Weight | Score | Evidence |
|---|---|---|---|
| Delivery reliability | 35% | — | no orders logged |
| Quality consistency | 35% | — | no orders logged |
| Volume confidence | 30% | — | 0/4 orders — **unproven** |
| **Composite** | | **—** | |

Reads as `unproven` until 4 logged orders, regardless of score. A close relationship is not order history.

---

## Broker Terms — What Actually Needs Confirming

Under the broker model, Emmanuel does not hold Matte's stock — he posts it and collects it when a buyer commits. That makes these the questions that matter, and none of them are answered yet:

| Question | Answer | Why it matters |
|---|---|---|
| **Does a quoted price hold, and for how long?** | **UNKNOWN** | The whole spread lives or dies here. A price that moves ₦15k between quote and collection erases a typical deal. |
| **Will he hold a unit once a buyer commits?** | **UNKNOWN** | The core broker failure: buyer pays, unit already sold to someone else. |
| **How long can he hold it — an hour, a day?** | **UNKNOWN** | Sets how fast Emmanuel has to move after a buyer says yes. |
| **What happens when a unit is bad?** | **UNKNOWN** | Ask before it happens, not after. A vendor who will not answer has answered. |
| **Will he let a unit be inspected before money changes hands?** | **UNKNOWN** | Non-negotiable — the brand depends on it. See [[broker-model]]. |
| **His own stock vs his boss's — different terms?** | **UNKNOWN** | Almost certainly yes. Price and flexibility both. |

**These six answers are worth more than any price list.** They are one conversation. Queue item `g006`.

---

## The Relationship Risk — Name It Now

Matte is close to Emmanuel personally, and this is genuinely valuable: better prices, first look at good units, trust that a stranger would not extend.

It is also the exact condition under which the gates get skipped. The pattern is predictable and it is not about anyone being dishonest:

- Skipping the IMEI check because it feels like an insult to a brother
- Accepting "I'll sort you out" instead of a confirmed price
- Not raising a defect because it would be awkward
- Letting him become the sole source because dealing with him is easy

**The rule that protects both the business and the friendship: every unit gets the same checks regardless of who it came from.** Make the check impersonal and routine from the start — an IMEI check performed on every single unit, always, is a policy. One performed selectively is an accusation. Establishing it now, before there is ever a problem, is what makes it survivable later.

[[middleman-lesson]] is the cautionary case here. That arrangement also ran on trust rather than terms, and the cost landed on Emmanuel.

---

## Order History

| Date | SKU | Units | Unit cost | Quoted price held? | On time | Defects | Notes |
|---|---|---|---|---|---|---|---|

---

## Sole-Source Exposure

| SKU | Only supplier? | Backup | Status |
|---|---|---|---|

Matte and [[yemi-group]] overlap on phones, which is genuinely good — two independent Ikeja sources on the anchor category. Keep it that way. The supplier gate is satisfied on phones **only while both are live.**

---

## Red Flags Observed

- [ ] Quoted price changed at collection
- [ ] Unit did not match the description
- [ ] Went silent mid-deal
- [ ] Pushed for full payment upfront
- [ ] Refused or dodged an IMEI check
- [ ] Vague about where stock comes from
- [ ] Pressure tactics — "someone else is buying it today"

None observed. None checked either — this is a blank record, not a clean one.

---

## Relationship Notes

### 2026-08-08 — Node created
Created during the broker-model correction. Everything above about terms is unconfirmed; the relationship facts came from Emmanuel directly. First action is the six-question conversation.

---

## Linked

[[gadget-index]] · [[yemi-group]] · [[broker-model]] · [[middleman-lesson]] · [[identity]]
