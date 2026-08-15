---
sensitivity: private
entity_type: domain
name: Gadget Pricing — Margin Targets and Philosophy
last_updated: '2026-08-09'
---

# Pricing — Margin Targets and Philosophy

## The Hard Floor

**35% gross margin. Below it, do not stock. No exceptions.**

This is a gate, not a target. The reasoning, because a gate nobody understands gets argued with at the worst possible moment:

A 20% margin on a ₦400k phone is ₦80k. That feels like money. Then one unit comes back with a fault (–₦400k until it's resold), the naira moves 8% between the PO and the sale (–₦32k on the batch), a courier loses one (–₦400k), and a buyer negotiates ₦15k off. The batch is now underwater and the operator is working for free while carrying all the risk.

35% is not greed. It is the number where a single normal-sized thing going wrong does not erase the batch. In a market with FX volatility, no reliable warranty upstream, and physical handling risk on every unit, the margin **is** the risk buffer.

**Corollary that matters more than the number:** when a product cannot clear 35%, the answer is almost never "sell it at 22% anyway." It is "source it better or sell something else."

---

## Margin Targets by Category

Floor is 35% everywhere. Targets are what a well-run version of this business achieves.

| Category | Floor | Target | Notes |
|---|---|---|---|
| Used premium phones | 35% | **42–50%** | The anchor. Inspection work is what earns the spread. |
| New sealed phones | 35% | 36–40% | Thin by nature — market price is public. Sell for the frame, not the money. |
| Premium audio | 35% | **45–55%** | Highest margin category. Counterfeit fear does the selling. |
| Power & charging | 40% | 50–60% | Low ticket needs a higher percentage to be worth the handling. |
| Wearables | 35% | 42–50% | Battery health drives the whole valuation. |
| Laptops | 35% | 38–45% | High ticket, slow turn. Percentage matters less than absolute naira. |
| Accessories (attach) | 50% | 60–70% | Only sold attached. Pure margin on an already-won sale. |

---

## Landed Cost — What Actually Counts as COGS

The single most common way a gadget business believes it is profitable while losing money is calling the invoice price "cost."

**Landed cost = every naira spent to get one sellable unit into a buyer's hands.**

```
  invoice price (at the FX rate actually paid, not the rate quoted)
+ freight / shipping share per unit
+ customs and clearing per unit
+ inbound transport (Computer Village → storage)
+ inspection and testing time (₦2,000/unit standing charge)
+ accessories included in the box (cable, case, protector)
+ outbound delivery if absorbed rather than charged
+ payment processing fees
+ expected loss provision  ← see below
= LANDED COST
```

**Expected loss provision.** Add a per-unit percentage for units that will not sell at full price. This is not pessimism, it is arithmetic — some percentage always does.

| Category | Provision |
|---|---|
| Used phones | 5% |
| New sealed | 2% |
| Audio | 4% |
| Power & charging | 3% |
| Laptops | 7% |

`gross_margin_pct = (selling_price − landed_cost) / selling_price × 100`

Margin on **selling price**, not on cost. ₦100k cost sold at ₦150k is a 33% margin, not 50%. Getting this backwards is how a business talks itself past its own floor.

---

## The FX Rule

Any product with USD or GBP cost exposure is priced at the rate the operator can **actually buy at today, plus 5%.**

Not the official rate. Not the rate from last week. Not the rate the supplier quoted. The parallel-market rate available right now, plus a 5% buffer for the gap between committing to a PO and selling the last unit of the batch.

If the naira moves more than 7% against the PO rate before the batch clears, **re-price the remaining units immediately.** Selling the tail of a batch at the old rate is a silent transfer of the whole batch's profit to the last buyers.

Record the PO-date rate in the product node. Without it, margin cannot be reconstructed and there is no way to know whether a product was actually profitable or just lucky on timing.

---

## Pricing Philosophy — Six Rules

**1. Price against certainty, not against the market.**
The competitor is not the ₦380k listing on the timeline. It is that listing *plus* the buyer's risk of getting a bad unit from a stranger. Hephzibah sells the same device with the fear removed. That is worth 10–15% and it should be charged for.

**2. Never be the cheapest. Never be more than 20% above the honest market.**
Below the market invites suspicion — buyers assume something is wrong. More than 20% above needs a reason the buyer can see on the listing (warranty, documented inspection, same-day delivery). Between those, the position is defensible.

**3. One price, stated up front, small negotiation room built in.**
Nigerian buyers will negotiate. That is not a problem to fight, it is a mechanic to design for. Build 5–8% of room into the listed price and concede it once, deliberately, in exchange for something — immediate payment, collection today, buying the case too. Never concede twice. A second concession tells the buyer the first price was fiction and the third is coming.

**4. Bundle instead of discounting.**
"I can't move on the price, but I'll put the case and the 20W charger in the box" costs ₦8k of landed cost and reads as ₦20k of value. A ₦20k discount costs ₦20k. Bundling protects the price anchor for the next buyer, discounting destroys it.

**5. Anchor high, then justify.**
Lead with the flagship-spec unit, then present the one being sold. The buyer's reference point is set by the first number they see.

**6. Clearance is a decision with a deadline, not a slow bleed.**
Dead stock (60+ days live, <2 units sold) gets one clearance decision: liquidate at a set price by a set date, or retire it and stop spending attention on it. Slowly dropping the price by ₦5k a week is the most expensive way to sell anything — it burns capital, attention, and the price anchor at the same time. **Trapped capital is a real cost even though it never appears as a loss.**

---

## Payment Terms

| Situation | Terms |
|---|---|
| Hand delivery (Lagos) | Full payment on inspection. Buyer inspects first, then pays. |
| Courier (nationwide) | Full payment before dispatch. Video of the unit + packing sent before it leaves. |
| Pre-order / custom import | **50% deposit, non-refundable after the PO is placed.** Balance before dispatch. |
| Swap | Valuation given with reasoning. Difference settled in full at handover. |
| Bulk / reseller | 50% deposit, balance on delivery. Never full credit. |

**No exceptions on the pre-order deposit.** Direct inheritance of [[middleman-lesson]] — Emmanuel built and delivered without protection and never got paid for the last job. The same rule that protects him from clients protects him from buyers who change their mind after a PO is committed.

---

## When Emmanuel Wants to Break the Margin Gate

He will. Usually when cash is tight — which is exactly when [[financial-fragility]] makes the decision worst.

The OS response, in order:
1. State the actual margin number and the actual naira at risk.
2. Name what has to go right for it to work — and how likely that is.
3. Offer the reframe: *"At this cost you can't hit 35%. What would the cost need to be? Can Yemi get it there, or is there a different SKU that clears the gate today?"*
4. If he insists after all that: it is his business and his call. Log it with `forced_stock: true` in the product node so the outcome data is marked and the pattern is visible later.

Never just comply silently. Never lecture twice.

---

## Linked

[[gadget-index]] · [[gadget-niche]] · [[gadget-brand]] · [[middleman-lesson]] · [[financial-fragility]]

### HARD RULE — no vendor cost on a public surface — 2026-08-09 12:29

Set by Emmanuel, 2026-08-09: *"u need approved price and always add profit price, because when customer see the price they stick to that."*

**The rule: every number that reaches a customer is a SELLING price. Vendor cost never appears on a public surface. Ever.**

Not on a story, not in a comparison, not in a WhatsApp reply, not "just as a rough idea".

### Why it is absolute

Anchoring is permanent and one-directional. The first number a buyer sees becomes the number they believe the phone is worth, and every figure after it reads as a mark-up rather than a price. A cost quoted once cannot be walked back — "that was my cost" sounds like an excuse even when it is true, and it tells the buyer exactly how much margin there is to argue over.

It also leaks the sourcing position. A buyer who knows Yemzy's number can go to Yemzy.

### The mechanic



Bands are in  (): ₦10k under ₦150k, ₦20k to ₦350k, ₦30k to ₦600k, ₦40k above. Split 50/50 with Yemi afterwards.

### Where this nearly went wrong

The iPhone 14 Pro vs 15 comparison drafted on 2026-08-09 used ₦600,000 and ₦610,000. Both were vendor medians pulled straight from the parsed Yemzy feed. Correct public figures are **₦640,000 and ₦650,000**.

**The failure mode is specific and worth naming:**  outputs vendor cost, because that is what the group posts. Anything drawn from that file is a cost until profit is added. Every price that moves from the price ladder onto a customer-facing surface has to pass through the band first.

### Companion rule — confirm before publishing

Also set 2026-08-09. Nothing goes on a public surface unverified: a price, a spec, a battery figure, a date, a claim about what a phone can do. Check it, or attribute it ("seller states"), or leave it out. The brand is built on the numbers being true, so a single confident wrong figure costs more than the post earns.
