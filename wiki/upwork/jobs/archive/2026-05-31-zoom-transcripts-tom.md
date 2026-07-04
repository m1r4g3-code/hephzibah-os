---
sensitivity: private
entity_type: job
name: "Automated System for Zoom Transcripts"
url: "https://www.upwork.com/jobs/~022060770510501597655"
posted: "2026-05-30"
evaluated: "2026-05-31"
scores:
  job_quality: 48
  client_quality: 82
  fit_score: 38
  urgency: 5
  competition: 5
composite_score: 55
decision: "bid"
forced_bid: true
decision_rationale: "Score below gate (55 < 65). Proceeding on Emmanuel's call — reasoning: 'certain information' vagueness is likely legal OPSEC (law firm context), client discloses specifics on call. Logged forced_bid for outcome tracking."
bid_amount: "$25-30/hr"
budget_posted: "not disclosed"
client_spend: "$23,000"
client_hire_rate: "63%"
client_country: "United States"
client_username: "Tom (Houston, TX)"
client_avg_review: 5.0
red_flags:
  - "'Extract certain information' — undefined deliverable, JSS risk if scope disputes arise"
  - "Ongoing project with no scope boundary defined"
  - "PHP + Power Automate listed — Emmanuel's stack is n8n/TypeScript, profile mismatch"
  - "Budget not disclosed; some previous jobs paid $10-12/hr"
green_flags:
  - "Payment verified"
  - "5.0 stars (3 reviews)"
  - "US client, individual — solo attorney or small firm, easier to communicate"
  - "$50.83 avg hourly rate paid; paid $80/hr on prior technical job"
  - "$23K total Upwork spend"
  - "63% hire rate — decisive client"
jss_risk: "medium"
status: "evaluated"
proposal_file: "outputs/proposals/2026-05-31-tom-zoom-transcripts.md"
connects_spent: 0
---

# Automated System for Zoom Transcripts

**URL:** https://www.upwork.com/jobs/~022060770510501597655
**Client:** Tom | United States (Houston, TX) | $23K total | 63% hire rate | 5.0★
**Budget:** Not disclosed | Hourly, 1-3 months, <30 hrs/week
**Posted:** 2026-05-30 | 20-50 proposals competing

---

## Job Description (Summary)

Law firm owner (Houston) wants an automated system that accesses Zoom transcripts or Zoom AI summaries and extracts specific information, delivered in a usable format. Skills listed include PHP, MySQL, Power Automate, ChatGPT, Zoom. "Certain information" not specified in post — almost certainly legal OPSEC (client names, case facts, action items, billing notes not suitable for a public job listing).

---

## Real Problem (Diagnosis)

Solo attorney doing multiple Zoom calls per week (client consultations, case reviews). After each call, someone manually reads the Zoom AI summary and copies key details into their case management system or MySQL database. This is 15-30 minutes per call. They want it automated: call ends → system extracts the relevant fields → data lands where it needs to go. The "certain information" will be defined once there's a trusted freelancer in the room.

---

## Score Breakdown

| Factor | Score | Rationale |
|---|---|---|
| Job quality | 48 | 3-sentence description, no defined deliverables or budget |
| Client quality | 82 | Verified, 5.0 stars, $23K spent, $50/hr avg technical rate |
| Fit score | 38 | PHP + Power Automate mismatch; n8n/Claude is better stack anyway |
| Urgency | 5 | Posted yesterday, no interviews yet |
| Competition | 5 | 20-50 proposals, medium-high competition |
| **Composite** | **55** | Below 65 gate |

---

## Red Flags

- "Extract certain information" — undefined deliverable, JSS risk if scope disputes arise
- Ongoing project with no scope boundary defined
- PHP + Power Automate listed — Emmanuel's stack is n8n/TypeScript, profile mismatch
- Budget not disclosed; previous gigs paid as low as $10-12/hr

## Green Flags

- Payment verified
- 5.0 stars across all reviews
- US client, law firm — well-defined professional context
- $50.83 avg hourly rate paid, $80/hr on prior technical job
- 63% hire rate — decisive, not a tire-kicker

---

## Decision: BID (forced_bid: true)

**Rationale:** Composite 55 is below the gate. Emmanuel overrode on the basis that "certain information" vagueness is likely legal confidentiality, not scope laziness — client will disclose specifics on discovery call. Logged as forced_bid to track outcome. If this goes sideways, the data point is marked.

**Positioning angle:** Frame as Zoom → n8n → Claude extraction → MySQL. Show the system architecture. Proactively address the PHP/Power Automate mismatch by positioning n8n as the better tool for AI pipelines. Close with a question about extraction fields or call volume to signal you're already designing the system.

---

## Proposal Notes

- Client name: Tom (confirmed from freelancer review text)
- Loom format: portfolio/context Loom — show a simple workflow diagram, explain the architecture
- Key move: name the typical legal extraction fields (action items, client names, dates, billing notes) to show domain understanding without asking "what do you want?"
- Address PHP/n8n: don't hide it — reframe n8n as better for this use case
- Rate target: $25-30/hr (above $20 profile default; within client's $50 technical budget)
- Closing question: "How many Zoom calls per week are we processing roughly?"
