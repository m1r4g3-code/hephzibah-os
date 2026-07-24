---
name: liubovi-b2b-ai-agency
sensitivity: private
platform: fiverr
status: suspended-platform
introduced_by: "Oba (Adelaja O.)"
created: 2026-07-22
updated: 2026-07-24
off_platform_contacts:
  email: "unknown"
  linkedin: "unknown"
  instagram: "unknown"
  notes: "Lost access when Oba's Fiverr account was permanently suspended 2026-07-24. No off-platform contact captured at intake. Unrecoverable."
---

# Client: liubovi_b — B2B AI Agency (Unknown company name)

**Platform:** Fiverr (Oba's gig) — 50/50 split
**Client type:** AI agency selling chatbots, voice agents, workflow automations to businesses
**Target audience:** Corporate decision-makers, business owners, legal entities
**Location:** Likely Russian-speaking (username liubovi_b, languages requested include Russian)
**Contact:** Via Fiverr DM to Oba's gig

---

## What They Need

Daily AI avatar video content to promote their own B2B AI agency, and eventually to resell video production to their own B2B clients.

**Volume:** 3-5 short (15s) vertical videos + 1 long video (1-3 min) per day, 6 days/week
- Monthly: ~96 short + ~24 long = ~120 videos/month

**Languages:** English (master) + Russian + Romanian adaptation

**Platforms:** LinkedIn, Facebook, Telegram communities, Instagram Reels, YouTube Shorts, TikTok

**Style:** Professional, expert-led, trust-building B2B tone. NOT consumer UGC — corporate avatar presenter.

**Reference:** YouTube video they sent (https://www.youtube.com/watch?v=3rDs6FhFoUQ)

---

## Their Offered Rates (Do Not Accept)

- Short 15s video: $5/video
- Long 1-3 min video: $150/video

At these rates: 96×$5 + 24×$150 = $480 + $3,600 = $4,080/month gross. But manual production at this volume is not viable, and they want freelancer to cover own tool costs during "test period" — a red flag.

---

## The Pivot Oba Made (Correct)

Oba refused the per-video frame and pitched a full automation pipeline. Sent a demo link (Google Drive, Jul 22 10:53 AM). As of 2026-07-22 they have not responded to the automation pitch yet.

---

## Our Positioning: Automation Build + Managed Service

This is the ONLY version of this deal worth taking. Two options to present:

**Option A — Build + handoff: $9,000 one-time**
Full pipeline built, documented, handed to client to operate.
Payment: 50% ($4,500) before build starts, 50% on delivery.

**Option B — Build + managed service: $9,000 build + $3,500/month**
Same pipeline plus daily production managed by Oba/Emmanuel.
All tool costs included in retainer. Client approves via Telegram bot.

**Floors (do not go below):**
- Build floor: $7,500
- Monthly floor: $2,800

---

## Economics (Fiverr, 20% Fee, 50/50 Split)

| Item | Gross | After Fiverr 20% | After 50/50 Split | Emmanuel Net |
|---|---|---|---|---|
| Build ($9,000) | $9,000 | $7,200 | $3,600 | $3,600 |
| Monthly ($3,500) | $3,500 | $2,800 | $1,400 | ~$1,000-1,100 after tools |
| Build floor ($7,500) | $7,500 | $6,000 | $3,000 | $3,000 |
| Monthly floor ($2,800) | $2,800 | $2,240 | $1,120 | ~$720-820 after tools |

**Tool costs at full volume (~$300-400/month):** HeyGen + ElevenLabs + Creatomate + n8n + publishing

---

## The ROI Argument (Why $9,000 is Easy to Justify)

They plan to resell video production to their own B2B clients. A system producing 120 videos/month that they resell at $5,000+/month to clients recoups the $9,000 build fee in under two months. Lead with this frame — the build fee is not a cost, it is a revenue-generating asset.

---

## Stack Decided

| Layer | Tool |
|---|---|
| Daily trigger | n8n cron (morning) |
| Script + concept | Claude API (B2B corporate tone, rotating topics) |
| Language adaptation | Claude API (English master to Russian + Romanian) |
| AI avatar presenter | HeyGen API (talking-head B2B presenter) |
| Voiceover | ElevenLabs (multi-language: EN, RU, RO) |
| Short video edit | Creatomate (captions, lower thirds, logo, CTA) |
| Long video assembly | Creatomate or Runway |
| Approval flow | Telegram bot in n8n |
| Publishing | n8n nodes for all 6 platforms |

**Key new tech vs SERAMAN:** HeyGen for AI avatar (SERAMAN used Kie AI for product video — different use case). HeyGen has API, similar call pattern.

---

## Red Flags

- Wants freelancer to cover tool costs during test period — non-starter, baked into retainer
- Posted "less than 10 hours/week" on brief, revealed 120 videos/month scope in messages — deliberate mismatch
- Requested free test sample — Oba correctly declined with portfolio
- Russian-sounding client — verify payment method is clean before any build starts
- "We plan to offer your services to our B2B clients" — treat as a carrot, not a discount justification

## Green Flags

- B2B AI agency = understands automation value immediately
- Self-disclosed reseller ambition = potential white-label deal worth multiples of this contract
- Offered $150/long video themselves = not poverty budget
- Gave detailed brief = serious about the project
- High volume = recurring value once built

---

## Next Move

Oba sends the following message once liubovi_b responds to the demo:

```
Hi Liu,

Did you get a chance to watch the demo?

Here are two ways I can structure this for your agency:

Option A — Build + handoff ($9,000 one-time)
I build the full pipeline: AI avatar presenter, English / Russian /
Romanian adaptation, Telegram approval flow, auto-publish to LinkedIn,
Facebook, Telegram, Instagram, YouTube Shorts, and TikTok.
Fully documented, yours to operate. Payment: 50% before build,
50% on delivery.

Option B — Build + managed service ($9,000 build + $3,500/month)
Same pipeline, plus I run daily production for you — QA on every video,
prompt updates, platform maintenance, all tool costs included.
You approve content via Telegram, we handle everything else.

For an agency planning to offer this to your own B2B clients,
Option B gives you a production system you can white-label and resell.

Which direction fits better?
```

---

## Status Log

| Date | Event |
|---|---|
| 2026-07-21 | Oba responded to Fiverr brief, sent samples |
| 2026-07-22 | liubovi_b revealed full scope + budget ($5/$150) |
| 2026-07-22 | Oba pivoted to automation pitch, sent demo link |
| 2026-07-22 | Awaiting liubovi_b response to automation demo |

---

[[seraman]] [[automation-asset-pricing]] [[madson-children-animation]]
