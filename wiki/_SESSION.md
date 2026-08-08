---
sensitivity: private
entity_type: system
name: Session Checkpoint
last_updated: 2026-07-24
---

# Session Checkpoint

Write to this file at the END of every session. Read it at the START of every session BEFORE anything else.
This prevents cold starts. Context should never have to be rebuilt from scratch.

---

## Last Session: 2026-08-07 to 2026-08-08 — Portfolio batch 2 + Project Catalog + SolarCheck

**What we worked on:**
- Rendered 3 new portfolio slide sets (3 slides each, 9 PNGs total):
  - Kairos — statistical value bet engine (Python, Pinnacle, Kelly Criterion)
  - YCT Exam Nav — university exam scheduling system (Next.js, Supabase, DSatur)
  - Hephzibah OS — autonomous AI outreach system (Python, Claude AI, Playwright, Telegram)
- Portfolio form copy written for all 3 projects → `outputs/strategy/2026-08-07-portfolio-copy-batch2.md`
- All 10 portfolio projects have slides + form copy. Upload order documented.
- Project Catalog set up on Upwork: both items sent to review
  - $149 diagnostic: "Diagnose your broken n8n workflow and give you a written repair plan"
  - $499 agent build: "I'll build an n8n AI agent that runs a real task in your business every day"
- SolarCheck Contributor Agreement reviewed (Bayonet team sent it)
  - Agreement gives zero guaranteed compensation, permanent IP assignment, permanent confidentiality
  - Advised counter-proposal with 3 asks: (1) 2-year confidentiality limit, (2) monthly hour cap, (3) equity clause (0.5-1% vesting over 2 years)
  - Emmanuel has not signed yet — waiting to send counter to Bayonet

**What is LIVE and needs action:**
1. **Upwork ID verification** (q010) — still not confirmed done. CRITICAL. Settings → Identity Verification.
2. **Withdrawal method** (q011) — still not confirmed done. CRITICAL. Settings → Get Paid.
3. **Bayonet solar (SolarCheck)** (q015) — send counter message to Bayonet with 3 asks before signing.
4. **Cert sprint** (q016) — education.anthropic.com (14 courses) then learn.n8n.io (4 courses). Deadline 2026-08-14.
5. **Portfolio Looms** (q012) — Emmanuel recording 3 Looms himself. SERAMAN first.
6. **Overview rewrite** (q018) — Recent work section + new CTA. Can run /profile-audit to get current text.
7. **Testimonials** (q014) — Follow up if any not submitted by 2026-08-16.
8. **Portfolio slide design** — product color accent planned: each slide gets one color pulled from the actual product's visual identity. Not done yet.

**What was decided:**
- Do NOT sign SolarCheck agreement as written. Counter first with 3 asks.
- Equity must be in writing before any work starts on SolarCheck.
- Project Catalog q017 resolved — both items sent to review.
- Portfolio slides for all 10 projects are complete (form data ready, images uploaded separately).

**Brain commits needed:**
- _SESSION.md ✓ (this update)
- _QUEUE.md ✓ (q017 resolved earlier this session)

---

## Last Session: 2026-08-05 to 2026-08-06 — Upwork own account full profile build

**What we worked on:**
- Upwork restriction on Emmanuel's own account (011b48d2eabbfa6361) was lifted. Switched from partner account to own account.
- `profile_scraper.py` fixed — clipboard method, CRLF normalization, parser rebuilt from scratch.
- Scraped 4 competitor profiles: Brian Wade ($73/hr), Mikhail Oskola ($95/hr), Gopal/Twopir ($65/hr), Ryan Ramshaw ($50/hr).
- Full competitor intelligence node written → `upwork/market/patterns/competitor-profiles-n8n-niche.md`.
- Built Emmanuel's profile section by section in Ramshaw coaching mode:
  - Title: "AI Automation & Python Engineer | n8n | Full Stack | API Integration" (68 chars, $55/hr)
  - Overview: Ramshaw format (promise opener + Loom offer + "A little more about me" + bullet proof + expertise list). SERAMAN project referenced as real proof.
  - Skills: 20 skills in priority order (AI Agent Development, n8n, Automated Workflow, API Integration, BPA, Workflow Automation, AI Model Integration, CRM Automation, AI Implementation, Automation, Python, Django, React, Next.js, TypeScript, JavaScript, OpenAI API, Zapier, Airtable, Email Automation).
  - Certifications: 4 total (updated n8n cert name, kept Hugging Face, added 2 custom manual certs).
  - Employment History: 4 entries. Fixed "Upwork | Upwork" and "Contract | Contract" duplicates.
  - Other Experiences: Basketball & Chess entry written. Keyword spam section removed.
- 5 LinkedIn testimonial requests sent via email + Upwork recommendation requests:
  1. Cyrus (osawayecyrus@gmail.com) — n8n technical peer, 4 workflows in 4 days. LinkedIn: cyrus-osawaye-6b71a1267
  2. Rejoice (rejoicedindu18@gmail.com) — content automation client. LinkedIn: rejoice-chikeluba-08326a386
  3. Oba (obanijesu7@gmail.com) — full-stack web app client (outside client voice). LinkedIn: adelaja-obanijesu-730490396
  4. Bayonet (bayomisimon@gmail.com) — social media automation collaboration (Revamp project). LinkedIn: bayomi-simon-b92870238
  5. Samuel (jammyrix@gmail.com) — lead generation automation client. LinkedIn: samuel-john-b24911205
- Intro video script written → `outputs/strategy/2026-08-06-profile-intro-video-script.md`
- Client account created on Upwork ("Adekoya Digital") for competitive research and fake job analysis.
- Bayonet new opportunity: solar energy calculator project (fuel spend → solar capacity recommendation). US client connection behind it. Emmanuel advised to confirm payment terms before committing.

**What is LIVE and needs action:**
1. **Upwork ID verification** — NOT done. Blocker. Settings → Identity Verification.
2. **Withdrawal method** — NOT done. Blocker. Settings → Get Paid.
3. **Available Now badge** — NOT confirmed on. Settings → toggle on. 2 connects/day.
4. **Portfolio Looms** — 3 needed: SERAMAN pipeline first, SavvySox second, one software project third.
5. **Intro video** — script ready. Needs recording and upload.
6. **Project catalog** — not set up yet. Do after ID verification.
7. **Testimonials** — 5 in motion. Follow up if not submitted by 2026-08-16.
8. **Bayonet solar project** — Emmanuel must confirm payment structure before committing to the build.
9. **SERAMAN (Giovanni)** — M2 test status unknown from last session. Check with Oba.
10. **Revamp Consulting (Bayonet)** — still blocked on payment number + logo. Now deprioritized given solar project is the new conversation.

**What was decided:**
- Own Upwork account (011b48d2eabbfa6361) is now the active account. Partner account retired.
- Rate set at $55/hr (held the line against Emmanuel's $15/hr push).
- Ramshaw's actual overview format is longer than previously documented — includes promise + Loom offer + "A little more about me" + bullet credibility + expertise list.
- Testimonials: "Basics" is a weak word in cert titles. Generic company names trigger Upwork account review.
- Client account company name: "Adekoya Digital" — can be changed later via Settings → My Info.
- Fake job strategy: use adjacent title (not exact niche) to avoid recognition by savvy freelancers.

**Brain commits needed:**
- _SESSION.md (this file) ✓
- _QUEUE.md (q001 resolved, new items added) — doing now
- upwork/identity/profile.md (full rewrite for own account) — doing now
- upwork/market/patterns/competitor-profiles-n8n-niche.md — already committed earlier in session

---

## Last Session: 2026-07-24 (UPDATED — full day)

**What we worked on:**
- LinkedIn brand card (light version) — Apple shadow, lemon pills, role labels fixed. Shipped to Desktop.
- SavvySox LinkedIn post went live (Post 1 of the hard schedule). 33 impressions — dormant account tax, expected.
- LinkedIn content strategy locked with hard dates: Post 1 Thu 2026-07-24 ✓, Post 2 Sat 2026-07-26, Post 3 Tue 2026-07-29, Post 4 Thu 2026-07-31, Post 5 Sat 2026-08-02, Post 6 Tue 2026-08-05. All 8AM WAT.
- Fiverr suspended permanently. Crisis protocols written and wired into CLAUDE.md.
- Giovanni (SERAMAN) — notified of Fiverr suspension via Oba. Giovanni replied warm, said he'll test M2 this weekend.
- Giovanni's M2 test imminent — SERAMAN workflow pre-test audit completed (see below).
- Petit Lit Furniture (Fradel Saks) — contacts found: sales@petitlitfurniture.com / 718.851.0367. Reconnect email drafted (Fiverr suspension context). PDF proposal already on file at outputs/strategy/2026-07-10-petit-lit-furniture-redesign-proposal.pdf.
- WhatsApp crisis debrief (Oba) — Oba partnership protocol written. Communication rules under pressure documented.
- OS deep fix: 4 new concept nodes (client-intake-protocol, platform-crisis-protocol, active-agent-mode, tool-first-rule), CLAUDE.md Operational Mechanics section added.

**What is LIVE and needs action:**
1. **Giovanni (SERAMAN) testing M2 this weekend** — SERAMAN pre-test audit done. Open risks: Blotato social posting never confirmed end-to-end, Scene 1/8 volume inconsistency (60%/100% vs 200% for scenes 2-7), Gemini Omni switch awaiting Giovanni's greenlight. Monitor for any test results or errors.
2. **Petit Lit (Fradel Saks)** — reconnect email ready to send. Send to sales@petitlitfurniture.com. Once she replies, resend PDF proposal and move to deposit.
3. **Revamp Consulting (Bayonet)** — still waiting on payment number + logo PNG. Build cannot start.
4. **Elbert (SavvySox)** — recovery email sent to elbert@savvysox.com. Await reply. LinkedIn Day 3, Instagram Day 5 if no reply.
5. **Post 2 LinkedIn** — publish 2026-07-26 8AM WAT (SERAMAN debugging transparency angle). Card already rendered. Be online 60 min after posting. First comment within 60 seconds.
6. **Emmanuel's Upwork account** — payment method not added. Fix to unlock bidding.

**What was decided:**
- Off-platform contact capture is MANDATORY — $12,500 lost in one night enforced this permanently.
- Petit Lit outreach = reconnect (not cold) — proposal was already sent via Fiverr.
- Rate floor for Petit Lit going direct = $700 (was $600 because of Fiverr 20% + Oba 50/50 cut — now 100% to Emmanuel).
- SERAMAN M2 is functionally ready. Open items are non-blocking for Giovanni's weekend test unless Blotato fails.

**Brain commits pushed:**
- client-intake-protocol.md ✓
- platform-crisis-protocol.md ✓
- active-agent-mode.md ✓
- tool-first-rule.md ✓
- oba-partnership.md ✓
- fiverr/_INDEX.md updated ✓
- _PIPELINE.md updated (Petit Lit added as prospect) ✓
- upwork/clients/active/petit-lit-fradel.md ✓
- CLAUDE.md Operational Mechanics section ✓

---

## SERAMAN Pre-Test Audit (for Giovanni's weekend test)

**System prompt:** v5.10 LIVE. Phonetic respelling for English loanwords active.

**CONFIRMED FIXED before test:**
- ✅ English caption bug (voiceover_text field fixed in Edit Videos Code node)
- ✅ Doubled/garbled captions (second Creatomate text element deleted)
- ✅ Hallucinated background text (no-text block in every presenter scene prompt)
- ✅ CVN4 product name as label (no-text block at START of prompt)
- ✅ Skull and crossbones (no skulls/crossbones/danger symbols block added)
- ✅ Pronunciation of English loanwords (v5.10 phonetic respelling live)
- ✅ Wrong product in last scene (re-verified, already fixed by 2026-07-08)
- ✅ VO cut mid-sentence (12-word cap, "finish by second six" pacing, v5.6)
- ✅ Volume scenes 2–7 boosted to 200%
- ✅ Kie outage error emails now show amber "upstream issue" instead of generic red failure
- ✅ Gmail alert nodes (rejection + duplicate) — operation field restored, now sending

**OPEN before Giovanni's test (non-blocking but worth watching):**
- ⚠️ Blotato social posting — never confirmed end-to-end. Fires when Giovanni clicks Approve in the review email. If it fails: manually post from Creatomate render URL + debug Blotato node.
- ⚠️ Scene 1 volume at 60%, Scene 8 at 100% — scenes 2-7 are at 200%. Inconsistent. Low priority but Giovanni flagged volume before.
- ⚠️ Gemini Omni switch still awaiting Giovanni's greenlight — Veo3 Fast still in production. Joint defect class exists on hand/contact scenes. May or may not surface on his weekend test.
- ⚠️ Sheet2 stale duplicate rows — could corrupt regen URL writes if he triggers a regen. Workaround: if regen writes corrupt, manually clear Sheet2 rows before re-run.
- ⚠️ "seraman" end-card too bare — Giovanni flagged Jul 06, still unconfirmed if fixed.

**If Giovanni hits an error:** Read the Error Handler email he receives — amber = Kie platform issue (wait and retry), red = workflow bug (pull n8n execution log for that run ID).

---

## Session Template (copy for each new session)

```
## Last Session: YYYY-MM-DD

**What we worked on:**
- 

**What is LIVE and needs action:**
1. 

**What was decided:**
- 

**Brain commits needed:**
- 
```

---

## How to Use

**At session START:** Read this file first. Skip the "what are we doing" back-and-forth — the context is here.

**At session END:** Update the "Last Session" block above with:
- What was worked on
- What is now live and needs follow-up
- Decisions made
- Whether brain was committed and pushed
