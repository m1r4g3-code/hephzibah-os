---
sensitivity: private
entity_type: concept
name: Brand Identity — Hephzibah
aliases: ["brand-system", "visual-identity", "hephzibah-brand", "proposal-design"]
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

# Brand Identity — Hephzibah

Emmanuel Adekoya operates under the **Hephzibah** brand. This is the visual and tonal system
applied across every professional touchpoint: Upwork portfolio, LinkedIn, SOW documents, Loom
thumbnails, and any deliverable a client receives.

**The goal:** A client sees a portfolio thumbnail, an SOW PDF, or a Loom cover — and immediately
reads: "This is a serious operator. This is not a freelancer. This is a practice."

---

## Brand Concept — "Terminal Precision"

The design language borrows from the best developer tool aesthetics (Raycast, Linear, Vercel,
Anthropic) and applies it to a freelance/consulting context where everyone else is running
blue corporate templates or generic gradient startups.

**The logic:**
- Monochrome base = restraint, discipline, nothing wasted
- Single lemon accent = the one electric insight that cuts through
- JetBrains Mono at scale = proof of depth at the code level
- Poppins at display = confident, geometric, human at large sizes
- Inter for body = neutral, precise, highly legible

Every design decision maps to the written voice. Monochrome = directness. Lemon accent = the
specific insight that changes the frame. JetBrains Mono = the practitioner, not the salesman.

---

## What Hephzibah IS / IS NOT

**IS:**
- Dark, precise, and technical
- A single electric accent in a monochrome world
- The aesthetic of a developer tool — intentional, frictionless, serious
- Confident without performing it
- Uncommon in the freelancer context — memorable by standing apart

**IS NOT:**
- Generic startup gradient blue/purple
- Multiple competing accent colors
- Eager or approachable-as-a-puppy energy
- Corporate conservative (suits + navy)
- Colorful, playful, or illustration-heavy
- Anything that looks like a template

---

## Color System

### Palette

| Token | Name | Hex | Lightness | Role |
|---|---|---|---|---|
| `--lemon` | Electric Lemon | `#E8FF3A` | 97% | Brand accent — the only chromatic color |
| `--lemon-dim` | Lemon 15% | `#E8FF3A26` | — | Hover fills, soft backgrounds |
| `--lemon-10` | Lemon 10% | `#E8FF3A1A` | — | Subtle glow backgrounds |
| `--black` | True Black | `#000000` | 0% | Terminal backgrounds, absolute dark moments |
| `--bg` | Near Black | `#0A0A0A` | 4% | Primary background — all dark surfaces |
| `--surface` | Surface | `#141414` | 8% | Cards, sections, elevated surfaces |
| `--surface-2` | Surface 2 | `#1C1C1C` | 11% | Secondary card level |
| `--border` | Border | `#2A2A2A` | 16% | Dividers, input borders, subtle lines |
| `--muted` | Muted | `#6B6B6B` | 42% | Disabled, secondary metadata |
| `--secondary` | Secondary | `#A3A3A3` | 64% | Body text emphasis, captions |
| `--body` | Body Text | `#E0E0E0` | 88% | All default body copy |
| `--heading` | Heading | `#FFFFFF` | 100% | Display headings, primary labels |

### Usage Rules — Strict

**Lemon is used for:**
- One brand moment per design surface (one accent per thumbnail, one highlight per document)
- Active state borders (2px outline on focus)
- A single stat or metric you want remembered
- Tech stack label on portfolio thumbnails
- Section marker glyphs in SOW (the `▪` before each section)
- Profile ring border in Canva (circle around photo)

**Lemon is never used for:**
- Large fills (never fill a full background section in lemon)
- Body text (illegible at small sizes against anything)
- Decoration (never apply it randomly)
- More than one element per surface

**Monochrome rule:**
Everything else is monochrome. If a design element isn't lemon, it is a shade of gray or white on
black. No other hues. No other accent colors. No gradients. Monochrome means discipline.

### Contrast Standards (WCAG AA minimum)

| Foreground | Background | Ratio | Pass |
|---|---|---|---|
| `#FFFFFF` on `#0A0A0A` | — | 19.8:1 | AAA |
| `#E0E0E0` on `#0A0A0A` | — | 15.3:1 | AAA |
| `#E8FF3A` on `#0A0A0A` | — | 14.1:1 | AAA |
| `#A3A3A3` on `#0A0A0A` | — | 6.2:1 | AA |
| `#FFFFFF` on `#141414` | — | 16.1:1 | AAA |

Every live design must pass AA minimum. Lemon on near-black easily clears AAA.

---

## Typography System

### Font Stack

| Role | Font | Weight | Size Range | Application |
|---|---|---|---|---|
| Display | Poppins | 700 | 48–72px | SOW title, portfolio headline at max size |
| Heading 1 | Poppins | 700 | 36–48px | Document section titles |
| Heading 2 | Poppins | 600 | 28–36px | Sub-section headers |
| Heading 3 | Inter | 600 | 20–24px | Item titles, card headers |
| Body Large | Inter | 400 | 18px | Lead text, first paragraph |
| Body | Inter | 400 | 15–16px | All body copy, proposals |
| Body Small | Inter | 400 | 13–14px | Captions, metadata |
| Label | Inter | 500 | 11–12px | Tags, uppercase labels (letter-spacing: 0.08em) |
| Code | JetBrains Mono | 400 | 13–14px | Workflow names, tool references, code blocks |
| Code Display | JetBrains Mono | 700 | 32–56px | Large stat numbers, key metrics in portfolio |
| Emphasis | Inter | 500 Italic | same as context | Selective — one phrase per section maximum |

### Why This Stack

**Poppins at display scale:**
Geometric, confident, and slightly warm. Creates presence and authority at large sizes without being
corporate or stiff. Used by Framer, Shopify, and many premium design-forward products. At 48–72px it
has the weight to anchor a page.

**Inter for body:**
The best screen-reading typeface available. Optimized by Rasmus Andersson specifically for interface
legibility. Neutral at small sizes, invisible in the best way — the content reads, not the font. Used
everywhere that matters (Linear, Vercel, Stripe, Anthropic).

**JetBrains Mono for technical signals:**
Non-negotiable for anything technical. When a stack reference (`n8n | Claude API`), a metric
(`12 min → from 6 hours`), or a workflow name appears in JetBrains Mono, it signals: "the person who
wrote this works at the code level." It creates instant credibility differentiation from every other
freelancer writing the same thing in Inter or Roboto.

**JetBrains Mono at LARGE scale (Code Display):**
A deliberate premium pattern. Showing `"6 hrs → 12 min"` in 48px JetBrains Mono Bold on a
portfolio thumbnail creates a striking typographic moment — technical precision + visual weight.
Raycast, Vercel, and 1-page portfolio sites from senior engineers use this technique.

### Hierarchy Rule

One Poppins Display or H1 per surface. One Code Display stat per portfolio item. Everything else
is Inter. JetBrains Mono appears exactly where technical context requires it — nowhere else.

Never mix Poppins and Inter at the same weight and size on the same surface. They are for
different hierarchy levels.

---

## Spacing System

**Base unit: 8px**

```
4px   — hairline gaps (icon-to-label, tight list items)
8px   — internal component padding (small tags, badges)
12px  — between related elements (icon row, form field group)
16px  — default element spacing (between paragraphs, list items)
24px  — section internal spacing (between a label and its content)
32px  — between sections within a component
48px  — major section separation
64px  — page-level section breaks
96px  — hero-level breathing room
128px — maximum whitespace (intentional empty space as a design element)
```

Restrained whitespace is a brand signal. Cramped = amateur. Generous = premium.

---

## Component Language

### Border Radius

```
0px     — data tables, code blocks, hard-edged technical elements
4px     — tags, small badges, code labels
8px     — buttons, inputs, small cards
12px    — portfolio thumbnail corners, main cards
9999px  — pills, avatar circles, toggle tracks
```

The near-zero radii on technical elements reinforce the terminal precision concept. The 12px radius on
thumbnails is modern without being bubbly. Never use > 16px radius on document elements.

### Shadows (dark-mode native)

```
Subtle:   0 1px 3px rgba(0,0,0,0.5)
Card:     0 4px 16px rgba(0,0,0,0.6)
Elevated: 0 12px 32px rgba(0,0,0,0.8), 0 0 0 1px rgba(232,255,58,0.06)
```

The `Elevated` shadow has a near-invisible lemon glow (6% opacity) in the ring — not visible
consciously, but subliminally adds a warm "lit from within" quality. Stripe uses this technique.

### Borders

Default: 1px `#2A2A2A` — almost invisible, defines boundaries without adding visual weight.
Active/Focus: 2px `#E8FF3A` — the lemon border appears only on interactive focus states.
Accent line: 2px left-border `#E8FF3A` — used for pull quotes or key callouts.

---

## Portfolio Thumbnail System

**Dimensions:** 1500 × 1000px (Upwork portfolio standard)

**All 12 thumbnails use identical template. Only screenshot + text changes.**

### Layout

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   [Screenshot — fills full width, dark content]        │
│   (n8n canvas, Claude interface, Zapier flow,          │
│    or API response in terminal)                         │
│                                                         │
│   Top-right corner: [H] monogram                       │
│   1px × 16px lemon line on left edge                   │
│   (70% vertical height)                                 │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  Near Black #141414 info bar (30% of card height)      │
│                                                         │
│  [Left]                    [Right, JetBrains Mono]     │
│  TITLE — Poppins 600 18px  n8n · Claude API            │
│  Outcome — Inter 400 13px  [#E8FF3A lemon text]        │
│                                                         │
│  [Bottom left: tiny "Hephzibah" wordmark, Inter 400]   │
└─────────────────────────────────────────────────────────┘
```

### Color Specs

- Screenshot area background: `#0A0A0A` (near black)
- Info bar: `#141414` (surface)
- Title text: `#FFFFFF` (Poppins SemiBold)
- Outcome text: `#A3A3A3` (Inter Regular)
- Tech stack: `#E8FF3A` (JetBrains Mono — the lemon moment)
- Brand monogram: `#E8FF3A` letter `H` on `#0A0A0A`, top-right, 14px
- Left-edge accent: 2px vertical lemon line, full height of screenshot area

### The Code Display Variant

For automation/results thumbnails, replace the outcome line with a large stat:

```
[Screenshot top 60%]
─────────────────────────────────────────
[Bottom 40%: Black #000000]

  6 hrs          →          12 min
  [JetBrains Mono 700 40px, #FFFFFF]
              [#E8FF3A arrow]

  Lead processing time after automation
  [Inter 400 13px, #A3A3A3]
```

This pattern: visual data proof in JetBrains Mono at large scale. Rare in freelancer portfolios.
Clients remember it.

### Screenshot Content

Ideal screenshot content for AI automation:
1. n8n canvas showing a complex workflow (the more nodes the better — depth signal)
2. Claude API response in a terminal or API testing tool
3. A data table before/after comparison
4. A Zapier/Make flow with 8+ steps
5. A webhook endpoint returning clean JSON

Avoid: blank state interfaces, basic 2-node automations, personal profile pages.

### Making Thumbnails

Build in Canva. All 12 should be in the same Canva project, same template. Swap screenshot + title + outcome + tech stack only. Every other element locked.

---

## SOW (Scope of Work) Document

The SOW is the close mechanism after a discovery call. It signals: this is a practice, not a
freelancer making it up as they go. Ramshaw: Fathom transcript → AI → SOW PDF.

### Document Structure

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  HEPHZIBAH                        [Date]
  Scope of Work
  [Client Name] ×  Emmanuel Adekoya
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

▪ UNDERSTANDING

  What we discussed on the call — their problem in their own language.
  2-3 sentences. Demonstrates you listened.

▪ WHAT I'LL BUILD

  1. [Deliverable name]
     What: [exact thing being built]
     How: [technology used]
     Outcome: [what this does for their business]

  ⟳ CHECKPOINT 1 — [Name the review gate]
     You review [specific output] before work continues.
     Nothing builds on unapproved foundations.

  2. [Deliverable name]
     What / How / Outcome

  ⟳ CHECKPOINT 2 — Final Walkthrough
     Complete system demo before handoff. You test, I document.

  [Add/remove checkpoints based on project complexity.
   Simple projects: 1 checkpoint. Complex: 2-3. Never zero.]

▪ COST PER RUN  [include for automation/recurring-output projects only]

  Operational cost per [unit — e.g., report generated, lead processed, record synced]:

  [Tool or API]          [per-unit cost]    [role in the workflow]
  [Tool or API]          [per-unit cost]    [role in the workflow]
  ──────────────────────────────────────────────────────────────
  Automated cost/run     $X.XX

  Manual baseline:       $XX.XX   (current staff/VA time at market rate)
  Automated cost:        $X.XX
  Savings per run:       $XX.XX   |  Payback in: [N weeks at projected volume]

  [This section turns the project fee into a math problem the client wins.]

▪ ONGOING PLATFORM COSTS  [include if client needs tool subscriptions post-delivery]

  Running costs after delivery — what the system depends on:

  [Tool]    [Plan]     [~Monthly]    [Why it's in the stack]
  [Tool]    [Plan]     [~Monthly]
  ──────────────────────────────────────────────────────────
  Total     ~$XX/month

  These are tool costs, not fees to me. I'll flag before including
  anything that requires a paid subscription.

▪ TIMELINE

  Phase 1  (Days 1–X)   [milestone]
  Phase 2  (Days X–Y)   [milestone]
  Go live: [date]

▪ INVESTMENT

  Upfront  (40%)   $X,XXX  — due to start
  Midpoint (30%)   $X,XXX  — due at [milestone]
  Final    (30%)   $X,XXX  — due at delivery
  ─────────────────────────────
  Total            $XX,XXX

▪ WHAT I NEED FROM YOU

  □ [API key / access / tool]
  □ [Decision needed]
  □ [Asset or content]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Emmanuel Adekoya   hephzibah.dev   femijames613@gmail.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### When to Include Optional Sections

| Section | Include when |
|---|---|
| `▪ COST PER RUN` | Project automates a repeating output (reports, leads, records, posts, emails) |
| `▪ ONGOING PLATFORM COSTS` | Client needs to pay for tools after delivery (API subscriptions, SaaS plans) |
| `⟳ CHECKPOINT` gates | Any project with >1 sequential phase — always include at least one |
| Neither cost section | One-time builds with no recurring compute (static website, one-off integration) |

**Why cost sections work:**
The client is already doing the math in their head. If you show it first — honestly, with the manual baseline alongside — you control the frame. The automated cost looks small against what they're currently spending. This is not manipulation; it is clarity.

### SOW Color Application

**Dark mode (for digital delivery):**
- Background: `#0A0A0A`
- Header bar: `#141414` with 2px top border `#E8FF3A`
- Section markers `▪`: `#E8FF3A`
- Section titles: `#FFFFFF` Poppins 600 14px
- Body text: `#E0E0E0` Inter 400 14px
- Divider lines: `#2A2A2A`
- Footer bar: `#141414` border-top `#2A2A2A`

**Light mode (for PDF printing):**
- Background: `#FAFAFA`
- Header: `#0A0A0A` bar full-width, 60px tall
- Header text: `#FFFFFF` Poppins 700 (name) + Inter 400 (subtitle)
- Header accent stripe: 4px `#E8FF3A` bottom border on header bar
- Section markers `▪`: `#000000` — lemon only on the header accent
- Body: `#1A1A1A` Inter 400 14px on white
- Footer: `#F0F0F0` background, `#6B6B6B` text

**PDF generation:** Build in Google Docs (light mode version, printable) or Canva. Export PDF.

**Tone:** Professional but direct. Consultant, not vendor. Not corporate. Not eager.

---

## LinkedIn Visual Identity

**Banner (1584 × 396px):**

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  [Background: #0A0A0A]                                          │
│                                                                  │
│  [Left side, vertically centered]                               │
│                                                                  │
│  HEPHZIBAH                           [Poppins 700 32px #FFFFFF] │
│  AI Automation Engineer              [Inter 400 16px #A3A3A3]   │
│                                                                  │
│  [Below, small monospace tag line]                              │
│  n8n  ·  Claude API  ·  Make  ·  Zapier  [JetBrains Mono 12px] │
│  [#E8FF3A]                                                      │
│                                                                  │
│  [Right side: profile photo circle, 160px, subtle ring]        │
│  Ring color: 2px #E8FF3A                                        │
│                                                                  │
│  [Bottom: 3px lemon stripe, full width]                        │
│  #E8FF3A                                                        │
└──────────────────────────────────────────────────────────────────┘
```

**Profile ring photo:** Profile photo in Canva, circular crop, 2px `#E8FF3A` border ring.

**Profile name on LinkedIn:** Emmanuel Adekoya (legal name, not brand name — LinkedIn enforces this)

**Headline text:** `AI Automation Engineer · n8n · Claude API · Make · Zapier`

---

## Loom Video Thumbnails

Auto-generated Loom thumbnails are unusable. Always set a custom thumbnail.

**Option 1 — Screen-first (preferred):**
Pause at a frame showing your screen with their website or workflow visible. Expression: neutral,
looking at screen, not mugging for camera.

**Option 2 — Canva cover (for no-context Looms or general profile use):**

```
[Background: #0A0A0A]

[Center-left, Poppins 700 24px #FFFFFF]
"Quick walkthrough for [Client First Name]"

[Below, Inter 400 14px #A3A3A3]
[2-3 word description of what you found]

[Right side: profile photo, 120px circle, #E8FF3A ring]

[Bottom left: tiny Hephzibah wordmark, Inter 400 11px #6B6B6B]

[Top-left: small lemon accent — 2px × 40px vertical line]
```

---

## Upwork Profile Ring

Ramshaw's branding signal: a distinct colored profile ring sets you apart from default avatars.

**How to make it:**
1. Open Canva, create 500×500px canvas
2. Background: `#0A0A0A`
3. Upload profile photo
4. Apply circle crop at 440px diameter, centered
5. Add circle shape at 460px diameter, stroke only, stroke color `#E8FF3A`, stroke width 6px
6. Export as PNG, upload as Upwork profile photo

The lemon ring is instantly distinctive in a feed of default blue/gray profile photos.

---

## Brand Application Matrix

| Touchpoint | Background | Primary Text | Accent | Font(s) | Notes |
|---|---|---|---|---|---|
| Portfolio thumbnails | `#0A0A0A` | `#FFFFFF` | `#E8FF3A` | Poppins + JetBrains Mono | 12 items, identical template |
| SOW (digital) | `#0A0A0A` | `#E0E0E0` | `#E8FF3A` | Poppins + Inter | Section markers in lemon |
| SOW (print PDF) | `#FAFAFA` | `#1A1A1A` | — | Poppins + Inter | Lemon only on header stripe |
| LinkedIn banner | `#0A0A0A` | `#FFFFFF` + `#A3A3A3` | `#E8FF3A` | Poppins + Inter + JetBrains | Bottom lemon stripe |
| Loom thumbnail | `#0A0A0A` | `#FFFFFF` | `#E8FF3A` | Poppins + Inter | Profile photo with ring |
| Upwork profile ring | `#0A0A0A` | — | `#E8FF3A` | — | Circle crop photo |
| Proposals (text-only) | — | — | — | — | Voice carries brand; no visual formatting in Upwork text |
| Email (SOW follow-up) | White | `#1A1A1A` | — | Inter | Plain text, no decoration |

---

## Wordmark

**Brand name display:**

`HEPHZIBAH` — all caps, Poppins 700, `#FFFFFF` on dark. Tracked at 0.04em letter-spacing.

No logo required at this stage. The wordmark + the profile photo + the lemon ring is sufficient.

**Monogram:** `H` — JetBrains Mono 700, `#E8FF3A` on `#0A0A0A`. Used in thumbnail corners.

---

## Canva Brand Kit Setup

1. Open Canva → Brand Hub → Create Brand Kit, name it "Hephzibah"
2. **Brand colors — add all:**
   - `#E8FF3A` (Electric Lemon)
   - `#0A0A0A` (Near Black)
   - `#141414` (Surface)
   - `#2A2A2A` (Border)
   - `#A3A3A3` (Secondary)
   - `#E0E0E0` (Body Text)
   - `#FFFFFF` (Heading)
3. **Fonts:**
   - Heading: Poppins Bold
   - Sub-heading: Poppins SemiBold
   - Body: Inter Regular
   - Upload JetBrains Mono (download from JetBrains.com free)
4. **Logo:** Upload the `H` monogram (lemon on black, once made)
5. **Templates to create:** Portfolio thumbnail, SOW dark, SOW light, LinkedIn banner, Loom cover

**All 12 portfolio items go in one Canva file, 12 pages, identical template.**

---

## Voice ↔ Visual Alignment

The visual brand mirrors the written voice:

| Written Voice Attribute | Visual Brand Equivalent |
|---|---|
| Directness — no hedging | Monochrome base — nothing extra |
| Specificity — one sharp insight | Lemon accent — one focal moment |
| Confident register | Near-black heavy — weight, gravitas |
| Technical depth | JetBrains Mono — practitioner signal |
| Length discipline | Generous whitespace — nothing wasted |
| Lagos cadence — slightly elevated | Poppins at display — confident, not stiff |

If the visual ever looks busy, add more monochrome. If it looks cold, apply one lemon moment.
If it looks generic, check that JetBrains Mono appears on the technical content.

---

## What NOT to Do

- Never add a second accent color (not teal, not orange, not purple alongside lemon)
- Never fill a large area in lemon (it becomes a yellow warning sign)
- Never use gradients (it reads as 2019 startup, not 2026 precision)
- Never use colored backgrounds behind text except the defined dark surfaces
- Never mix Poppins display with Inter at the same size on the same line
- Never apply more than 12px border radius to document elements
- Never use Inter at 700 weight where Poppins should be — they fight each other

---

## Wikilinks

[[identity]] · [[proposal-anatomy]] · [[elite-freelancer-model]] · [[upwork-voice]]
