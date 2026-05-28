---
sensitivity: private
entity_type: concept
name: Proposal Framework
aliases: ["proposal-playbook", "proposal-methodology"]
last_updated: 2026-05-27
relationships:
  - target: "[[proposal-anatomy]]"
    type: reinforces
    strength: 10
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
  - target: "[[elite-freelancer-model]]"
    type: part_of
    strength: 9
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
  - target: "[[pain-before-pitch]]"
    type: reinforces
    strength: 9
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
---

# Proposal Framework

The operational playbook for writing Upwork proposals through the OS. This is the working methodology — not the structural concept (that's in `concepts/proposal-anatomy.md`).

---

## The Goal of a Proposal

Ramshaw's words: "The goal of your proposal isn't even to get hired. The goal is to get viewed. Stop trying to win the job in 200 words. Start trying to win the conversation."

The sequence: Proposal → get viewed → get replied → start conversation → close on call.

The written proposal's only job is to make them reply. The close happens on the call.

---

## Step 0 — Determine Job Type (Context vs No-Context)

Before any other pass, classify the job:

**Context job:** Has website URL, social media links, or a Google-able business name → Full Audit pipeline (all passes)

**No-context job (80% of jobs):** No external links, no identifiable business → Short Loom asking for more context. Skip to Pass 6 only.

**To find context jobs quickly:** In Upwork Advanced Search, type `www` in the "Any of these words" field. Filters for jobs containing URLs.

---

## The 6-Pass Pipeline (Context Jobs)

Every proposal goes through 6 passes. For high-value jobs (composite score 80+): all passes. For mid-range (65–79): passes 1, 3, 4, 5, 6.

### Pass 1 — Research

**Output:** Structured understanding of the job and client.

Questions to answer:
1. What is the stated deliverable?
2. What is the actual business outcome the client wants?
3. What does the client's history tell us about them?
4. What is the client's likely technical sophistication level?
5. What is the urgency signal?
6. Any red flags? Any green flags?

**Source:** Job card from `/job-qualify` output. If not yet qualified, run qualification first.

---

### Pass 2 — Psychology

**Output:** Client archetype + hidden fear + what they need to believe to hire.

Questions to answer:
1. Which client archetype matches? (See `playbooks/client-types.md`)
2. What fear is driving this job post? (5 fears in `concepts/upwork-psychology.md`)
3. What has the client tried before? (Often implied in the description)
4. What does the client need to believe about Emmanuel to hire him?
5. What's the one thing that would make this client say "finally, someone who gets it"?

**Output format:**
```
Archetype: [name]
Hidden fear: [1 sentence]
What they need to believe: [1 sentence]
"Finally someone who..." moment: [the insight to land in the proposal]
```

---

### Pass 3 — Strategy

**Output:** The diagnosis frame + proof selection + question choice.

Decisions to make:
1. What is the diagnosis frame? (The real problem, not the stated one)
2. Which proof point maps most directly to this situation?
3. What is the conversation-opening question?
4. What is the positioning angle? (expert? operator? specialist?)

**Do NOT start writing the proposal here.** This is the blueprint.

```
Diagnosis frame: [1-2 sentences — the real problem to name]
Proof to use: [the one specific thing from Emmanuel's history]
Opening question: [the sharp, specific question for the CTA]
Positioning angle: [how Emmanuel positions relative to this job]
```

---

### Pass 4 — Draft

**Output:** Full proposal text, 150–250 words.

**Structure (from `concepts/proposal-anatomy.md`):**
```
[Opener — 1 sentence. Their situation. NOT "I". Something specific from their job.]
[Bullets — 3-4 observations about THEIR specific situation. Scannable. Not skills.]
[Loom link — "I put together a quick walkthrough: [link]"]
[Question — 1 sentence. Low friction. Answerable in 10 seconds.]
```

**The closing question rule (Ramshaw: "increases reply rate 50%+"):**
A question mark creates an open loop the brain can't ignore. But the question must require minimal cognitive load. Ask something answerable in 10 seconds:
- YES: "Is this project live yet or still in planning?"
- YES: "Roughly how many leads are you generating per month?"
- YES: "Would Tuesday work for a quick call?"
- NO: "What's the big vision for the company?" (homework — too much effort)
- NO: "What are your thoughts on my approach?" (vague — no clear answer)

**Voice constraints:**
- First word: not "I"
- No AI-smell phrases (see `identity/voice.md`)
- Confident, not eager
- Length: 150–250 words
- Bullets = specific findings, not skill lists

---

### Pass 5 — Voice Check

**Output:** Voice score (1–10) + specific phrases to fix.

Run `python scripts/voice.py "[draft text]"` for automated check.

If score < 7: revise. Rerun check.

**Common fixes:**
- Replace "I would be happy to" → "I can"
- Replace "I believe I can" → just state it
- Cut the last sentence if it's "I look forward to hearing from you"
- If first word is "I": restructure the opening line
- If over 250 words: cut proof section to 1 sentence

---

### Pass 6 — Loom Script

**Output:** 60–90 second video script ready to record.

This is non-optional on jobs scoring 75+. Ramshaw built $10k/month specifically on Loom video proposals. A personalized video attached to a proposal is immediately memorable — most clients have never received one. It makes the proposal feel 10x more custom regardless of the text quality.

**Structure (60–90 seconds exactly):**
```
[0:00–0:10] Hook — Name the specific thing from their job post that caught your attention.
            "I noticed you're building [X] — you mentioned [specific detail]."
            DO NOT say "Hi, I'm Emmanuel." They can see your name. Start with their situation.

[0:10–0:25] Problem reframe — Show you understand the real problem.
            "The thing that usually trips people up with this is [non-obvious insight]."
            This is the diagnosis from Pass 2, spoken aloud.

[0:25–0:55] Solution sketch — Walk through how you'd approach it.
            If possible: open a blank doc or whiteboard and sketch the architecture live.
            Ramshaw often builds a quick workflow diagram on screen while narrating.
            "Here's how I'd structure this: [X] feeds into [Y], and the tricky part is [Z]."
            This is PROOF. You are demonstrating thinking, not claiming capability.

[0:55–1:10] One result — Name a similar thing you built and the outcome.
            "I did this for [type of company], they went from [state A] to [state B]."
            Specific. Not "I have experience with similar projects."

[1:10–1:20] CTA — Same sharp question as the written proposal.
            "One thing I'd want to know before scoping this: [the question]."
            Close. Don't say "I hope to hear from you."
```

**Recording notes:**
- Use Loom (loom.com) — the client gets a link, not a file attachment
- Paste the Loom link in the first line of your written proposal, above the text
- Video thumbnail should show your face + screen share simultaneously (Loom default)
- No script reading on camera — talk like you're explaining to a colleague
- One take unless you stumble badly. Imperfect = authentic. Perfect = scripted.
- Title the Loom: "[Job type] — Quick thoughts on your project"

**When to skip Loom:**
- Jobs scoring below 75 (don't spend the time)
- Client has 0% hire rate (window shoppers won't watch a video)
- Very simple/small tasks where a video feels disproportionate

---

## Proposal Anti-Patterns (With Fixes)

### The Resume Dump

**Problem:** Lists all technologies and certifications. No diagnosis.
**Why it fails:** Client reads it as "this person knows stuff." Not "this person understands my problem."
**Fix:** Delete the skills list. Replace with one diagnosis sentence.

### The Enthusiasm Trap

**Problem:** Leads with excitement ("I'm really excited about this project!").
**Why it fails:** Signals more need than expertise. Client loses frame.
**Fix:** Lead with an observation about their situation, not your feelings about it.

### The Question Flood

**Problem:** Ends with 5 questions about scope, timeline, budget, etc.
**Why it fails:** Puts the burden of the interview on the client before they've decided to hire.
**Fix:** One sharp question. The rest come after they reply.

### The Generic Proof

**Problem:** "I have 5 years of experience with React."
**Why it fails:** Everyone says this. It means nothing specific.
**Fix:** "I built this exact dashboard pattern for a SaaS company in Q1 — their load time went from 4.2s to 0.8s after the state management restructure."

### The Wall of Text

**Problem:** 400-word proposal covering everything.
**Why it fails:** Client scans, doesn't read. Shows you can't prioritize.
**Fix:** Cut to 200 words. If you can't say it in 200 words, you haven't understood it well enough yet.

---

## The Bid Decision Flowchart

```
1. Run /job-qualify → get composite score
   ├── Score < 65 → SKIP. Done.
   ├── Score 65-79 → WATCHLIST unless strong niche fit
   └── Score 80+ → BID. Proceed.

2. Any red flags triggered?
   └── Yes → SKIP regardless of score.

3. Apply Ryan Ramshaw filter: "Would a top 1% freelancer bid on this?"
   └── Honest no → SKIP. Or reconsider the rate.

4. Is scope clear enough to protect JSS?
   └── No → SKIP. Or ask clarifying question first (only for 90+ score jobs).

5. PROCEED to 5-pass pipeline.
```

---

## After Sending

1. Log in `upwork/proposals/sent/YYYY-MM-DD-slug.md`
2. Note connects spent
3. Set follow-up reminder if no reply in 5 days
4. Log outcome within 24h of knowing it

---

## SOW — Post-Discovery Call Structure

When a client replies and a discovery call happens, the SOW closes the deal. It is not a
follow-up email. It is a formal document that signals: this is a practice.

Full template in `identity/brand.md`. Key additions beyond the basic structure:

**Checkpoint gates in every multi-phase build:**
Number them into the pipeline. "⟳ CHECKPOINT 1 — Prompt Review" between steps. The client
approves before work continues. This protects JSS (no "it wasn't what I expected") and signals
professionalism. Never deliver a multi-phase project without at least one explicit gate.

**Cost per run (automation projects only):**
For any project that produces repeating outputs — leads processed, reports generated, emails
sent, records synced — include a line-item cost table: tool/API + per-unit cost + role.
Then add: manual baseline cost vs automated cost vs savings per run. This turns the project
fee into a math problem the client wins. Niche-agnostic: works for CRM automation, lead
scoring, content pipelines, data sync — anything with a recurring output.

**Ongoing platform costs (if client needs tool subscriptions):**
List every tool the system depends on post-delivery, with monthly cost and why it's in the
stack. Clients hate surprise bills after delivery. Showing this upfront is a trust signal.
Clearly note: "These are tool costs, not fees to me."

**When NOT to include cost sections:**
One-time builds, static integrations, or any project with no recurring compute cost. Don't
add sections that don't apply — an overcomplicated SOW reads as padding.

---

## Wikilinks

[[proposal-anatomy]] · [[upwork-psychology]] · [[elite-freelancer-model]] · [[pain-before-pitch]] · [[upwork-voice]] · [[job-scoring]]
