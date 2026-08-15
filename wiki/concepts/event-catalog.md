---
sensitivity: private
entity_type: concept
name: Event Catalog
last_updated: 2026-07-27
---

# Event Catalog — Upwork OS

Every event the OS monitors, with its handler, trigger condition, and required response.
Events are checked by `scripts/heartbeat.py` at session start.
Some events are automated (script detects them). Some are manual (Emmanuel logs them).

---

## Event Schema

```
event_id     — unique identifier
name         — human-readable name
trigger      — what causes this event to fire
detection    — automated (script detects) | manual (Emmanuel logs)
handler      — what the OS does when this fires
urgency      — CRITICAL | HIGH | MEDIUM | LOW
platform     — which platform this event belongs to
```

---

## Platform: Upwork

### `upwork.job_posted`
```
trigger:    New job posted matching active niche keywords
detection:  Manual (Up Cat browser extension alerts Emmanuel)
handler:    Run /job-qualify immediately.
            OODA: check time since posted — if <1h, MOVE NOW flag.
            If score 80+: write proposal within 60 minutes.
urgency:    HIGH (degrades to MEDIUM after 2h)
```

### `upwork.proposal_sent`
```
trigger:    Proposal submitted on Upwork
detection:  Manual (Emmanuel logs via /log-outcome)
handler:    Create proposal node in upwork/proposals/sent/
            Start 72h follow-up timer in _QUEUE.md
            Update client node state → outreach_sent
urgency:    LOW (starts timer for future HIGH event)
```

### `upwork.proposal_viewed`
```
trigger:    Upwork shows "Viewed" status on submitted proposal
detection:  Manual (Emmanuel checks Upwork and logs)
handler:    Update proposal node: viewed: true, viewed_date: today
            Reset 72h timer — they've seen it, standard window restarts
            Chess read: viewed but not replied = considering. Don't follow up yet.
urgency:    MEDIUM
```

### `upwork.reply_received`
```
trigger:    Client replies to a submitted proposal
detection:  Manual (Emmanuel sees notification, logs it)
handler:    Update proposal node state → replied
            Update client node state → engaged
            Run chess read on their message immediately
            Run /prep-call if they mention a call or ask questions
            Respond within same session — 24h max
urgency:    CRITICAL (revenue gate)
```

### `upwork.72h_no_reply`
```
trigger:    72 hours elapsed since proposal_sent with no reply
detection:  Automated (heartbeat.py reads proposal sent_date)
handler:    Surface in heartbeat output as FOLLOW-UP DUE
            If viewed: send one brief, value-adding follow-up
            If not viewed: do not follow up — profile suppression issue, fix profile first
urgency:    HIGH
```

### `upwork.7d_ghost`
```
trigger:    7 days elapsed since proposal_sent with no reply
detection:  Automated (heartbeat.py)
handler:    Move client state → ghosted
            Log in proposal node: outcome: ghosted
            Run /log-outcome [file] ghosted
            Extract learning: what did this proposal miss?
urgency:    MEDIUM (learning opportunity, not revenue event)
```

### `upwork.contract_started`
```
trigger:    Client accepts offer / contract goes active on Upwork
detection:  Manual (Emmanuel logs)
handler:    Run full client intake protocol (concepts/client-intake-protocol.md)
            Capture off-platform contact IMMEDIATELY
            Update client state → contract_active
            Create client node if not exists
            Add milestone dates to _QUEUE.md
urgency:    CRITICAL (intake protocol must run now — no delays)
```

### `upwork.contract_ended`
```
trigger:    Contract closed on Upwork (by client — never by us)
detection:  Manual (Emmanuel logs)
handler:    Run /close-contract
            Update client state → closed_won
            Log revenue in performance/metrics.md
            Add to portfolio backlog
            Request review engineering (private NPS setup)
urgency:    HIGH
```

---

## Platform: Direct / Fiverr

### `client.first_contact`
```
trigger:    Any new client makes first contact on any platform
detection:  Manual (Emmanuel or Oba)
handler:    IMMEDIATELY capture: email, WhatsApp, LinkedIn, Instagram
            File in _PIPELINE.md — off-platform contact column MUST be filled
            Create client node with state → prospect
            If Oba referred: get contact from Oba at first mention
            THIS CANNOT WAIT — MadSoN ($3,500) + Liubovi ($9,000) lost 2026-07-24
urgency:    CRITICAL
```

### `client.payment_received`
```
trigger:    Deposit or milestone payment received
detection:  Manual (Emmanuel logs)
handler:    Log in client node: payments[]
            Update _PIPELINE.md revenue column
            Add to performance/metrics.md
            If deposit: begin work — not before
urgency:    HIGH
```

### `client.goes_silent`
```
trigger:    No client response after agreed communication cadence
detection:  Manual + heartbeat.py (if last_contact_date in client node)
handler:    Chess read: why are they silent? (busy / unhappy / platform issue)
            Send one check-in message — warm, no pressure
            If no reply in 48h: escalate to CRITICAL — relationship at risk
urgency:    HIGH
```

---

## Platform: SERAMAN (n8n Pipeline)

### `seraman.job_submitted`
```
trigger:    Giovanni submits form via Tally
detection:  Automated (n8n webhook fires)
handler:    Pipeline runs automatically
            Log JOB_ID when execution email arrives in inbox
            Monitor execution chain for any failure emails
urgency:    MEDIUM (pipeline handles itself)
```

### `seraman.credits_exhausted`
```
trigger:    Kie AI returns HTTP 402 on image submit
detection:  Automated (n8n IF node, triggers alert emails)
handler:    Giovanni receives credits exhausted alert (amber email)
            Emmanuel receives internal alert (operational email)
            Add to _QUEUE.md: "Top up Kie AI credits, reset STATUS column, re-run wrapper"
            Do NOT re-run until credits confirmed replenished
urgency:    HIGH
```

### `seraman.job_failed`
```
trigger:    Error Handler workflow fires with red failure email
detection:  Automated (error email arrives at seraman.adv@gmail.com)
handler:    Pull n8n execution log for the failed run ID
            Diagnose: amber = Kie platform issue (wait), red = workflow bug (fix)
            Communicate to Giovanni via Oba within same session
urgency:    HIGH
```

### `seraman.images_pending_approval`
```
trigger:    Image review email sent to Giovanni — awaiting Approve click
detection:  Manual (watch for email in pipeline)
handler:    Confirm Giovanni or partner has received and can action the email
            If >24h with no action: send reminder via Oba
urgency:    MEDIUM
```

---

## Platform: LinkedIn

### `linkedin.post_due`
```
trigger:    Scheduled post time reached (8AM WAT on hard schedule dates)
detection:  Automated (heartbeat.py checks schedule vs. today's date)
handler:    Confirm post is live
            Post first comment within 60 seconds (hashtags + portfolio link)
            Flag: "Stay online and reply to every comment for the next 60 minutes"
            Log to content/posts/YYYY-MM-DD-slug.md
            Check engagement at 1h and log
urgency:    HIGH (hard schedule — algorithm punishes inconsistency)
```

### `linkedin.engagement_spike`
```
trigger:    Post receives unusual comment/reaction volume within 1h
detection:  Manual (Emmanuel monitors)
handler:    Reply to every comment immediately — velocity is the algorithm signal
            Consider whether content is portfolio-worthy for Upwork
urgency:    HIGH (reply window is short)
```

---

## System Events

### `os.session_start`
```
trigger:    Every session opens
detection:  Automatic
handler:    Run python scripts/heartbeat.py
            Read output, surface #1 action
            Load session files in order (as per Session Initialization)
urgency:    CRITICAL (no session starts cold)
```

### `os.session_end`
```
trigger:    Session is closing
detection:  Manual (Emmanuel signals end or OS detects natural close)
handler:    Update _SESSION.md with what was worked on, live items, decisions
            Update _QUEUE.md — mark resolved items, add new ones
            Commit and push brain: cd hephzibah-brain-temp && git add . && git commit -m "upwork: session [date]" && git push
urgency:    CRITICAL (cold starts happen when this is skipped)
```

### `os.platform_down`
```
trigger:    Any primary platform becomes inaccessible (suspended, restricted, down)
detection:  Manual (Emmanuel discovers)
handler:    Run platform-crisis-protocol.md IMMEDIATELY
            Open _PIPELINE.md — list all clients on that platform
            Triage by contact status: who has off-platform contact, who doesn't
            Send recovery emails to all contacts within 30 minutes
urgency:    CRITICAL
```

---

## Event Log Format

When an event fires, log it in the relevant client node or proposal node:

```markdown
## Event Log
- 2026-07-27 09:00 | upwork.proposal_sent | proposal: 2026-07-27-client-slug.md
- 2026-07-29 09:00 | upwork.72h_no_reply | auto-flagged by heartbeat | action: send follow-up
- 2026-07-30 14:00 | upwork.reply_received | client replied positive | state: engaged
```
