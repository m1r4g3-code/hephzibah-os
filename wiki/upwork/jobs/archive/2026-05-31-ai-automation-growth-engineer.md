---
sensitivity: private
entity_type: job
name: "AI Automation & Growth Systems Engineer"
url: "https://www.upwork.com/jobs/~022061184978349348035"
posted: "2026-05-31"
evaluated: "2026-05-31"
scores:
  job_quality: 72
  client_quality: 90
  fit_score: 72
  urgency: 9
  competition: 4
composite_score: 78
decision: "bid"
decision_rationale: "Composite 78, strong niche fit. n8n explicitly listed as bonus skill — this is Emmanuel's primary tool. Best client quality seen in weeks. Duration rule mitigated by client's own 'project-based/fractional start' language. Screening question filters generic bidders and favors technical depth."
bid_amount: "$35/hr (floor: $30)"
budget_posted: "$15–$50/hr hourly"
client_spend: "$47,000"
client_hire_rate: "73%"
client_country: "United States (New York)"
client_username: "unknown"
client_avg_review: 5.0
red_flags:
  - "Duration 6+ months / 30+ hrs/week — conflicts with short-contract rule (partner account). Mitigated: client explicitly offers project-based/fractional entry."
  - "Mandatory skills listed as Electrical Engineering / Embedded Systems — client form error. Actual requirements are Python/AI/APIs."
  - "$31.54/hr average paid — may anchor lower than job deserves"
green_flags:
  - "n8n named explicitly as bonus skill"
  - "$47K spent, 5.0 stars / 36 reviews, zero bad reviews"
  - "Specific deliverable examples match Emmanuel's portfolio exactly"
  - "Fresh post (28 min old at eval time) — first-mover window"
  - "Project-based/fractional start explicitly offered by client"
  - "Technical screening question filters generic applicants"
jss_risk: "low"
status: "evaluated"
proposal_file: ""
connects_spent: 0
forced_bid: false
---

# AI Automation & Growth Systems Engineer

**URL:** https://www.upwork.com/jobs/~022061184978349348035
**Client:** United States (New York) | $47K total | 73% hire rate | 5.0★ (36 reviews) | Mid-sized company (10-99)
**Budget:** $15–$50/hr | Hourly | 30+ hrs/week | 6+ months
**Posted:** 2026-05-31 | 20-50 proposals competing (at time of evaluation)

---

## Job Description (Summary)

Performance marketing agency (NYC) building internal AI-powered operational tools for their paid media team. Looking for a technical automation/systems engineer who can connect Meta Ads API, Google Ads API, Shopify, Slack, and AI models (OpenAI/Claude/Gemini) into automated internal dashboards, diagnostic systems, and reporting workflows. Not a chatbot role — they want real systems engineering.

---

## Real Problem (Diagnosis)

Agency is scaling paid media operations but their team is drowning in manual reporting, account monitoring, and performance analysis. They need a technical person who can build the infrastructure layer under their media buying team — AI systems that surface insights automatically rather than requiring an analyst to pull data every day. The Slack analyst example reveals the core need: decision-relevant information delivered without human effort.

---

## Screening Question (Required Answer)

Client asks: *"A short explanation of how you would approach building: an AI-powered Slack analyst that reviews Meta ad account performance daily and recommends actions."*

**Answer to use:**

n8n handles the daily trigger + Meta Ads API pull. The data gets structured (campaigns, ad sets, yesterday's spend vs benchmark, ROAS, CPC shifts) and fed to Claude or GPT-4o with a prompt built around their KPIs. Claude produces a structured digest: what's fatiguing, what's scaling, what to pause, what to test. n8n posts it to a Slack channel in a clean format — no spreadsheet, no dashboard login, just the daily decision brief. First build: 3-4 days. Connects to existing Meta account structure. No ongoing developer required.

---

## Score Breakdown

| Factor | Score | Rationale |
|---|---|---|
| Job quality | 72 | Crystal-clear scope, specific examples, serious technical operator |
| Client quality | 90 | $47K spent, 5.0/36 reviews, 73% hire rate, NYC agency with real budget |
| Fit score | 72 | n8n as bonus (Emmanuel's primary tool), Python + LLM core. Gap: no Ads API portfolio piece |
| Urgency | 9 | Posted 28 min ago at eval — first-mover window active |
| Competition | 4 | 20-50 proposals but technical screening filters most out |
| **Composite** | **78** | |

---

## Red Flags

- Duration 6+ months, 30+ hrs/week — conflicts with short-contract rule for current partner account (handback ~June 2026). Mitigated by client's explicit "project-based/fractional start" language.
- Client form skills error: "Mandatory skills" lists Electrical Engineering / Embedded Systems — clearly wrong, almost certainly a client form mistake. Actual job needs Python/AI/APIs.
- $31.54/hr avg hourly paid — tracks lower than this job deserves, though they've paid $47-$115/hr for the right specialists.

## Green Flags

- n8n explicitly listed as a bonus skill — Emmanuel's primary tool mentioned by name
- $47K spent, 5.0 stars across 36 reviews — exceptional client quality
- Specific deliverable examples (Slack analyst, creative fatigue detection, scaling recommendations) match Emmanuel's portfolio exactly
- Job was 28 minutes old at evaluation — first-mover advantage available
- Client explicitly says "begin as project-based/fractional" — short engagement entry point
- Technical screening question eliminates all generic AI agency applicants

---

## Decision: BID

**Rationale:** Composite 78, strong niche fit. n8n called out by name in a $47K client's job post — that alignment is rare. The duration rule is real but mitigated by the client's own project-based entry language. Screening question favors Emmanuel because it requires actual technical architecture knowledge, not generic promises. Submit fast — job is in the 2-hour high-ROI window.

**Positioning angle:** Answer the Slack analyst screening question directly and concisely in the proposal. Show the 4-step architecture. n8n → Ads API pull → Claude analysis → Slack digest. Nobody else submitting will show the actual build path. That is the differentiator.

---

## Proposal Notes

- Rate: $35/hr. Not $20 (profile default). Not below $30.
- Lead with the screening question answer — don't bury it at the bottom
- Mention n8n by name — they already know it, they listed it
- Address the "not a generic AI chatbot role" signal — show you understand systems architecture, not prompt engineering
- Do NOT promise 6-month availability — frame around the initial project
- Portfolio to reference: "Automated Lead Generation & CRM Pipeline" is closest to their operational workflow needs
