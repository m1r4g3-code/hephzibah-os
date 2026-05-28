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

## The 5-Pass Pipeline

Every proposal goes through 5 passes. For high-value jobs (composite score 80+): all 5 passes. For mid-range (65–79): passes 1, 3, 4, 5.

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
[Hook — 1 sentence. Their situation. NOT "I".]
[Diagnosis — 2-3 sentences. Name the real problem.]
[Proof — 1-2 sentences. One specific relevant thing.]
[Question — 1 sentence. Sharp. Specific to this job.]
```

**Voice constraints:**
- First word: not "I"
- No AI-smell phrases (see `identity/voice.md`)
- Confident, not eager
- Length: 150–250 words

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

## Wikilinks

[[proposal-anatomy]] · [[upwork-psychology]] · [[elite-freelancer-model]] · [[pain-before-pitch]] · [[upwork-voice]] · [[job-scoring]]
