---
sensitivity: private
entity_type: concept
name: Realistic Scoping Framework
last_updated: 2026-08-10
source: SERAMAN project data + NZ Business Group analysis + Microsoft Graph API research
relationships:
  - target: "[[concepts/business-model-library]]"
    type: companion
    strength: 8
  - target: "[[concepts/value-based-pricing-framework]]"
    type: prerequisite_for
    strength: 9
  - target: "[[playbooks/proposal-framework]]"
    type: governs
    strength: 10
---

# Realistic Scoping Framework

The default failure mode in freelance proposals: estimate from optimism, not from data. The result is a 2-week quote for a 3-month build, a damaged relationship, a stalled project, and a JSS hit. This framework eliminates optimism from scoping.

---

## The SERAMAN Benchmark

SERAMAN is the calibration point. It is one automation pipeline, for one company, for one content type (product videos), with a known tech stack (n8n, HeyGen, Rendi, Blotato). At 1.5 months in, it is not complete.

This is the baseline unit. Everything more complex than SERAMAN takes proportionally longer.

---

## The Timeline Formula

Apply this formula to every engagement. Do not skip steps.

### Step 1: Count the integration types

For each distinct system the automation connects to, estimate:

| Integration type | Time estimate |
|---|---|
| Well-documented REST API (Stripe, HubSpot, Gmail) | 3-5 days |
| Partially documented API (GoHighLevel, Airtable) | 1-2 weeks |
| Microsoft Graph API (Outlook + Teams + SharePoint) | 3-5 weeks (OAuth, Entra ID, multi-tenant permissions, webhook reliability) |
| NZ/AU-specific ERP (Accredo, MYOB, Xero) | 1-3 weeks depending on API quality |
| Custom or legacy system with no public API | UNKNOWN — must confirm before scoping |
| File-based integration (CSV export, FTP) | 1 week |

### Step 2: Add the AI layer

| AI component | Time estimate |
|---|---|
| Simple prompt + output (one-step generation) | 3-5 days |
| Multi-step AI pipeline (intake → processing → output) | 2-3 weeks |
| AI with business-logic rules (exception detection, thresholds) | 3-4 weeks |
| AI trained on domain-specific patterns | Add 1-2 weeks |

### Step 3: Add testing time

| Testing type | Time estimate |
|---|---|
| Unit testing (individual component) | Built into integration estimates |
| Integration testing (end-to-end with demo data) | 1 week |
| Stability testing with real data (catch real-world failures) | 2-3 weeks minimum |

Real data always breaks what demo data passed. The 2-3 weeks of stability testing is not optional. It is where production-grade reliability is built. A system that runs for 10 consecutive days on real data without intervention is a production system. A system that ran on demo data is not.

### Step 4: Add teaching/build-alongside time

If the client wants to understand and eventually modify the system themselves:

- Add 30-40% to the total timeline
- Each working session is not free time — it is design time, explanation time, and training time
- Client calendar availability compounds the timeline: if they miss two sessions, add 2 weeks

### Step 5: Add handoff and documentation

- Simple system: 1 week
- Complex system: 1-2 weeks
- Multi-business, multi-system: 2 weeks

### Step 6: Sum everything. If it seems long, it is probably right.

The number you get feels uncomfortable. Quote it anyway. The discomfort is what kept you from quoting it before. But the alternative is discovering the real timeline mid-engagement, under pressure, when the relationship is already strained.

---

## The Technical Feasibility Check

Before any proposal is written on a deal over $5k, run this check:

1. List every integration the job requires
2. Mark each: KNOWN (built before), UNFAMILIAR (new but documented), UNKNOWN (no public API or undocumented)
3. For any UNKNOWN: can the integration be confirmed before accepting the contract? If yes, ask in the proposal. If no, scope Phase 1 as discovery only.
4. Check: does Emmanuel have hands-on experience with this stack, or is this a learning engagement?

**The UNKNOWN rule:** Any engagement with more than one UNKNOWN integration should be structured as Phase 1 = discovery only, paid, with Phase 2 contingent on what discovery reveals. This protects the client (no false promises) and Emmanuel (no unrecoverable scope surprises).

---

## The Multi-Phase Structure Rule

For any engagement estimated over 3 months total:

Never scope it as one monolithic contract. Break it into phases where each phase:
- Delivers standalone value (can be used even if no further phases happen)
- Has a defined completion milestone and deliverable
- Has its own contract on Upwork (separate fixed-price contract, not one open-ended ongoing)
- Has a payment milestone structure (not 100% upfront)

This protects JSS: each phase closes cleanly with its own review. If phase 1 ends well, phase 2 starts fresh. A single open-ended contract for an 8-month engagement is a JSS liability.

---

## Reference: NZ Business Group Analysis

What a realistic scope looks like for a Management Operating System engagement:

| Phase | Components | Realistic timeline |
|---|---|---|
| Phase 1 | Discovery + Microsoft 365 integration + 4 business system connectors + AI synthesis engine + daily report delivery + stability testing + handoff | 3 months |
| Phase 2 | Weekly reporting + group consolidation + inbox triage + response drafting | 3 months |
| Phase 3 | Board reports + presentations + meeting intelligence + KPI tracking + new-business playbook | 2-3 months |
| Total | Complete Management Operating System | 8-9 months |

A 2-week quote for Phase 1 of this system is not a scope. It is a misunderstanding of the complexity, communicated as a price.

---

## When the Client Pushes Back on Timeline

The client may say: "I've seen other freelancers quote 2 weeks for this."

The correct response: "Those quotes are either for a simpler version of what you described, or they don't include stability testing with your real data. The Microsoft Graph API integration alone — Outlook, Teams, and SharePoint together with proper OAuth — takes 3 to 6 weeks for a production-grade connection. A system that runs on demo data for a week is not the same as a system that handles your actual Accredo data and job-scheduling data reliably every morning. The 3-month estimate is what it takes to build something you can rely on."

State this calmly. The client who wants fast over right will have a problem with any contractor. That is not your client.

[[concepts/business-model-library]] · [[concepts/value-based-pricing-framework]] · [[concepts/executive-presence]] · [[playbooks/proposal-framework]]
