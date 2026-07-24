---
sensitivity: private

aliases: [intake, new-client-checklist, contact-capture]
entity_type: concept
last_updated: 2026-07-24
name: Client Intake Protocol
relationships:
- first_seen: '2026-07-24'
  last_reinforced: '2026-07-24'
  strength: 2
  target: '[[hephzibah-os]]'
  type: governs
- first_seen: '2026-07-24'
  last_reinforced: '2026-07-24'
  strength: 2
  target: '[[middleman-lesson]]'
  type: prevents
---

## Why This Exists

MadSoN ($3,500) and Liubovi ($9,000) are gone forever because no off-platform contact was captured.
Elbert ($700-1,200) is recoverable only because contacts were found externally after the fact.
Giovanni is recoverable because his email was in the system.

Total cost of skipping this protocol: $12,500+ in lost pipeline. One night. One platform suspension.

The rule is not "capture contacts when convenient." The rule is: **no client enters the pipeline without off-platform contact. No exceptions.**

---

## The Protocol — Run This At First Client Message

The moment a new client makes first contact (Upwork, Fiverr, direct, referral — anywhere), Claude runs this checklist before doing anything else.

### Step 1 — Capture the contact (first 5 minutes)

Ask or research immediately. Do not wait until the project is active.

| Field | What to capture | How to get it |
|-------|----------------|---------------|
| Email | Primary email address | Ask directly: "What's the best email to reach you at?" |
| WhatsApp | Phone number with country code | "Do you use WhatsApp for updates?" |
| LinkedIn | Profile URL | Search by name + company |
| Instagram | Handle | Search by name or company |
| Website | URL | Usually in their post or bio |
| Company name | Legal or trading name | From their profile or messages |

You need at minimum: **email + one social (LinkedIn or Instagram)**. Email alone is acceptable if nothing else is findable. No contact at all = flag immediately.

### Step 2 — File it in _PIPELINE.md

Add a row to the correct table in `hephzibah-brain-temp/_PIPELINE.md` immediately. The off-platform contact column must be filled. Not "TBD." Not blank.

```
| Client Name | Platform | Project | Status | Next Action | Off-Platform Contact |
| Giovanni    | Fiverr   | SERAMAN | Active | M2 delivery | seraman.adv@gmail.com |
```

### Step 3 — Create the client node

Create `hephzibah-brain-temp/upwork/clients/active/SLUG.md` (or `fiverr/clients/SLUG.md`).

Minimum fields:
```yaml
name: [Client name]
platform: [Upwork / Fiverr / Direct]
email: [email]
whatsapp: [number]
linkedin: [url]
instagram: [handle]
website: [url]
introduced_by: [name if referral]
first_contact: YYYY-MM-DD
status: active
```

### Step 4 — Verify the contact works

If email: send a brief intro ("connecting directly so you always have my info").
If WhatsApp: add the number. Confirm it sends.

Do not assume a found email is current. One verification touch is worth more than 10 assumed contacts.

---

## How to Ask Without Being Awkward

Never say "I need your off-platform contact in case the platform gets suspended."

Say:
- "What's the best email to reach you at? I like to keep direct contact for faster communication."
- "Do you use WhatsApp? Sometimes easier for quick updates."
- "I'll send you a quick message outside the platform too — what email works?"

Most clients are happy to share. The ones who resist are a yellow flag.

---

## For Oba-Referred Clients

When Oba introduces a client, Claude asks Oba for the contact immediately. Do not wait for the client to appear directly. Oba has the contact — get it from him at first mention of the client.

Script for Emmanuel to send Oba:
> "Oba, what's [client]'s direct email? I want to have it on file."

If Oba doesn't have it, get it from the client profile, their website, or LinkedIn. Find it before the project starts.

---

## Platform Trust Levels

| Platform | Trust Level | Why |
|----------|------------|-----|
| Upwork | Medium | Account restrictions happen. JSS drops can limit bidding. Always have client email. |
| Fiverr | Low | TOS violations can suspend account with no warning and no appeal. **Never let a Fiverr relationship exist without direct contact.** |
| Direct | High | No platform intermediary. Still capture all contact details. |

Fiverr is permanently suspended as of 2026-07-24. All Fiverr history is gone. The lesson is permanent.

---

## What Claude Does If This Was Skipped

If a client appears in conversation without an off-platform contact on file:

1. Flag it immediately: "No off-platform contact on file for [client]. This is a risk. Let's fix it now."
2. Help Emmanuel compose a natural outreach to get the contact.
3. Do not let the session continue without resolving it.

## See Also

[[platform-crisis-protocol]] · [[middleman-lesson]] · [[hephzibah-os]] · [[oba-partnership]]
