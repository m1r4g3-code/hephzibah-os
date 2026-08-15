---
sensitivity: private
entity_type: concept
name: Capital Velocity
last_updated: 2026-08-08
relationships:
  - target: "[[gadget-pricing]]"
    type: underpins
    strength: 9
    first_seen: "2026-08-08"
    last_reinforced: "2026-08-08"
  - target: "[[financial-fragility]]"
    type: mitigates
    strength: 8
    first_seen: "2026-08-08"
    last_reinforced: "2026-08-08"
---

# Capital Velocity

**A gadget business does not make money from margin. It makes money from margin × turns.**

---

## The Arithmetic

₦1,000,000 of capital, two ways to run it:

**A — high margin, slow:** 60% margin, sells in 90 days.
Four turns a year is impossible; this is 4 turns ÷ 90-day cycle ≈ 4 cycles. ₦1m × 60% × 4 = **₦2.4m gross profit/year.**

**B — lower margin, fast:** 40% margin, sells in 21 days.
17 cycles a year. ₦1m × 40% × 17 = **₦6.8m gross profit/year.**

B nearly triples A while looking worse on every listing.

This is the number that separates a gadget business that grows from one that just cycles the same stock. It is also almost never tracked, because margin is visible on every sale and velocity is only visible across a quarter.

---

## Why It Gets Ignored

Margin feels like skill. Negotiating ₦20k off a supplier is a satisfying, legible win. Selling four days faster is invisible — nothing happens, there is just no phone on the shelf anymore.

So attention flows to margin and away from velocity, and the business optimises the wrong variable while feeling competent.

---

## What This Changes

**1. Price to move, not to maximise.**
Once the 35% floor is cleared, an extra 5 points of margin that adds three weeks to sell-through is a loss. Run the arithmetic before holding out for a better price.

**2. Dead stock is a velocity failure, not a demand failure.**
A SKU sitting 90 days has not just failed to profit — it has consumed a slot that could have turned four times. The opportunity cost is roughly four times the margin that was foregone, which is why the clearance decision must have a deadline.

**3. Small, frequent buys beat large, cheap ones.**
A bulk discount that doubles the holding period usually destroys more value than it captures. Bulk quantity above normal sell-through gets its own qualification run.

**4. The listing bottleneck is the most expensive bottleneck in the business.**
Stock that has landed but is not published is capital at zero velocity, and it is entirely self-inflicted. This is why `heartbeat.py` flags approved-but-unpublished listings at 7 days — it is the cheapest possible fix for the most avoidable loss.

**5. Velocity protects against FX.**
Fast turns mean less exposure to a naira move between PO and sale. In a volatile currency, speed is a hedge that costs nothing.

---

## The Cash Discipline

[[financial-fragility]] is documented in `me/identity.md` and it interacts badly with slow stock. When cash is tight, decision quality drops — and slow-moving inventory is precisely what makes cash tight while looking like an asset on the shelf.

Rules:
- **Never commit more than 60% of available capital to a single PO.** A stockout is recoverable. Being unable to act on a good opportunity is not.
- **Keep a reserve that covers one full return.** The ability to refund without argument is the thing that protects the trust position.
- **Slow SKUs get their capital released on a deadline, not on a feeling.**

---

## The Metric

`capital_efficiency = gross_profit ÷ average_capital_deployed`

Tracked in `performance/metrics.md`. It is the only number that answers "is this business actually working," because it collapses margin and velocity into one figure that cannot be gamed by either alone.

---

## Linked

[[gadget-index]] · [[gadget-pricing]] · [[dead-stock]] · [[financial-fragility]] · [[trust-as-margin]]
