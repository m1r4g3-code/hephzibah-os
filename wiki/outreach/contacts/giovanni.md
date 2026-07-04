---
sensitivity: private
entity_type: person
name: Giovanni
aliases: [giovanni-seraman]
tags: [active-client, italian]
company: SERAMAN
platform: Fiverr
email: seraman.adv@gmail.com
website: shop.seraman.com
country: Italy
status: active
introduced_by: Oba (Adelaja O.)
last_updated: '2026-06-28'
relationships:
- target: '[[seraman]]'
  type: works_at
  strength: 10
  first_seen: '2026-06-28'
  last_reinforced: '2026-06-28'
- target: '[[identity]]'
  type: targeted_by
  strength: 9
  first_seen: '2026-06-28'
  last_reinforced: '2026-06-28'
- target: '[[oba]]'
  type: mentioned_in
  strength: 7
  first_seen: '2026-06-28'
  last_reinforced: '2026-06-28'
- target: '[[n8n]]'
  type: has_pain
  strength: 8
  first_seen: '2026-06-28'
  last_reinforced: '2026-06-28'
---

# Giovanni — SERAMAN

Active client. Italian. Runs **SERAMAN** — a tactical and military gear brand (sunglasses, boots, bandages, medical equipment). Website: shop.seraman.com.

Introduced by [[oba]] (Adelaja O.) — originally Oba's Fiverr client. Oba managed client relationship, Emmanuel built the entire pipeline. Revenue split 50/50. Oba back in Lagos ~July 2026 — long-form build will be done together then.

## Financials

| Milestone | Amount | Status |
|---|---|---|
| Milestone 1 | $1,000 | Delivered — 5-star review |
| Milestone 2 | $1,000 | In progress |
| Long-form pipeline (5–8 min) | $1,500 | Scoped, not started |

**Total potential: $3,500+**

## Review (Milestone 1 — 5 stars)

> "Excellent work, fast and super professional. Perfect communication. They were able to produce what I asked for, modifying it as requested. Delivery was early. Highly recommended!!!"
> Seller communication: 5 | Quality: 5 | Value: 5

## The Pipeline Built

Full automated content pipeline (6 workflows):

```
Tally Form → n8n → Claude AI (Italian script)
  → Kie AI Veo 3.1 (dual-branch parallel)
  → Creatomate (assembly + captions)
  → Blotato (4-platform social publishing)
  → Branded email notifications (success + error)
  → Google Sheets (3-sheet tracking)
```

Architecture: dual-branch parallel Kie AI generation (Branch A: scenes 1+8, Branch B: scenes 2-7), async state machines, retryCount 20, regenCount 3 per scene, item-identity integrity (scene_number travels explicitly through all nodes), Claude v4 trust-first prompt (Product → Experience → Feature → Benefit).

## M2 Bugs (2026-06-28)

1. English caption "That changes everything" — caption field pulling video_prompt (English) instead of voiceover_text (Italian). Fix: change field source in Edit Videos Code node.
2. Doubled/garbled captions — second text element in Creatomate template. Fix: delete it.
3. "s bliped" hallucinated background text — Kie AI reads blurry environmental text on set. Fix: add full environment no-text block to every presenter scene prompt.
4. Hallucinated label on CVN4 package — product name in opening dialogue declaration. Fix: move name mid-sentence, no-text block at START of prompt.
5. Skull and crossbones on CVN4 — TCCC + "no second chance" language triggers danger symbol association. Fix: add `no skulls no crossbones no danger symbols no hazard markings` at top of prompt.
6. Wrong product form — per-scene product images not supported. Fix: pick one form per video, or add per-scene image support to schema.

**System prompt fix (v5.1 → v5.2):** No-text rules block must be FIRST. Dialogue must not open with product name as standalone declaration. Remove Think tool from LangChain agent (incompatible with Structured Output Parser).

## Strategy

M2 delivery includes scene-level approval + selective regen system (not charged as M3 — rebuilds trust after QC issues). Long-form $1,500 pitched as clean M3 from restored trust position.

## Client Stack (his side)

Kie AI (pay-per-use) · Creatomate ($29/mo) · Blotato ($29/mo) · n8n · Google Sheets · Tally form

## Flags

- Green: pays, reviews promptly, expanding scope
- Green: Italian speaker — content stays in Italian
- Green: long-form already scoped at $1,500
- Watch: Blotato posting failed once (execution 279) — social publishing still being confirmed

## Wikilinks

[[seraman]] · [[oba]] · [[n8n]] · [[claude-api]] · [[identity]]
