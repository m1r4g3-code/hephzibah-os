---
sensitivity: private
entity_type: domain
name: Winning Signals
last_updated: 2026-05-27
---

# Winning Signals

Patterns from proposals that got replies, interviews, or wins. Each pattern confirmed by 3+ observations. Start adding after first 20 proposals.

Append-only. Mark superseded patterns, never delete.

---

## Active Patterns

None confirmed yet. Need 3+ observations per pattern.

---

## Hypothesis Queue (1-2 observations — not yet confirmed)

None yet.

---

## Confirmed Pattern Template

```
### Pattern: [Name]

**Confirmed:** [date]
**Observations:** [N]
**Evidence:** [proposal slugs that showed this]

**What it is:** [description]
**Why it works:** [hypothesis]
**How to apply:** [specific instruction]

**Status:** Active | Superseded [date]
```

---

## How Patterns Get Confirmed

1. `/log-outcome` is run for a won/replied proposal
2. Learning is extracted and stored in the proposal file
3. `/strategy-review` checks for proposals with shared characteristics + shared positive outcome
4. After 3 matches: pattern is moved from hypothesis to confirmed

---

## Wikilinks

[[red-flags]] · [[proposal-framework]] · [[metrics]]
