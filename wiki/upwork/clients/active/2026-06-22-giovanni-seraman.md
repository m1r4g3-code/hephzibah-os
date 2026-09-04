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
| Milestone 1 | $500 | Delivered — 5-star review |
| Milestone 2 | $500 | In progress |
| Long-form pipeline (5–8 min) | ~$1,500 (agreed floor, not a fixed quote) | Not started |

**Net reality (M1+M2 combined, $1,000 total):** Fiverr takes 20% off the $1,000 total → $800 → 50/50 with Oba → **$400 each**, across both milestones combined — not $400 each per milestone. (Correction 2026-08-23: this section previously read $1,000 per milestone, conflicting with the actual $500/$500 figures tracked in `wiki/outreach/contacts/giovanni.md` — confirmed by the operator as $500 per milestone, $1,000 total.) The $1,500 figure is an agreement between Emmanuel and Oba that no future Giovanni job goes below $1,500 — not a price Giovanni has accepted.

**Pricing note (2026-07-06):** This build is worth $5K–8K at market. Underpricing accepted as cost of the first flagship case study. Decision: never renegotiate delivered work; reprice future scope (long-form, retainer) with ROI framing. Giovanni signals budget pressure from his own partners ("I just have to keep my partners happy" — Jul 05), so any price move must arm him with ROI numbers he can show them, not squeeze him.

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

## Client Feedback Log

### Giovanni, Jul 06 2026 3:12 PM (verbatim, on the sunglasses M2 test video)

> Good job! We're almost there, I just need to fix the text because the pronunciation on some things isn't correct. But this is a problem with all AIs that read in one language and don't change their accent when they read a word in another. For example, "cerakote" is English, and it reads it in Italian as it's written. In this case, just write the word "ceracot" and it's in English. Just write the correct text and you're done. A few things:
> - the glasses in the last scene aren't the ones shown;
> - there are some sharp cuts between one scene and the next; something would be needed to translate them;
> - the volume is generally low, but that's secondary for now.
> - the writing in the bottom right is "seraman," too "bare."
> But let's just say we're getting down to the details; generally speaking, we're on the right version.
> Bravo

**Status check against current pipeline (as of 2026-07-10):**

1. **Pronunciation of English loanwords read in Italian accent** ("cerakote" → should be spelled phonetically, e.g. "cerakot", so Italian TTS doesn't read it letter-for-letter) — **FIXED, script agent v5.10 (2026-07-10).** Added a mandatory phonetic-respelling rule for English brand/technical terms inside spoken VO ("Cerakote" → "Cerakot" pattern), with a new pre-output checklist item. Live on n8n node "SERAMAN | Generate Script" (workflow `bIDbAPsBbK9wh0c6`), published `activeVersionId: a976a2a5-563a-44ec-9eab-981712aa656b`, byte-verified against source.
2. **Wrong glasses/product shown in last scene (scene 8)** — **RE-CHECKED, ALREADY FIXED.** Inspected the live "SERAMAN Generate Images" workflow (`R2uqd2tnN687vcuH`, updated 2026-07-08 — after Giovanni's message): the Kie submit node sources `PRODUCT IMAGE` / `PRODUCT IMAGE 2` identically for every scene including scene 8, no divergent path. This was likely already broken when Giovanni saw it (Jul 06) and got fixed by the time this workflow was last touched. A separate, narrower bug remains on the hardening list — scene 1/8's *video regen* path (only triggers if those scenes get flagged for regen) still uses an older generation mode — but that's not what caused the original wrong-product complaint.

**Bonus fix while applying v5.10 (2026-07-10):** Publishing the script agent workflow re-surfaced a known recurring n8n bug (see [[n8n-mcp-gotchas]]) — two Gmail alert nodes, "SERAMAN | Reject Invalid Input" and "SERAMAN | Duplicate Submission Alert", had their `operation` parameter wiped (missing "send"), meaning those client-facing rejection/duplicate emails likely weren't sending. Pre-existed my changes (same warning showed up before I touched anything), not caused by this session — but fixed and published now.
3. **"Sharp cuts between scenes... something would be needed to translate them"** — re-read (2026-07-10, operator's call): "translate" is almost certainly a mistranslation of "transition," but the real cause is probably not a missing visual effect — it's the presenter's VO not finishing before the hard 8-second scene cut, which reads as an abrupt/incomplete cut regardless of any crossfade. **LIKELY FIXED, NOT RECONFIRMED ON THIS EXACT VIDEO.** This matches the "speech cut mid-sentence at every 8s boundary" bug fixed via script agent v5.6 (12-word VO cap, 15 for scene 2, "finish by second six" pacing), whisper-verified on a later job at 6.2–7.5s speech-end out of 8s. Giovanni's message (Jul 06 3:12 PM) falls right in the window of that fix — plausible his feedback is what triggered it — but there's no confirmation the fix had landed on the specific render he was reacting to. (Separately, every scene does also have a 3.5s fade-in animation live in the current Creatomate template, so the visual-transition reading, if that's what he meant, is also covered.)
4. **Volume generally low** — **MOSTLY FIXED.** Scenes 2–7 audio boosted to 200% volume (done in an earlier session — "edit the json template for each scene to be 200% not 100% for scene 2-7"). Scene 1 is still at 60% and scene 8 has no volume override (defaults to 100%) — worth normalizing these two to match the rest.
5. **"seraman" bottom-right end-card text too bare** — **UNCONFIRMED, LIKELY STILL OPEN.** The only branded text/logo element in the render is the outro CTA ("Shop now at: seraman.com" + logo image) at the very end of the video — plain Montserrat white text with a thin dark stroke, no visual upgrade evident since Jul 06. Would need an actual rendered video to confirm whether this reads as "bare" now.

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

## Incident — Kie Outage on Real Client Job + Image Quality Bugs (2026-07-08 → 09)

**Real job PRB1RG5 (rangefinder "Impact 4000") hit a live Kie platform outage.** All 8 scenes failed video generation, Edit Videos threw "Cannot render final video - bad scene URLs" (execution 545), and the Error Handler sent Giovanni a plain **"[FAILED] Seraman Edit Videos"** email (execution 546, 2026-07-08 23:35 UTC) — generic red failure badge, no indication it was Kie's outage and not our workflow. Unknown whether Giovanni saw/reacted to this specific email before the fix below shipped — worth confirming with him directly.

**Fix shipped:** Error Handler email template now distinguishes Kie-platform-caused failures (amber, "upstream provider issue") from actual workflow bugs (red) so Giovanni never mistakes a Kie outage for broken automation.

**Separately, image-generation quality bugs surfaced from screenshot QC (job aODBMQE, CVN4 Trauma Responder Bandage):**
1. **Subject missing in some scenes** — investigated, found mostly intentional (Scene 5's hands-only macro is a deliberate grip-demo per the script agent's Feature-to-Visual Mapping), not a systemic bug. Rule tightened in v5.8 so this stays a rare, justified exception.
2. **Product scale inconsistent / rendered too large** (bandage) — genuine architecture gap: no scale-anchor language ever existed in the prompt spec. Root-caused and fixed in script agent **v5.8** (scale classification + anchor phrasing bank, mandatory presenter face-in-frame). First regen of scenes 2 & 7 for aODBMQE **did not visually fix it** — caught directly by comparing before/after screenshots. Root cause of that: the scale-anchor sentence was appended after a handling action ("holds it flat between both open palms") that itself implied a two-handed span — nano-banana-pro follows the described physical motion over a trailing descriptive sentence. Fixed properly in **v5.9**: rewrote the handling action itself to a one-hand cupped-palm motion, hardened the prompt with an explicit rule forbidding a scale clause that contradicts the action verb. Both scenes regenerated and re-sent to seraman.adv@gmail.com.

**Script agent is now on v5.9** (live in n8n node "SERAMAN | Generate Script", workflow bIDbAPsBbK9wh0c6), byte-verified.

## Ad Creative — Video Model A/B Test (2026-07-19)

Veo3 has a recurring shape-drift defect on hand/joint contact scenes (observed on Disk-Bunk job WJpQ9eR, scene 7 — presenter hand seating a pole into a disc adapter). Ran a real, controlled test: same reference images, same prompt, same scene, submitted to 3 alternative Kie AI models to see if any fix it natively.

**Result (verified frame-by-frame, t=1/3/5/6.5s, not just spec claims):**
- **Kling 3.0** — fixes the joint defect. Voiceover reads robotic/synthetic.
- **Seedance 2.0** — introduces a new, different defect (phantom object duplication). Also by far the most expensive. Disqualified.
- **Gemini Omni** (Google's own model, via Kie) — fixes the joint defect. Voiceover reads natural/human. Fastest generation of the three. **Best pick.**

**Verified per-clip cost (from actual `creditsConsumed`, not published estimates):**
| Model | Cost/8s clip |
|---|---|
| Veo3 Fast (current) | $0.30–$0.40 |
| Gemini Omni | $0.525 |
| Kling 3.0 | $1.08 |
| Seedance 2.0 | $4.08 |

**Status:** 4-way comparison video sent to Giovanni with cost breakdown and recommendation to switch to Gemini Omni (cheaper than Kling, fixes the defect, better VO). Awaiting his greenlight. If approved, production workflow `fygNTt3a5LphUJO7` ("Seraman Generate Videos") needs its Kie submit nodes pointed at `gemini-omni-video`. Only tested against this one defect class — character consistency across a full 8-scene job and material hallucination not yet stress-tested on Omni.

## Prompt Hardening v5.14–v5.16 — Confirmed Fixed on a Real Live Job (2026-08-15)

Root-caused and fixed three separate hallucination/pacing defects flagged after reviewing job rDkyR8v, all via direct image/video inspection (downloaded and viewed the actual reference image, generated stills, and extracted video frames rather than guessing from prompt text alone):

1. **Long pauses** — every dialogue scene's system prompt instructed a 2-second silent freeze-frame hold at the close ("Beat 3"), compounding to ~15-18s of dead time across the ~56s video. Fixed: Beat 3 now requires continuous handling motion through the full close, never a static pose. (`SERAMAN | Generate Script`, v5.14)
2. **Background hallucination** — traced to the image-generation step (nano-banana-pro), not the video step. It was wholesale-redrawing the shop background (wrong shelf layout, SERAMAN wall signage dropped entirely), not just adding stray marks — the old negative tail only banned additions, not full reconstruction. Fixed with an explicit structural-lock clause. (v5.16)
3. **Clothing-logo hallucination** — Kie's video step (gemini-omni-video) separately invented a fake apparel brand logo on the presenter's fleece, a hallucination class the negative tail never covered. Added an explicit ban. (v5.16)

Each fix was verified in isolation before publishing (rejected a "padding trick" video test that fixed nothing and actually made background fidelity worse; confirmed the real fix via a side-by-side image regen showing the SERAMAN signage correctly restored).

**Live validation:** a real fresh job — Helikon-Tex T25 wrist compass, JOB_ID `Z9ZNaqv`, submitted via the real Tally intake (not a synthetic test) — ran through the fully patched pipeline end to end. Result confirmed clean: no long pauses, no background hallucination, no clothing-logo hallucination. First real proof the fixes hold on a brand-new product, not just the one job they were diagnosed against.

**Correction (same session):** initially misread this — both approval stages for this job were submitted for real via the live Tally webhook (same `respondentId` as prior self-testing, not a Giovanni submission), and the pipeline did run all the way through `SERAMAN | Call Post to Socials`, all 4 platform nodes (IG/TikTok/FB/YouTube Shorts) reporting success. First read was "this actually posted live" — wrong. There's a deliberate dead end wired into each platform branch (by design, per the operator) so the full pipeline can be exercised end to end without ever actually publishing during testing. Confirms as fake/non-live: all 4 "Create Post" nodes returned the identical media ID and URL, which isn't what distinct real per-platform post confirmations look like — it's passthrough from the upload step. One real side effect: the automated "[Report] Social Media Publishing — 4 post(s) scheduled" notification email did genuinely send to `seraman.adv@gmail.com` (Giovanni's real inbox) — worth knowing it's sitting there, but it says "scheduled," not "published," and is likely indistinguishable from routine test telemetry to him.

**Fixed the same night:** VO dialogue extraction was silently truncating lines containing an internal apostrophe (Italian elisions like "L'ago") — the model was doubling the straight quote as an improvised escape (`L''ago`), which broke the regex used both for the client review email preview and for splicing in Giovanni's corrections. Confirmed via job Z9ZNaqv scene 5. Fixed at the source: elisions inside spoken VO must now use the typographic apostrophe (’), reserving the straight `'` exclusively as the `says: '...'` delimiter. (v5.17, published)

## Two More Real Bugs Found and Fixed — Job 7XpW0OZ (2026-08-15, SOG Aegis AT Tanto knife)

Operator ran another live test and reported a black flash between scene 1 and scene 2, and scene 1 feeling shorter than 8 seconds. Root-caused directly against the Creatomate render template (`AH4d4awNiHliDToR` → `SERAMAN | Render Final Video`), not guessed from symptoms:

1. **Scene 1 missing `duration: 8`.** Every scene (2–8) in the render composition has an explicit `"duration": 8` locking it to fill its full slot. Scene 1 was the only one missing that key — it only had `"speed": "114%"` (from the earlier "continuous motion" pacing fix). Without a locked duration, Creatomate just played the clip at its natural length adjusted for the 114% speed-up: 8s ÷ 1.14 ≈ 7.02s. Scene 2 is hardcoded to start at t=8 regardless of when Scene 1 actually finishes. That left a ~0.98s window with nothing on Scene 1's track before Scene 2 faded in — the blackout, and the reason Scene 1 felt short. **Fix:** added `"duration": 8` to Scene 1, matching every other scene. Published.

2. **Render-failure alert node was non-functional.** While investigating, found `SERAMAN | Creatomate Render Timeout Alert` (a Gmail node, live-wired from both the "render explicitly failed" and "15 polling attempts / ~15 min timeout" branches) was missing its `resource`/`operation` discriminators and had no Gmail credential attached at all — it would have errored the instant it tried to fire. Checked the two historical error executions on this workflow (781, 770): both died earlier in the pipeline before ever reaching this node, so the gap has been live and untested since it was built — nobody would have found out until a real render actually timed out. The downstream halt step always throws regardless (so a broken video still could never have reached Giovanni), but the human alert itself would have silently failed to send. **Fix:** added `resource: message`, `operation: send`, attached the existing Gmail account credential (`seraman.adv@gmail.com`, same one the working review-email nodes use). Published.

Both fixes are the same class as the push_brain.py sync gap found earlier tonight: correct-looking on the surface, invisible until the specific failure path actually executes. Worth another test render to confirm the scene 1/2 transition is clean.

## Real Bug Found the Hard Way — Scene 1 Blackout Root Cause Corrected (2026-08-17/18)

The Scene-1-duration fix above turned out to be the wrong theory. A follow-up test (job BE29x15) still showed the blackout. Root-caused properly this time by checking the script itself, not just the render template: the master script-writer prompt had scenes 1 and 8 explicitly defined as short "cold open" / "end card" beats (3–4 seconds), directly contradicting the render template's fixed 8-second-per-scene grid — a structural mismatch nobody had reconciled. Fixed at the actual source: Scene 1 now required to generate a full 8 seconds, matching every other scene (v5.18). Scene 8 left as-is (4s, by design, per operator decision).

**Second real bug found while verifying the fix, on Giovanni's own submitted product** (K9 canine ear protection, job kbkxD6Z, 2026-08-18): visually compared all 8 generated images against the real product photo. Two scenes (5, 6) showed the model hallucinating a rigid over-ear headphone cushion — an oval foam driver pad that does not exist on the real product, which is a single continuous soft fabric hood. Root cause: the script described the product as having "ear cups" and instructed the model to "open" one "to expose the interior," pulling Veo/nano-banana toward its generic two-cup headphone prior. Fixed at the source with a new rule banning cup/interior-reveal language for single-piece soft products (v5.19).

**Also added same session:** a CLOTHING/APPAREL entry to the product-handling table (garments held and demonstrated by hand, never worn by the presenter — same reference-image-fidelity risk already proven costly by the clothing-logo hallucination incident).

Both new fixes verified against real execution data (ffprobe on actual generated video durations; direct visual comparison of generated images against the product reference photo) before being applied — not assumed from symptoms.

## Architectural Fix — Product Handling Table Replaced with Axis Classification (2026-08-18)

Operator flagged a real structural problem: the product-handling logic was a growing list of named categories (footwear, medical, vests, knives, optics, clothing), meaning every unusual product Giovanni sends ("special products, precisely to better stress the system," per his own framing) potentially needs a new category added by hand — not sustainable given he's explicitly sending edge cases on purpose.

Replaced the named-category table with a 4-axis structural classification (v5.20): how the product attaches to the body, structural rigidity, hazard profile, operable mechanism. Every prior named category collapses into a combination of these axes (a vest is "worn-in-real-use"; a knife is "held + edged"; the K9 headset is "held + single-piece-soft"), and any future product — including ones never seen before — is covered without needing a prompt edit. This reuses the physical classification Engine 2 already produces internally instead of running a second, redundant category system alongside it.

Checked the underlying Claude model too: the script-writer agent already runs Claude Opus 4.8, which is not the bottleneck — the K9 hallucination happened downstream in Veo's video generation, not in Opus's script reasoning. Opus 5 is now available as an incremental upgrade if wanted, but flagged separately since it wasn't the cause of anything found so far.

---

## Pacing Fix — Static Pre-Speech Hold Removed (2026-08-18, v5.21)

Operator relayed feedback from Oba: Giovanni specifically liked how the videos demonstrate product usage, so any further tuning should stay minimal rather than adding more prompt bulk. Separately, operator noticed the presenter sometimes (not every scene) waits 1–3 seconds before starting to talk in scenes 2–8.

Verified against real execution data before touching anything (job execution 826, 2026-08-18, K9 headset job, running v5.20): every feature scene's actual generated `video_prompt` contained the literal phrase "holds it...for 1 second; presenter looks to camera and says" — copied near-verbatim from the old canonical example in the system prompt. The Beat Structure section already told Veo the setup beat should be "seconds 0–1, no long silent setup," but the worked example modeled a sequential hold-then-look-up-then-speak beat, and the agent copied that pattern into every scene. Veo doesn't treat "1 second" as a hard cap, so this explicit instruction to pause is exactly what produced the inconsistent 1–3s dead air.

Fix (v5.21): rewrote Beat 1 to require the opening action and the first word of dialogue to happen concurrently, not sequentially — no more "holds for 1 second" as a discrete step. Updated the canonical example to match. This is also the "minimal, no slop" fix the operator asked for: the actual demonstration (the bracketed mid-sentence action cues, e.g. "[presses thumb gently into the padded shell]") is untouched — Giovanni liked that part. Only the mechanical, identical, value-adding-nothing setup pause was cut.

Two accidental placeholder-value pushes happened while assembling this fix (retyping a ~77KB prompt by hand for `setNodeParameter` risks transcription slips) — caught immediately via byte-level diff against the verified source before publishing, never went live. One real transcription typo ("Il commercial" for "The commercial" in an unrelated instructional line) was also caught the same way and corrected. Published only after an exact byte-for-byte match was confirmed. Live as `activeVersionId: 7efaa2c5-00ca-4a82-92c6-02b3358e55bf`.

---

## Real Bug Found in the Rerun — Two-Hand Lift Hallucinates a Rigid Headphone (2026-08-19, v5.22)

Operator asked which 2 of 3 available product photos to submit for a rerun (a dog wearing the goggles+hood combo, plus two isolated hood shots in different colors) — recommended the dog-wearing shot + the black isolated shot, since the isolated shot gives clean construction detail and the worn shot gives real scale/integration context the isolated shots can't (exactly the kind of context that would have prevented the earlier ear-cup hallucination). Operator submitted product photo #1 (unchanged from the original job) plus a second file (`..._6600.jpg`, confirmed via download to be the dog-wearing shot).

Reran the pipeline (job `dbkOLGo`). Static images came out clean per operator confirmation. Operator then reported the **video** still "mistook it for a headset" and shared frames proving it. Verified directly against the real generated video (not assumptions): checked the raw Kie clips for scenes 1,3,4,5,6,7 (all clean, soft fabric hood throughout) and the final Creatomate-stitched render frame-by-frame. Found the hallucination isolated to **scene 2 only** — starts right at the scene transition, a fully rigid two-cup over-ear headphone with a hard headband, for several seconds of the 8-second clip.

Root cause: not a language problem — scene 2's `video_prompt` never says "cup," "headphone," or anything like it; it correctly says "canine hearing-protection hood" and "soft fabric-and-foam shell" throughout. The trigger was the **motion**: "lifts the hood into frame with both hands and turns it toward camera" — a symmetric two-hand lift-and-rotate at chest height. That exact gesture matches Veo's training prior for a person holding up or putting on headphones strongly enough to override the correct product shape for a few seconds, independent of what the text says. This only surfaced now because this job's Engine 2 classified the product as **two-hand scale** (the dog-wearing photo gave it real proportional context — last time, with only isolated photos, it was misclassified as one-hand and used an asymmetric cup-in-palm motion that never triggers this).

Fix (v5.22): new standalone rule — two-hand-scale products must stage their opening lift asymmetrically (one hand supports/tilts, mirroring the one-hand pattern that already renders correctly everywhere else), never both hands mirrored lifting-and-rotating symmetrically. Referenced from AXIS 1 and added to the pre-output trust-score checklist. Confirmed failure mode documented inline with job ID and exact phrasing. Published as `activeVersionId: 129c7a28-4133-4258-a81d-b3d57be8283b`, verified byte-exact against source before publishing.

Not yet done: a fresh test job to confirm scene 2 renders correctly under the new rule.

---

## Policy Reversal — Clothing Now Shown Worn by Presenter, Per Client Preference (2026-08-19, v5.23)

Operator reran the pipeline for a Lynx merino wool midlayer top (job `RWVO1Ov`) to test whether the v5.22 fixes held on a fresh job. They did — Scene 1 duration, no pre-speech hold, and (since this is soft apparel, not a two-hand rigid product) no headphone collision either.

Before recommending the video be sent to Giovanni, checked the actual final render frame-by-frame and found the presenter wearing the garment on his body in scenes 3 through 7 — collar sitting naturally, sleeve down his arm — instead of holding it up, which directly violated the standing AXIS 1 rule ("never shown worn by the presenter") that had been in place since v5.19. Flagged this as a real defect and recommended against sending, since the existing rule existed specifically to avoid inventing fit/drape that was never in the reference image.

Operator corrected this: Oba reports Giovanni specifically likes it when the presenter wears the product — held-only demonstration was never what he wanted for apparel. This is new, confirmed client preference that overrides the original engineering-caution rule, and the actual renders looked clean and natural in every scene checked (no visible fit/drape distortion, no fabricated logos), so the original risk the rule was guarding against didn't materialize here anyway.

Fix (v5.23): split AXIS 1's "worn on body" bullet in two. **Soft apparel** (shirts, base layers, jackets, pants) is now shown worn by the presenter, matching Giovanni's stated preference. **Structural worn gear** (vests, plate carriers, chest rigs, harnesses, headwear) still follows the original never-worn rule, since an invented strap routing or plate position is a tactical-credibility risk apparel doesn't carry — scoped narrowly rather than reversing the whole AXIS 1 rule wholesale. Published as `activeVersionId: 7226b4f3-994c-40a0-9c9b-cb1e70b73220`, verified byte-exact against source before publishing.

Open question for Giovanni, not yet asked: does the "shown worn" preference extend to structural worn gear (vests, plate carriers, headwear) too, or is it apparel-specific? Left scoped narrow until confirmed either way.

---

## Scene-Correction Field Was Misused, Not Broken — Mechanism Fixed, Disc-O-Bed Job Completed (2026-08-20/21)

Operator flagged that Giovanni likely submitted an independent test himself: a Disc-O-Bed Disc-Bunk (modular camping bunk/cot, job `6DMe8Ak`), the first genuinely novel furniture-scale product run through the pipeline. Script and image generation handled it correctly with zero prompt changes — validates the v5.20 axis system on real unseen product data (JOINT/CONNECTOR rule applied correctly, real numbers from his product description carried through, no lift-related issues since a bunk bed is never lifted).

Video generation failed for 6 of 8 scenes with identical Kie `gemini-omni-video` failCode 500 "Internal Error" — a Kie-side outage, not a prompt problem (confirmed via raw API responses: clean-prompt scenes failed identically to the two affected ones below). `SERAMAN | All Videos Ready Gate` correctly blocked the job from being marked done — nothing broken reached posting.

Separately, scenes 2 and 5 had genuine director feedback from Giovanni ("The aluminum bar along the tarp doesn't exist. Rest your hand on the orange mat.") typed into the "corrected line" field built in an earlier session. That field's mechanism only ever anticipated literal replacement dialogue — it spliced his raw English staging note directly into `says: '...'`, and never touched `IMAGE PROMPT` at all, so even the wording fix wouldn't have addressed the actual complaint (presenter gripping the aluminum frame rail instead of the orange fabric deck).

**Fix, `NysDrlj3XSi7RDDo` (SERAMAN Scene Approval):** replaced the blind regex splice with a new `SERAMAN | Interpret Scene Correction` agent (same Anthropic-agent pattern as the existing `Clean Regen Prompt` node) that classifies the note as a wording fix vs. a staging fix vs. both, and rewrites `IMAGE PROMPT` + `VIDEO PROMPT` + `VOICEOVER TEXT` accordingly — never echoes the client's raw text into spoken dialogue. Corrected-line scenes now also auto-trigger image regeneration (confirmed operator preference: no longer gated behind the checkbox), via a new `Apply Voiceover Corrections → Get Job Record (Image)` connection that reuses the checkbox path's existing round-limited entry point rather than skipping into the middle of it — first wiring attempt skipped straight to `Get Sheet1 Data (Image Regen)` and broke the downstream round-counter step, caught via a real test run and corrected.

**Verified against production, not simulation:** used `test_workflow` with pinned trigger data (real field labels pulled from a genuine prior execution, not guessed) — pinning only the trigger meant everything downstream ran for real. First run exercised the new correction path against Giovanni's actual note for job `6DMe8Ak`; confirmed by downloading and viewing the regenerated images directly — hand now flat on the orange fabric deck in both scenes, matching exactly what he asked for. Second run replayed a real "Approve All" for the same job, which resubmitted all 6 previously-failed scenes to Kie (now recovered) and completed the full pipeline through to final Creatomate render. Confirmed in the actual final rendered video, not just intermediate state.

Final video: `https://f002.backblazeb2.com/file/creatomate-c8xg3hsxdu/cc7b32fe-b81c-4ddd-87a1-5cd059510ca0.mp4`

Follow-up sent (2026-08-21) consolidated both threads into one message rather than risking contradiction with whatever had already gone out on Fiverr (no visibility into that thread from here): explained the correction box now handles any scene issue (wording or staging), not just VO text, and confirmed the Disc-O-Bed video was done with his note applied.

### Giovanni's reply — two messages (2026-08-21)

**Message 1** (general reaction to the fix + finished video):
> I've seen both of them and I think the final product is excellent. There are still some small details, but as I said before, I sent you products that were difficult to produce so I could see how the system reacted. I'd definitely start testing with already-made products to see how it reacts. I see there are now two photos to upload. Let's see what happens. I'd say it's getting better and better. GREAT WORK. [...] I'm preparing the editorial plan until January. Let's see what happens.

Also requested a copy change: replace the end-card "Shop now at: https://seraman.com/" with "Compra su Seraman.com" — "much cleaner and more direct."

**Message 2** (sent after the correction-mechanism update went live):
> When I saw the scenes, I corrected it by writing it in the box. I hope I did it correctly. Did you intervene at this point, or was it regenerating everything on its own? So now I can tell it what to do if I find a scene that's incorrect? As soon as I get back, I'll try to generate the video of the water purification tablets, which had several things wrong.

**Read on this exchange:**
- Confirms he deliberately stress-tested with hard products on purpose ("difficult to produce so I could see how the system reacted") and is now satisfied enough to move to normal production — a real trust milestone, not just politeness ("GREAT WORK" + noticing small remaining details unprompted).
- **"Editorial plan until January"** is the load-bearing sentence — it signals recurring content volume planned out ~4-5 months, which is exactly the retainer-shaped opening the pricing note above has been waiting for ("reprice future scope with ROI framing," never renegotiate delivered work). Worth raising the long-form/retainer conversation soon, while he's expressing satisfaction — waiting risks him settling into "this is just free/uncapped" before a boundary is set. See [[project_giovanni_negotiation]] memory.
- **"Water purification tablets"** is almost certainly Aquatabs — the product flagged in standing memory as possibly already reused for an NGO context without new scope being agreed. Not raised with Giovanni here (would be a bad-faith read on a message where he's happy and being transparent, and there's no confirmation yet it's the same use case) — just worth the operator watching for when this job actually runs, and factoring into the scope conversation above rather than reacting to this message in isolation.
- His question ("did you intervene, or was it regenerating on its own?") got an honest answer: yes, automatic on our end for interpreting his note; separately flagged that this specific job hit an unrelated one-time Kie-provider hiccup needing manual resubmit, unconnected to how he used the box.

**Fixed same session:** end-card CTA text changed from "Shop now at: https://seraman.com/" to "Compra su Seraman.com" in the Creatomate render template (`AH4d4awNiHliDToR`, node `SERAMAN | Render Final Video`, element `Text-BZZ`). Published, verified byte-exact against the rest of the JSON body (only that one text field changed).

---

## Hardening Pass — Cross-Job Dedup Bug, Idempotency, Alert/Coverage Gaps (2026-08-21)

Operator's "editorial plan until January" comment prompted a "higher bar" audit against coming recurring volume, naming three suspects from an old 2026-07-06 hardening note (scene 1/8 regen using an old generation mode, no idempotency guard, Sheet2 stale duplicate rows) and explicitly excluding social posting.

**Two of the three named suspects were already fixed** — confirmed by reading current node configs, not assumed from the stale note:
- Scene 1/8 regen submission (`NysDrlj3XSi7RDDo`) is byte-for-byte identical to Branch A's first-pass submission (`fygNTt3a5LphUJO7`) — same model, params, everything.
- Sheet2 writes are all keyed `update`/`appendOrUpdate` on `["SCENE","JOB_ID"]`, never a bare append; `AH4d4awNiHliDToR`'s URL-map builder additionally sorts by `row_number` for last-write-wins protection. No exploitable stale-duplicate path exists.

**The real, more serious gap was new, found via a direct read of `94ON9lonhDLNPc99` (SERAMAN Error Handler):** node `Clear Stale Dedup Rows` deleted every `status:"started"` dedup row (table `AN3YgyQOI1D8BG42`) on **any** workflow error anywhere in the SERAMAN system, with no JOB_ID or time-window scoping. At one-job-at-a-time test volume this rarely collided with anything. Under Giovanni's coming recurring/overlapping volume, one job's failure would routinely wipe every *other* concurrently in-flight job's duplicate-submission protection — meaning a redelivered/duplicate Tally webhook during that window would no longer be blocked, and the full pipeline (script + 8 images + 8 videos) would rerun and re-charge. **Fix:** added a `processed_at < now-3h` condition (matchType `allConditions`) so only genuinely stuck rows get cleared, not rows for jobs still legitimately in progress. Confirmed `lt` is a valid condition operator for the string column via `explore_node_resources` before writing it (ISO 8601 timestamps sort correctly as strings).

**Bonus fix found while verifying the above:** `Notify Seraman` — the single Gmail node all 5 workflows' error alerts ultimately route through — had the same missing-`resource`/`operation` defect already confirmed twice this session as a real silent-send-failure (not a safe runtime default, per `get_node_types`). The validator flagged it as "pre-existing, can be intentional"; fixed anyway rather than trusting that caveat, since this is the system's entire failure-visibility backbone.

**Idempotency guards added** (no pre-submit check existed anywhere; a crash-then-manual-retry before a sheet's STATUS flips to Done would resubmit and burn duplicate paid credits):
- `fygNTt3a5LphUJO7` (Generate Videos): new `SERAMAN | Get Existing Video Results` → `SERAMAN | Skip Already-Submitted Scenes` inserted between `Scene-count` and `Sort1` — drops any scene already holding a non-empty, non-FAILED `VIDEO URL` for the job before the branch split into the two Kie submit nodes. `Scene-count`'s own expected-count (used by `All Videos Ready Gate`) is computed before the filter, so it still reflects the full original scene set.
- `AH4d4awNiHliDToR` (Edit Videos): new parallel Sheet3 lookup (`SERAMAN | Check Existing Final Video` → `SERAMAN | Normalize Existing Check`) merged via a position-combine `Merge` node with the existing video-map output, gated by a new IF node. False (normal) branch reaches `SERAMAN | Render Final Video` completely unchanged; true (already-rendered) branch terminates in a new No-Op rather than reusing the existing success-path update chain, since that chain's node-reference expression (`$('SERAMAN | Extract Final Video URL')...`) would break on a path where that node never ran.
- **Not applied** to the three Scene Approval regen-submit nodes (`Regen Submit (Scene 1/8)`, `Regen Submit (Middle Scenes)`, `Submit Image Regen`) — investigated directly rather than mechanically copying the same pattern. Regen is *supposed* to overwrite an existing (flagged-as-wrong) Sheet2 value, so "does a URL already exist" isn't a valid "already done" signal here the way it is for first-pass generation — there's no round/timestamp marker in the current schema to distinguish "this regen round already completed" from "the prior, now-flagged-wrong result is still sitting there." Forcing a guard without a clean signal risked a worse bug (silently skipping a legitimate correction Giovanni actually asked for) than the one being prevented. Left as-is; flagged here rather than silently dropped.

**Also fixed:**
- `R2uqd2tnN687vcuH` (Generate Images) and `NysDrlj3XSi7RDDo` (Scene Approval) had no `errorWorkflow` configured at all — any unhandled throw in either alerted no one. Both now point at `94ON9lonhDLNPc99`, matching the other 3 workflows.
- Two more broken alert nodes in Scene Approval, same defect class as ones fixed earlier this session: `SERAMAN | Approval Confirmed Alert` and `SERAMAN | Send Video For Review` — correct `sendTo`/`subject`/`message`/credential, just missing `resource`/`operation`.
- `SERAMAN | Get Sheet1 Scene Data` (Scene Approval) read all of Sheet1 unfiltered, relying on a downstream JS fallback (`!jobId || scene.JOB_ID === jobId`) that would match every job's rows if `jobId` ever came back falsy, and an unbounded read that grows with total historical scene rows as volume climbs. Added a direct `JOB_ID` filter matching the pattern used everywhere else in the pipeline.

**Explicitly out of scope this pass** (real gaps, bigger structural decisions, flagged not fixed): no 429/rate-limit handling for Kie bursts under concurrent jobs; no credential-expiry monitoring for any of the 6 credentials in use (the Creatomate key already expired once, 2026-07-05); Anthropic script-gen `retryOnFail=true, maxTries=3` left as-is (pennies per retry vs. Kie's $0.30–$1+/clip, and auto-retry on a transient LLM failure is often desirable).

Every change published and verified against a fresh fetch of the live workflow (not assumed from the update call's own response) before moving to the next — same discipline used all session. One real process note: `addNode` operations silently drop `executeOnce` (not a supported field on that op) — caught on the first new Sheets node via verification, had to be set separately via `setNodeSettings` on both new read nodes added this pass.

---

## Ad Creative — Background Music Research (2026-07-20)

Investigated whether to replace the current stock background track. Key findings:

- **Do not use live trending TikTok/Reels sounds.** They're licensed for organic posts, not paid ad placement, and burn out in 1–2 weeks — wrong fit for a Creatomate-rendered ad meant to run for a while.
- Commercial-library tracks in the **100–140 BPM** range consistently outperform generic background music for this content type.
- Pairing music with voiceover (already the Seraman format) gets roughly **2x the conversion** of either alone per TikTok ad data — don't let music compete with/drown the VO.
- One concretely documented reference: Artlist track **"Game Over" by 2050** — electronic + orchestral, builds from dramatic strings/synths into driving percussion and brass. Picked by an automotive brand for a cinematic commercial. Closest verified match to the rugged/confident/builds-to-a-payoff register Seraman needs. Worth previewing directly on Artlist.
- **Real validation method (not yet run):** check Meta Ad Library (facebook.com/ads/library) for live video ads from comparable DTC tactical/EDC brands — Tactical Geek, 5.11 Tactical, Elite Survival Systems, Marsupial Gear, M-Tac, Falco. A track reused across multiple currently-running ads from different advertisers is real proof it converts (they're paying to keep it live). Attempted again 2026-08-15 — Meta's ad library is a JS-heavy app that refuses automated/non-browser fetches outright (socket hang up, not just a block page). This check needs an actual human browsing session; it cannot be done by the OS. Still open.

### Round 2 (2026-08-15) — re-verified + new candidates

- **"Game Over" by 2050 re-confirmed real and live**: present on [Artlist](https://artlist.io/royalty-free-music/song/game-over/77369), [SoundCloud](https://soundcloud.com/2050music/2050-game-over), and [YouTube](https://www.youtube.com/watch?v=mKHqMpHyWX8) — safe to preview/license from any of the three. Still the strongest single lead.
- **Platform split confirmed:** Epidemic Sound has the deeper catalog (~50k tracks) and better mood/BPM filtering, plus a dedicated Tactical/Equipment *sound-effects* category (not music) — better for discovery once someone can browse and filter live. Artlist is smaller (~30k) but more tightly curated for cinematic/corporate moods and is where "Game Over" already lives — one less new account to manage.
- **Two new named candidates found (Uppbeat, free tier w/ attribution or paid tier without):**
  - **"No Turning Back" by Albert Behar** — tagged Dramatic / Cinematic / Tense. Closer to a slow-build tension register than Game Over; worth an A/B preview against it.
  - **"Currents" by Philip Anderson** — tagged Dramatic / Cinematic / Documentary. Closest match yet to the "documentary realism, calm authority, not hyped" brand voice specifically — worth checking first since it's the only candidate that leans documentary rather than trailer/epic.
- All three (Game Over, No Turning Back, Currents) still need actual listening + Giovanni's ear against a real cut — genre tags and descriptions can't substitute for hearing it under the Italian VO. None of the automated research tools here can play audio.

**Status:** three concrete, named, verified-real candidates now on the table (up from one). No track selected yet — next step is a human listening pass (ideally against an actual Seraman scene cut, since "2x conversion" only holds when music doesn't fight the VO) and, separately, someone browsing Meta Ad Library directly in a real browser to close out the validation method above.

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

---

## Major Incident + Two Real Production Bugs Found and Fixed — Full Night, K9 Tourniquet + Aquatabs (2026-08-26)

Long overnight session covering: an Aquatabs pipeline fix and real delivery, a self-inflicted data-corruption incident during testing, two genuinely new production bugs discovered (one via the incident, one via a live real client submission), both fixed and verified, plus a real Kie credit-exhaustion failure on the K9 Tourniquet job. Documenting in full since this directly bears on reliability going into Giovanni's planned 30-product medkit/K9 launch.

### Aquatabs — zero-item-skip bug found and fixed, real delivery completed

Root-caused a silent, total video-generation failure affecting **every first-time job approval**, not just Aquatabs. In `fygNTt3a5LphUJO7` ("Seraman Generate Videos"), node `SERAMAN | Skip Already-Submitted Scenes` was fed only by `SERAMAN | Get Existing Video Results` — a Sheet2 lookup that correctly returns 0 rows for any job that's never had video results written yet. n8n skips a node entirely when it receives zero input items, even if the node's own code correctly handles the empty case. That skip cascaded to the next node too, since it was fed solely by the skipped node's (nonexistent) output — meaning video generation silently never ran for any brand-new job, with zero error signal to anyone.

**Fix:** added a parallel connection from `Scene-count` (already guaranteed non-zero, having passed the hard-fail 8-scene check) directly into `Skip Already-Submitted Scenes`, removed the old zero-item-risk connection, and rewrote the node to read existing rows via `$('SERAMAN | Get Existing Video Results').all()` (cross-node reference) instead of `$input.all()` (physical flow). Verified live: manually retriggered Generate Videos for the real Aquatabs job (JOB_ID `6DMqPoN`) — all 8 scenes rendered for real, Sheet1 STATUS flipped to Done. Then retriggered Edit Videos — real Creatomate render succeeded (`64598238-ce9a-4e92-b6c4-3627dde1d1bb`, 60.01s, 720×1280), Sheet3 `FINAL VIDEO URL` written. Delivered to Giovanni via the exact real "SERAMAN | Send Video For Review" Gmail template (job-specific values substituted, template unchanged) — confirmed real send, `id: 1a03b1d5a52f6c4c`.

### Self-inflicted incident — Google Sheets `appendOrUpdate` overwrote live Aquatabs rows during manual testing

While manually testing a second product (K9 Tourniquet, temp `JOB_ID: K9TEST01`), used `appendOrUpdate` matched on `["SCENE NUMBER", "JOB_ID"]` to write 8 new test rows to Sheet1. This **overwrote the live Aquatabs rows at physical row_numbers 2–9** instead of appending new ones, despite `K9TEST01` never matching any existing `JOB_ID`. Caught via a pre-existing `VOICEOVER TEXT` value (untouched by the test write) that still showed real Aquatabs Italian VO text after the "K9" write landed.

**Recovered:** captured Aquatabs' original 8-scene data from an earlier execution's node output (before the overwrite), rebuilt via `operation: "update"` matched strictly on `["row_number"]` — never `SCENE NUMBER`/`JOB_ID` again. Verified byte-correct via an independent read filtered on `JOB_ID=6DMqPoN`. This incident is what surfaced the real underlying bug, documented next — not just a one-off mistake, a structural flaw in how the production system creates new job rows.

### Real production bug #1 — `appendOrUpdate` matching was landing brand-new jobs on top of old ones, confirmed on a real client job

The production node that creates every new job's 8 scene rows, `SERAMAN | Append Script in sheet` (workflow `bIDbAPsBbK9wh0c6`), used `appendOrUpdate` matched on `["SCENE NUMBER", "JOB_ID"]` — the same operation type introduced on 2026-08-23 (see entry above, "RESOLVED... switched to appendOrUpdate keyed on SCENE NUMBER+JOB_ID") as the fix for the *original* ArWa5G0 duplicate-row contamination. That earlier fix traded one bug for a different one: this session found the matching logic itself was unreliable and would land writes on rows 2-9 (the physical top of the sheet) instead of the true last row, **even for a genuinely new, never-before-seen JOB_ID that could not legitimately match anything**.

Confirmed this wasn't just a testing artifact: audited the full live Sheet1 (232 rows at the time, 29 clean contiguous 8-row job blocks, zero gaps anywhere) and found a **real, live Tally submission** — JOB_ID `M1MozPE`, the actual K9 Tourniquet product, submitted for real (likely by Oba, per his earlier offer to run things manually) — had landed on rows 2-9, overwriting the just-restored Aquatabs data a second time. This happened independent of any of the night's manual testing.

**Fix:** switched `SERAMAN | Append Script in sheet` from `appendOrUpdate` to plain `append`, `matchingColumns: []`. Every `JOB_ID` from Tally is a unique submission id — there is never a legitimate case where this node should "update" an existing row, so matching served no purpose except the collision risk it caused. Verified live: fetched the published node, confirmed `operation: "append"`, `matchingColumns: []`, `versionId === activeVersionId`. Also proved the fix mechanically: rescued M1MozPE's real data using plain `append` (no matching) and it landed correctly at rows 234-241 — the true end of the sheet — on the first try.

### Real production bug #2 — stale captions/image URLs riding along on new jobs, from the same root cause

`SERAMAN | Append Script in sheet` never wrote or cleared the `VOICEOVER TEXT` column when creating a new job's rows (not in its column list). Combined with bug #1 landing new jobs on top of old physical rows, this meant a new job's rows could silently inherit **leftover data from whatever job previously occupied that row** — both the `VOICEOVER TEXT` caption (confirmed: M1MozPE's rows showed Aquatabs Italian dosing copy verbatim) and, per the row-collision timing, potentially a stale `GENERATED IMAGE URL` too, since that column also isn't part of this node's write.

This is the actual explanation for the "K9 review email shows Aquatabs" report from the operator: the review email that had already gone out (fired ~00:26 UTC, mid-collision) caught a mix of freshly-generated K9 images and leftover Aquatabs image URLs/captions from whichever scenes hadn't yet had their `GENERATED IMAGE URL` overwritten by the real K9 generation run at the moment the "all ready" gate fired. Confirmed by downloading and visually inspecting all 8 of M1MozPE's *current* `GENERATED IMAGE URL` values directly (not assumed) — every one is correct K9 tourniquet content; the defect was specifically in what got captured into the *already-sent* email, not the underlying data once it settled.

**Fix:** added an explicit blank `VOICEOVER TEXT: ""` to the columns `SERAMAN | Append Script in sheet` writes for every new job, so new jobs no longer inherit a previous job's caption. Verified live in the published node.

### Corrected review email sent for the real K9 job

Rescued M1MozPE's real data (script text, all 8 confirmed-correct `GENERATED IMAGE URL` values) to safe rows (234-241, true end of sheet), cleared the contaminated rows 2-9. Sent a corrected review email to `seraman.adv@gmail.com` using the exact real "SERAMAN | Send Image Review Email" template, with a clear red-flagged banner explaining it supersedes the earlier (partially wrong) email and should be the only one used to approve/flag scenes. Confirmed real Gmail send, `id: 1a03bdd2bc37fb38`. Extracted correct dialogue per scene directly from each scene's `VIDEO PROMPT` (`says: '...'` clause) since `VOICEOVER TEXT` was deliberately left blank on the rescue write.

### K9 Tourniquet video generation blocked — real Kie AI credit exhaustion, not a code bug

A real Tally approval submission came in for M1MozPE (Scene Approval fired, `SERAMAN | Flag Scenes Intake`), triggering Generate Videos. It ran, then correctly threw: *"6 scene(s) failed video generation (scenes 2,3,4,5,6,7)... refusing to mark Sheet1 STATUS as Done."* Root cause, confirmed via the raw Kie submission response: `code 402, "Credits insufficient — please top up to continue"` on all 6 failed scenes. Retried automatically a second time (a second real approval submission came in ~30 min later) — failed identically, confirming the account genuinely needs topping up, not a transient issue.

**Gap flagged, not yet fixed:** `fygNTt3a5LphUJO7` (Generate Videos) has no credits-exhausted alert path, unlike `R2uqd2tnN687vcuH` (Generate Images), which does (`SERAMAN | Alert — Credits Exhausted` / `Alert — Credits (Internal)`). The workflow failed correctly and loudly in its own logs, but nobody was notified — this should be added before the 30-product launch, given it will recur at scale.

### Medkit candidate selected but not run

Researched Giovanni's live site for the medical-kit product line he mentioned launching. The actual bundled "3 types × 10 products" medkits are not yet live on the site. Found 9 individual existing SKUs under the "Kit Medico" category instead. Operator picked **BCB International Foil Hypothermia Blanket** (emergency thermal blanket, code CL041, €2.50) as the next test candidate — real product photos pulled and verified (folded mylar sheet, person wrapped outdoors, retail box art). Flagged as a genuinely harder visual case than anything tested so far (a plain reflective sheet with almost no distinguishing shape/texture, unlike every product tested up to this point). **Not yet run** — paused after the credit-exhaustion discovery shifted priority to messaging Giovanni; still open for whenever the operator wants to proceed.

### Process notes for future sessions on this build

- The `appendOrUpdate`-with-matching pattern is now confirmed unreliable for *new row creation* in this Google Sheet, twice, on two different nodes across two different debugging sessions three days apart. Default to plain `append` (no matching) for any future "create new job rows" write in this pipeline; reserve `appendOrUpdate`/`update`-with-matching strictly for genuine in-place corrections where `row_number` is the match key.
- Any node writing a new job's initial rows should explicitly blank every column it doesn't set a real value for (`VOICEOVER TEXT`, `GENERATED IMAGE URL`), not just omit them — omission means silent inheritance of whatever the previous occupant of that physical row left behind.
- When multiple temp webhook-trigger nodes coexist on the same workflow even briefly, `execute_workflow` can fire the wrong one — always remove the previous temp trigger before adding a new one, confirmed again multiple times this session.

---

## Deep-Audit Tooling Built + Full Pipeline Scan + Three Real Fixes (2026-08-26, later same night)

Following the incident above, the operator asked to bring in a set of principal-engineer-grade audit skills from another local project and formalize them as reusable commands. Found 8 of the 11 source files were genuinely generic reviewer subagents (security, architect, data-model, perf-review, dx-review, test-strategy, researcher, debt-assessor) — copied into `.claude/commands/` in this project, reframed from spawned-subagent persona to direct command instructions, content preserved. The other 3 (`Audit.md`, `Deep-Audit.md`, `Senior-level Audit.md`) were hardcoded to the source project's own domain (DSatur graph coloring, Dijkstra navigation, Yabatech exam halls) — not reusable as-is, so instead built `.claude/commands/deep-audit.md` from scratch for this pipeline specifically: same report structure and rigor (RED/YELLOW/ORANGE/GREEN-equivalent sections, a numbered failure-pattern catalogue, domain checklists, cross-workflow integration checks, P0–P3 remediation priority), but populated with real confirmed failure patterns from this build's actual history instead of borrowed content.

**Ran `/deep-audit everything` for real** against all six SERAMAN workflows. Three real findings survived verification (full report and reasoning in conversation; summary here is the fixes actually shipped):

**Finding 1 — Scene Approval's regen-write nodes matched on `[SCENE, JOB_ID]`, not `row_number`.** Traced *why*: `row_number` was never carried through the regen chain (`SERAMAN | Filter Flagged Scenes` dropped it, unlike its sibling `Filter Flagged Images` which already carried it correctly) — the original implementer had no `row_number` available at that point, so fell back to business-key matching, the exact pattern already proven unreliable earlier tonight.
**Fix:** added `row_number` to `Filter Flagged Scenes`'s output; switched `SERAMAN | Update Sheet2 (1/8)` and `(Mid)` to match on `row_number`.

**Finding 2 — the video/image regen accumulators used `$getWorkflowStaticData` across two independently-polling parallel branches, each with its own Wait node.** Already flagged elsewhere in this file as unreliable across Wait-node suspensions (see `SERAMAN | All Videos Ready Gate`'s own code comment). While fixing this, found something the audit hadn't caught: `SERAMAN | Regen Failed` (both branches, video and image) **never wrote anything back to Sheet2/Sheet1 at all** — a failed regen attempt just vanished, leaving whatever stale data was there before untouched. A Sheet-read-back fix wouldn't have worked without closing that gap first.
**Fix, both paths:** added the missing failure writes (`SERAMAN | Write Regen Failure (1/8)`, `(Mid)`, `SERAMAN | Write Regen Image Failure`, all `row_number`-matched), then replaced both `Accumulate Regen Results`/`Accumulate Regen Images` Code nodes' static-data counting with a live Sheet2/Sheet1 read-back gate — same proven pattern as `All Videos Ready Gate`: re-read the actual sheet fresh on every completion event, cross-reference against the full flagged-scene list, proceed only when every flagged scene has a real recorded result (success or FAILED).

**Finding 3 — Edit Videos had the same zero-item-skip vulnerability as tonight's original bug, in a new spot.** `Code in JavaScript` (builds the Creatomate video-URL payload, with a hard-fail check for missing/bad scenes) was fed only by a Sheet2 lookup with no STATUS filter. A zero-row response — e.g. Edit Videos triggered before Generate Videos wrote anything — would skip the node entirely, including its hard-fail check, and cascade to skip the render-vs-skip IF and the failure alert too. Nothing would fire, indistinguishable from success in the execution list.
**Fix:** same pattern as the original fix — added a parallel connection from `Start` (guaranteed non-zero) directly into `Code in JavaScript`, rewrote it to read the real Sheet2 rows via `$('SERAMAN | Get row(s) in sheet').all()` instead of `$input.all()`, with an explicit thrown error on the zero-row case naming the JOB_ID.

All three published and verified live (fresh fetch after each publish, connections and code confirmed byte-exact, zero orphaned nodes). Scene Approval went from 81 to 86 nodes. Not yet tested against a real live regen cycle — needs an actual flagged scene going through the loop with the operator watching, not forced blind.

---

## Giovanni reply — editorial plan through December/February (2026-08-27)

Giovanni replied to the "Talk soon, K9 is next" message: apologized for a busy day, archived the old 70-message thread in favor of a fresh one, and said he's working today on an editorial plan through December (stretch goal: February), acknowledging it may shift as they go — "let's hope this is the definitive path."

**Read:** two signals stacked together — tidying the relationship (fresh thread) plus formalizing a multi-month production calendar — point to a client settling into an ongoing working rhythm, not one evaluating whether to continue. This directly follows his "very beautiful, good job" reaction to the corrected Aquatabs delivery, so the [[project_giovanni_negotiation]] trigger (raise expansion/retainer once a delivery ships clean and gets confirmed) has now fully fired.

**Why it matters beyond the update:** his editorial plan is the thing that will actually determine Kie credit burn — volume × cadence. The K9 job's real credits-exhausted failure (2026-08-26) is still sitting there with no funding/retainer conversation raised. His message hands a clean, non-awkward opening: ask about production *pace* (a capacity question), not money — get the real volume number first, then size the Kie/retainer conversation against it as its own separate message later, once M2 is fully locked.

**Reply sent** (calibrated question, no money mentioned): asked him to share the rough monthly pace once the plan is roughed out, framed as making sure the pipeline matches his cadence with zero friction.

**New standing principle for this build, worth carrying into every future session:** whenever `row_number` isn't available at a write site and business-key matching gets used instead, that's not a stylistic choice — it's a sign `row_number` should have been threaded through and wasn't. Check the upstream filter/map step first before accepting the matching-key compromise.

---

## K9 Retry Saga — Three New Real Bugs Found and Fixed, Plus a Real Hallucination Root-Caused (2026-08-28/29)

Giovanni topped up Kie credits; operator re-ran K9 (JOB_ID M1MozPE) from where it stopped. What followed was a chain of three genuinely new production bugs in `fygNTt3a5LphUJO7` (Generate Videos) and `AH4d4awNiHliDToR` (Edit Videos), each found via real execution logs (not guessed), each fixed and verified live.

**Bug 1 — partial-retry array-position misrouting.** `SERAMAN | Extract only First & Last Scene` / `SERAMAN | Extract all Scenes except First and Last Scene` selected items by array position (`scenes[0]`/`scenes[length-1]` vs `slice(1,-1)`), correct only when the full 8-scene set flows through. On a partial retry (only the 6 previously-failed scenes resubmitted), position 0/last ≠ scene 1/8 — misrouted scenes 2 and 7 into the bookend branch, which finished fast and reached `All Videos Ready Gate` before the correctly-targeted branch (scenes 3-6) had even run, causing a premature hard-fail that aborted the whole execution before Kie was ever called for those 4 scenes. **Fixed:** both nodes now filter by literal `SCENE NUMBER` (`===1||===8` vs not) instead of array position. First fix attempt actually failed silently — `setNodeParameter` with path `/parameters/jsCode` wrote to the wrong nested location (`node.parameters.parameters.jsCode`) and reported success without applying; caught by refusing to trust the tool's own OK response and diffing live content instead. Second attempt had a real typo (extra closing brace, would have shipped a syntax error). Third attempt verified correct via `new Function()` syntax check plus a simulated full-run/partial-run trace before publishing.

**Bug 2 — wrong node-name reference, live since 2026-08-26.** Edit Videos' `Code in JavaScript` referenced `$('SERAMAN | Get row(s) in sheet')`, a node name that does not exist — the real node is just `Get row(s) in sheet` (no prefix). Introduced by the 2026-08-26 zero-item-skip fix, which apparently assumed a naming convention that didn't apply to this one older node. That fix's own verification checked connections and confirmed the code matched intended source byte-for-byte, but never checked that the node name *inside* the code string actually resolved — so it shipped invisibly and only surfaced now, the first real run to exercise this path with data. **Fixed:** corrected the reference.

**Bug 3 — double-execution from a redundant wire.** `Code in JavaScript` had two incoming connections into the same input (`Start` and `Get row(s) in sheet` both wired in — leftover from the same 2026-08-26 fix, which added the `Start` wire but never removed the original). n8n runs a node once per incoming wire, so it ran twice per execution. The second run's `Merge Render Check` pairing found no partner item (the Sheet3 check only ran once) and came out empty; since that empty run finished last, n8n reported *it* as the sub-workflow's return value to Scene Approval — discarding the already-correct first run and silently sending zero items to `Send Video For Review`, even though the real Creatomate render had already succeeded and Sheet3 was already correctly written. This is why the review email didn't send even after the video genuinely rendered. **Fixed:** removed the redundant `Get row(s) in sheet` → `Code in JavaScript` wire (the node reads real data via cross-node reference anyway, so the wire was never structurally needed) — leaves `Start` as the sole, always-non-zero trigger.

All three fixes published and verified via fresh live re-fetch (not assumed from the tool's own response) before moving to the next. End-to-end result: Generate Videos succeeded for real (execution 1036), Edit Videos rendered for real (execution 1040, real Creatomate render `fcc9261b...`, 60.01s, Sheet3 updated), and the corrected retry of Scene Approval (execution 1041) sent the review email correctly once bug 3 was fixed.

### Real hallucination found in the rendered video — root-caused, not patched

Operator reviewed the actual rendered K9 video and flagged visible product distortion. Compared six screenshots directly against the real product reference photo (downloaded and viewed, not assumed): the video invented a black "X"-shaped cutout molded into the buckle that does not exist on the real product, and lost the windlass bar / paracord toggle / TacMed brand patch entirely in several scenes, rendering a bare featureless strap instead.

**Root cause, found by reading the actual script-writer system prompt (not guessing):** every one of the K9 job's 8 scene `image_prompt`s closed with "...exactly as shown in the product reference image" — a near-miss paraphrase of a callback phrase the document already banned ("as in the reference image"), close enough in meaning to still trigger the same "reconstruct from words instead of attending to the real image" failure mode without matching the banned phrase's exact wording. The actual smoking gun: the document's own labeled **"Correct image_prompt Structure Example"** — the model's primary imitation target — itself contained this exact banned pattern, directly contradicting the rule stated a few lines above it.

First hypothesis (add more descriptive shape language for the buckle/windlass) was walked back before implementing — the document's own SEALED-DOSE section already found that exact approach backfires (invented shape language overrides the real reference image and can render the *wrong* shape). Went with the evidence-grounded fix instead.

**Fixed in `bIDbAPsBbK9wh0c6`, node `SERAMAN | Generate Script`, systemMessage v5.33 → v5.34:**
1. Strengthened the callback-phrase ban to explicitly name "exactly as shown in the product reference image" and close variants, and clarified it applies to every product category, not just consumption-mode.
2. Fixed the worked example so it no longer violates its own rule.
3. Logged the K9 failure with evidence, matching the document's existing citation style.
4. Cleaned a stray duplicate `parameters.parameters.options.systemMessage` placeholder key found on the node (same defect class as bug 1's silent-wrong-path failure, from an earlier session).

Pushed via full-parameter replace (99,510-char systemMessage, manually transcribed since no file-reference mechanism exists in the tool) — verified **exact byte-for-byte match** against the locally-edited authoritative copy via direct string comparison before publishing, not assumed correct.

### Site-wide risk scan — which other products might hit the same class of failure

Scanned shop.seraman.com (Cuffie, Brandine/Disc-O-Bed, Soccorso → Kit Medico/Immobilizzazione/Medicazione/Tactical, water-purification tablets) to check which other real SKUs structurally match the axes that have already produced confirmed failures. Then ran a self-consistency audit of the full v5.34 document (grepped for two-hand-symmetric-lift, joint-insertion, and ear-cup language) to check for a second silent worked-example contradiction like the one just found — came back clean; only two worked-example blocks exist in the whole document (video_prompt and image_prompt), and both are now correct.

**Conclusion: these products are already covered by name in the existing structural AXIS rules — not a prompt gap.** Logging as a watch-list, not a to-do, since the real risk isn't "the rule doesn't exist," it's "a rule existing doesn't guarantee the model follows it under real generation pressure" (exactly what happened with the K9 callback-phrase bug despite the rule already existing).

- **Tier 1 (highest — same failure class as a confirmed 2x-repeat bug):** [Walker's Cuffia Low Profile Ripieghevole Nera](https://shop.seraman.com/6478-Walker-s-Cuffia-Low-Profile-Ripieghevole-Nera.html) — foldable ear protection, soft molded cups. Same shape class as the K9 ear-hood that failed twice (rigid-cup fabrication, then two-hand headphone-prior lift collision). Worth a manual look the first time it's actually scripted.
- **Tier 2 (JOINT/CONNECTOR risk, rule exists, untested on this line):** [Disc-O-Bed modular cot/bed/chair system](https://shop.seraman.com/catalogo-23-0-brandine.html) — 24 SKUs, explicit modular disc-and-pole construction; PAX Mummy-mat/I-Mat vacuum mattresses and splint sets ([Immobilizzazione](https://shop.seraman.com/catalogo-230-226-Soccorso-Immobilizzazione.html)).
- **Tier 3 (same category as the actual K9 failure, AXIS 4):** [CVN Medical TQ Tourniquet](https://seraman.com/6709-CVN-Medical-TQ-Tourniquet.html), [PAX Extremities Tourniquet PET](https://seraman.com/6535-PAX-Extremities-tourniquet-pet.html) (winch-based), [MedNet Laccio emostatico](https://shop.seraman.com/1031-MedNet-Laccio-emostatico-Tourniquet.html) — three more tourniquets, each with its own real hardware shape that needs grounding from its own reference photos when scripted.
- **Tier 4 (already covered, confirmed pattern):** [BCB International water purification tablets](https://shop.seraman.com/945-bcb-international-compresse-per-la-purificazione-dell-acqua-50-pcs....html) — the real Aquatabs-equivalent SKU already in catalog; AXIS 5 already handles it correctly.

## Pipeline-wide readiness sweep, ahead of confirmed 2 videos/week volume (2026-09-02)

Operator asked to fix everything necessary across the whole pipeline before real volume hits. Full sweep across all 5 SERAMAN workflows:

**Gmail resource/operation consistency — 19 nodes total** (Generate Videos: 2, Edit Videos: 1, Product Automation: 2, Generate Images: 3, Scene Approval: 6, wait — plus the earlier 5 already fixed 2026-08-26: Notify Seraman, Approval Confirmed Alert, Send Video For Review, Creatomate Render Timeout Alert warning). **Correction to the record, found mid-sweep:** these were framed as "confirmed silent-send-failure" fixes based on the type schema listing `resource`/`operation` as required discriminators — but direct evidence contradicts that. `SERAMAN | Send Image Review Email` in Generate Images was missing both fields and had been sending real emails successfully all session (confirmed message IDs in execution logs). n8n defaults safely here rather than silently failing. All 19 fixes are still correct and were applied (explicit is more robust than relying on an undocumented default), but they were a defensive-consistency cleanup, not bug rescues — worth remembering so a future session doesn't over-credit this pattern.

**Dead code removed, two places:**
- Product Automation: 3 fully orphaned nodes (`SERAMAN | Get Description for Job` → `Wait` → `Call Seraman Edit Videos`) — leftover from before Scene Approval took over calling Edit Videos. Confirmed zero connections either direction before removing.
- Generate Images: 7-node dead chain (`Download Product Image` → `Convert Product Image Format` → `Upload Converted Image` → `Preserve File ID` → `Share Converted Image` → `Merge Converted Image` → `Set Converted Image URL`), an apparently half-built "resize oversized product image" feature. `Download Product Image` had zero inputs (could never fire) — but the chain's output landed as a *second* input into `SERAMAN | Count Scenes`, alongside the real `Get Scene Prompts` path. Same shape as the confirmed double-execution bug from the K9 retry saga (Edit Videos, `Code in JavaScript`) — currently inert only because the chain never fires, but a real landmine if anyone ever wired `Download Product Image` up later. Operator chose to remove rather than finish it.

**False-positive check, worth noting:** initially flagged 4 nodes in Scene Approval as orphaned (`Anthropic Chat Model2/3`, two Output Parser nodes) — turned out to be a detection bug on my end (only checked `main` connections, missed `ai_languageModel`/`ai_outputParser` connection types LangChain sub-nodes use). Verified properly wired before reporting; no actual issue there.

All changes published and verified live (fresh fetch after each publish) before moving to the next, same discipline as the rest of tonight.

---

## First real job after the readiness sweep — clean first pass, new product category (2026-09-02)

Real live Tally submission, JOB_ID `xV6dzDd` — a thermal-digital multispectrum binocular (dialogue names it "Habrok 4K" — "questo è l'Habrok 4K. Non un semplice visore, ma un binocolo multispettro"). First SERAMAN product in the optics/electro-optical category — not on the risk watch-list logged above, a genuinely new axis combination for the script system.

**Ran clean end to end, no rework:**
- Product Automation (exec 1043, 21:51–21:57 UTC) → script generated → Generate Images (exec 1044, integrated) → all 8 scene images generated.
- Scene Approval webhook (exec 1045, 21:58–22:06) received the review submission: `Approve All` checked, zero scenes flagged, zero corrected lines — **images approved on the first pass**, no regen needed. Same clean-first-pass pattern as the K9 job (2026-08-26), now confirmed on a second, unrelated product category — real evidence the axis-based classification generalizes rather than overfitting to tactical gear.
- Called Generate Videos (exec 1046) → all 8 scene videos generated successfully.
- Called Edit Videos (exec 1047, 22:05–22:06) → Creatomate render succeeded (`e4d6b328-e192-4ef2-8cc9-321d21ea19af`, 60.01s, 720×1280, 13.68MB) → Sheet1/Sheet3 updated → review email sent to `seraman.adv@gmail.com` (Gmail message `1a064289603cfa57`, confirmed in SENT/INBOX).

**Validates the pipeline-wide readiness sweep in real production conditions** — the double-execution fix in Edit Videos' `Code in JavaScript` held (all 8 videos correctly built into one payload, no duplicate/empty run overwriting the result the way it did on K9), and none of the 19 Gmail resource/operation fixes or dead-code removals caused any regression.

## Social caption feature — built, published, brutally audited (2026-09-04)

Giovanni asked for a copy-paste caption (short description + product link + hashtags) attached to the video-review email, since automatic Blotato publishing currently ships videos with zero caption and he'd rather publish manually with real copy than fix bare posts after the fact. Full request/decoding logged in `wiki/outreach/contacts/giovanni.md` under "Negotiation posture — decoding the real trigger."

**Discovery that changed the build plan:** while checking feasibility, found a 7th, previously-unexamined workflow — `Seraman Post to Socials` (`gfN4514IJb4TpBRM`) — a fully-engineered 23-node social publishing system (LangChain agent with a genuinely sophisticated platform-specific copywriting system prompt, per-platform hashtag/character-limit rules, Blotato integration wired to real seramanltd IG/TikTok/FB/YouTube accounts) that has never been connected to the live pipeline (nothing calls it — `triggerCount: 0`, no caller anywhere in the other 5 workflows) and whose only input, Sheet3's `PRODUCT DESC` column, is never populated by anything upstream (the same broken/empty column found and dismissed as "not our bug" on 2026-09-02 — turns out it's exactly the input this orphaned system was built to consume). Its four Blotato "Create Post" nodes are all `disabled: true` — matches Giovanni's own words that "the workflow is paused waiting for your approval." Left this entire system untouched — didn't repair, connect, or enable it. Reconnecting it would mean turning on real automated cross-platform posting, a materially bigger and harder-to-reverse decision than what Giovanni actually asked for right now (a caption to copy manually). Worth surfacing to him later as a real, already-built option if he ever wants full auto-publish restored.

**Brand link, verified against the real site, not derived from a new intake field.** Giovanni's own Gatorz example linked to a brand collection page (`shop.seraman.com/marca-Gatorz`), not a specific product page. Fetched the real `marche.html` brand nav and confirmed the exact slug rule against 57 real brands: spaces become underscores, everything else (existing hyphens, apostrophes, periods) stays literal. First naive guess (hyphen instead of underscore) produced a real, silently-empty page for "BCB International" — loaded fine, zero products, no error — exactly the kind of failure this build has learned to distrust. Rule is fully derivable from the brand name already present in every product's submitted script, so no new Tally intake field was needed.

**Architecture — isolated from the script-writer agent, per explicit direction not to touch it again.** New 5-node chain inserted into `SERAMAN Scene Approval` (`NysDrlj3XSi7RDDo`), between `SERAMAN | Call Edit Videos After Gen` and `SERAMAN | Send Video For Review`:
1. `SERAMAN | Build Caption Prompt Input` (Code) — pulls `VOICEOVER TEXT` for the job from the already-fetched `SERAMAN | Get Sheet1 Rows for Corrections` node (cross-node reference, no redundant Sheet read) — real dialogue already grounded in the actual product, not the fragile external `PRODUCT DESC` column.
2. `SERAMAN | Generate Caption` (Anthropic, `claude-opus-4-8` — same model as the script-writer, same `Anthropic account` credential) — small, dedicated system prompt (not the 99KB script-writer prompt), strict JSON out: `{brand, short_description, hashtags}`, explicitly banned from inventing specs/certifications beyond the real dialogue.
3. `SERAMAN | Parse Caption & Build Link` (Code) — defensive JSON parse (regex-extract + try/catch, safe fallback on any malformed input), applies the verified brand→slug rule.
4. `SERAMAN | Validate Brand Link` (HTTP GET, `neverError: true`) — fetches the constructed brand page for real before trusting it.
5. `SERAMAN | Finalize Caption` (Code) — falls back to the generic `shop.seraman.com` homepage if the response contains "Nessun risultato", builds the final 3-part caption block (description / link / hashtags) matching Giovanni's simplified format exactly.

Email body (`Send Video For Review`) updated to append a clearly-labeled, monospace copy-paste block with the generated caption — video download/approve links untouched.

**Real bug found and fixed during the audit, before publishing:** inserting nodes changed what `Send Video For Review` receives as `$json` (confirmed against the SDK reference's own documented pitfall for this exact pattern) — the two existing `{{ $json.finalVideoUrl }}` references would have broken had they not been updated to explicit `$('SERAMAN | Call Edit Videos After Gen').item.json.finalVideoUrl` cross-references. Caught and fixed before publish, verified via direct occurrence count in the live message body (3 occurrences, all correct).

**Second real bug found and fixed:** the new Anthropic and HTTP nodes had default error behavior (`stopWorkflow`) — meaning any external failure (API hiccup, network blip) in the new caption chain would have silently halted the entire execution, blocking `Send Video For Review` from ever firing. That would have broken the one thing that's worked reliably all week, for the sake of a nice-to-have addition. Fixed: `onError: continueRegularOutput` on both external-dependency nodes — combined with the already-defensive parsing code (safe fallback on any malformed/error-shaped input), a caption-generation failure now degrades to a generic fallback caption rather than ever blocking video delivery.

**Verification performed:** validated all 5 node configs before writing (`validate_node_config`, all passed); full before/after diff of all 86 pre-existing nodes confirmed zero unintended changes (only the one intentional edit to `Send Video For Review`); connection chain re-verified single-path, no stray wires (the exact double-execution bug class found twice earlier this week); published and re-fetched to confirm `versionId === activeVersionId` live.

**Live-verified, real bug found and fixed, before Giovanni ever saw it (2026-09-04, same session).** Rather than wait for a real job to surface the unverified Anthropic output-shape risk, built a throwaway standalone test workflow (webhook trigger, real Habrok 4K script hardcoded, identical 5-node chain), executed it for real — one real Claude API call, one real HTTP GET to shop.seraman.com, zero Kie/Creatomate involvement. First run failed immediately with a genuine, guaranteed-to-recur bug: `claude-opus-4-8` rejects the `temperature` parameter outright (`400: temperature is deprecated for this model`). This meant the **live production node had the identical bug** — every real caption generation would have failed and silently degraded to the generic fallback via the `onError` safety net, meaning the feature would never have actually produced a real caption for Giovanni, without any visible error anywhere. Removed `temperature` from both the test and the live `SERAMAN | Generate Caption` node, republished, re-ran the test — full real success:

- **brand**: `"Hikmicro"` — correctly extracted.
- **short_description**: grounded, accurate Italian summary pulling real features from the actual script (multispettro, sensore termico, ottica digitale 4K, modalità Fusion, IP67, zoom 22x) — no invented specs.
- **hashtags**: `#Seraman #Hikmicro #VisioneTermica #Habrok4K #BinocoloMultispettro #Outdoor` — matches the required format.
- **link**: `https://shop.seraman.com/marca-Hikmicro` — HTTP-validated for real, 341KB real page returned (not "Nessun risultato").
- Real output shape confirmed: `{ content: [{ type: "text", text: "..." }] }` — validated the defensive multi-branch parsing code was written correctly (the array-of-content-blocks branch is the one that actually fires; the naive `raw.content === 'string'` guess would have been wrong on its own).

Test workflow archived after verification. This closes the open risk completely — the feature is now confirmed working end-to-end with real data, not just structurally sound.

## Two more real findings from the live re-trigger, and a link-format correction (2026-09-04, same session)

Operator re-approved the real Habrok 4K job (fresh Tally submission, job `xV6dzDd`) to force a genuine live end-to-end run of the real Scene Approval workflow (not the throwaway test copy) — safe and free to do, since two separate idempotency guards (Generate Videos' `Skip Already-Submitted Scenes`, Edit Videos' render-skip check) both correctly detected the job was already complete and submitted nothing new to Kie or Creatomate.

**Discovery: Scene Approval already calls the dormant "Post to Socials" workflow after every send.** Missed in the earlier audit — the search was for the literal string "Blotato" in the workflow text, not for the actual call node. This had apparently never fired on a real approval before today. Confirmed from real execution data, not assumption: the four Blotato "Create Post" nodes executed in 0-1ms and returned data identical to the media-upload step — the signature of a disabled pass-through, not a real API call. **No post went out to any real platform.** Only the video file itself got uploaded to Blotato's media CDN (real but non-public).

**Real bug found in that same path, pre-existing, unrelated to this build:** the workflow's own "Social Media Publishing Report" email fired regardless of the posting nodes being disabled, sending Giovanni a real email claiming "4 post(s) have been successfully scheduled" — false, and directly contradicting what he'd just been told (Blotato is paused). Explained to him as a leftover testing artifact. **Not yet fixed** — the report should either be suppressed while the posting nodes stay disabled, or reworded to reflect reality. Flagged, decision pending.

**Giovanni corrected the link format:** confirmed the description quality directly ("Exellent description"), but the link should go to the specific product's own page (`shop.seraman.com/6458-Hikmicro-Habrok-4K-HE25L-850nm.html`), not the brand-collection page the caption chain was building. The numeric catalog ID in that URL isn't derivable from anything in the pipeline — no guessing, so a new optional "Product Link" field was added to the intake capture chain instead:

- `SERAMAN | Extract Fields` (Product Automation) now dynamically finds the Tally question whose **label** contains "link" (regex match, not a hardcoded question ID — Tally assigns opaque per-question IDs that don't exist until the field is created, same constraint already documented elsewhere in this build for the flag-form's job_id field). Verified locally against three cases: field not yet added, field added with a value, field added but left blank — all behave correctly.
- New `PRODUCT LINK` column added to the `Append Script in sheet` write, alongside the existing PRODUCT IMAGE columns.
- Scene Approval's caption chain (`Build Caption Prompt Input`, `Parse Caption & Build Link`) now reads this column and uses it directly when present, falling back to the brand-collection-page construction only for older jobs or if the field is left blank.

**One thing this tool cannot do:** actually add the field to the live Tally form — that requires Tally's own form builder, outside any available tool's reach. The n8n-side capture is ready and waiting; the field itself needs to be added in Tally (label must contain the word "link", e.g. "Product Link (optional)") by whoever has access to that form.

All changes published and verified live (versionId === activeVersionId on both workflows), node counts unchanged from before (only existing nodes edited, nothing added/removed).

**Loose thread investigated and closed (2026-09-04):** Sheet3 row 48's `PRODUCT DESC` column read `"#ERROR! (Formula parse error.)"` in this execution. Checked the actual workflow config (`AH4d4awNiHliDToR`, `Update row in sheet1` node): `PRODUCT DESC` is explicitly marked `removed: true` in the column mapping — no node in this pipeline (or any of the other 4 SERAMAN workflows) ever writes to it. Confirmed by comparing to row 47 (K9 Tourniquet job), which holds a full, well-formed Italian SEO product description in that same column — content our pipeline never generated or wrote. This column is populated by something entirely outside our build, most likely a manual paste or a spreadsheet-native formula/template Giovanni or his side maintains per product row. Row 48 (Habrok 4K, the newest row) simply doesn't have it filled in yet or its formula didn't extend to the new row correctly — a Giovanni-side spreadsheet issue, not a pipeline bug, and it never blocked anything (`FINAL VIDEO URL` wrote correctly to the same row regardless). No action needed on our side.
