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
| Long-form pipeline (5–8 min) | ~$1,500 (agreed floor, not a fixed quote) | Not started |

**Net reality per $1,000 milestone:** Fiverr takes 20% → $800 → 50/50 with Oba → **$400 each.** The $1,500 figure is an agreement between Emmanuel and Oba that no future Giovanni job goes below $1,500 — not a price Giovanni has accepted.

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
