---
sensitivity: private
entity_type: concept
name: Discovery Call Playbook
aliases: ["discovery-call", "prep-call", "client-call", "meeting-prep"]
last_updated: 2026-05-28
relationships:
  - target: "[[elite-freelancer-model]]"
    type: reinforces
    strength: 10
    first_seen: "2026-05-28"
    last_reinforced: "2026-05-28"
  - target: "[[handoff]]"
    type: part_of
    strength: 8
    first_seen: "2026-05-28"
    last_reinforced: "2026-05-28"
  - target: "[[upwork-psychology]]"
    type: reinforces
    strength: 9
    first_seen: "2026-05-28"
    last_reinforced: "2026-05-28"
---

# Discovery Call Playbook

The discovery call is not a sales call. It is a diagnostic session.

Emmanuel is the doctor. The client is describing symptoms. The job is to find the actual disease —
then decide whether to treat it, and at what price.

This reframe is not cosmetic. It changes everything:
- Doctors set the agenda. Patients don't interview doctors.
- Doctors ask the questions. Patients answer them.
- Doctors give the verdict. Patients do not prescribe for themselves.
- Doctors can refer you elsewhere. They don't beg for your case.

If Emmanuel walks into a call hoping to impress the client enough to get hired, he will lose
the frame within 90 seconds. If he walks in as someone evaluating a problem — he holds it.

Generate the pre-call brief with `python scripts/call_prep.py` before every meeting.

---

## Before the Call — Pre-Call Research Protocol

Run `/prep-call [job-file or client-name]`. This generates the brief. The brief has:

1. **What we know** — hard facts from the job card and client data
2. **The kill shot** — one specific observation from their site or post to open with
3. **Question stack** — 7-8 questions ordered by call phase
4. **Red flags to listen for** — signals that change the decision
5. **Close script** — exact words to end with a clear next step

**Minimum research before any call (15 minutes):**

- Read the job post again. The second read reveals what the first one missed.
- Visit their website. Find ONE specific thing that relates to what they're building.
  It doesn't need to be a problem. Just something specific you noticed.
- Check their Upwork reviews section. Freelancers address clients by name — this is how
  you find their first name if not visible on the profile.
- Google the company name if identifiable. AppSumo listings, LinkedIn, Product Hunt —
  any signal of their market and size.
- Check what they've hired for before (Upwork job history) — this tells you what they
  understand and what they don't.

**The kill shot:** One specific observation that shows you did homework before the call.
Not generic ("I saw your website looks great"). Specific:

- "I noticed your pricing page has three tiers but your Zapier integration only supports the top
  two — is that intentional or a gap you're trying to close?"
- "I was looking at your product — it seems like the intake form is the bottleneck before leads
  reach your CRM. Is that where the problem is?"
- "I can see you're running Make and Airtable from the stack you mentioned — that combination
  tends to hit record limits around 50k rows. Where are you now?"

One observation like this in the first 60 seconds and you are not like any other freelancer
they spoke to that day.

---

## Call Structure

Total time: 25-35 minutes. Do not run long. Sharp and focused signals respect for their time.

```
Phase 1  Rapport               1-2 min
Phase 2  Agenda Frame          30 sec
Phase 3  Diagnosis             12-15 min
Phase 4  Recommendation Frame  3-4 min
Phase 5  Qualification         3-4 min
Phase 6  Close to Next Step    1-2 min
```

---

### Phase 1 — Rapport (1-2 min)

Light. Human. Do not linger here.

- Where are they from (Upwork shows country, but asking acknowledges them as a person)
- How long they've been using Upwork or working on this project
- One genuine observation about their business or post

The goal is: they feel like they're talking to someone who already knows a bit about their
world — not a stranger pitching blind.

**Do not:**
- Ask "So tell me about yourself!" (too vague, puts labor on them)
- Over-talk about yourself
- Stay in rapport longer than 2 minutes (it reads as nervousness)

---

### Phase 2 — Agenda Frame (30 sec)

This is the moment that signals seniority. Set the agenda before they do.

"Before I give you any recommendations, I want to make sure I actually understand the full
picture. I have a few questions — is it okay if I lead for a bit?"

They will always say yes. And now you control the session.

Variation for complex builds:
"I've looked at what you've described and I have some thoughts already — but some of my
recommendations depend on details I don't have yet. Can I ask you a few things first?"

This phrase does three things:
1. Signals you've already been thinking (credibility)
2. Positions questions as due diligence, not ignorance
3. Builds anticipation for your eventual recommendation

---

### Phase 3 — Diagnosis (12-15 min)

This is the core of the call. Work through phases, not a fixed list. Let the answers guide
which question comes next.

**3a — Current State**

Understand what exists today before discussing what needs to change.

| Question | Why it matters |
|---|---|
| "How are you handling this right now?" | Reveals actual pain and current cost |
| "Walk me through the current workflow step by step." | Surfaces hidden complexity |
| "How much time does this take your team weekly?" | Quantifies the cost — use this in SOW |
| "What tools are you using for this currently?" | Stack intelligence + migration risk |
| "How many people touch this process?" | Scope signal — more people = more risk |

**3b — Problem Depth**

Dig under the surface answer. The stated problem is rarely the real problem.

| Question | Why it matters |
|---|---|
| "What made you decide now was the time to fix this?" | Reveals urgency trigger and priority |
| "Have you tried to solve this before? What happened?" | Surfaces past failures — and what not to repeat |
| "When this breaks or slows down — what's the downstream effect on the business?" | Reframes cost from time to money/risk |
| "What would 'fixed' actually look like in your day-to-day?" | Forces them to define success concretely |
| "What's the single biggest pain point with how you do this today?" | Gets them to rank, so you know where to focus |

**"Tell me more about that."** — use this after every answer. Never accept the surface.
The real answer is usually one follow-up question deeper.

**3c — Stakes and Urgency**

This tells you if there's a real deadline and what's actually at risk.

| Question | Why it matters |
|---|---|
| "What breaks if this isn't solved by [their date]?" | Hard vs soft deadline |
| "Is there a specific launch or event driving the timeline?" | External forcing function |
| "What does this problem cost you right now — time, revenue, both?" | ROI baseline for your SOW |
| "Who else in the business is affected when this isn't working?" | Stakeholder map + JSS risk signal |

**3d — Technical Qualification** (for automation, pipeline, agent, integration)

| Question | Why it matters |
|---|---|
| "What's your expected volume at launch — and 6 months out?" | Scalability decisions change at 10x |
| "What other systems does this need to connect to?" | Hidden integration complexity |
| "Who on your team owns this after delivery?" | Maintenance reality — and scope of training |
| "Any data sensitivity or compliance requirements?" | GDPR, HIPAA, PII — changes architecture |
| "Have you documented the current process, or is it mostly in people's heads?" | Tribal knowledge = longer engagement |
| "What's your tolerance for downtime on this?" | SLA expectations — price accordingly |

**Challenging assumptions (this is what signals senior level):**

When their stated solution doesn't match their actual problem:

"Most people in your situation go for [what they asked for] — but from what you're describing,
the real bottleneck is [actual problem]. If we fix that instead, you'd get [better outcome]
without [the cost/risk of their approach]. Does that track?"

This will surprise them. It also earns trust. You just showed you understood their problem
better than they did.

---

### Phase 4 — Recommendation Frame (3-4 min)

Don't wait until the SOW to share your thinking. Give them a preview here.
This signals confidence and keeps them engaged.

**The structure:**
1. Paraphrase what you heard: "Let me make sure I have this right..."
2. Name the real problem (not the symptom): "The core issue isn't [X] — it's [Y]."
3. Signal the approach without full detail: "The way I'd approach this is [general direction]."
4. Name what most people get wrong: "Most implementations skip [X], which is why they break
   at [specific scale or time]."
5. Set up the SOW: "I'll put this into a Scope of Work so you can see exactly what's included,
   what's not, and how we'd stage it."

**Do not:**
- Give away the full solution on the call. The SOW closes. The call opens.
- Say "I can definitely do that!" (sounds junior and eager)
- Say "Whatever you need." (you have no position)
- Agree with everything they propose (yes-people don't run $15k projects)

---

### Phase 5 — Qualification (3-4 min)

You are evaluating them. This is not an interview. Ask directly.

| Question | Why it matters |
|---|---|
| "Who else is involved in the decision besides yourself?" | Single decision-maker vs committee |
| "Have you spoken to other freelancers about this?" | Where you sit in their process |
| "Is there a budget range you're working within?" | Qualify price range before SOW |
| "If the Scope of Work looks right — what does starting look like on your end?" | Uncovers blockers |
| "What's your timeline from decision to actual start?" | Urgency reality vs wishful timeline |

**On budget:** If they haven't mentioned it, ask. Frame it as helping you scope correctly:
"I want to make sure the SOW fits your range — do you have a rough budget in mind for this?"

If they give a number that's too low:
"Okay, that's helpful context. Depending on the scope, I may need to structure it differently —
there are a few ways to approach this, and I'll show you the options in the SOW."

Do not negotiate on the call. The SOW is where price is discussed.

---

### Phase 6 — Close to Next Step (1-2 min)

Do not leave without a concrete next step. Not "I'll think about it." Not "I'll send you
something." A specific action with a specific time.

**The close:**

"Based on everything you've told me — [1-sentence summary of the real problem] — I have a
clear picture of what this needs. Here's what I'd suggest:

I'll put together a Scope of Work by [tomorrow / Friday]. It'll show you exactly what's
included, what's not, the milestone structure, and the investment. You'll have everything
you need to make a decision from that.

Does that work?"

**They say yes:** "Good. You'll have it by [date]. I'll send it to [email/Upwork message]."

**They say "we need to talk to others first":**
"Of course. When will you have alignment? I'll time the SOW to land before that conversation."

**Do not:**
- Ask "Would you like to hire me?" (weak close)
- Say "Let me know if you want to move forward." (no next step)
- Mention the rate again unprompted (SOW handles it)
- Add "It was great talking to you!" (fine, but don't lead with it)

---

## The "Sounds Like It Handles Billion-Dollar Projects" Signals

These are behaviors, not phrases. They compound.

**1. You've done research and open with it.**
They've talked to 5 freelancers. You're the only one who mentioned something specific from
their website in the first 60 seconds. You're already different.

**2. You set an agenda instead of waiting for one.**
"Can I lead for a bit?" — small move, huge signal. You own the room.

**3. You listen more than you talk.**
Ramshaw: "Shut up and listen." The more they talk, the more they invest. You ask, they answer.
You follow up. You don't fill silence.

**4. You think out loud about scale.**
"At 10x your current volume, that approach would..."
"The thing that usually breaks at this stage is..."
Shows you've seen how things fail, not just how they work.

**5. You name what they didn't say.**
"The real cost here isn't the tool subscription. It's the 12 hours a week your ops team
spends on reconciliation that this replaces."
You calculated something they hadn't. That's what consultants do.

**6. You have an opinion.**
"I'd actually push back on that approach — here's why."
Junior freelancers agree with everything. Senior consultants have positions.

**7. You qualify them as much as they qualify you.**
"Before I recommend anything, I need to understand [X]."
You are evaluating whether this is a project worth taking. That's the frame.

**8. You control the close.**
You don't wait to be asked "so what happens next?" You tell them:
"Here's what I'd suggest as next steps." Full stop.

---

## Red Flags During the Call

If you hear these, adjust or walk away.

| Signal | Risk | Response |
|---|---|---|
| "We just need something quick" | Scope undefined — they want fast, not right | "Help me understand what 'quick' means for you — what's the actual deadline?" |
| "Budget is tight but there's more work after" | Speculation. Not money. | Note it. Don't factor future work into the price. |
| Multiple decision makers, no clear lead | Committee = slow or no close | "Who has final sign-off?" |
| Hired 3+ freelancers for the same problem | Scope issues or difficult client | "What happened with the previous freelancers?" |
| Can't answer what the current workflow is | They don't know their own process | SOW will be a moving target. Price for it. |
| "Can you start today?" | No planning = chaos | Slow down: "My next available start is [date]." |
| Pushing back on upfront before you mention it | Payment risk | "That's standard for all my projects — 40% before any work starts." If they resist: walk. |
| Vague when asked to define success | No acceptance criteria = JSS risk | Push: "If I delivered X by Y date — what would have to be true for you to say it's done?" |
| "We'll handle the testing" | They won't. You carry the JSS risk. | "Testing is part of what I deliver — it's how I make sure I can close the contract cleanly." |

---

## Post-Call Protocol

Do this immediately after the call (memory degrades fast).

1. Write down every number they mentioned: volume, team size, timeline, current cost, budget.
2. Write one sentence: what is the real problem (not the stated problem)?
3. Run `/quote` with the project type and complexity you've now confirmed.
4. Send the SOW within 24 hours — while you're fresh in their mind and they're still warm.
5. Create a client node: `upwork/clients/active/SLUG.md` if you intend to bid.

**SOW timing:** The average freelancer says "I'll send something over" and takes 3 days.
You send in 24 hours. That gap is where deals die. Prioritize it.

---

## Recording the Call

Use Fathom (free, works with Zoom and Google Meet). Records + transcribes automatically.
After the call: put transcript into Claude to extract:
- Key numbers mentioned
- Their exact words describing the problem (use these in the SOW — clients respond to
  seeing their own language reflected back)
- Any red flags that weren't obvious in the moment

---

## Wikilinks

[[elite-freelancer-model]] · [[handoff]] · [[upwork-psychology]] · [[pricing]] · [[proposal-anatomy]]
