---
sensitivity: public
entity_type: concept
name: Job Scoring Methodology
aliases: ["job-score", "bid-gate", "upwork-scoring"]
last_updated: 2026-05-27
relationships:
  - target: "[[elite-freelancer-model]]"
    type: part_of
    strength: 9
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
  - target: "[[client-quality-score]]"
    type: reinforces
    strength: 8
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
---

# Job Scoring Methodology

The scoring system used by `scripts/qualify.py` to evaluate every Upwork job before a bid decision. This is the bid gate. Composite score < 65 = automatic skip, no exceptions.

---

## The Five Scores

### 1. Job Quality Score (0–100)

Does this job have a real, scoped, winnable problem?

**What raises the score:**
- Clear deliverable defined (not "various tasks")
- Realistic budget for the scope described
- Specific tech stack named
- Timeline is reasonable (not "need ASAP, takes 2 weeks")
- Job description shows client understands the domain
- Milestones or phases mentioned

**What lowers the score:**
- Scope is vague ("and other duties as needed", "ongoing tasks")
- Budget is mismatched to complexity (React SaaS app for $200)
- No timeline or unrealistic timeline
- All caps job titles or descriptions
- "Simple", "easy", "quick" to describe complex tasks
- Job posted > 7 days ago with many proposals

**Calculation:** Start at 50. +/-5 per signal. Clamp 0–100.

---

### 2. Client Quality Score (0–100)

Is this a client worth working with?

Full methodology in `concepts/client-quality-score.md`. Short version:

**Key signals:**
- Total Upwork spend (verified payment is baseline)
- Hire rate (< 20% = window shopper)
- Average hourly rate paid to previous freelancers
- Review score (< 4.5 = concern)
- Number of open contracts (too many = distracted client)
- Job post history (repeated posting of same job = warning)

**Hard disqualifiers:**
- Payment not verified
- Zero Upwork spend
- 0% hire rate

---

### 3. Fit Score (0–100)

Does this match Emmanuel's positioning and stack?

**What raises the score:**
- Tech stack is n8n, Claude API, automation, full-stack JS/TS/Python
- Industry match (medical practices, SaaS, agencies — current niches)
- Problem type matches proven delivery (AI workflows, dashboards, integrations)
- Budget signals premium positioning ($50+/hr or $2k+ fixed)

**What lowers the score:**
- Stack is outside core skills (mobile apps, hardware, DevOps-heavy)
- Commodity positioning ("need a WordPress developer")
- Budget signals price-shopping
- Requires non-remote or location-restricted work

---

### 4. Urgency Score (0–10)

How pressing is their need? Higher urgency = more likely to hire fast.

**High urgency signals (8–10):**
- "Previous freelancer left mid-project"
- Specific deadline mentioned
- Business operations depending on this
- "ASAP" with realistic budget

**Low urgency signals (1–3):**
- "No rush", "whenever you get to it"
- Exploratory / "thinking about building"
- No timeline mentioned at all

Note: High urgency can compensate for moderate job quality but not for bad client quality.

---

### 5. Competition Score (0–10)

How crowded is this job? Lower competition = better. Counterintuitive scoring: **higher score = lower competition.**

**High competition signal (1–3):** > 30 proposals, posted < 24h ago, broad/generic job
**Medium competition (4–6):** 10–30 proposals, niche job
**Low competition (7–10):** < 10 proposals, specialized job, client has good history

---

## Composite Score Calculation

```
composite_score = (
    job_quality   * 0.30 +
    client_quality * 0.30 +
    fit_score      * 0.25 +
    urgency        * 0.08 * 10 +   # normalize to 0-100
    competition    * 0.07 * 10     # normalize to 0-100
)
```

**Thresholds:**
- < 65: Skip. Always.
- 65–79: Bid if strong niche alignment. Default: watchlist.
- 80–89: Priority bid.
- 90+: Rare. Drop everything, write the best proposal possible.

---

## Red Flag Overrides

These trigger an automatic skip regardless of composite score:

- `payment_not_verified: true`
- `hire_rate < 10%` AND `total_spend == 0`
- Job description contains: "trial task", "test first for free", "pay per task"
- Budget: "< $5/hr" or "< $100 fixed" for complex scope
- Client reviews average < 3.5
- Job asks for: "full-time exclusive" without long-term contract
- Any mention of: "I need someone to do everything"

---

## Calibration Notes

Calibration is ongoing. When Emmanuel's gut score disagrees significantly with the machine score, log the disagreement:
- `scripts/qualify.py --calibrate [job-slug] [emmanuel-score]`
- This updates the weighting formula over time

The goal: after 20 calibrations, machine scores track within ±10 of gut scores.

---

## Wikilinks

[[client-quality-score]] · [[elite-freelancer-model]] · [[upwork-psychology]] · [[financial-fragility]]
