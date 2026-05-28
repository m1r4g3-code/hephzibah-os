---
sensitivity: private
entity_type: concept
name: Pricing Philosophy
aliases: ["upwork-pricing", "rate-strategy", "quote-system"]
last_updated: 2026-05-28
relationships:
  - target: "[[identity]]"
    type: part_of
    strength: 10
    first_seen: "2026-05-28"
    last_reinforced: "2026-05-28"
  - target: "[[elite-freelancer-model]]"
    type: reinforces
    strength: 9
    first_seen: "2026-05-28"
    last_reinforced: "2026-05-28"
---

# Pricing Philosophy

Upwork reality: the client sets the budget. Fixed price or hourly. This system exists for three
things:
1. Reading a posted budget as a signal — not a ceiling
2. Deciding bid price relative to scope
3. Generating accurate SOW pricing after discovery calls (full pricing control)

Use `python scripts/quote.py` for all calculations.

---

## Reading Client Budgets

**Fixed price:** Their estimate of what it costs. Often wrong — based on what a cheap freelancer
quoted them, or a number they invented. Not the ceiling.

**Hourly:** Their estimate of fair pay. Always bid at the top of their stated range or above it.
Bidding at the bottom signals you don't believe in your own value.

**Budget as a client quality signal:**
- Under $300 for a complex build → commodity mindset, scope blindness, or bad experience. JSS risk.
- $0 spend history + low budget → window shopper. Skip.
- High budget relative to simple scope → serious buyer or confused. Qualify before bidding.

---

## Bid Pricing Logic

```
Client budget vs our scope estimate (run quote.py to get estimate):

  budget >= estimate x 1.1   →  BID_AT_BUDGET  — offer scope expansion
  budget within 10% either   →  BID_AT_BUDGET  — aligned, straightforward
  budget < estimate x 0.85   →  BID_ABOVE      — reframe in proposal, justify clearly
  budget < estimate x 0.60   →  REFRAME_OR_SKIP — serious mismatch
  budget < estimate x 0.40   →  SKIP           — commodity signal, not worth JSS risk
```

**Bidding above their budget:**
The proposal must contain a reframe — not an apology. One line that earns the higher number:
"Most implementations skip [X], which is why they take twice as long and need rework. I include
[Y] in scope — that's the difference in price, and the difference in outcome."

**The Ramshaw example:** 60 people bid $4–5k. He bid $15k. He got it. Premium price signals
premium capability. Cheap pricing attracts clients who will extract maximum work for minimum pay.

Never negotiate yourself down in the proposal text. Hold the number. Explain the value.
If they push back: scope conversation, not price conversation.

---

## Rate Anchors

Reference points for SOW generation. Adjust for client quality, scope clarity, and niche.

| Project Type | Core | Full | Premium |
|---|---|---|---|
| Simple integration (webhook, single API) | $500 | $700 | $1,000 |
| Automation workflow (n8n, Make, Zapier) | $1,500 | $2,200 | $3,000 |
| Multi-system pipeline (3+ systems + AI) | $3,500 | $5,000 | $7,000 |
| Full AI agent (Claude + tools + interface) | $5,000 | $7,500 | $10,500 |
| Complex enterprise build | $8,000 | $12,000 | $18,000+ |
| Hourly consulting | $65/hr | $80/hr | $95/hr |

**Tier definitions:**
- **Core:** Stated deliverables only. No extras, no full documentation, no post-delivery support.
- **Full:** Core + optimizations, error handling, full documentation, 1-week question support.
- **Premium:** Full + 30-day support, training walkthrough, monitoring setup, one change order free.

Present all three tiers in every SOW. Most clients who engage pick Full. Core makes Full look
reasonable. Premium makes Full look conservative. Never present only one number.

---

## Payment Structure (Non-Negotiable)

40% upfront — due before any work starts
30% at midpoint milestone
30% at delivery

No work starts without the 40% paid. Any client who pushes back on this is a payment risk.
Flag it in the client node. Walk away if they insist — a client who won't pay upfront won't
pay at the end either.

For change orders: 50% upfront / 50% at delivery. Simpler for smaller additions.

---

## Change Orders

When scope expands beyond the SOW:
1. Stop. Do not absorb extra work silently.
2. Name it: "This is outside what we scoped. Happy to add it — here's what that looks like."
3. Send a mini SOW for the new item with the additional fee.
4. Collect 50% before starting the addition.

Never do extra work hoping the client appreciates it. They won't. They'll expect it included next time.

---

## Pricing Red Flags

| Signal | Risk |
|---|---|
| "Can you do it cheaper?" before scope discussion | Commodity buyer |
| "Trial project first" | Not paying for your learning curve |
| "Budget is tight but lots of future work" | Speculation. Not money. |
| Pushes back on 40% upfront | Payment risk — walk away |
| "Per task" or "as needed" scope | Undefined scope = JSS risk |
| "Available immediately" or "daily check-ins" | Micromanager signal |

---

## Wikilinks

[[elite-freelancer-model]] · [[identity]] · [[job-scoring]] · [[client-quality-score]]
