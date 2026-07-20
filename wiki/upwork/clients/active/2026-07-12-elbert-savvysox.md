---
name: elbert-savvysox
sensitivity: private
platform: fiverr
status: active
created: 2026-07-12
---

# Client: Elbert Irving — SavvySox

**Business:** Sock brand — www.savvysox.com
**Platform:** Fiverr (Oba's gig)
**Client type:** Small e-commerce product owner, price-sensitive but expandable

---

## Deal History

### Phase 1 — Manual Hologram Videos ($200)
- Original brief: AI sock product videos, $100 budget
- Oba upsold to $700 for 50 videos, client negotiated to $200 for 13 styles
- Delivered: 13 hologram 3D rotating videos (4 African styles + 9 Anunnaki styles)
- Specs: 650x1557, 30fps, black background, 3D rotating, neon holographic glow
- Status: ALL 13 APPROVED by client (Jul 12 2026)
- Issue: 2 missing videos (African Futuristic Eloko + Anunnaki Ninhursag), 1 wrong video delivered (Change the Earth). Fix pending.

### Phase 2 — Automation Pipeline (PENDING PITCH)
- 37 remaining sock designs unpaid
- Oba pitched automation: drop image → auto-generate hologram video → Drive delivery
- Client responded positively: "Now what's that thing you can do all of them faster?"
- Discovery questions to send before proposal
- Target price: $1,000 (basic: video + Drive delivery) or $1,500 (full: + auto-posting)

---

## Client Behavior Profile

- Started at $100 budget ceiling
- Negotiated 50 videos → 13 videos to stay at $200
- Price sensitive but responds to value framing
- Communicates clearly, gives specific feedback
- Interested in efficiency/speed ("all of them faster")
- Sells on delivery model (made-to-order socks)
- Has 50 total sock designs in current catalogue

---

## Automation Pipeline Scope (Planned)

**UX for Elbert:** Drop image in "Sock Input" Drive folder → receive email when video is ready → video appears in "Sock Videos" folder. Zero technical steps.

**Stack:**
- n8n (orchestration)
- Google Drive (trigger + I/O)
- Kie AI / Kling AI (video generation — confirm API availability)
- Gmail (notification)
- Blotato or n8n social nodes (auto-posting — optional upsell)

**Flow:**
1. Drive trigger detects new image in Input folder
2. Download image + extract filename
3. Call Kie AI API with image + fixed hologram prompt
4. Poll until video ready
5. Upload to "Sock Videos" folder (named after sock)
6. Email Elbert with Drive link
7. Move input to "Processed" subfolder

**Fixed prompt (locked):** "3D rotating hologram sock animation, black background, neon holographic glow, cinematic product showcase, 15 seconds"

**API cost per video:** ~$0.05-0.15 (negligible margin)

---

## Discovery Questions to Send (Before Proposal)

1. How many new designs do you launch per month?
2. Where do you post — TikTok, Instagram, both?
3. Auto-post when ready or deliver to Drive and you post manually?
4. Logo/brand watermark on videos?
5. Background music or visuals only?
6. Just you on notifications or team too?

---

## Pricing Tiers

| Tier | Scope | Price |
|---|---|---|
| Basic | Image → Video → Drive + email | $1,000 |
| Full pipeline | Image → Video → Auto-post Instagram + TikTok | $1,500 |

Lead with full pipeline. Let him downgrade if needed.

## Negotiation Plan (finalized 2026-07-14)

- **Anchor price stated in proposal:** $1,200 — justified via [[automation-asset-pricing]] framing (pay once, forever asset)
- **Realistic floor / expected close:** $700
- **Fiverr order value:** $700 gross → 20% Fiverr fee (-$140) → $560 net
- **Split (Emmanuel / Oba, 50/50):** $280 each
- Floor still clears the $569 manual-cost baseline (37 videos × ~$15.38) and is ~100x raw API cost — defensible even at the bottom of the range

---

## Key Lesson Applied

Automation = permanent asset pricing. Not per-unit pricing.
At $13/video manual, 37 videos = $481. But the pipeline runs for life.
Priced accordingly: $1,000-1,500 one-time.
