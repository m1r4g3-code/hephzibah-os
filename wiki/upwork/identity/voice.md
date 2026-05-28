---
sensitivity: private
entity_type: concept
name: Upwork Voice Guide
aliases: ["upwork-voice", "proposal-voice", "writing-style"]
last_updated: 2026-05-27
relationships:
  - target: "[[identity]]"
    type: part_of
    strength: 10
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
  - target: "[[proposal-anatomy]]"
    type: reinforces
    strength: 9
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
  - target: "[[specificity-as-credibility]]"
    type: reinforces
    strength: 8
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
---

# Upwork Voice Guide

Emmanuel's writing voice for Upwork proposals. This is the calibration document for the voice engine. Every proposal should pass through this before sending.

The goal: proposals that sound like a senior consultant who happens to be 20, not like an AI assistant pretending to be senior.

---

## The Voice in One Sentence

**Direct, specific, slightly elevated register, confident without being arrogant, occasional Lagos rhythm in sentence construction.**

Not formal. Not casual. The register of a smart person who respects your time and expects you to respect theirs.

---

## Sentence-Level Patterns

### What Emmanuel's voice sounds like:

**Directness:**
- "Your data sync problem is actually a schema design problem in disguise."
- "This isn't a performance issue — it's an architecture decision that needs to be made."
- "The job post says 'simple integration' but I've seen this exact setup before and it isn't."

**Confident questioning:**
- "Before I can give you an accurate scope, I need to know one thing..."
- "Are you open to a slightly different architecture? One that solves this permanently rather than patching it?"
- "What happens to this system when your user base doubles? That's the question that changes the design."

**Proof via specificity (not credential):**
- "I built this for a German medical admin team — 4 workflows in 4 days."
- "Last month I solved a near-identical data pipeline problem for a SaaS company. Their 6-hour manual reconciliation went to 12 minutes."
- "I've hit this exact n8n bottleneck before. The fix is unintuitive but it works."

**Slight elevation (not formal):**
- "This is solvable." (not "I can help you solve this")
- "The architecture here matters." (not "I believe the architecture is important")
- "Let me know if that framing resonates." (not "Please let me know your thoughts at your earliest convenience")

---

## Sentence-Level Patterns to Avoid

**AI-smell phrases (immediate disqualifiers):**
- "I would be delighted to..."
- "I am passionate about..."
- "As per your requirements..."
- "I hope to hear from you soon."
- "I am a highly motivated and dedicated..."
- "Leverage my expertise to..."
- "I believe I would be a perfect fit..."
- "Please feel free to reach out..."
- "I have extensive experience in..."
- "I am well-versed in..."
- "I would love the opportunity to..."
- "Thank you for considering my application."

**Corporate/consulting jargon:**
- "leverage", "synergy", "holistic approach", "robust solution", "scalable", "best-in-class"
- "going forward", "at the end of the day", "move the needle"

**Weakness signals:**
- "I think I could...", "I believe I can..."
- "I would try to...", "I'll do my best to..."
- "I'm not sure if this is exactly what you need but..."
- Starting with "I" as the first word

**Over-explaining:**
- Listing all technologies you know
- Explaining what your tech stack is before diagnosing their problem
- Writing more than 250 words

---

## Structure Patterns

### The Opening Line (Most Important)

Rule: First word cannot be "I". First sentence must be about THEM.

**Patterns that work:**
- Lead with the diagnosis: "Your [X] has a [Y] problem that shows up as [Z]."
- Lead with the reframe: "The [stated problem] is usually a symptom of [real problem]."
- Lead with a specific observation: "Three things in your job description tell me [insight]."
- Lead with the outcome at risk: "If [problem] isn't addressed properly, [consequence]."

**Patterns that kill proposals:**
- "Hi, I'm Emmanuel..." (they don't care yet)
- "I came across your job post..." (obviously — you're applying)
- "I'm very interested in your project..." (everyone is, that's why they applied)

### The Length

150–250 words. Always.

Count them before sending. If over 250: cut the proof section to one sentence. If under 150: the diagnosis is too thin.

---

## Calibration Corpus

Best proposals that have won or gotten replies go in `upwork/proposals/best/`. Before writing a new proposal, read 1-2 of these to recalibrate. The goal is not to copy them — it is to hear the voice in your head before writing.

---

## Voice Score Scale (used by voice.py)

| Score | What it means |
|---|---|
| 9–10 | Unmistakably Emmanuel. No AI smell. Specific, confident, right length. |
| 7–8 | Mostly sounds right. One or two phrases to clean up. |
| 5–6 | Some AI-smell phrases present. Or too long. Or generic hook. Fix before sending. |
| 3–4 | Multiple AI phrases, generic opening, or wrong length. Rewrite. |
| 1–2 | Sounds like a ChatGPT proposal. Do not send. Start over. |

**Minimum acceptable score before sending: 7**

---

## Calibration Log

Update this section when Emmanuel gives feedback on specific proposals:

| Date | Feedback | What to adjust |
|---|---|---|
| — | — | Add entries here after Emmanuel rates proposals |

---

## Wikilinks

[[proposal-anatomy]] · [[specificity-as-credibility]] · [[identity]] · [[builds-before-asking]]
