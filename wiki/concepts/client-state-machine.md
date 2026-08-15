---
sensitivity: private
entity_type: concept
name: Client State Machine
last_updated: 2026-07-27
---

# Client State Machine

Every client and prospect in the pipeline exists in exactly one state at any time.
State is tracked in the client node frontmatter under the `state:` field.
The OS validates transitions — you cannot skip states or move backwards without logging a reason.

---

## States

```
PROSPECT ──► OUTREACH_SENT ──► ENGAGED ──► PROPOSAL_SENT ──► REPLIED ──► CALL_BOOKED
                                                │                              │
                                                ▼                              ▼
                                            GHOSTED                      NEGOTIATING
                                                                               │
                                           CLOSED_LOST ◄────────────────────  ├──► CONTRACT_ACTIVE
                                                                               │         │
                                                                          CLOSED_LOST    ▼
                                                                                    DELIVERY
                                                                                         │
                                                                                         ▼
                                                                                   CLOSED_WON
```

---

## State Definitions

### `prospect`
Identified as a potential client. No contact made yet.
- **Entry condition:** Client identified via job post, referral, or outreach list
- **Required fields:** name, platform, project_type, potential_value
- **Time limit:** 48h before escalating to OUTREACH_SENT or archiving
- **Next states:** `outreach_sent`, `archived`

### `outreach_sent`
First contact made — proposal submitted, cold email sent, or DM sent.
- **Entry condition:** Proposal submitted OR first message sent
- **Required fields:** contact_date, contact_method, proposal_file (if applicable)
- **Time limit:** 72h → auto-flag for follow-up. 7d → move to `ghosted`
- **Next states:** `engaged`, `ghosted`
- **Triggers:** `proposal_sent` event → starts 72h follow-up timer

### `engaged`
Client has replied. Conversation is active.
- **Entry condition:** Client sends any reply to our outreach
- **Required fields:** reply_date, reply_sentiment (positive/neutral/negative)
- **Time limit:** 24h to respond to any client message
- **Next states:** `proposal_sent`, `call_booked`, `closed_lost`
- **Triggers:** `reply_received` event → run chess read immediately

### `proposal_sent`
Formal proposal sent (Upwork proposal, PDF, or SOW).
- **Entry condition:** Full proposal delivered to client
- **Required fields:** proposal_file, proposal_value, sent_date
- **Time limit:** 72h → follow-up. 7d → move to `ghosted`
- **Next states:** `replied`, `ghosted`

### `replied`
Client replied to formal proposal. Interest confirmed.
- **Entry condition:** Client responds to the proposal specifically
- **Required fields:** reply_date, reply_content_summary
- **Time limit:** Book call or next step within 24h of reply
- **Next states:** `call_booked`, `negotiating`, `closed_lost`
- **Triggers:** `reply_received` event → run /prep-call immediately

### `call_booked`
Discovery call scheduled.
- **Entry condition:** Call confirmed with date/time
- **Required fields:** call_date, call_platform (Zoom/Upwork/phone)
- **Time limit:** Run /prep-call before the call. No exceptions.
- **Next states:** `negotiating`, `closed_lost`
- **Triggers:** `call_completed` event → send SOW within 24h

### `negotiating`
Scope and pricing discussion active.
- **Entry condition:** Client engaged on price/scope, not yet signed
- **Required fields:** proposed_value, client_budget (if shared), sticking_points
- **Time limit:** 48h without movement → follow up
- **Next states:** `contract_active`, `closed_lost`
- **Chess rule:** Never lower price without removing scope. Every concession costs something.

### `contract_active`
Work is underway. Contract signed and active.
- **Entry condition:** Upwork contract started OR direct agreement signed with deposit received
- **Required fields:** contract_value, deposit_received, start_date, delivery_date
- **Time limit:** Deliver on or before delivery_date. Update client every 3-5 days.
- **Next states:** `delivery`, `paused`
- **JSS rule:** Manage temperature. No surprises. Engineer the private NPS to 9-10.

### `delivery`
Work delivered. Awaiting client confirmation and contract close.
- **Entry condition:** Final deliverable sent to client
- **Required fields:** delivery_date, delivery_notes, unexpected_extra_delivered (bool)
- **Time limit:** 7d → gentle close prompt to client
- **Next states:** `closed_won`
- **JSS rule:** NEVER close the contract yourself. Always: "Could you close the contract when you get a chance?"

### `closed_won`
Contract complete. Revenue received. Review secured.
- **Entry condition:** Contract closed by client, payment confirmed
- **Required fields:** final_value, review_received (bool), review_score (if known), nps_estimate
- **Actions on entry:** Log outcome, update metrics.md, add case study to portfolio backlog
- **Next states:** `prospect` (for repeat business)

### `closed_lost`
Did not convert. Client went elsewhere or project cancelled.
- **Entry condition:** Client explicitly declined OR 30d of silence after last contact
- **Required fields:** loss_reason, loss_stage (which state they were in when lost)
- **Actions on entry:** Extract learning, update red-flags.md if pattern emerges

### `ghosted`
No response after threshold period. Not yet lost — recoverable.
- **Entry condition:** 7d silence after `outreach_sent` or `proposal_sent`
- **Required fields:** last_contact_date, attempts_made
- **Time limit:** 2 follow-up attempts max. If no reply after 2nd attempt → `closed_lost`
- **Next states:** `engaged` (if they reply), `closed_lost`

### `paused`
Project on hold. Both parties aware.
- **Entry condition:** Explicit agreement to pause
- **Required fields:** pause_reason, resume_date (if known)
- **Time limit:** 30d → check in. 90d → move to `closed_lost` unless renewed
- **Next states:** `contract_active`, `closed_lost`

### `archived`
Never pursued. Not a loss — just deprioritized.
- **Entry condition:** Prospect identified but decision made not to pursue
- **Required fields:** archive_reason

---

## Client Node Frontmatter Schema

Every client node in `upwork/clients/active/` or `fiverr/clients/active/` must include:

```yaml
---
sensitivity: private
entity_type: person
name: "[Client Name]"
company: "[Company]"
platform: "[Upwork | Fiverr | Direct]"
state: "[current state from machine above]"
state_entered: YYYY-MM-DD
potential_value: [number in USD]
contact_email: ""
contact_whatsapp: ""
contact_linkedin: ""
contact_instagram: ""
introduced_by: "[name or 'direct']"
---
```

The `state` field is the machine's position. `state_entered` is when they entered it.
heartbeat.py reads these to detect stale states and surface follow-up alerts.

---

## Transition Log

Every state change must be logged inside the client node:

```markdown
## State Log
- 2026-07-27: prospect → outreach_sent (proposal submitted via Upwork)
- 2026-07-28: outreach_sent → replied (client replied, positive tone)
- 2026-07-29: replied → call_booked (call scheduled for 2026-07-30 9PM EDT)
```

---

## Chess Rules Per State

| State | Chess Read |
|---|---|
| `outreach_sent` | They have all the leverage — they choose whether to reply. Your only job: be the most interesting thing in their inbox. |
| `engaged` | Frame is shifting — read their message for who's leading. If they're asking questions, you have interest. If they're correcting, you have resistance. |
| `negotiating` | This is the board. Never show desperation. Every concession you make should cost them something. Anchor high, move reluctantly. |
| `delivery` | You're in the NPS engineering phase. The private survey determines your JSS more than the public review. Engineer the experience, not just the deliverable. |
| `ghosted` | Don't over-pursue. Two attempts maximum. Desperation reads on both sides. |
