---
sensitivity: private
entity_type: concept
name: Digital Twin of a Person
aliases: [digital-twin, person-twin, self-model]
last_updated: '2026-06-07'
type: startup-idea
stage: idea — depends on [[ai-memory-system]]
relationships:
- target: '[[persistent-ai-thesis]]'
  type: part_of
  strength: 9
  first_seen: '2026-06-07'
  last_reinforced: '2026-06-07'
- target: '[[ai-memory-system]]'
  type: reinforces
  strength: 8
  first_seen: '2026-06-07'
  last_reinforced: '2026-06-07'
- target: '[[simulated-world]]'
  type: reinforces
  strength: 8
  first_seen: '2026-06-07'
  last_reinforced: '2026-06-07'
---

# Digital Twin of a Person

**Layer 2 of the [[persistent-ai-thesis]]. Needs [[ai-memory-system]] first.**

## The Idea (Emmanuel's framing)

> A digital twin that is exactly me (or anyone else) and can do future things as if it were me.

Not a chatbot that knows facts about you. A persistent model of *how you think* that can act on your behalf and predict what you'd do.

## What It Captures

- Not just remembering facts — capturing how a person thinks.
- Acting on their behalf.
- Predicting decisions.
- Simulating future actions.
- Becoming a persistent representation of a person.

```text
Human
 ↓
Experiences
 ↓
Knowledge
 ↓
Behavior
 ↓
Digital Twin
```

## Why It Depends on Memory

A twin is only as real as the memory under it. Facts come from memory; *behavior* comes from patterns across that memory over time. You can't model how someone decides until you've captured enough of how they've decided. So [[ai-memory-system]] is the substrate — the twin is what you build on top once memory holds identity reliably.

## Open Design Questions

- **Behavior ≠ knowledge.** Capturing decision *patterns*, values, and risk tolerance — not just stored facts.
- **Prediction validation.** How do you test that the twin would actually do what the person would? (Backtest against past decisions — the [[kairos]] calibration instinct applies here.)
- **Drift.** People change. The twin must update as the person evolves, not freeze them.
- **Authorization & trust.** A twin acting "as you" is a security and identity problem, not just an ML one.

## Note

The brain itself is a primitive self-model. [[identity]], [[goals]], [[engineering]], and the coaching nodes already encode how Emmanuel thinks and decides. A twin is what happens when that's made *predictive and agentic* rather than descriptive.

## Wikilinks

[[persistent-ai-thesis]] · [[ai-memory-system]] · [[simulated-world]] · [[identity]] · [[kairos]]
