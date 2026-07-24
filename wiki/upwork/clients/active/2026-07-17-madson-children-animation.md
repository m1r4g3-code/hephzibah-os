---
name: madson-children-animation
sensitivity: private
platform: fiverr
status: follow_up_sent
created: 2026-07-17
updated: 2026-07-17
---

# Client: MadSoN — AI Children's Animation Studio

**Business:** Children's animated content creator (social media focus)
**Platform:** Fiverr (Oba's gig)
**Client type:** New to Fiverr, price-sensitive but vision-clear, trust problem not budget problem

---

## Project Vision

Fully automated children's cartoon production pipeline triggered from Telegram. Client sends an episode brief, pipeline generates script, character options, 3-minute video with voiceover narration and music, and delivers the finished video. Full multi-stage approval at every step.

---

## Discovery Answers Received (2026-07-17)

1. **Characters:** Consistent across ALL episodes. Client controls when to upgrade. Character reference system required.
2. **Audio:** Both voiceover narration AND music confirmed. ElevenLabs + Suno both in scope.
3. **Volume:** 100 videos/month at full capacity. 3-minute videos.
4. **Approval:** 4-stage Telegram approval per episode.
5. **Budget:** Asked for total fixed price. Opened the door to us naming the number.
6. **Bonus scope:** Also interested in music video editing. Scoped as Phase 2.

---

## Competitive Intelligence (2026-07-17)

**MadSoN is shopping multiple platforms simultaneously.**

Same job scope appeared on Upwork through a separate middleman group (the same group that previously underpaid Emmanuel on a different project). They cropped their screenshot to hide the real Upwork budget, then offered Emmanuel $500 to build it.

**Moves executed:**
- Move 1: Told the greedy middlemen the scope requires $2,500 minimum. They cannot build without Emmanuel. Their Upwork channel is dead.
- Move 2: Oba sent a follow-up message to MadSoN on Fiverr re-engaging before the middlemen can regroup with another builder or quote lower directly.

**Awaiting:** Responses from both MadSoN (Fiverr) and the middlemen (to confirm they've folded).

**Advantage:** Emmanuel completed a full discovery with MadSoN. Understands his requirements (character consistency, 4-stage approval, 100 videos/month, Phase 2 interest) better than any competing bidder. That depth is the moat.

**Risk:** If middlemen find another builder quickly, they may submit a lower Upwork quote before MadSoN commits to Oba. Speed of close matters.

---

## Stack Decided

| Layer | Tool |
|---|---|
| Trigger + Delivery | Telegram + n8n native node |
| Orchestration | n8n Cloud |
| Script generation + Scene breakdown | Claude API (HTTP node in n8n) |
| Character generation + Video clips | Kie AI (Veo 3 Fast + image models) |
| Character consistency | Reference image system (locked reference injected into every generation) |
| Voiceover | ElevenLabs |
| Music | Suno API |
| Final assembly | Creatomate |

---

## Character Consistency Architecture

**What we build:** Reference image system.
- First session: client describes character, AI generates 4-6 image options, client selects one
- That approved image is stored and injected as a reference into every future generation call
- Consistency: ~75-85% (same design, colors, style; minor variation between clips)
- Limitation disclosed: not pixel-perfect. Current ceiling of AI video generation.
- Upgrade path (not in scope): custom character LoRA training for 95%+ consistency

At 100 videos/month with 18-36 clips per video = 1,800-3,600 individual clip generations/month.

---

## Approval Flow (4 Stages Per Episode)

1. Client submits episode brief via Telegram → Claude generates script → sent for approval or edit
2. Character reference displayed for confirmation before scene generation begins
3. Generated clips previewed before assembly
4. Assembled video presented before final delivery

At 100 videos/month: ~400 approval interactions/month on client's end. Disclosed upfront.

---

## Estimated Monthly Running Costs at Scale (100 videos/month)

| Tool | Cost |
|---|---|
| n8n Cloud | $24-50/month |
| Kie AI (2,500+ clips) | $400-800/month |
| Creatomate (100 renders) | $100-150/month |
| ElevenLabs | $22-50/month |
| Suno API | $20-30/month |
| Claude API | $15-30/month |
| **Total** | **~$580-1,100/month** |

---

## Pricing

**Quoted:** $3,500 fixed price
**Covers:** Full cartoon pipeline, 4-stage Telegram approval, character consistency system, voiceover + music
**Running costs disclosed:** $600-1,000/month at 100 videos/month
**Payment terms:** 50% before build, 50% on delivery and handoff
**Phase 2 (music video editing):** Separate scope and quote

---

## Client Behavior

- New to Fiverr
- Proposed $10-11/hr x 10hrs/day originally (~$2,000 max signal)
- Psychology: scared of being duped, not actually broke
- Hold price. $3,500 fixed. Monthly running cost makes the build fee look small.
- Shopping multiple platforms simultaneously — close speed matters

---

## Status

- Discovery answered (2026-07-17)
- $3,500 quote sent via Oba
- Oba follow-up sent (2026-07-17) to re-engage before competing channel closes
- Greedy middleman Upwork channel neutralized (2026-07-17)
- Awaiting MadSoN response
- **2026-07-24: LOST — Oba's Fiverr account permanently suspended. No off-platform contact captured. Unrecoverable.**

---

[[automation-asset-pricing]] [[elbert-savvysox]]
