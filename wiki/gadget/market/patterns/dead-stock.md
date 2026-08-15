---
sensitivity: private
entity_type: concept
name: Dead Stock Patterns — What Not To Buy Again
last_updated: 2026-08-08
---

# Dead Stock Patterns

Products that tied up capital and did not move. The most expensive file in the domain and the most valuable one, because dead stock does not announce itself as a loss — it sits on a shelf looking like an asset.

Same rule as the winning patterns: three products sharing a trait and an outcome makes a pattern. One is bad luck.

---

## Confirmed Anti-Patterns

*None yet.*

**Entry format:**

```markdown
### [Anti-pattern name]
**Confirmed:** YYYY-MM-DD — [N] products
**The trait:** [what these products had in common]
**What happened:** [days sat, capital tied, eventual disposal, realised loss]
**Cost:** ₦[total capital that sat] over [N] days
**The tell we missed:** [what was visible BEFORE buying that should have stopped it]
**Scoring change:** [rubric adjustment made]
```

The **tell we missed** line is the one that has to be filled honestly. Every dead-stock decision looked reasonable when it was made. The value is in naming the signal that was present and got overruled.

---

## Known Dead-Stock Risks — Watch These From Day One

These are documented from market structure rather than from Hephzibah's own losses. They are the failure modes this business has not made yet.

**Buying into a launch window.**
Stocking the outgoing generation in the 6 weeks before an Apple or Samsung launch. Resale value drops 10–20% on announcement, and the stock is worth less than it cost before a single unit sells. **Rule: no bulk PO on a flagship within 6 weeks of its successor's expected announcement.**

**Colour and storage variants nobody asked for.**
The base colour and the mid storage tier move. The unusual colour and the 1TB variant sit. They look like the same product on a spreadsheet and behave completely differently. **Rule: variants get their own pipeline row and their own qualification.**

**Deep discount bulk buys.**
A supplier offers 20 units at a great price. The price is great because the market does not want 20 of them. The discount is the market telling you something and it is very easy to mishear as an opportunity. **Rule: bulk quantity above normal weekly sell-through needs its own `/product-qualify` run at the actual quantity.**

**Accessories bought as a standalone category.**
Accessories are pure margin *attached to a device sale*. Bought as their own line, they are low-ticket, high-count, slow-moving capital. **Rule: accessory quantity is capped at expected device sell-through, never bought independently.**

**Cosmetically damaged units bought "cheap enough to be worth it."**
There is no price low enough to make a hard-to-describe device easy to sell. The discount required to move it usually exceeds the discount received on it. **Rule: units below Grade B do not enter stock, at any price.**

**Holding through a strengthening naira.**
Stock bought at ₦1,700/$ and sold at ₦1,500/$ loses the difference on every unit, silently. It shows up as "prices came down" rather than as a loss. **Rule: no more than 3 weeks of stock in a strengthening window — see `market/intelligence.md`.**

---

## The Dead-Stock Review

Runs on the 1st of every month, or whenever `heartbeat.py` flags a SKU as `dead_stock`.

For each flagged SKU:

1. **Compute the real cost.** Capital tied × days held. Then ask what that capital would have earned in the best-performing SKU over the same window. That opportunity cost is the actual loss, and it is always larger than it feels.
2. **Decide once, with a date.** Liquidate at a set price by a set date, or retire it. Never "reduce it a bit and see." A slow bleed costs more than a clean cut and it consumes attention the whole time.
3. **Name the tell.** What was visible before the purchase? Write it above.
4. **Check for a third instance.** If this makes three of the same kind, write the confirmed anti-pattern and change the rubric.

---

## Linked

[[gadget-index]] · [[winning-products]] · [[product-qualification]] · [[gadget-pricing]]
