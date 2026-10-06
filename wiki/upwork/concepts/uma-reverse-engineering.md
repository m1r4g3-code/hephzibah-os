---
sensitivity: private
entity_type: concept
name: UMA Reverse Engineering — Upwork AI Matching System
last_updated: 2026-08-16
tags: [upwork-algorithm, UMA, JSS, matching, account-launch, strategy]
---

# UMA Reverse Engineering

UMA (Upwork's AI matching system) builds a semantic fingerprint of every freelancer from ALL signals across the account simultaneously. When contracts close, UMA updates this fingerprint. Every signal is engineerable before the job is even posted.

---

## What UMA reads from a closed contract

| Signal | Source | Weight |
|---|---|---|
| Contract title | What the client names the job when posting | Very high |
| Job category | Category client selects when creating the job | Very high |
| Skills tagged on job | Skills client adds when posting | High |
| Public review text | Keywords in the client's written review | High |
| Private NPS score | Client's private satisfaction survey (0-10) | High (JSS formula) |
| Contract value | Dollar amount of the milestone | Medium |
| Contract duration | How many days the contract stayed open | Medium |
| Proposal text sent | Keywords in Emmanuel's cover letter/proposal | Medium |
| Message thread content | Tool names and deliverable details discussed | Low-medium |
| Portfolio piece tied to contract | If linked immediately after contract closes | Medium |

---

## The Core Exploit

Every signal above is set BEFORE the job is posted. Engineer them all and UMA receives a perfectly shaped fingerprint update from each contract.

**Step 1 — Choose the category deliberately:**
Category is the highest-weight signal. Two contracts in related but distinct categories signals breadth within a niche without scatter penalty.

**Step 2 — Engineer the job title:**
The client should name the job with the exact keyword cluster you want to rank for. This becomes a permanent work history entry UMA indexes.

**Step 3 — Coach the review text:**
Do not give word-for-word. Give the keywords to hit. Let the client write naturally. The review text is read semantically. Keywords in reviews carry direct ranking weight.

**Step 4 — Send a real proposal with keywords:**
Even for a known client, send a proper proposal through Upwork. The proposal text is part of the contract record and feeds UMA.

**Step 5 — Create a message trail:**
2-3 messages in the contract thread that name the tools being used. This is not for the client. It is for the contract record.

**Step 6 — Tie a portfolio piece immediately after close:**
Portfolio content is read alongside contract history. Linking them multiplies the keyword signal.

**Step 7 — Engineer private NPS:**
After every contract, Upwork sends a private 0-10 survey. 9-10 = Promoter (ranking boost). 7-8 = Passive = JSS NEGATIVE. Tell the client privately that the rating matters before the survey arrives.

---

## The 2-Contract Blueprint (Cyrus Jobs)

### Contract 1 — n8n AI Automation anchor

**Client posts:**
- Title: "n8n Workflow Automation — AI Content Pipeline Setup"
- Category: Web Development > Automation / Scripts
- Skills: n8n, Workflow Automation, API Integration, AI Automation, Webhook Integration
- Budget: $20 fixed

**Deliverable:** Real n8n workflow. Webhook trigger → AI processing → formatted output. Documented. Screenshot for portfolio.

**Proposal keywords to include:** n8n, webhook, AI automation, workflow, content pipeline, API integration

**Message trail to create:** 2-3 messages naming the tools: "the n8n webhook is live and connected to the OpenAI node..."

**Review keywords to coach:** n8n, automation, workflow, AI, delivered clean, on time, would hire again

**Portfolio piece:** Add immediately after close. Title: "n8n AI Content Automation Pipeline"

---

### Contract 2 — Python AI Agent anchor (1-2 weeks later)

**Client posts:**
- Title: "Python AI Agent Development — Business Process Automation"
- Category: AI & Machine Learning OR Software Development > AI
- Skills: Python, AI Agent Development, OpenAI API, Claude API, Business Process Automation
- Budget: $20 fixed

**Deliverable:** Real Python script with AI integration. Agent that takes input, calls AI API, returns structured output. Documented. Terminal screenshot for portfolio.

**Proposal keywords to include:** Python, AI agent, OpenAI API, automation, business process, structured output

**Review keywords to coach:** Python, AI agent, automation, clean code, delivered on time, would hire again

**Portfolio piece:** Add immediately after close. Title: "Python AI Agent — Business Process Automation"

---

## Cumulative UMA fingerprint after both contracts

- 2 completed contracts, 5-star each, JSS 100%
- Contract titles containing: n8n, AI, automation, workflow, Python, AI agent, business process
- Two categories: Automation + AI & Machine Learning (related, not scattered)
- Review text containing keyword clusters twice, from a real client
- Skills confirmed by actual contracts, not just profile claims
- Rising Talent badge unlocked
- Portfolio pieces tied to both contracts adding a third keyword layer
- Work history showing: AI automation specialist who builds real systems

UMA matches Emmanuel to: n8n automation jobs, AI workflow jobs, Python AI agent jobs, business process automation jobs. All high-budget. All premium positioning.

---

## The Ramshaw Path — Why Fullstack Still Lives Here

Automation is the entry point. Not the ceiling.

Ramshaw's $160k, $10k+ development contracts did not come from "fullstack developer" positioning. They came from clients who trusted him through automation work and expanded scope. The n8n anchor was the door. Full development was the room behind it.

Emmanuel's fullstack proof (YCT, Kairos, HephFlow) sits in the portfolio as supporting evidence. The UMA anchor stays on AI automation. As JSS builds and Rising Talent activates, clients who find Emmanuel through automation discover the development capability and expand scope. That is the natural path to the big development contracts.

Second specialization profile for fullstack can be created separately once the automation profile has JSS > 85% and Rising Talent active.

---

## What to do between Contract 1 and Contract 2

1. Add portfolio piece for Contract 1 immediately after close
2. Get all 5 LinkedIn testimonials live
3. Update overview with Recent Work section referencing the contract
4. Run uprankmir.com to check what keywords UMA is now registering
5. Record SERAMAN Loom (q012)

By the time Contract 2 closes, the entire profile is dense with the same keyword cluster. UMA scans everything simultaneously. Every layer reinforces the same signal.

---

## Geographic Suppression Note

UMA's cold-start suppression is real. New accounts land in the "Other Proposals" bucket regardless of proposal quality (confirmed: Denis Y., Andrei Z. in 31-proposal fake job sample). The two Cyrus contracts are the unlock. After them:

- JSS becomes visible
- Account exits "new" status
- Rising Talent eligibility opens
- Invitation rate increases
- Proposal visibility improves

Do NOT send real proposal batches before at least Contract 1 is closed. You are spending connects into a suppressed account. Wait for the unlock.

---

## Wikilinks

[[profile-gravity]] · [[account-launch]] · [[ramshaw-advanced-tactics]] · [[jss-mechanics]] · [[proposal-psychology-weapons]] · [[account-situation]]
