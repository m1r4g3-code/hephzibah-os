---
sensitivity: private

aliases: [crisis, platform-down, suspension-protocol]
entity_type: concept
last_updated: 2026-07-24
name: Platform Crisis Protocol
relationships:
- first_seen: '2026-07-24'
  last_reinforced: '2026-07-24'
  strength: 2
  target: '[[hephzibah-os]]'
  type: governs
- first_seen: '2026-07-24'
  last_reinforced: '2026-07-24'
  strength: 2
  target: '[[client-intake-protocol]]'
  type: depends_on
---

## Why This Exists

2026-07-24: Oba's Fiverr account suspended permanently with no warning. Three active client relationships at risk. No playbook existed. Result: midnight panic, scattered WhatsApp messages, $12,500 in lost pipeline (MadSoN + Liubovi with no contacts on file).

This protocol exists so that when a platform goes down — and it will happen again — Emmanuel moves calmly and fast, not in panic.

---

## The First 30 Minutes

When a platform suspension or outage is confirmed, run these in order. Do not skip. Do not freestyle.

### Minute 0-5: Confirm and assess

1. Confirm the suspension is real (not a temporary glitch). Log in from incognito, check email for platform notification.
2. Open `hephzibah-brain-temp/_PIPELINE.md` immediately.
3. List every client currently in "Live Clients" or "Proposals Awaiting Reply" on that platform.
4. For each client: do we have off-platform contact? Yes/No.

### Minute 5-15: Triage by contact status

**Clients WITH off-platform contact:**
Priority tier. Draft and send the direct email now. Template below.

**Clients WITHOUT off-platform contact:**
Emergency research. In this order:
1. Search their name + company on LinkedIn
2. Search their website (listed on platform profile)
3. Search their Instagram
4. Check their platform profile for any linked external handles
5. If still nothing: log as "contact lost — unrecoverable" in _PIPELINE.md

### Minute 15-30: Send recovery emails

Send to every client with a found contact. One email. Keep it human. No panic, no pitch.

**Recovery email template:**
```
Subject: Quick message from Emmanuel

Hi [Name],

Hope you're well. The platform we've been working through has had some issues on our end, 
so I wanted to reach out directly to make sure we don't lose touch.

Everything on your side is fine and unchanged. Just wanted you to have my direct email 
in case you need anything.

Emmanuel
```

Do not mention the suspension specifically unless they ask. "Issues on our end" is enough.
Do not pitch work in this email. The goal is contact, not conversion.

### Minute 30+: Update the pipeline and log the loss

Move suspended clients to "Suspended / Lost" table in `_PIPELINE.md`:
- Note: date, platform, what was lost, contact status, recovery possible Y/N
- For lost contacts: "contact lost — no email captured. Unrecoverable."

This is a permanent record. It stays there as a reminder.

---

## Oba-Specific Protocol

When Oba's account is the suspended one:

1. Message Oba immediately — not to panic, but to coordinate: "Oba, your account got suspended. Let's move fast. Which clients do you have contacts for?"
2. Get all client contacts from Oba before attempting any outreach.
3. Divide the outreach: Emmanuel handles clients he built the work for, Oba handles the pure client relationship ones.
4. Set clear lanes — "You handle X, I'll handle Y. Meet back here in 30 minutes."
5. Do NOT send duplicate emails to the same client from both of you.

The midnight chaos in July 2026 happened because there was no division of labour and both people were reacting in parallel to the same problem without coordination.

---

## Income Continuity Checklist (run immediately after crisis is contained)

- [ ] Which active invoices are outstanding on the suspended platform? Can they still be paid?
- [ ] Are any escrow funds locked on the platform? If Upwork: check if Fiverr: usually lost.
- [ ] What work was in progress? Does the client still expect delivery?
- [ ] Update Upwork / direct client pipeline — is there anything to activate as emergency income?
- [ ] Is Revamp Consulting or any direct client ready to start? Push that forward.

---

## Post-Crisis Action (within 48 hours)

1. Update `_SESSION.md` with what happened and what was lost.
2. Log the total pipeline lost to `upwork/performance/insights.md`.
3. Add the lesson to `concepts/` if a new pattern emerged.
4. Review whether a similar crisis could happen on the remaining active platforms.
5. Make sure every remaining client has off-platform contact. No exceptions.

---

## The Deeper Fix

A crisis protocol should almost never be needed if [[client-intake-protocol]] is followed.
If this protocol is being run, something upstream already failed.

After every crisis: trace back to where the intake protocol was skipped and why.

## See Also

[[client-intake-protocol]] · [[middleman-lesson]] · [[oba-partnership]] · [[hephzibah-os]]
