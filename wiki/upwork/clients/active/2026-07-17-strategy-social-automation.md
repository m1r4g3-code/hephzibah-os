---
name: strategy-social-automation
sensitivity: private
platform: direct (school contact)
status: awaiting_pricing
created: 2026-07-17
updated: 2026-07-18
---

# Client: Revamp Consulting LLC — Social Media Automation

**Business:** Revamp Consulting LLC — Strategic Advisory & Business Transformation
**Website:** https://www.revampconsult.com (recently developed by Bayonet)
**Platform:** Direct. School contact (Bayonet) intermediary. End client is a strategy consulting firm.
**Middleman:** Bayonet (school friend) — passes messages, pays Emmanuel directly from his cut
**Pay:** TBD — Bayonet said "I'll sort u from my end." Emmanuel asked for a number. Awaiting confirmation.
**Emmanuel's floor:** $200 (original agreement). Do not build without confirmed number.

---

## Project Scope

Daily social media automation tool that generates business strategy content, presents it for approval via Telegram, then posts to social platforms automatically.

**Cron trigger:** 9:00 AM daily

**Platforms confirmed:** Instagram + LinkedIn only. No others.

**Content specs:**
- Max 75 words per post
- Text + image (Instagram and LinkedIn require matching image)
- Dynamic CTA based on content relevance to the business services
- CTA points to their contact form

**Content topic areas:**
- Business case studies: who won, why, how
- Definition of strategy: ideas, misconceptions, myths
- Strategy development process
- Business nuggets: strategy, people, finance, org structure, culture, team management
- Disruption and innovation
- Competition in business
- Leadership
- Succession planning
- Strategy execution

---

## Stack Decided

| Layer | Tool |
|---|---|
| Trigger | n8n cron node (9:00 AM daily) |
| Content generation | Claude API |
| Image generation | Kie AI (image models) |
| Approval flow | Telegram bot in n8n (approve / edit / regenerate image) |
| Social posting | Upload-Post ($16/month) |
| n8n hosting | Self-hosted VPS — Hostinger or Namecheap (Bayonet's server) |

**n8n hosting update:** NOT n8n Cloud. Bayonet will host on a VPS. Reduces monthly running cost significantly vs Cloud ($24/month saved). Emmanuel builds on Bayonet's n8n instance using JWT credentials Bayonet shared.

**Trial approach:** Build goes live on Bayonet's own LinkedIn + Instagram credentials first. Once client sees the demo and approves, credentials switch to the end client's accounts. Lower-stakes first run.

---

## Monthly Running Costs (Updated — Self-Hosted n8n)

| Tool | Cost |
|---|---|
| VPS (Hostinger/Namecheap) | ~$3-6/month |
| Claude API | ~$5-15/month |
| Kie AI credits | Already available (from existing bundle) |
| Upload-Post Basic | $16/month |
| **Total estimate** | **~$25-37/month** |

Cost drops significantly from original estimate ($45-55) because n8n Cloud ($24/month) is replaced by a self-hosted VPS.

---

## Approval Flow Design (Confirmed)

1. Cron fires at 9AM
2. Claude generates 75-word post + picks CTA pointing to revampconsult.com contact form
3. Kie AI generates matching strategy-themed image
4. Telegram bot sends text + image to single approver
5. Approver options: approve / edit text / regenerate image
6. Edit: bot collects revised text, re-presents with original image
7. Regenerate image: Kie AI generates new image, re-presents for approval
8. Approve: posts to LinkedIn + Instagram simultaneously

**Confirmed:** 1 person approving (not a team). Edit and image regeneration both required.

---

## Discovery Status (2026-07-18)

| Question | Status |
|---|---|
| Platforms beyond Instagram/LinkedIn? | Answered: LinkedIn + Instagram only |
| What does the business do? | Answered: Revamp Consulting LLC — Strategic Advisory & Business Transformation |
| Contact form link | Pending — pull from revampconsult.com once site is fully live |
| Instagram Business account linked to Facebook Page? | NOT YET CONFIRMED — critical before build |
| Brand assets: logo, colors, image style | Logo PNG pending (Bayonet said he'll send) |
| One person or team approving? | Answered: 1 person on Telegram |

---

## Pending Before Build Starts

1. Bayonet confirms his number (pricing — BLOCKER)
2. Logo PNG from Bayonet
3. Confirm Instagram is a Business account linked to a Facebook Page
4. Contact form URL from revampconsult.com

---

## Key Notes

- Instagram API requires Facebook Business account + Instagram Business account linked to Facebook Page. Most complex setup step. Must confirm before build starts — cannot post to Instagram without this.
- Trial build uses Bayonet's own credentials. Switch to end client credentials after demo approval.
- n8n credentials: Bayonet shared JWT token (his n8n instance, email: bayomisimon@gmail.com). Do not store the raw token here.
- This is Emmanuel's own job. No Oba involvement.
- "Free tier" request is dead — Emmanuel correctly flagged $25-37/month running cost. Bayonet agreed client will pay once tested.
- Business topic areas (for Claude prompt): strategy case studies, strategy definition/myths, strategy development process, business nuggets (finance/culture/people/org), disruption/innovation, competition, leadership, succession planning, strategy execution.
