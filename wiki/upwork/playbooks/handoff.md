---
sensitivity: private
entity_type: concept
name: Handoff Playbook
aliases: ["delivery-brief", "project-handoff", "contract-close", "delivery-system"]
last_updated: 2026-05-28
relationships:
  - target: "[[identity]]"
    type: part_of
    strength: 9
    first_seen: "2026-05-28"
    last_reinforced: "2026-05-28"
  - target: "[[elite-freelancer-model]]"
    type: reinforces
    strength: 9
    first_seen: "2026-05-28"
    last_reinforced: "2026-05-28"
  - target: "[[upwork-psychology]]"
    type: reinforces
    strength: 8
    first_seen: "2026-05-28"
    last_reinforced: "2026-05-28"
---

# Handoff Playbook

JSS is not won at delivery. It's won at the handoff. Ramshaw's private NPS insight: Upwork sends
every client a private satisfaction survey after contract close. You never see the score. Score 7
= "Passive" — suppresses your profile ranking even if their public review is 5 stars.

A client who got exactly what they asked for but felt uncertain, confused, or unguided at the end
gives a 7. The delivery brief, the unexpected extra, and the clean close sequence convert 7s to 9s.

---

## Pre-Handoff Checklist (Run Before Sending Anything)

□ Every deliverable in the SOW is complete and tested from the client's perspective
□ Documentation is written — not "I'll explain it in the message"
□ The unexpected extra is ready (the small addition not in scope — 10 min max, stays forever)
□ Client temperature check: if communication has been cold or sparse, one check-in call before delivery
□ Nothing obvious will break in the next 7 days — fix it now, not after handoff
□ Contract is set up for CLIENT closure, not freelancer closure

---

## The Delivery Brief

Generate with `python scripts/handoff.py`. Send alongside the final deliverable.

The goal: client reads it and thinks "I know exactly what I got and what to do." Not impressed
by the detail — reassured by the clarity.

**Structure:**

```
WHAT WAS BUILT
Plain English. One numbered item per deliverable. No jargon. The client should
be able to explain what they received to their own team without you in the room.

HOW TO USE IT
The 3-5 things they need to know to operate this. Not a full manual —
the critical path. What to do, what to watch, what to expect.

IF SOMETHING BREAKS
One clear instruction. Usually: "Message me first with [these specifics]."
Or: "Check [specific log]. The most common issue is [X] — fix is [Y]."

WHAT I ADDED (NOT IN SCOPE)
The unexpected extra. One thing. Named clearly.
"I also added [X] — wasn't in the brief but prevents [specific problem you'd have hit]."
This is the moment that earns 9s and 10s, not the delivery itself.

MAINTENANCE NOTES
Anything time-sensitive they need to know: API key rotation schedule, rate limits,
monthly cost checks, what to do when the tool updates.
```

**Tone:** Same as proposals. Direct, specific. Not "Please do not hesitate to reach out."
Just: "If something breaks, message me with [details] and I'll have it fixed same day."

---

## The Contract Close Message

Send in Upwork chat after client confirms the delivery is working.

```
Hey [name],

Everything's wrapped up on my end. [Project name] is live and ready.

Could you close the contract when you get a chance?

Emmanuel
```

**Why this exact wording:**
- One action: close the contract. Nothing else to do.
- "When you get a chance" removes pressure — pressure = negative feeling before the survey
- No "Please leave me a 5-star review" — Upwork flags this, and it reads as desperate
- No "It was a pleasure working with you" — save warmth for after they close, not before

**Never close the contract yourself.** Freelancer-initiated contract endings register as JSS
negatives regardless of the reason. Always let the client close.

---

## If the Client Goes Silent After Delivery

They received it, aren't responding, contract still open:

**Day 5:**
```
Hey [name], just checking in — did you get a chance to look at [deliverable]?
Let me know if anything needs adjusting. Happy to wrap this up once you confirm it's working.
```

**Day 10:**
```
Hey [name], everything's still ready on my end whenever you are.
Happy to do a quick walkthrough if that would help before we close.
```

**Day 21:** Stop. Do not chase further. Upwork auto-closes dormant contracts eventually.
A client who completely disappears after delivery is unlikely to cause a JSS issue.

---

## Review Engineering

The private NPS survey asks: how satisfied were you, would you recommend this freelancer,
was the work as described?

**What generates 9s and 10s:**
- Got what was promised (baseline — minimum to avoid a 6)
- Got something they didn't expect (the unexpected extra — converts 7s to 9s)
- Transition from done → closed felt smooth and professional (the close sequence)
- Understood exactly what they received (the delivery brief)

**What generates 7s (the invisible JSS killer):**
- Work was fine but they felt like they had to manage Emmanuel
- Communication dropped off near the end
- They weren't sure if it was really done or just quiet
- They had to ask questions to understand what was delivered
- They felt like one of many clients, not the focus

**The unexpected extra is the highest-ROI action in the entire OS.** It costs 10 minutes.
It signals: "I thought about your problem beyond the brief." Clients remember this. The survey
score reflects it.

---

## Wikilinks

[[elite-freelancer-model]] · [[identity]] · [[client-quality-score]] · [[upwork-psychology]]
