---
sensitivity: private
entity_type: concept
name: Product Qualification Playbook
last_updated: 2026-08-08
---

# Product Qualification — The Scoring Rubric

The single most important document in this domain. Every naira of capital the business commits passes through this rubric first.

**The gate: composite < 65 → SKIP. No exceptions.**

Not "skip unless the price is really good." Not "skip unless Yemi is confident." The gate exists precisely for the moments when the price looks really good and someone is confident — those are the conditions under which capital gets destroyed. Enforced by `scripts/qualify.py`.

---

## The Composite

```
composite = demand      × 0.30
          + margin      × 0.25
          + competition × 0.20      (inverted — high score = LOW competition)
          + fit         × 0.15
          + logistics   × 0.10
```

**Why demand is weighted highest.** In this market, sourcing is not a moat — anyone can walk into the same Computer Village stall and buy the same phone. What cannot be manufactured is people wanting the thing. A brilliantly sourced product nobody is searching for is capital sitting on a shelf. A mediocre deal on something in demand sells in a week.

**Why margin is second.** Margin is the risk buffer, not the profit. See `identity/pricing.md`.

**Why competition is inverted.** A crowded category is not proof of demand — it is proof that the demand is already being served by people with more stock and lower costs.

**Why logistics is only 10%.** It is a real cost but a knowable one. It rarely changes the decision on its own; it changes the price. The exception is import complexity, which can turn a good product into a three-month capital trap — that is why it is scored at all.

| Composite | Decision | What it means |
|---|---|---|
| **80–100** | **STOCK** | Move now. Sample, then bulk. |
| **65–79** | **WATCHLIST** | Real but not compelling. Stock only with a specific edge — better cost, existing demand from a waiting buyer, or it completes a bundle. |
| **< 65** | **SKIP** | No. Log it and move on. |

---

## Hard Disqualifiers — Checked Before Scoring

If any of these are true, the product is dead regardless of composite. Run this list first; it costs 60 seconds and saves the scoring work.

| Disqualifier | Why |
|---|---|
| Category is in the OUT table of `identity/niche.md` | Brand gate. Absolute. |
| Gross margin below 35% at realistic pricing | Margin gate. Absolute. |
| Counterfeit, replica, or "AAA copy" | Brand gate. Ends the business, not just the deal. |
| Cannot verify IMEI / provenance | Legal and reputational exposure. |
| Grade below B | No price is low enough to make a hard-to-describe device easy to sell. |
| Sole-source with no backup, on a top-5 SKU | Supplier gate. Fix the sourcing or skip. |
| Bulk PO within 6 weeks of the successor model's expected launch | Guaranteed 10–20% value drop before the stock sells. |
| Capital required exceeds available buying capital | Cash gate. Stock that cannot be paid for is not a decision, it is a wish. |

---

## Scoring Each Dimension

### 1. Market Demand (30%)

*Is anyone actually looking for this, and is that number going up or down?*

| Score | Condition |
|---|---|
| 90–100 | Buyers asking for it unprompted. Existing waiting list. Clear upward trend. |
| 75–89 | Strong steady demand. Consistent search and listing activity. Well-known model. |
| 60–74 | Moderate. Sells, but needs to be found and pushed. |
| 40–59 | Thin. Niche appeal. Long sell-through. |
| 0–39 | Declining or nonexistent. Superseded, obsolete, or unknown. |

**Evidence to gather, in order of quality:**
1. Actual inbound requests — someone asked for it. This is the only first-party signal and it outranks everything below.
2. Jiji / marketplace listing count and how fast listings disappear.
3. Google Trends for the model name, Nigeria, 12 months.
4. Competitor posting frequency — sellers post what moves.
5. Yemi's read from the physical market. Weight this heavily; it is the fastest signal available and it is usually right.

**Trend beats level.** A product with moderate but rising demand beats one with high but falling demand, every time. Stock arrives in the future, not today.

---

### 2. Margin Potential (25%)

*What is the realistic gross margin at landed cost against achievable price?*

| Score | Gross margin at realistic pricing |
|---|---|
| 90–100 | 55%+ |
| 75–89 | 45–54% |
| 60–74 | 38–44% |
| 35–59 | 35–37% — at the floor, no room for anything to go wrong |
| 0 | Below 35% — **hard disqualifier** |

**"Realistic" is doing all the work in that sentence.**
- **Landed** cost, not invoice. Full stack from `identity/pricing.md`.
- **Achievable** price, not aspirational. What comparable units actually sold for in the last 30 days, minus the 5–8% negotiation room that will be conceded.
- Include the loss provision for the category.

The most common failure in this business is scoring margin on the invoice price and the asking price. That combination flatters every product and has no relationship to what lands in the account.

---

### 3. Competition (20%) — Inverted

*How crowded is this? Higher score = less crowded = better.*

| Score | Condition |
|---|---|
| 90–100 | Almost nobody selling it locally. Real supply gap. |
| 75–89 | Few sellers, none with a trust position. Room to own it. |
| 60–74 | Competitive but differentiable — inspection and documentation still win. |
| 40–59 | Crowded. Price is the main axis. Margin under pressure. |
| 0–39 | Saturated. Race to the bottom already running. |

**Score the differentiability, not just the count.** Twenty sellers with generic "UK used, neat, DM for price" listings is *less* competitive than five sellers publishing battery health and named flaws. The first group is not competing for the same buyer at all.

---

### 4. Brand Fit (15%)

Scored directly from the table in `identity/niche.md`. IN category and premium signals accumulate; OUT category is a zero and a hard stop.

The question underneath the points: **does selling this make Hephzibah Gadgets a more specific thing, or a less specific one?** Every product either sharpens the position or blurs it. Blurring is slow and never feels like a decision, which is why it needs a score.

---

### 5. Logistics (10%)

| Score | Condition |
|---|---|
| 90–100 | Light, robust, pocket-sized, sourced locally, no import. |
| 75–89 | Compact, reasonably robust, simple import if any. |
| 60–74 | Moderate size or some fragility. Manageable. |
| 40–59 | Bulky, fragile, or complex import. Needs special handling. |
| 0–39 | Heavy, very fragile, regulated, or long/uncertain import chain. |

Factors: weight and volume, fragility (screens, glass), battery shipping restrictions, customs treatment, capital cycle time (how long money is tied up in transit), and warranty exposure if it fails.

**Cycle time is the underrated one.** A 10-week import chain ties capital for 10 weeks, during which the FX can move, a launch can happen, and demand can shift. A product with good margin and a long chain is riskier than its score suggests.

---

## The Qualification Pipeline

```
1. HARD DISQUALIFIERS   → any hit = SKIP, stop here
2. GATHER EVIDENCE      → demand signals, real cost, competitor listings
3. SCORE 5 DIMENSIONS   → each with written reasoning, not just a number
4. RUN qualify.py       → composite + decision
5. INVERSION PASS       → "what would make this a mistake?" before committing
6. DECISION             → STOCK / WATCHLIST / SKIP
7. WRITE THE NODE       → products/active/[sku].md, add to _PIPELINE.md
8. IF STOCK             → sample first. Quality gate. Always.
```

**Step 5 is not optional and it is not the same as scoring.** Scoring asks "how good is this?" Inversion asks "how does this go wrong?" Run it explicitly: *If this product ends up as dead stock in 90 days, what will the reason have been?* If the honest answer is something knowable today, it is not a risk — it is a fact that has not been scored yet.

---

## Sample Before Bulk — The Quality Gate

**Every new product from every new supplier gets a sample order before a bulk PO. No exceptions.**

The sample is not about whether the product is good. It is about whether *this supplier's version* of the product is good, and about what happens when something is wrong with it.

The sample tests six things:
1. Does the unit match the description?
2. What is the *actual* lead time versus the quoted one?
3. What is the packaging like — will it survive a courier?
4. How does the supplier respond when a problem is raised?
5. Are there defects that are invisible until the unit is in hand?
6. Does the landed cost match the projection?

A supplier who is excellent on a sample and terrible at volume is common. A supplier who is bad on the sample is never good at volume. Skipping the sample to move fast is how a business converts one bad decision into twenty units of bad decision.

---

## Rubric Calibration

This rubric is a hypothesis about what predicts success. It gets corrected by outcomes.

Every time a pattern is confirmed in `market/patterns/`, ask: **would this rubric have caught it?** If a product scored 82 and became dead stock, something in the rubric is wrong — find it and change it. Log every change here.

| Date | Change | Reason |
|---|---|---|
| 2026-08-08 | Initial rubric | Foundation build. Weights set from market structure reasoning, not yet from outcome data. Expect the first real revision after 10 logged outcomes. |

---

## Linked

[[gadget-index]] · [[gadget-niche]] · [[gadget-pricing]] · [[winning-products]] · [[dead-stock]]
