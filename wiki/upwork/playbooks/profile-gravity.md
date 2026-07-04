---
sensitivity: private
entity_type: playbook
name: Profile Gravity — The Inbound Engine
last_updated: 2026-05-30
relationships:
  - target: "[[upwork-algorithm]]"
    type: implements
    strength: 10
    first_seen: "2026-05-30"
    last_reinforced: "2026-05-30"
  - target: "[[elite-freelancer-model]]"
    type: implements
    strength: 9
    first_seen: "2026-05-30"
    last_reinforced: "2026-05-30"
---

# Profile Gravity — The Inbound Engine

The OS is 90% outbound: qualify job → write proposal → send. That's correct for the first 90 days. But Ramshaw's actual income comes mostly from **invitations** — clients finding him and reaching out directly. Profile gravity is how you build the machine that runs while you sleep.

**The transition:** Outbound grinder → Invited expert. Not an overnight switch. A 90-day engineering project.

---

## What Is Profile Gravity

Profile gravity is when the algorithm consistently surfaces your profile to clients who are actively hiring in your niche — without you proposing first. It has two sources:

1. **Search gravity:** Clients searching for freelancers → your profile appears in their results
2. **Invite gravity:** Upwork proactively emails clients a shortlist of matching freelancers → you're on it

Both depend on the same underlying signals but operate differently. Search gravity is keyword-driven. Invite gravity is performance + behavioral signal driven.

---

## The Category Gravity Flywheel

```
Win contract in target category (n8n)
    ↓
Algorithm records success signal for that category
    ↓
Portfolio piece + keyword tags added
    ↓
Client review mentions keyword
    ↓
Contract title updated with keyword
    ↓
Profile keyword count increases
    ↓
Algorithm ranks your profile higher for that category
    ↓
More invites + better Best Match position on proposals
    ↓
More wins → repeat
```

**Threshold:** 3+ category wins → flywheel activates. Full effect visible at weeks 6-8.

**Critical rule:** All proposals go in ONE category for 90 days minimum. No scatter. Spreading across categories dilutes the gravity signal for every category.

---

## The 90-Day Profile Gravity Plan

### Days 1-30 — Foundation Layer

**Profile signals to engineer:**

- [ ] 100% profile completion (non-negotiable — required for Rising Talent + invite eligibility)
- [ ] Primary keyword (e.g., "n8n") appears 10+ times across all sections (Ctrl+F check on live profile)
- [ ] Title: `[Keyword] Specialist | [Specific outcome promise]`
  - NOT: "Automation Expert"
  - YES: "n8n Automation Engineer | End-to-end workflow builds that run 24/7"
- [ ] Overview: keyword in first line, keyword spam at the very bottom (separate block of keywords)
- [ ] All 20 skill tag slots filled — prioritize keyword variants: n8n, Workflow Automation, AI Automation, Make.com, Zapier (if relevant), API Integration, etc.
- [ ] Enable Available Now badge (2 connects/day — always on)
- [ ] Add 2 free Upwork certifications — use them for keyword placement, not credential value
- [ ] Upwork Membership active (shows proposal counts, gives connects)

**Invite system foundation:**
- [ ] Response time to ALL messages: under 2 hours (builds Responsiveness tag)
- [ ] If any invitations arrive: reply within 1 hour, every time, no exceptions
- [ ] Login daily — consistent signal, not bursts

**Measurables at Day 30:**
- Profile views/week (baseline)
- Invitations received/week (baseline)
- Proposal View Rate % (baseline via Upwork analytics)

---

### Days 31-60 — Category Signal Building

**This phase is about feeding the algorithm consistent signals in ONE category.**

- [ ] All proposals → n8n Automation category only (or chosen primary keyword category)
- [ ] Proposal cadence: 3-5 quality proposals/day, not more
- [ ] Every won contract: ask client to rename contract title with primary keyword
- [ ] After every completed contract: add portfolio piece tagged with keyword
  - Title: keyword-first ("n8n Lead Qualification Workflow — SaaS Client")
  - Description: 2-3 paragraphs, keyword appears naturally 2-3x
  - Skills: n8n + automation + relevant stack tags (5 tags per piece)
- [ ] Start LinkedIn testimonials process (anyone with a LinkedIn account)
  - Target: 5 testimonials
  - Process: name + email + LinkedIn URL → Upwork profile settings → Upwork emails them
  - Follow up if not appeared after 8 days: open Upwork support ticket

**Profile deepening:**
- [ ] 8+ portfolio pieces minimum (12 preferred)
- [ ] Each piece: multiple images, not just one
- [ ] No two pieces from the same industry (algorithm sees category diversity as signal of real experience)
- [ ] Tie portfolio pieces to testimonials where possible (Bob the hairdresser → Bob's portfolio piece)

**Invite optimization active:**
- [ ] Check invite frequency weekly (measure vs. baseline from days 1-30)
- [ ] If invite arrives: respond within 1 hour with a short, specific reply — never ignore
- [ ] If declining an invite: send a message explaining why ("project scope isn't the right fit but I appreciate the invite")
- [ ] Track: invite acceptance rate (accept ≥70% of relevant invites — the algorithm is watching)

**Measurables at Day 60:**
- Profile views/week (compare to Day 30 baseline)
- Invitations received/week (should be rising)
- Proposal View Rate % (should be >30%)
- Keyword Ctrl+F count on live profile (should be 10+)

---

### Days 61-90 — Gravity Compounding

By day 60-70 you should see the first signs of flywheel activation: invitations starting to arrive unprompted, PVR climbing, profile appearing in searches.

**Acceleration moves:**

- [ ] Upwork Mirror check (uprankmir.com): which keywords are you now ranking for? What position?
- [ ] Profile video (Loom): record AFTER portfolio is fully built (show the work, not just a talking head)
  - Walk through 2-3 portfolio pieces on screen
  - Under 3 minutes
  - Goal: personable + competent + can do the job
- [ ] Rate escalation: if first 5-star review is in — raise rate $5-10/hr
- [ ] Specialization profile: consider creating a separate Upwork specialization profile focused purely on n8n (algorithm treats these as independent ranking entities)
- [ ] Run A/B experiments from the protocol (see upwork-algorithm.md → Reverse Engineering Protocol)

**The compounding signal stack at day 90:**
```
100% profile completion
+ Available Now badge always on
+ 10+ keyword appearances across all profile sections  
+ 12 portfolio pieces (keyword-tagged, multi-image, multi-paragraph)
+ 5+ LinkedIn testimonials
+ 2 free certifications (keyword placed)
+ 3+ category wins (flywheel threshold crossed)
+ Fast response time (Responsiveness tag active)
+ Single category proposal history (gravity signal)
+ Contract titles contain keyword
```

This is the profile that gets invited to 80% of its work instead of grinding proposals for 80%.

---

## The Daily Habit Stack (5-10 min/day)

These behaviors send compound signals to the algorithm every day:

```
Morning:
  ✓ Login (daily activity signal)
  ✓ Check invitations → reply within 1 hour if any
  ✓ Check messages → reply within 2 hours if any
  ✓ Set Available Now badge ON (check it's still active)

Proposal session (when running):
  ✓ 3-5 proposals, same category only
  ✓ Each one: job-specific language (no copy-paste)
  ✓ First 15-60 minute window jobs = priority

Weekly (10 min):
  ✓ Check Upwork analytics: profile views, proposal view rate, invitations
  ✓ Log metrics to performance/metrics.md
  ✓ If any win: add portfolio piece, ask client to rename contract title
```

---

## Invitation Response Playbook

When an invite arrives — the algorithm is watching whether you reply, how fast, and whether you accept.

**Relevant invite (you want this project):**
```
Hey [name],

Thanks for the invite. I looked at what you're building — [one specific observation
about their project from the job post]. I've done similar work for [brief proof point].

Quick question before I put together a full response: [one low-friction question
about scope/timeline/stack].

Looking forward to hearing more.

Emmanuel
```

**Irrelevant invite (can't take it, but must reply):**
```
Hey [name],

Thanks for thinking of me. The [specific thing] in this project falls outside
my current focus — I'm head-down in [your niche] right now and want to give
clients my full attention.

Appreciate the invite regardless.

Emmanuel
```

**Never:** ignore an invite. Never: just click decline without a message. Both tank invite frequency.

---

## Measuring Profile Gravity Progress

Track in `upwork/performance/metrics.md` weekly:

| Metric | Week 1 | Week 4 | Week 8 | Week 12 |
|---|---|---|---|---|
| Profile views/week | — | — | — | — |
| Invitations received/week | — | — | — | — |
| Proposal view rate (PVR) | — | — | — | — |
| Proposal-to-interview rate | — | — | — | — |
| Keyword count (Ctrl+F n8n) | — | — | — | — |
| Portfolio pieces live | — | — | — | — |
| LinkedIn testimonials live | — | — | — | — |
| Upwork Mirror keyword rank | — | — | — | — |

**Gravity is working when:**
- Invitations/week is rising
- PVR is 35%+
- You're receiving invites from clients who found you — you didn't propose to them

**Gravity is NOT working when:**
- PVR stuck below 30% after 6 weeks
- Zero invitations after 4+ weeks of activity
- Profile views flat or declining

If stuck: don't change proposal strategy. Fix the profile (keyword count, category scatter, PVR suppression). The proposal is not the problem.

---

## Wikilinks

[[upwork-algorithm]] · [[jss-mechanics]] · [[elite-freelancer-model]] · [[profile]] · [[proposal-framework]]
