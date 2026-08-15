---
sensitivity: private
aliases: [upwork-algorithm, uma-shortlisting, algorithm-exploit]
entity_type: concept
last_updated: 2026-08-14
name: Upwork Algorithm Reverse Engineering
relationships:
- first_seen: '2026-08-14'
  last_reinforced: '2026-08-14'
  strength: 1
  target: '[[proposal-framework]]'
  type: informs
- first_seen: '2026-08-14'
  last_reinforced: '2026-08-14'
  strength: 1
  target: '[[upwork-psychology]]'
  type: extends
type: concept
---

## What This Is

Full reverse engineering of Upwork's three-layer algorithm system. Researched 2026-08-14 from cross-referenced algorithm guides, Uma AI documentation, JSS formula analysis, and behavioral signal tracking across millions of job posts.

Full research file: `outputs/intel/2026-08-14-upwork-algorithm-deep-research.md`

---

## The Three Separate Systems

| System | When It Fires | What It Controls |
|---|---|---|
| Talent Search | Client searches profiles | Whether profile appears at all |
| Best Match / Proposal Ranking | After proposal submitted | Order client sees proposals |
| Uma Shortlisting | Moment job is posted | Who gets invited before everyone else sees it |

---

## System 1 — Talent Search Weights

- Keyword match (title + first 160 chars + skill tags): **40%**
- Performance metrics (JSS, completion, reviews): **30%**
- Availability alignment (badge, response rate, recency): **20%**
- Behavioral signals (clicks, message checks, profile edits): **10%**

**Critical:** Upwork only reads the first 160 characters of the overview for search ranking. Keywords must be in the first two sentences or the profile is invisible.

**Critical:** Skill tags are exact-match strings, not semantic. "workflow automation" does NOT match "n8n."

---

## System 2 — Proposal Ranking Suppression Triggers

- Proposal-to-interview ratio below 10% = visibility suppression
- Same opening sentence across 5+ proposals in 7 days = ranking suppression
- JSS below 90% = active Best Match suppression
- Boosting weak match = bounce signal that lowers organic rank after boost ends
- Best Match requires 40% skill-tag overlap minimum

---

## System 3 — Uma Shortlisting (Zero-Connect Invitations)

All five must be true simultaneously to get shortlisted:
1. Profile title contains exact search term client used
2. First 160 chars contain the keyword
3. At least 8/20 skill tags match job post skills
4. Last login within 7 days
5. Availability set to "available"

Uma shortlisting = invitation sent before most freelancers see the job. Zero connects spent.

---

## JSS Formula

(Positive outcomes - Negative outcomes) / Total scorable outcomes

**Positive:** Contract with private NPS 9-10. Retainer adds positive outcome every 90 days.

**Negative (invisible):** Private NPS 7-8 (even with public 5-star), paused contracts, freelancer-ended contracts.

**Weighting:** $5k contract carries more weight than $50 contract. 90-day recency weighted heavily.

---

## Private NPS — The Invisible Hand

- 9-10 = JSS positive + ranking boost
- 7-8 = JSS NEGATIVE + suppression (invisible to freelancer, even with public 5-star)
- 0-6 = Immediate JSS hit

Engineer every contract close for 9-10 before the survey fires.

---

## 10 Exploits (New Account)

1. First 160 chars: keyword + credibility signal
2. Skill tags: exact match to AI automation job posts
3. Daily micro-signals: mobile login + job clicks + message check
4. Profile edit every 10-14 days: triggers ranking boost
5. $15 consultation: first JSS data point in category
6. Never bid below composite 80: protects proposal-to-interview ratio
7. Contract title keyword: ask client to rename with "AI automation"
8. Title pipe structure: "AI Automation | n8n | Workflow Systems"
9. Respond to invitations within 15 minutes: Availability Multiplier
10. $35/hr rate: Uma diversity algorithm places at different price point

---

## Observable Algorithm Traces

| Signal | Meaning |
|---|---|
| Proposal View Rate below 30% | Profile-level suppression. Fix keywords. |
| Zero invitations/week | Uma not shortlisting. Fix title, 160 chars, tags. |
| High view, low reply | Proposal quality issue. Profile works, proposal fails. |
| JSS stuck below 90% | Private NPS averaging 7-8. Fix contract close process. |

## See Also

[[proposal-framework]] · [[upwork-psychology]] · [[proposal-ab-data]]
