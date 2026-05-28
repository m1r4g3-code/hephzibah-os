---
sensitivity: public
entity_type: concept
name: Client Quality Score
aliases: ["client-score", "client-evaluation"]
last_updated: 2026-05-27
relationships:
  - target: "[[job-scoring]]"
    type: reinforces
    strength: 8
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
  - target: "[[upwork-psychology]]"
    type: part_of
    strength: 7
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
  - target: "[[middleman-lesson]]"
    type: reinforces
    strength: 8
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
---

# Client Quality Score

How to evaluate a client's Upwork history before deciding to bid. A great job with a bad client is worse than no job at all — bad clients destroy JSS, drain time, and create financial risk.

---

## Scoring Formula

Start at 50. Apply adjustments. Clamp 0–100.

### Payment Verification
- Verified payment: +15
- Not verified: -40 (this is a near-disqualifier)

### Total Upwork Spend
- $10,000+: +15
- $1,000–$9,999: +8
- $100–$999: +2
- $0–$99: -10
- $0 (no history): -20

### Hire Rate
- 60%+: +10
- 30–59%: +5
- 10–29%: 0
- < 10%: -15
- 0%: -25 (window shopper — automatic concern)

### Average Hourly Rate Paid
- $50+/hr: +10
- $25–49/hr: +5
- $10–24/hr: 0
- < $10/hr: -15

### Review Score (as client, received from freelancers)
- 4.8–5.0: +10
- 4.5–4.7: +5
- 4.0–4.4: -5
- < 4.0: -20
- No reviews yet: 0 (neutral — new client)

### Number of Active Contracts
- 0–2: +5
- 3–5: 0
- 6–10: -5
- 10+: -15 (distracted client, unlikely to be responsive)

### Same Job Posted Multiple Times
- First time posting this job: 0
- Second time: -10
- Third time or more: -25 (serious red flag — something is wrong with their hiring process)

---

## Hard Disqualifiers (Skip Regardless of Total Score)

- Payment not verified AND zero spend
- Hire rate = 0% with 10+ posted jobs
- Average review score < 3.5
- Reviews from multiple freelancers mentioning: "scope creep", "didn't pay", "changed requirements", "ignored messages"
- Job description explicitly requests: "trial task", "test first", "unpaid test"

---

## Green Flags

These don't add points but provide context worth noting:

- Client has hired from the same niche before (shows domain understanding)
- Client left detailed, positive reviews for previous freelancers
- Client's hire history shows long-term relationships (not just one-off gigs)
- Client's Upwork member since date is recent (new client, could be great or terrible — needs other signals)
- Location matches Emmanuel's target market (US, UK, EU)

---

## Red Flag Taxonomy

Named patterns that trigger concern:

**The Window Shopper:** 10+ posted jobs, 0–5% hire rate. Posts jobs to "see what's out there." Very rarely hires. Wastes connects. Skip.

**The Micromanager:** Signs in description — "must be available immediately", "daily video calls required", "I need to approve everything before you proceed." High time cost, low outcome quality. Skip unless score is very high.

**The Scope Creeper:** Signs — vague initial scope, "and other related tasks", long list of requirements that don't quite fit together, previous freelancer history shows short contracts (kept cycling through people). Get everything in writing. Charge for changes. Consider skipping.

**The Disappearing Client:** Signs — irregular hire pattern (hires 3 people, then nothing for 6 months, then 2 more), multiple incomplete contracts in history. High risk of going silent mid-project.

**The Bitter Client:** Reviews they've received from freelancers mention poor communication, scope changes, unfair reviews. This client disputes. Skip entirely.

**The Naive Poster:** First-time Upwork client, no history, detailed but technically confused job description. Could be excellent — they just don't know the platform. Score as neutral. Evaluate based on budget and description quality.

---

## Wikilinks

[[job-scoring]] · [[upwork-psychology]] · [[middleman-lesson]] · [[elite-freelancer-model]]
