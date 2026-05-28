---
sensitivity: private
entity_type: concept
name: Brand Identity
aliases: ["brand-system", "visual-identity", "proposal-design"]
last_updated: 2026-05-28
relationships:
  - target: "[[identity]]"
    type: part_of
    strength: 10
    first_seen: "2026-05-28"
    last_reinforced: "2026-05-28"
  - target: "[[proposal-anatomy]]"
    type: reinforces
    strength: 8
    first_seen: "2026-05-28"
    last_reinforced: "2026-05-28"
---

# Brand Identity — Emmanuel Adekoya

The visual and tonal system used across Upwork profile, proposals, portfolio thumbnails, SOW documents, and LinkedIn.

The goal: look like a £10k/month operator at every touchpoint. Not a freelancer. A specialist who runs a practice.

---

## Color Palette

Inspired by Ramshaw's insight: top freelancers brand their profiles with distinct, consistent colors. He and his student Harrison both use purple/pink to signal Top Rated Plus and stand out from the sea of blue corporate palettes.

Emmanuel's palette:

| Role | Color | Hex | Use |
|---|---|---|---|
| **Primary** | Electric Indigo | `#5C3BFE` | Main brand color — Upwork profile ring, portfolio thumbnail bars, SOW headers |
| **Accent** | Vivid Cyan | `#00D4FF` | Highlights, icons, dividers, CTA buttons in SOWs |
| **Dark BG** | Near Black | `#0D0D14` | Portfolio thumbnail backgrounds, dark-mode proposals |
| **Light BG** | Off White | `#F5F4FF` | Proposal document backgrounds, SOW body |
| **Text** | Slate | `#1E1E2E` | Body text in proposals and SOWs |
| **Success** | Emerald | `#10B981` | Checkmarks, deliverable ticks, status indicators |

**Why these colors:**
- Indigo/Cyan combination reads as "technical + forward-thinking" — appropriate for AI automation
- Dark background in portfolio thumbnails makes the automation screenshots pop (white n8n canvas on dark = striking)
- Not blue (corporate generic), not red (urgent/alarming), not green (basic)

---

## Typography

For all documents (proposals, SOWs, Canva thumbnails):

| Role | Font | Weight | Where |
|---|---|---|---|
| **Heading** | Inter | 700 (Bold) | Document titles, section headers |
| **Subheading** | Inter | 600 (SemiBold) | Section sub-headers |
| **Body** | Inter | 400 (Regular) | All body text, descriptions |
| **Mono / Code** | JetBrains Mono | 400 | Code blocks, technical specs, workflow names |
| **Emphasis** | Inter | 500 Italic | Key phrases, not overused |

**Why Inter:** Clean, legible at small sizes, has technical credibility without being stiff. Used by Linear, Vercel, and most premium SaaS tools — signals the right context.

**Font alternatives (if Inter unavailable):**
- Google Docs: Use "Nunito" for headers, "Roboto" for body
- Canva: "Plus Jakarta Sans" for headers, "Lato" for body

---

## Logo / Personal Mark

No logo needed yet. Use:
- Profile photo (professional, circle crop, with Indigo ring border)
- Monogram: "**EH**" in Inter Bold, Indigo on dark background — for Canva thumbnail corners

---

## Portfolio Thumbnail Template

**Dimensions:** 1500 × 1000px (Upwork portfolio standard)

**Layout:**
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   [Screenshot of actual automation / interface]     │
│   (takes 70% of the card)                          │
│                                                     │
├─────────────────────────────────────────────────────┤
│ [Indigo bar — 30% of card]                         │
│                                                     │
│  EH   TITLE OF PROJECT                TECH STACK   │
│       Short outcome line              n8n | Claude  │
└─────────────────────────────────────────────────────┘
```

**Colors:** Dark BG `#0D0D14` for screenshot area, Indigo `#5C3BFE` bar at bottom
**Text on bar:** White, Inter Bold for title, Inter Regular for outcome line
**Tech stack:** Cyan `#00D4FF` text, right aligned

Make these in Canva. All 12 portfolio items use identical template — only screenshot and text change.

---

## SOW (Scope of Work) Document

Used after discovery call to send a formal proposal to close the deal. Ramshaw's workflow: Fathom transcript → AI → SOW PDF.

**Document structure:**

```
[Header — Indigo bar full width]
SCOPE OF WORK
[Client Name] × Emmanuel H. | [Date]

[Section 1: Understanding]
What we discussed on the call — their problem in their language.
Demonstrates you listened. 2-3 sentences.

[Section 2: What I'll Build]
Specific deliverables. Numbered list. Each item states:
  - What: The exact thing being built
  - How: Technology used
  - Outcome: What this does for their business

[Section 3: Timeline]
Phase 1 (Days 1-X): [milestone]
Phase 2 (Days X-Y): [milestone]
Go live: [date]

[Section 4: Investment]
Upfront (40%):  $X,XXX  — due to start
Midpoint (30%): $X,XXX  — due at [milestone]
Final (30%):    $X,XXX  — due at delivery
─────────────────────
Total:          $XX,XXX

[Section 5: What I need from you]
Short checklist — API keys, access, decisions needed.

[Footer — Indigo]
Emmanuel Adekoya | [Upwork profile URL] | femijames613@gmail.com
```

**PDF generation:** Build in Google Docs using the brand colors, export as PDF. Or use Canva (SOW template).

**Tone in SOW:** Professional but direct. Not corporate. Not eager. Consultant, not vendor.

---

## Proposal Visual (Loom thumbnail)

When recording Loom videos, the auto-generated thumbnail often shows your face mid-sentence. Override this:

**Loom custom thumbnail:** Pause at a frame where you're looking at the screen, expression neutral/confident. Or create a Canva cover:
```
[Indigo background]
"Quick walkthrough — [3-word summary of what you found]"
[Your profile photo, circle, right side]
```

---

## LinkedIn Visual Identity

Same palette. Profile banner (1584 × 396px):
```
[Dark BG #0D0D14]
AI Workflow Engineer   [cyan text]
n8n · Claude API · Automation for SaaS & Agencies  [white, smaller]
[Indigo gradient stripe at bottom]
```

---

## Voice Tone (Written)

The visual brand matches the written voice:

| Attribute | Description |
|---|---|
| Directness | States things. No hedging. "This is solvable." Not "I believe I may be able to..." |
| Specificity | Numbers, tool names, outcomes. Never vague claims. |
| Confidence register | Senior consultant who's done this before. Not eager. Not formal. |
| Warmth | Present but not performative. Occasional Lagos cadence in sentence construction. |
| Length discipline | Everything shorter than you think it needs to be. |

**This is the same voice in every channel:** Upwork proposals, SOW documents, LinkedIn posts, Loom videos, Upwork chat messages.

---

## Where to Apply Each

| Touchpoint | Colors | Fonts | Notes |
|---|---|---|---|
| Upwork profile ring | Indigo | — | Thin ring around profile photo in Canva |
| Portfolio thumbnails | Indigo bar + Dark BG | Inter Bold | All 12 items identical template |
| Portfolio Loom videos | — | — | Face in bottom-left, screen fills frame |
| Video introduction | — | — | Scroll through branded portfolio |
| Proposals (text) | — | — | No visual formatting; voice carries the brand |
| SOW documents | Full palette | Inter | Google Docs → PDF |
| LinkedIn banner | Dark BG + Indigo | Inter | 1584×396px Canva |
| Loom thumbnails | Indigo | Inter | Optional custom thumbnail |

---

## Canva Brand Kit Setup

1. Open Canva → Brand Hub → Create Brand Kit
2. Brand colors: add all 6 hex values from the palette above
3. Fonts: Upload Inter (Google Fonts, free). Set Inter Bold as heading, Inter Regular as body
4. Logo: Upload the EH monogram once created
5. All portfolio thumbnails and SOW templates should be in this Brand Kit so they're consistent

---

## Wikilinks

[[identity]] · [[proposal-anatomy]] · [[elite-freelancer-model]]
