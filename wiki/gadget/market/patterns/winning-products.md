---
sensitivity: private
entity_type: concept
name: Winning Product Patterns
last_updated: 2026-08-08
---

# Winning Product Patterns

What products that actually sold had in common. Promoted here only when **three or more** products share a trait and an outcome. Two is a coincidence.

This file is the calibration source for `qualify.py`. When a pattern is confirmed here, the scoring rubric in `playbooks/product-qualification.md` gets adjusted to reflect it. That feedback loop is the entire reason the OS gets better instead of just older.

---

## Confirmed Patterns

*None yet — the business has not logged enough outcomes. This is expected on day one and should not stay true past 10 sold SKUs.*

**Pattern entry format:**

```markdown
### [Pattern name]
**Confirmed:** YYYY-MM-DD — [N] products
**Observation:** [the trait these products shared]
**Outcome:** [what consistently happened — sell-through days, margin achieved, return rate]
**Evidence:** [product slugs]
**Scoring change:** [what changed in the rubric because of this, or "none — informational"]
```

---

## Hypotheses Under Test

Not yet patterns. These are predictions written down *before* the data arrives, so the OS cannot quietly rewrite history afterwards. Each gets confirmed or killed once three products test it.

**H1 — The flaw-first listing outsells the clean listing.**
A listing that names a specific cosmetic flaw and prices for it will sell faster than a "clean" listing at a similar price, because the named flaw is proof the unit was inspected.
*Test:* compare days-to-sell on flaw-named vs generic listings. *Status:* untested.

**H2 — Battery health above 89% is a price cliff, not a slope.**
Buyers appear to treat 90% as a threshold. A unit at 89% may need a disproportionate discount versus 91%.
*Test:* track sale price against battery health across 5+ used iPhones. *Status:* untested.

**H3 — Anchor + attach beats anchor alone.**
Offering the case and charger as a bundle at point of sale converts better and protects the anchor price better than any equivalent discount.
*Test:* track attach rate and final margin with and without the bundle offer. *Status:* untested.

**H4 — One-generation-old flagships are the margin sweet spot.**
Current-gen has public pricing and thin margin. Three generations back is a price-only buyer. The generation just replaced is where a trust premium is actually payable.
*Test:* compare achieved margin by device generation across 6+ sales. *Status:* untested.

**H5 — Referral buyers negotiate less and return less.**
*Test:* tag every sale as referral or cold. Compare discount given and return rate. *Status:* untested.

---

## How to Log an Outcome Toward a Pattern

Every sold-out or retired SKU gets its outcome written into its product node under `## Outcome`. Then:

1. Check whether it shares a trait with two other logged products.
2. If yes — write a confirmed pattern block above.
3. If it confirms or kills a hypothesis — update the hypothesis status here with the evidence.
4. If it changes how a product should be scored — update `playbooks/product-qualification.md` and note the change in the pattern block.

The loop only closes if step 4 happens. A pattern nobody scores against is a diary entry.

---

## Linked

[[gadget-index]] · [[dead-stock]] · [[product-qualification]] · [[gadget-intelligence]]
