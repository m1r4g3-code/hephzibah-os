---
sensitivity: private
entity_type: job
name: "Build Automated X/Twitter Posting Tool"
url: "https://www.upwork.com/jobs/~022087315536078203823"
posted: "2026-08-12"
evaluated: "2026-08-12"
scores:
  job_quality: 88
  client_quality: 95
  fit_score: 72
  urgency: 9
  competition: 4
composite_score: 81
decision: "bid"
decision_rationale: "Premium client ($442K, 5.0 stars) building a real production pipeline for a media company. Ongoing hourly = long-term relationship potential. Loom chosen over text because Nick is a content creator who consumes video daily and 50+ text proposals have already landed."
bid_amount: "$35/hr"
budget_posted: "$20-40/hr hourly, ongoing"
client_spend: "$442,000"
client_hire_rate: "78%"
client_country: "United States"
client_username: "unknown"
client_avg_review: 4.99
red_flags: []
green_flags:
  - "$442K Upwork spend"
  - "4.99 stars / 28 reviews"
  - "Clear detailed job post"
  - "Ongoing project — retainer potential"
  - "Data already exists — ingestion is the first milestone not a blocker"
  - "8-10 posts/day target = real production scale"
jss_risk: "low"
status: "proposal-sent"
proposal_file: ""
connects_spent: 19
forced_bid: false
---

# Build Automated X/Twitter Posting Tool — Nick Gerli / Reventure

**URL:** https://www.upwork.com/jobs/~022087315536078203823
**Client:** Nick Gerli (CEO, Reventure App) | USA (St. Petersburg FL) | $442K total | 78% hire rate | 4.99 stars
**Budget:** $20-40/hr | Hourly | Ongoing | 1-3 months duration
**Posted:** 2026-08-12 | 50+ proposals competing
**Proposal sent:** 2026-08-12 | Follow-up due: 2026-08-15

---

## Job Description Summary

Nick runs the Reventure housing market media brand: 100K+ X followers, 600K YouTube subscribers, 1M+ user real estate app, CNBC/Bloomberg appearances. He posts housing data daily — posts focused on surprising, counter-narrative findings get 100K-1M+ views. He wants an automated system that scans US housing data, finds the surprising anomalies, generates Reventure-branded charts, writes copy in his voice, and posts to X automatically 8-10 times per day.

---

## Real Problem (Diagnosis)

Nick's media business scales on content volume but he and his small team are bottlenecked by manual data research and post production every day. Every hour spent finding and formatting data is an hour not spent on higher-value work (YouTube, app, media appearances). He needs a production pipeline he can trust to maintain his brand standard autonomously. The risk isn't building the system — it's building one that embarrasses him publicly if it posts something wrong.

---

## Score Breakdown

| Factor | Score | Rationale |
|---|---|---|
| Job quality | 88 | Clear scope, real business, ongoing engagement, good budget range |
| Client quality | 95 | $442K spend, 4.99 stars, clear communicator, premium operator |
| Fit score | 72 | Python automation fits, chart generation is a stretch, chart styling will require iteration |
| Urgency | 9 | Posted <24h ago when evaluated, 50+ proposals = competitive |
| Competition | 4 | High competition (50+) but Loom creates pattern interruption |
| **Composite** | **81** | |

---

## Red Flags

None disqualifying. Note: Nick ended a contractor for being 6 minutes late to kickoff — he is precise and unforgiving of unprofessionalism.

## Green Flags

- $442K Upwork spend = serious, not testing
- 4.99 stars across 28 reviews = treats contractors well when they deliver
- Scope is clear and well-defined (unusual at this level)
- Data already exists = ingestion layer is a connection problem, not a data sourcing problem
- Ongoing = if Phase 1 impresses, Phase 2, 3, 4 follow naturally
- 8-10 posts/day = production scale = long-term contract

---

## Decision: BID

**Rationale:** Score 81. Premium client with clear scope. Ongoing project with real retainer potential. Nick is a media company founder who understands systems — he will appreciate the architectural thinking in the proposal. Loom with Excalidraw architecture diagram is the right format here: he's a content creator, video cuts through 50+ text proposals.

**Positioning angle:** You're not building a Twitter bot. You're building the production engine for his media brand. Every post goes out with his name on it — quality gates, voice matching, confidence thresholds, and the dry-run week are what separate this from a generic scraper + poster.

---

## Proposal Notes

**Loom sent:** YouTube unlisted (Loom free plan blocked upload)
**Cover letter text:**
"Hey Nick, Mapped out the full system before sending this 90-second breakdown: [YouTube link]
P.S. St. Pete's inventory data has been moving fast. Good market to stress-test the detection engine on first."

**5 questions answered:**
1. SERAMAN 7-node pipeline as architectural proof
2. Rolling Z-score + YoY seasonality + surprise-vs-national ranking + geographic cooldown + top 10 + performance feedback loop
3. X API v2, Tweepy, media upload, OAuth, rate limits, analytics retrieval
4. Matplotlib ax.annotate() + ax.text() + Ellipse patches + Pillow 1200x675 composition
5. Full stack: Python/pandas → Matplotlib/Pillow → Claude API few-shot → Tweepy v2 → PostgreSQL → APScheduler → Railway + promotional rotation flag

**Rate submitted:** $35/hr | Rate increase: Never

---

## Phase 1 Architecture (for call prep)

```
Morning run (APScheduler)
  ↓ Read Reventure housing database
  ↓ Z-score anomaly detection (scipy) across all markets
  ↓ Compare each to national trend (surprise vs national)
  ↓ Geographic cooldown filter (no repeat metro for 3 days)
  ↓ Rank top 3 for today
  For each:
    → Matplotlib + Pillow → chart image (1200x675, Reventure brand)
    → Claude API few-shot → caption in Nick's voice
    → APScheduler → queued at optimal time
    → Tweepy v2 → post to X with image
    → PostgreSQL → log market, metric, hook, timestamp
  48h later → fetch engagement → update performance model
```

## Milestones

| Milestone | Day | Deliverable | Payment |
|---|---|---|---|
| 1. Data Intelligence | Day 7 | DB connected, Z-score live, top anomalies outputting | 40% |
| 2. Content Generation | Day 16 | Charts + Claude copy working, 3 demo posts | 30% |
| 3. Publishing + Dry Run | Day 23 | Tweepy live, 5-day dry run, Nick reviews before autonomous | 20% |
| 4. Live Autonomous | Day 30 | Posting live, performance tracking, error alerts | 10% |

## Single Biggest Unknown to Name on Call

"Your data structure is the piece I can't evaluate from outside. If the database is clean and documented, Milestone 1 is 5 days. If it needs normalization, it's 10. I want to find that wall in week one, not at day 20."

---

## Kill Shot for Any Call

"I was reading your thread on home sales hitting the 5th lowest July in 30 years. The Z-score detection I'm building would have surfaced that signal automatically — specifically the deviation against the 90-day baseline and the comparison to pre-pandemic norms. That's the divergence the system is built to find first, before anyone else posts it."

---

## Output Files

- Full intel brief: `outputs/intel/2026-08-13-nick-gerli-full-brief.md`
- Client node: `upwork/clients/active/nick-gerli-reventure.md`
