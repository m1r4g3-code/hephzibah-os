---
sensitivity: private
entity_type: concept
name: Simulated World for AI Models
aliases: [simulated-world, ai-society, agent-world]
last_updated: '2026-06-07'
type: startup-idea
stage: idea — long horizon, depends on [[digital-twin]]
relationships:
- target: '[[persistent-ai-thesis]]'
  type: part_of
  strength: 9
  first_seen: '2026-06-07'
  last_reinforced: '2026-06-07'
- target: '[[digital-twin]]'
  type: reinforces
  strength: 8
  first_seen: '2026-06-07'
  last_reinforced: '2026-06-07'
- target: '[[ai-memory-system]]'
  type: reinforces
  strength: 7
  first_seen: '2026-06-07'
  last_reinforced: '2026-06-07'
---

# Simulated World for AI Models

**Layer 3 — the long horizon of the [[persistent-ai-thesis]]. The north star, not the next build.**

## The Idea (Emmanuel's framing)

> A simulated world where AI models act like humans in a world.

## What It Involves

- Multiple AI entities.
- Human-like behavior.
- A shared environment.
- Interaction between agents.
- Emergent behavior.
- A persistent world where AI "lives" rather than just responding to prompts.

```text
World
 ↓
Many AI Agents
 ↓
Interaction
 ↓
Society-like behavior
```

## Why It's Last

It needs the other two to exist first. The inhabitants of the world are [[digital-twin]]s; the twins need [[ai-memory-system]] to have continuity. Without memory and twins, a "simulated world" is just a multi-agent demo that resets every run — there's no *persistence*, which is the whole point.

## Where This Already Exists (study these)

This isn't sci-fi — it's an active research frontier. Prior art worth studying before building:
- **Stanford "Generative Agents" (Smallville)** — 25 agents in a town, memory + reflection + planning, emergent social behavior. The closest existing thing to this idea.
- **Voyager / agent sandboxes** — agents that persist and learn in an environment over time.

## Open Design Questions

- **What's the point of the world?** Research sandbox? Training environment for twins? Product (e.g. simulate how a market/team/customer base reacts)? The *use case* decides everything.
- **Emergence vs control** — how much do you script vs let arise?
- **Cost** — many persistent agents interacting is expensive; ties directly back to the cheap-memory problem in [[ai-memory-system]].

## Note

The most commercially grounded framing: a simulated world is a **prediction engine**. Populate it with twins of real people (a customer base, a team, a market) and you can simulate how they'd react to a decision before you make it. That makes it the [[kairos]] "predictor mech suit" pattern at societal scale.

## Wikilinks

[[persistent-ai-thesis]] · [[digital-twin]] · [[ai-memory-system]] · [[kairos]]
