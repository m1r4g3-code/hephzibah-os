---
sensitivity: private
entity_type: company
name: "Yemi — Gadget Group"
slug: "yemi-group"
last_updated: "2026-08-08"

supplier_type: "aggregator"
location: "Ikeja / Computer Village, Lagos — sources from direct vendors"
status: "active"
first_contact: "before 2026-05-27"

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
  - target: "[[yemi]]"
    type: operated_by
    strength: 10
    first_seen: "2026-08-08"
    last_reinforced: "2026-08-08"
  - target: "[[identity]]"
    type: partner_of
    strength: 8
    first_seen: "2026-08-08"
    last_reinforced: "2026-08-08"
---

# Yemi — Gadget Group

## Who They Are

[[yemi]] is Emmanuel's gadget business partner and the operator of a group where phone stock gets posted. Yemi takes phones from **direct vendors at Ikeja**; Emmanuel takes units from the group and posts them to his own channels.

This node covers the group as a *supply channel*. The person, the partnership, and the profit-split arrangement live in `outreach/contacts/yemi.md`.

**Structurally, this is one layer further from the device than [[matte]] is.** Yemi is himself sourcing from direct vendors, so a unit Emmanuel posts from the group has passed through at least two hands before reaching a buyer, and the original vendor is someone Emmanuel has no relationship with. That is not a problem in itself — it is the reason the condition on a group unit cannot be assumed and has to be established at collection.

---

## Contact

| Field | Value |
|---|---|
| Primary contact | Yemi |
| Phone / WhatsApp | **MISSING — fill in** |
| Group name / link | **MISSING — fill in** |
| Location | Ikeja / Computer Village |
| Underlying vendors | unknown to Emmanuel — sourced by Yemi |

---

## Reliability Scorecard

Nothing logged. Reads as `unproven` until 4 orders.

| Dimension | Weight | Score | Evidence |
|---|---|---|---|
| Delivery reliability | 35% | — | no orders logged |
| Quality consistency | 35% | — | no orders logged |
| Volume confidence | 30% | — | 0/4 orders |
| **Composite** | | **—** | |

**Scoring note:** a group is not one supplier. If units come from several underlying vendors, one composite score averages good vendors with bad ones and hides both. Once there is enough history, record the underlying vendor per unit in the order log and check whether the defects cluster. If they do, this node splits.

---

## Broker Terms — Unconfirmed

| Question | Answer | Why it matters |
|---|---|---|
| How is the split with Yemi structured on a group unit? | **UNKNOWN** | Determines the real spread. Partner split comes out of Emmanuel's margin. |
| Does a posted price hold? | **UNKNOWN** | The spread depends on it entirely. |
| How fast does group stock move? | **UNKNOWN** | Sets how stale a post is. Posting a gone unit costs credibility. |
| Can a unit be held once a buyer commits? | **UNKNOWN** | The core broker failure mode. |
| Who inspects before it reaches Emmanuel — anyone? | **UNKNOWN** | Decides how much of the condition report Emmanuel has to establish himself. |
| What happens when a unit is bad? | **UNKNOWN** | Partner or not, this needs an answer before it is needed. |

Queue item `g006` covers this alongside Matte.

---

## The Stale-Post Problem

Group stock is shared with everyone else in that group. A unit Emmanuel posts may already be sold by the time a buyer responds — and unlike a stockist, he finds out **after** he has made a promise.

This is the broker equivalent of dead stock: it costs no capital and it costs credibility, which under [[trust-as-margin]] is the more expensive of the two.

Mitigations, in order of how much they help:
1. **Confirm availability before collecting any money.** Not after.
2. **Post with a timestamp** — "as of this morning" — so a stale post reads as honest rather than deceptive.
3. **Pull the post the moment a unit goes.** A live listing for a sold unit is the single fastest way to look like every other page.
4. **Track it.** If the group sells out from under Emmanuel repeatedly, that is a measurable supply-reliability problem, not bad luck.

---

## Order History

| Date | SKU | Underlying vendor | Units | Cost | Price held? | Defects | Notes |
|---|---|---|---|---|---|---|---|

---

## Sole-Source Exposure

| SKU | Only supplier? | Backup | Status |
|---|---|---|---|

Overlaps with [[matte]] on phones. Two independent Ikeja sources on the anchor category satisfies the supplier gate — **while both stay live.**

---

## Red Flags Observed

- [ ] Posted price did not hold
- [ ] Unit did not match the group post
- [ ] Unit already sold when a buyer committed
- [ ] Went silent mid-deal
- [ ] Refused or dodged an IMEI check
- [ ] Vague about the underlying vendor

None observed, none checked.

---

## Relationship Notes

### 2026-08-08 — Node created
Created during the broker-model correction. Yemi was already in the brain as a person (`outreach/contacts/yemi.md`, one line) but not as a supply channel. The partnership terms and the group mechanics are both unrecorded.

---

## Linked

[[gadget-index]] · [[yemi]] · [[matte]] · [[broker-model]] · [[trust-as-margin]]
