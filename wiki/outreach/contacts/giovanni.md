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
last_updated: '2026-07-24'
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

| Milestone                    | Amount | Status                                                    |
| ---------------------------- | ------ | ---------------------------------------------------------- |
| Milestone 1                  | $500   | Delivered — 5-star review                                  |
| Milestone 2                  | $500   | **Paid** (the week after M1) — deliverable still outstanding |
| Long-form pipeline (5–8 min) | $1,500 | Scoped, not started                                        |

**Correction (2026-07-29):** M2 was paid up front, the week after M1 — not on delivery/approval as previously logged. This means the ArWa5G0 corrected-video work still owed is against money already collected, not money pending collection. No further payment is outstanding until the long-form pipeline is actually started.

**The actual promise, verbatim recollection (2026-07-29):** Giovanni said, informally, that he's "gonna drop something for us after the workflow complete build" — no number, no scope, tied to the *build* being complete, not to any specific feature. Soft and goodwill-based, not a firm commitment. Emmanuel's own read, in hindsight: this should have been a proper pitched conversation about business risk/value at the start of the engagement, not left as a vague verbal goodwill offer — logged as a lesson for future client intake, not just this relationship.

**When it becomes fair to raise it:** the six-workflow pipeline itself is functionally built and running end to end — what's outstanding on ArWa5G0 is content-level bug-fixing (packaging text, regen), not incomplete build work. Once the corrected video ships and is approved, it's honest (not opportunistic) to consider a low-pressure reference back to his own words — something like acknowledging the full build is complete and working well, no demand attached, giving him room to follow through or not. Raising it before the corrected video ships would look like asking for a bonus while the current thing is still broken — same timing problem as every other money conversation this week.

**Business context sharpening the urgency (2026-07-29):** no other client work currently moving; Elbert (Fiverr client, savvysox) was lost in the Fiverr suspension crisis. Giovanni is currently the only near-term revenue path, which raises the cost of getting the sequencing wrong here — one bad move and there's no fallback client relationship to lean on in the meantime.

**Real root cause found, 2026-07-29 (sharper than the sachet-vs-blister theory):** every scene sends BOTH product reference photos (`PRODUCT IMAGE` = box, `PRODUCT IMAGE 2` = individual sachets) to the image model with no per-scene disambiguation of which one is authoritative for that shot. That ambiguity, not a model weakness, is why results were inconsistent scene to scene. Fixed the immediate symptom (rewrote all 8 IMAGE PROMPT/VIDEO PROMPT entries to explicitly describe the sachet, regenerated all 8 images, visually confirmed blister-pack hallucination gone) but the underlying ambiguity is still there — even the "clean" sachet scenes are printing the box's tagline design onto a sachet shape, not the sachet's real print (different dosage/warning text, small icon). Durable fix identified but not yet built: select and send only the correct single product image per scene instead of both.

**Model comparison run (2026-07-29):** tested nano-banana-pro (current), Flux-2 Pro, and google/nano-banana-edit (edit/compositing mode) side by side on the same scenes. nano-banana-pro reliably preserves the SERAMAN wall sign but has inconsistent packaging content. Flux-2 Pro has better average text legibility but drops the wall sign in some scenes and makes its own typos. nano-banana-edit mode (edit the real reference photo directly instead of regenerating from description) gave the best background preservation and correctly used the sachet's real layout — but output resolution is too soft to confirm fine print, promising not conclusive. Sent both comparisons to Giovanni's own inbox as internal-test emails (not real review requests), using the actual production Gmail node/template.

**Voiceover/script approval UX — built 2026-08-04/05.** Closes the gap logged 2026-07-28 ("show him the text" was scoped but not built, and didn't actually solve his ask — he wanted to *correct* it, not just see it). Plan approved and shipped:
- Tally form (`yPGyxd`) now has 6 new optional long-text fields, one per dialogue scene (2-7; scenes 1 and 8 are silent product shots, no field needed) — "Scene N — corrected line (leave blank if it's fine)", no pre-fill (URL pre-fill would have exceeded safe email-link length with real dialogue text).
- Sheet1 got a new `VOICEOVER TEXT` column (column J) — the dialogue previously only existed embedded inside the `VIDEO PROMPT` blob.
- `SERAMAN | Parse Flag Response` now also emits `correctedLines` (dynamic label-match lookup, same pattern already used for the job_id hidden field — Tally's per-question keys are auto-generated and not predictable in advance).
- New chain (`Get Sheet1 Rows for Corrections` → `Build Corrected Rows` → `Apply Voiceover Corrections`) fans out from Parse Flag Response in parallel with the existing approval flow — writes corrected lines to `VOICEOVER TEXT` and regenerates the dialogue portion of `VIDEO PROMPT` via regex, upserted by `row_number` only (never SCENE NUMBER+JOB_ID — the exact bug class already hit once on ArWa5G0).
- The review email (`Send Updated Image Review Email`) now shows each dialogue scene's current line under its image, sourced via a new `Get Sheet1 Rows for Email` → `Merge Dialogue Into Regen Images` step, with a line telling him where to correct it.
- Deliberately skipped extending the script-generation agent's 69K-char system prompt to add a discrete voiceover field (higher risk, harder to verify) — confirmed via grep that no such field exists today, used regex extraction against the existing `video_prompt` text instead (consistent `says: '...'` pattern observed across every scene this build has produced).
- Parse-logic verified via a synthetic payload (confirmed `correctedLines` extraction works, blank/null fields correctly skipped). **Not yet verified**: a real live Tally submission — the exact field-key/label shape Tally assigns at actual submission time hasn't been confirmed against a live test. Caught and fixed one real mistake mid-build: an accidental duplicate of all 6 form fields from a multi-trigger execution ambiguity (same bug class flagged earlier this week), found via verification and cleanly removed before it reached Giovanni.

**STUCK, confirmed 2026-08-04 (real priority now):** Giovanni approved all images on 2026-07-29 06:27, which correctly triggered video generation (scene 1's clip confirmed complete). But the final assembly step (captions + Creatomate) never ran — checked the tracking sheet directly a week later and `FINAL VIDEO URL` is still the old, wrong pre-fix video. This is now a genuine stall needing real debugging, not "give it more time." Not yet root-caused.

**Honest tool-renewal ask sent via Oba (2026-07-29):** after ruling out the gift/psychology-based approaches, sent an honest, non-manipulative message via Oba: owns the original $1,000 pricing as our own call (not a complaint), explicitly decouples from what's already paid, mentions the incoming script-approval fix as a value-add rather than an apology, asks plainly for a contribution toward AI tooling costs, and gives him an explicit no-pressure exit ("nothing changes between us if the answer's no"). Deliberately does **not** invoke his earlier informal promise ("gonna drop something after the workflow complete build") — decision made to treat whatever he sends here, if anything, as the fulfillment of that promise rather than something separate, to avoid double-collecting on the same goodwill under two different names later. If he references the build-completion promise again unprompted once ArWa5G0 ships, that's his call to make — not something to re-raise ourselves.

**Cash-flow pressure, flagged and declined (2026-07-29):** Emmanuel is out of runway (spent the prior $1k, Claude Pro renewal at risk) and floated asking Giovanni for $500 framed as a "gift," then as a psychology-driven ask leaning on Oba's rapport, Giovanni's age (60s), and his calm/trusting nature to extract money he doesn't owe — while the M2 deliverable he already prepaid for is still unfinished, and while he's independently dealing with partners leaving him. Advised strongly against it: exploits the one asset (trust) the long-form $1,500 deal depends on, and is a bad bet even self-interestedly — if it works, the relationship absorbs the cost later; if he ever recognizes it as engineered, the relationship is over. Agreed alternative: send an honest, no-ask-attached update (used Claude Pro to move faster on M2, own the pace decision) as information only, not a lead-in to a request. If he offers something unprompted, that's real. The only legitimate near-term revenue event remains finishing ArWa5G0 and, once trust is fully intact, the long-form pipeline conversation.

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

### Negotiation posture — think ahead, don't just react (2026-07-26)

Applying [[strategic-frameworks]] to this relationship: [[poker-under-uncertainty]] for reading his ambiguous messages, [[batna]] before any scope conversation, [[red-team-inversion]] on any "helpful" move before it ships, [[voss-negotiation]] for the actual phrasing when it happens.

**Who he is:** experienced businessman, runs a real multi-category brand (SERAMAN), moves deliberately, not a first-time buyer of services. Treat him as a peer negotiating counterpart, not a typical small cold-outreach lead — he'll notice if we're reactive instead of strategic.

**The reuse risk:** the pipeline (`fygNTt3a5LphUJO7` / `AH4d4awNiHliDToR`, hosted on Giovanni's own n8n instance at seraman.app.n8n.cloud) is generalizable — swap the product, it works for anything. Job 6DrPK95 (Aquatabs, his NGO partner's separate project) used the exact same review-email system as Giovanni's own jobs, meaning the system is very likely already being pointed at a second, unrelated product with no new engagement or payment discussed. Confirm for certain once n8n MCP reconnects (check whether 6DrPK95 ran inside the same workflow vs. a duplicate).

**The pricing lesson:** M1/M2 ($500 each) were priced as one-off SERAMAN deliverables. What actually got built is a reusable content engine — the build cost was paid once, but every additional product it gets pointed at afterward is near-zero marginal cost to Giovanni and zero additional revenue to us. That gap, not the original numbers in isolation, is the real problem to fix going forward.

**The actual leverage — not the code, the maintenance:** anyone with n8n access can see the workflow. Debugging it (pairedItem lineage bugs, silent duplicate-row failures, API migration mismatches — all real bugs hit and fixed on this exact build) is a different skill entirely. That's the defensible, ongoing value a one-time handoff to a partner doesn't threaten. Lead with this, not with code-access anxiety.

**The approach:** don't assume bad faith — Giovanni's been consistently green-flag (pays, reviews promptly, warm). He likely handed his partner a working example without thinking of it as "extending paid scope," since nothing was ever put in writing limiting the build to SERAMAN specifically. When M2 closes, that's the natural moment to state a boundary plainly and non-confrontationally: this build covers SERAMAN's product line; a different product or brand (like the NGO/Aquatabs use) is new scope. Frame the NGO use case as a second sale opportunity, not a threat to shut down — price it as its own engagement rather than letting it ride for free inside the first one.

**10-steps-ahead checklist for future messages to him:**
1. Close M2 cleanly and get paid before raising any scope/pricing boundary — don't stack asks on an still-open milestone
2. State the SERAMAN-only scope boundary in writing, calmly, once M2 is closed
3. If the NGO/Aquatabs use is real and ongoing, price it as new work, not a favor
4. Keep leading with maintenance/reliability value, not "you can't use what you already have access to"
5. Match his register (warm, not formal) per [[oba]]'s established rapport, but keep the actual asks concrete underneath the casual tone

### Correction — don't hand over the how-to for free (2026-07-26)

Caught mid-session: the NGO partner's test is stalled at the review/flag step, and the immediate instinct was to offer a polished walkthrough video showing exactly how to use it. Wrong move — the partner's confusion at that one step is currently the only thing protecting the "maintenance/reliability" leverage above. Teaching them to self-serve past it, for free, before any scope conversation, gives away the exact thing that leverage depends on. This matters more than usual here specifically because Giovanni and his partner read as **not business-sophisticated** — a savvy operator would proactively ask about terms before leaning on a tool further; a naive one just keeps using what works once shown how, with no natural checkpoint ever firing on their side. The checkpoint has to be installed deliberately, not assumed.

**Revised sequencing:**
1. Send only a plain-text nudge now ("flag or approve, that's what triggers the next step") — cheap, keeps the thread alive, teaches nothing reusable
2. If it works after that: say nothing further, no video needed
3. If it's still broken (real bug, not confusion): step in directly and fix it — this reinforces maintenance leverage rather than undercutting it, since it's expertise, not a teachable trick
4. **The scope/pricing conversation with Giovanni happens right after the first successful result** — not before (reads as charging before proving anything works) and not much later (silence normalizes free access and makes raising it later feel like a rug-pull)
5. The walkthrough video, if it happens at all, gets offered *inside* that scope conversation as a deliverable of a real engagement — not handed over free beforehand

Also new signal worth weighing in: the partner has already bought real credit (Kie AI, pay-per-use) to run this test — this isn't idle curiosity, there's actual money committed, which raises the legitimacy and size of the second-sale opportunity.

### Reframe — what he actually wants this for (2026-07-28)

Researched SERAMAN independently (LinkedIn, D&B, europages) rather than assuming: small operation, 2-10 employees, founded 2012, Rome, describes itself as an "international trade and development company" — a dealer/distributor for military/tactical/outdoor/hunting gear (confirmed Warrior Assault Systems dealer), not a manufacturer, not a consumer D2C brand.

**Working hypothesis:** the video pipeline's real value to Giovanni is likely deal/pitch enablement, not social-media reach. Job ArWa5G0 (Aquatabs → NGO buyer via a partner) supports this — the video was made to pitch a specific buyer, not posted for a general audience. A small trade house's growth runs on landing specific deals with specific buyers, not follower count. If confirmed, this reframes the long-form $1,500 pipeline pitch: sell it as "generate a credible pitch video for any product/buyer combination fast," not as content marketing.

**Not yet confirmed** — plan is to surface this via one calibrated, low-pressure question once things are calm (post M2 close, post corrected-video delivery), not now while he's mid-crisis (partners leaving, still testing for bugs). Keep this conversation strictly about his goal — do not let it drift into "who else is using this," which is the separate reuse/scope conversation already deliberately sequenced for after M2.

Personal rapport notes (context only, not leverage): plays golf; has no children. Logged for relationship reference — not to be used as a psychological angle in any future ask.

## Client Stack (his side)

Kie AI (pay-per-use) · Creatomate ($29/mo) · Blotato ($29/mo) · n8n · Google Sheets · Tally form

## Contact Log

- **2026-07-24** — Direct email sent via Oba. Informed Giovanni that Fiverr was suspended, shared direct contact so relationship stays intact. No pitch.
- **2026-07-24** — Giovanni replied same day. Warm. Not upset. Confirmed he saw Fiverr is down. Said he'll test the finished work this weekend and update ASAP. Said "these days are truly endless" — he's busy, not cold. M2 test pending this weekend.
- **2026-07-26** — Giovanni emailed Oba (seraman.adv@gmail.com → Adelaja): hasn't published the videos yet, still revising — will test modifying text and generated images. M2 not yet approved/closed. No public-posting consent given or discussed.
- **2026-07-26** — Oba asked Giovanni to move to WhatsApp (+2347019486701) for easier communication. Giovanni did not take it up — replied by email instead, on a different topic.
- **2026-07-26** — Giovanni (evening): "I know a partner of mine is doing some testing. He's the person who will then manage the NGO project." — a partner of Giovanni's, running an NGO, is test-driving the pipeline for a **separate** project (not SERAMAN). Potential second client/vertical via Giovanni referral.
- **2026-07-26** — Corresponding system email seen: "Scene images ready for review — Job 6DrPK95" (images_ready, all 8 scene images generated, awaiting review before video gen). Different job ID from Giovanni's own SERAMAN job (jeG9az9) — confirms this is the NGO partner's separate test job. Emmanuel noted the partner "was testing a prod yesterday but didn't later get along with it" — test appears abandoned mid-review. Cause unconfirmed — needs execution/status check once n8n MCP reconnects.
- **2026-07-26** — Giovanni (morning, follow-up): partner "got the first email with the scenes, and then nothing else arrived. I don't know what he did; I'll check it later." Confirms the stall point exactly: images_ready email landed, nothing progressed past it. Two live hypotheses, unresolved pending n8n reconnect: (a) partner never submitted the Tally review form — system correctly waiting, not a bug — or (b) he submitted and it silently failed, same bug class as prior fixes on this build. Check whether a Tally submission for 6DrPK95 exists at all — that fact alone splits the two branches.
- **2026-07-26** — New job, **ArWa5G0** — different from both jeG9az9 (Giovanni's SERAMAN job) and 6DrPK95 (NGO partner's job). System emails: 09:47 "Scene images ready for review" (images_ready), 09:51 "Updated scene images ready for review" (images_updated) — proves a flag was submitted and the regen loop correctly fired. Giovanni, 10:24, first person ("I think everything is at a standstill") — likely his own self-test from the earlier "I'll modify text and images myself" plan, not the partner's. Read: flag→regen worked; what's likely missing is the separate approve step on the images_updated email that actually triggers video generation — reviewing/flagging alone doesn't do that. Unconfirmed pending n8n reconnect. Asked Giovanni directly whether he clicked "Approve All" on the second email.
- **2026-07-27** — n8n reconnected, root-caused. Job ArWa5G0 is SERAMAN's own new product line — Aquatabs water purification tablets, sold to an NGO buyer via a partner. SERAMAN branding intentionally present in presenter scenes (confirmed with Emmanuel) — not a bug. Found: **execution 711** (a second flag submission, scenes 1,2,3,4,6,7,8, ~08:52) got stuck at "running" forever, zero nodes executed — an isolated stuck-webhook glitch, not an instance-wide outage (no other running/crashed/error executions found in the same window). Replayed the exact captured payload via a temp-trigger swap → **execution 713, succeeded** (2m14s), new images sent. Separately found a real, fixable content bug: the IMAGE PROMPT/VIDEO PROMPT text describes the product as a "blister pack" with "domed tablet cavities," but the real product is individually sealed foil sachets — a packaging-description mismatch written at the script-generation stage, not a hallucination. This is very likely why nearly every scene keeps getting flagged. Fix identified, not yet applied: rewrite the prompt text to accurately describe the sachet packaging.
- **2026-07-27** — Giovanni: confirmed only 1 of 8 scenes (image 8) came back correct after the previous regen round; also asked whether he needs to check "Approve All" when only flagging some scenes — confirmed no, flag-only is correct behavior, Approve All is separate. Fixed the root cause: rewrote IMAGE PROMPT/VIDEO PROMPT for all 8 scenes (rows 371-378) to describe the real sealed-foil-sachet packaging instead of "blister pack/domed tablet cavities" — camera, lighting, timing, VO all preserved unchanged, only the packaging-description language corrected. Also found and fixed a live risk while there: `SERAMAN | Append Script in sheet` (in the SERAMAN Product Automation workflow) is a plain `append`, same duplicate-row bug class as the original engagement — not yet switched to appendOrUpdate; worked around it this time by writing the fix through a temp update-only path instead of re-running that node. Verified via the update node's own returned data (not just status) — execution 717, succeeded, 3s. Text is fixed; the actual images for these scenes have NOT been regenerated against the corrected text yet — that still needs one more regen pass (Giovanni re-flagging, or us triggering it directly) before the visuals actually change.

## Flags

- Green: pays, reviews promptly, expanding scope
- Green: Italian speaker — content stays in Italian
- Green: long-form already scoped at $1,500
- Green: direct email contact established 2026-07-24 (seraman.adv@gmail.com)
- Watch: Blotato posting failed once (execution 279) — social publishing still being confirmed
- Watch: M2 ($500) still in progress — confirm delivery and payment when Giovanni replies
- Watch: M2 still not approved as of 2026-07-26 — he's still revising text/images himself. Don't post publicly about this build naming SERAMAN/Giovanni until M2 is closed and he's explicitly asked
- Green: possible second client — Giovanni's partner (runs an NGO) is test-driving the pipeline for a separate project (Job 6DrPK95)
- Watch: that test (Job 6DrPK95) appears abandoned mid-review as of 2026-07-25/26 — first-time user friction at the image-review step is worth understanding, since it'll repeat with any future referral
- Watch: Giovanni ignored the WhatsApp ask, stayed on email — he's not moving off the channel he's already using
- Watch (technical debt): `SERAMAN | Append Script in sheet` (SERAMAN Product Automation workflow) is still a plain `append`, not `appendOrUpdate` — same bug class fixed elsewhere in this build. Any future job that runs script-generation twice for the same JOB_ID will create duplicate rows. Not urgent (rare path) but should be fixed properly, not just worked around again
- **2026-07-27, confirmed:** a real final video for job ArWa5G0 was rendered and sent (execution 716, parent 714 — triggered by a real "Approve All" submission at 10:03, independent of any of today's debugging) at 10:12, **13 minutes before** the packaging-text fix landed at 10:25. Downloaded and visually confirmed: every scene in the video Giovanni already has shows the wrong blister-pack packaging (verified frames at scene 1, 2, 6 — all show a visible plastic blister card with domed cavities, not the real sealed foil sachet). Giovanni currently has a defective video in hand. The tablet-hallucination-only framing drafted earlier is now outdated — the actual defect is bigger (wrong packaging throughout, not just an unconfirmable tablet detail) and needs a new message once a real corrected final video exists to offer alongside it. Not ready yet: only scene 1 has been correctly regenerated so far; scene 2's regen got corrupted by the cross-job bug below; scenes 3-7 haven't been regenerated with the fix at all.
- **2026-07-27, 11:18** — Oba sent Giovanni the honest explanation drafted earlier ("scene descriptions written before current product photos were finalized... regenerating against correct images now"). **11:32** — Giovanni replied warmly: "ok ok ok. You are working towards perfection. Grazie mille." He's not expecting anything back immediately and seems genuinely patient — takes pressure off rushing scenes 2-7 through regen before the cross-job contamination bug is properly handled.
- **RESOLVED (2026-07-27):** cross-job contamination root-caused precisely — not a shared-state/static-data bug as first hypothesized. Sheet1 had **two complete sets of 8 rows both tagged `JOB_ID: ArWa5G0`**: rows 2-9 with `PRODUCT IMAGE` pointing to a completely different job's product (`6704_bendaggio_tattico_cvn4.jpg` — a CVN4 tactical bandage), and rows 371-378 (the real ones) with the correct Aquatabs product image. A genuine JOB_ID collision/mislabeling, not concurrency. My first packaging-text fix (execution 717) matched by JOB_ID+SCENE and landed on the wrong duplicate set (2-9) — text got corrected there while the real rows (371-378) stayed unfixed. Scene 1's regen came out visually correct anyway (product-only shot, text-driven); scene 2 came out as the wrong product because presenter/hold shots lean heavily on the actual `PRODUCT IMAGE`, which on the contaminated rows was literally the CVN4 bandage.
  **Fix applied:** deleted rows 2-9 entirely (confirmed via fresh read they held no legitimate ArWa5G0 data), re-read to get the real rows' shifted numbers (371-378 → 363-370 after the delete), then reapplied the sachet-packaging correction matched strictly by `row_number` (unambiguous, no duplicates possible). Verified by reading back all 8 rows: exactly 8 rows, correct product image, correct sachet text on every scene. Confirmed clean.
  **Not yet done:** scenes 2-7 still need actual video regeneration against this now-correct text (only the sheet text is fixed; the videos from the contaminated run were never sent anywhere). Scene 1's video is already correct from execution 718.
  **Process note:** this session also had two self-inflicted mistakes while investigating — retried execution 718 as "stuck" before it actually finished (likely doubled some regen spend), and later left an old TEMP trigger node in the workflow which caused an execute_workflow call to fire the wrong (expensive) node instead of an intended read-only check. That execution (720) ran for 11 minutes and succeeded — since it ran before the contaminated rows were deleted, it likely also burned real credits producing more wrong-product videos, same as 718. Not worth chasing further since the bad underlying data is already cleaned up; the spend is just sunk cost. Lesson banked: always fully clean up TEMP nodes before leaving a workflow, and wait longer before concluding an execution is stuck.
- **2026-07-27** — Giovanni emailed again (unprompted, before any corrected video was sent back): confirms he's reviewing the already-sent defective final video directly. Two points: (1) audio is "almost perfect" but he wants to know if voiceover text can be edited directly post-generation, without a full regen; (2) "many errors" in pill packaging display across the various clips — "the only real one is the one you see at the end of the video." **This independently confirms the root-cause diagnosis with certainty**: the end clip is scene 8 (Branch A, product-only/text-driven, matte-black-surface shot) — the only scene that rendered correctly, exactly matching scene 1's outcome (also Branch A). Every Branch B scene (2-7, presenter-holding, image-driven) is confirmed wrong in his own words, consistent with those scenes having pulled from the contaminated product-image rows before the fix. No new information changes the plan — this is the same defective video already identified and downloaded; scenes 2-7 still need to be regenerated against the now-corrected sheet data (rows 363-370) before a replacement is sent.
  **Audio-edit question — resolved, corrected understanding:** "audio text" = caption/on-screen text, not the embedded Veo dialogue. Confirmed via Creatomate docs: captions are a text field on the Creatomate render step (separate from Kie AI video generation), currently sourced from `voiceover_text` — so caption wording can be edited and re-rendered without touching the underlying video. Cheap, fast, no regen needed.
  **Root cause, sharpened:** the product-only shots (1, 8) work because they barely deviate from the reference photo — near-direct reproduction. Presenter-hold shots (2-7) require the model to synthesize a new hand-object interaction it's never seen, and if the sachet's actual surface/print isn't clearly revealed toward camera in that synthesis, the model falls back on its training prior for "tablets in packaging" — blister pack. This holds independent of the now-fixed duplicate-row contamination bug. Fix direction: presenter must directly reveal the packaged product to camera in the shot (not just "hold" it) so there's nothing left for the model to guess.
  **Scope note sent to Giovanni:** caption/text editing was not part of the original build scope — flagged to him plainly as a deliverable we can do, but outside what was already scoped/priced. First explicit scope-boundary statement made to him this engagement — small and low-stakes (a nice-to-have, not a blocker), a soft precedent-setter ahead of the bigger SERAMAN-only boundary conversation planned for after M2 closes.
  **Correction (2026-07-28):** Giovanni clarified "audio text" himself — he means the presenter's spoken dialogue/script, not captions. My caption-based reading was wrong; his own words confirm the harder case: "So I remake the video from scratch" — no cheap edit path exists today, matching the original Veo-bakes-dialogue-in assessment.
  **Real gap found, fix identified:** checked the actual review-email nodes (`SERAMAN | Send Updated Image Review Email`, `SERAMAN | Send Video For Review`) in the Scene Approval workflow — confirmed neither ever surfaces the presenter's script text to Giovanni, only scene images. He has zero visibility into the dialogue before it's locked into a generated (expensive) video. Fix: add each scene's dialogue line into the existing scene-image review email, reusing the same per-scene Tally approve/flag loop already built — turns a post-hoc "remake from scratch" into a free catch at the image-review stage. Not yet built.
- **2026-07-28** — Giovanni: "Grazie sempre a te.. Excellent support. But we're close to perfection." Confirmed he's now testing across multiple different SERAMAN products (not just Aquatabs) — real, expanding usage of the pipeline. Also disclosed, unprompted: **his partners are leaving the project, saying they're not satisfied** — he personally still believes in it ("I believe we're on the right track and we'll get to the top"). Separately mentioned driving 800-1000km every other day in heavy heat, apologized for slow/piecemeal replies. Will run more tests this evening.
  **Read:** this is a trust/morale moment, not a business one — he's absorbing real pressure from departing partners and choosing to keep backing the project anyway. Reinforces the existing posture ([[strategic-frameworks]]): hold the scope/pricing boundary conversation until after M2 closes, don't stack any ask onto a message like this. Replied warmly, acknowledged the partner situation and the driving, no business ask attached.

## Wikilinks

[[seraman]] · [[oba]] · [[n8n]] · [[claude-api]] · [[identity]]
