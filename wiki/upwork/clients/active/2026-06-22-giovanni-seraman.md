---
sensitivity: private
entity_type: person
name: "Giovanni"
company: "SERAMAN"
platform: "Fiverr"
website: "shop.seraman.com"
email: "seraman.adv@gmail.com"
country: "Italy"
category: "Tactical / Military Gear (sunglasses, boots, medical equipment)"
status: "active"
quality_score: 90
introduced_by: "Oba (Adelaja O.)"
---

## Client Overview

Giovanni runs SERAMAN — an Italian tactical and military gear brand selling products like sunglasses (Gator Spectre), boots (AKU Tactical), bandages, and other gear via shop.seraman.com. He was originally a freelancer client of Oba's, who introduced the automation opportunity.

## Project: AI Video Production System

**Platform:** Fiverr (via Oba's account — 50/50 split)
**Partnership:** Emmanuel built the entire pipeline solo. Oba managed client relationship and follow-up. Revenue split 50/50. Oba currently in Ibadan, back in Lagos ~July 2026 — long-form build will be done together.
**Status:** Milestone 1 complete. Milestone 2 functionally complete — pipeline proven end-to-end 2026-07-06, final video with Giovanni for approval.

**What was built:**
Full automated pipeline — Tally Form → n8n → Claude AI (Italian script) → Kie AI Veo 3.1 (video generation, dual-branch parallel) → Creatomate (video assembly + captions) → Blotato (social publishing to 4 platforms) → branded email notifications (success + error). Google Sheets tracks every run across 3 sheets.

**Architecture highlights:**
- Dual-branch parallel Kie AI generation (Branch A: scenes 1+8, Branch B: scenes 2-7)
- Async state machines, retryCount 20, regenCount 3 per scene
- item-identity integrity — scene_number travels explicitly through all nodes
- Claude v4 trust-first prompt (Product → Experience → Feature → Benefit)
- 4 modular n8n workflows: Product Automation, Generate Videos, Edit Videos, Error Handler

## Financials

| Milestone | Amount | Status |
|---|---|---|
| Milestone 1 | $1,000 | Delivered — 5-star review |
| Milestone 2 | $1,000 | In progress |
| Long-form pipeline (5–8 min) | $1,500 | Scoped, not started |

**Total potential:** $3,500+

## Review (Milestone 1)

> "Excellent work, fast and super professional. Perfect communication. They were able to produce what I asked for, modifying it as requested. Delivery was early. Highly recommended!!!"
> — Seller communication: 5 | Quality: 5 | Value: 5

## Flags

- **Green:** Pays, reviews promptly, clear feedback, expanding scope
- **Green:** Italian speaker — product content stays in Italian
- **Green:** Long-form project already scoped at $1,500
- **Watch:** Blotato posting failed once (execution 279, "Call Seraman Post to Socials") — social publishing still being confirmed

## M2 Testing — Bugs Found (2026-06-28)

Two test videos run: Gatorz Magnum OPz sunglasses + CVN4 Tactical Responder Bandage.

**Confirmed bugs (all root-caused):**

1. **English caption "That changes everything" (sunglasses video, frame 4)**
   Root cause: n8n Edit Videos Code node maps `video_prompt` (English) to Creatomate caption field instead of `voiceover_text` (Italian).
   Fix: Change caption field source in Edit Videos Code node to `voiceover_text`.

2. **Doubled/garbled captions (sunglasses video, frame 9)**
   Root cause: Creatomate template has a second text element also receiving voiceover_text.
   Fix: Delete second text element in Creatomate template editor.

3. **"s bliped" hallucinated background text (sunglasses video, frame 9)**
   Root cause: Kie AI reads blurry store shelf packaging and completes partial text. "no text overlays" doesn't cover environmental surfaces.
   Fix: Add full environment text block to every presenter scene prompt. See [[kie-ai-veo3-prompt-engineering]].

4. **Hallucinated label on CVN4 package (CVN4 video, frames 1-2, 15-16)**
   Root cause: Product name "CVN4 Tactical Responder Bandage" in opening dialogue declaration → Kie AI renders it as a printed label on the packaging surface.
   Fix: Don't open dialogue with product name as standalone declaration. Move name mid-sentence. Put no-text block at START of prompt.

5. **Skull and crossbones on CVN4 (CVN4 video, frame 7) — HARD BLOCKER**
   Root cause: TCCC + "no second chance" language triggers Kie AI danger symbol association.
   Fix: Add `no skulls no crossbones no danger symbols no hazard markings` to no-text block. Put block at top of prompt.

6. **Wrong product form (CVN4 video, frame 9)**
   Root cause: CVN4 prompts alternate between vacuum package and unrolled bandage across scenes, but only one product image URL is passed to all scenes. Kie AI generates inconsistent product representations.
   Fix: Either (a) pick one product form for the whole video, or (b) support per-scene product images in the pipeline schema.

**System prompt fix needed (v5.1 → v5.2):**
- No-text rules block must be FIRST in prompt, before camera and dialogue
- Dialogue must not open with product name as standalone declaration
- Remove Think tool from LangChain agent (incompatible with Structured Output Parser)

**Strategy:** Include scene-level approval + selective regen system in M2 delivery (not as paid M3). Rebuilds trust after these QC issues. Long-form ($1,500) pitched as clean M3 from restored trust position.

## M2 Breakthrough — Pipeline Proven End-to-End (2026-07-05 → 06)

First-ever complete run: form approval → script → 8 images → 8 Veo videos → Creatomate edit → client review email. Then the scene-regen loop ran for the first time and was proven live: Giovanni-side flag (scenes 2–7) → regen with corrected prompts → re-edit → branded re-review email. Total spend for the regen round: 6 Kie credits, zero waste (the one failed attempt cost nothing — Kie only bills successful generations).

**Bugs found and fixed live (all in production now):**
1. Italian VO coin-flipping to English — `enableTranslation: true` on Kie submits translated quoted dialogue; set false on all dialogue-scene submit nodes (3 places).
2. Speech cut mid-sentence at every 8s scene cut — script agent wrote ~20-word VO lines needing ~10s; hard cap now 12 words (15 for scene 2) + "finish by second six" beats (system prompt v5.6).
3. Regen branch dead on arrival — prompt-cleaning agent nested output under `output`, downstream read top-level → empty prompts to Kie (422). Fixed with flatten node.
4. "Increment Regen Round" wrote to a nonexistent Sheet3 column → chain silently stopped; column added.
5. Regen retry counter reset every cycle → infinite 3-min poll loop on permanent failure; now carried through the wait loop.
6. Creatomate API key invalid (401) — Giovanni-side credential refresh.

**Also shipped:** all 9 client-facing emails re-skinned with the branded dark Seraman template (status badges, buttons, logo chip); rejection email rewritten from a bare "incomplete details" stub.

**Verification method worth reusing:** downloaded the final render, split audio per 8s scene with ffmpeg, transcribed each with faster-whisper (language detection per scene) — caught the English scene and measured speech-end times (7.6–8.0s before fix, 6.2–7.5s after) without burning a single credit on guesswork.

**Remaining before full M2 sign-off:** Post-to-Socials stage (Blotato) still never run — fires on Giovanni's approve; scene 1/8 regen path uses old generation mode (align with proven branch A); Sheet2 stale duplicate rows corrupt regen URL writes (dedupe); idempotency guard so crashes never re-burn credits; script-agent prompt slimming. Big-product caveat for future jobs: concept assumes handheld items — large gear (cots, tents) needs a "large item" presenter mode; the image-approval gate is the cheap test.

## Tech Stack (Giovanni's side)

- Kie AI credits (pay-per-use, no subscription)
- Creatomate ~$29/mo
- Blotato $29/mo
- n8n (self-hosted or cloud)
- Google Sheets (being migrated to his own account for M2)
- Tally form: https://tally.so/r/obx5vx

## Handoff

Handoff doc generated: `outputs/strategy/2026-06-22-seraman-handoff-v1.pdf`
Includes: workflow architecture screenshots, Google Sheet breakdown, email alert examples, engineering depth, running costs, Italian closing message.
