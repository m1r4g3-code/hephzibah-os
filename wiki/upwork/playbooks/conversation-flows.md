---
sensitivity: private
entity_type: concept
name: Conversation Flows
aliases: ["upwork-chat", "post-proposal-chat"]
last_updated: 2026-05-27
relationships:
  - target: "[[proposal-framework]]"
    type: part_of
    strength: 8
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
  - target: "[[challenger-reframe]]"
    type: reinforces
    strength: 7
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
  - target: "[[pain-before-pitch]]"
    type: reinforces
    strength: 8
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
---

# Conversation Flows

How to handle Upwork chat after a proposal is sent. Most freelancers lose contracts in the chat phase — not the proposal phase. This is where frame control matters most.

---

## Phase 1: After Sending the Proposal

**Typical wait time:** 1–5 business days.

If no reply in 5 days: one follow-up, maximum.

**Follow-up template:**
```
Hey [name] — following up on my proposal from [X days ago]. If you're still evaluating, happy to answer any questions you have about the approach. If the project has moved in a different direction, no problem at all.
```

**Do NOT:**
- Follow up more than once
- Say "just checking in" — this is the most generic and lowest-leverage phrase in freelancing
- Send a follow-up the same day you submitted

---

## Phase 2: The First Reply

When a client replies, they're interested. Your job now: qualify them and establish frame.

**Opening replies tend to be one of three types:**

**Type A — The Test:**
Client asks a technical question or scenario to see if you know what you're talking about.

Response: Answer it specifically. Don't hedge. If you don't know: "I haven't built that exact configuration, but the approach would be [X] — want me to mock up the architecture?"

**Type B — The Price Question:**
"What's your rate?" or "Can you give me a quote for the full project?"

Response: Don't quote immediately. First understand scope.
"Happy to give you a firm quote. Can you tell me more about [the one thing that most affects scope]? That'll let me give you a number I can actually commit to, not just an estimate."

**Type C — The "Tell Me More":**
"Can you share more about your experience with X?" or "Walk me through how you'd approach this."

Response: This is the interview. Show thinking, not just credentials.
Structure: "The way I'd approach this is [framework]. The thing that usually goes wrong here is [specific risk]. I've handled that by [specific method]. Want me to sketch the full plan?"

---

## Phase 3: The Discovery Conversation

Your goal: understand enough to scope accurately AND establish that you're the senior person in this relationship.

**Frame-setting principle:** You are selecting them as much as they are selecting you. Your questions should feel like a smart consultant's intake, not an eager applicant's audition.

**Questions to ask (pick 2-3 max):**
1. "What does success look like 3 months after this is built?" (business outcome)
2. "What's happened if this doesn't get done?" (urgency and stakes)
3. "What have you already tried?" (avoid re-solving solved problems, understand what failed)
4. "Who else will be using/maintaining this?" (scope and complexity)
5. "Is this replacing something that exists, or is it net new?" (legacy constraints)

**Questions NOT to ask in chat:**
- "What's your budget?" (ask by proposing a scope and seeing their reaction)
- "When do you need this?" before you've understood the scope
- "Do you have a detailed spec?" (shows you need hand-holding)

---

## Phase 4: The Close

Once scope is established, close with a concrete proposal — not "let me know if you're interested."

**Closing structure:**
```
Based on what you've described:
- [Deliverable 1] — [timeline]
- [Deliverable 2] — [timeline]
- [Deliverable 3] — [timeline]

Total: [price], 50% upfront, 50% at final delivery.

I can start [day]. Want me to send the contract?
```

**Critical:** Always include 50% upfront. Non-negotiable (middleman-lesson). If client resists: "That's my standard payment structure for all engagements — it protects both of us. Happy to explain the contract terms."

---

## Phase 5: During the Contract

**Communication protocol:**
- Weekly update: status + any blockers + next week's plan
- Same-day response to questions (business hours)
- Proactive risk flagging: "I've found [issue], here are the 2 options, recommend option A because [reason]" — don't just flag problems, bring solutions

**Scope change requests:**
When a client asks for something outside the agreed scope:
"That's a great addition — it's not in our current scope but I can add it. It'll take approximately [X] additional hours at [rate]. Want me to add it to the contract?"

Never just do extra work without acknowledgment. Never refuse extra work without offering a path to add it.

---

## Coaching Flags (same as outreach domain)

Watch for these in conversations. Flag them in `/analyze-conversation` output:

| Flag | Description |
|---|---|
| `lost_frame` | Client is setting the terms, you're following |
| `let_go_moment` | Client showed hesitation, you backed off instead of reframing |
| `close_vague` | Ended chat without a specific next step |
| `over_explained` | Gave more info than asked for |
| `pitch_rushed` | Offered price/scope before understanding the problem |
| `scope_accepted_silently` | Client expanded scope, you said nothing |

---

## Wikilinks

[[proposal-framework]] · [[challenger-reframe]] · [[pain-before-pitch]] · [[middleman-lesson]] · [[client-types]]
