---
sensitivity: private

aliases: [brand-card, linkedin-visual, card-system]
entity_type: concept
last_updated: 2026-07-24
name: LinkedIn Brand System
relationships:
- first_seen: '2026-07-24'
  last_reinforced: '2026-07-24'
  strength: 1
  target: '[[linkedin]]'
  type: implements
- first_seen: '2026-07-24'
  last_reinforced: '2026-07-24'
  strength: 1
  target: '[[brand]]'
  type: extends
---

## What This Is

The visual system for every Hephzibah LinkedIn post card. All image posts use this spec.
The renderer is `scripts/render_card.py`.

---

## Token System

### Color
| Token | Value | Usage |
|-------|-------|-------|
| `dark` | `#0A0A0A` | Dark theme card bg base |
| `lemon` | `#E8FF3A` | THE accent — one use per card surface |
| `white` | `#FAFAFA` | Light text on dark |
| `page-light` | `#E2DDD0` | Light theme page background |
| `card-light` | `#EDE8DC` | Light theme card surface |
| `page-dark` | `#060608` | Dark theme page background |
| `card-dark` | `#0C0C12` | Dark theme card surface |
| `ink` | `#18140E` | Dark chip background on light theme |

### Typography
| Role | Family | Weight | Usage |
|------|--------|--------|-------|
| Display | Poppins | 700 italic | Pull quote |
| Body | Inter | 400 | Attribution names |
| Technical | JetBrains Mono | 500 | Eyebrow, labels, chips, stats |

### Spacing & Shape
- Card border-radius: `24px`
- Image border-radius: `14px` (ratio: ~0.58 of card)
- Stats chip border-radius: `8px`
- Brand chip border-radius: `6px`
- Card padding: `24px`
- Page padding: `24px` (card floats inside page)

---

## Card Dimensions

- Viewport: `540×675` at `device_scale_factor: 2`
- Output: `1080×1350` PNG (LinkedIn 4:5 feed ratio)
- Image zone height: `296px` (at viewport scale)

---

## Image Matte Filter

All photography gets this CSS filter — preserves colors, kills harshness:
```css
filter: contrast(0.88) brightness(1.05) saturate(0.82);
```
Do NOT add grayscale. Do NOT add dark overlays or masks.

---

## Shadow System

**Light card** (shadow must be visible on cream bg):
```css
box-shadow:
  0 2px 6px rgba(0,0,0,0.05),
  0 10px 28px rgba(0,0,0,0.09),
  0 28px 56px rgba(0,0,0,0.07);
```

**Dark card** (stronger, still soft):
```css
box-shadow:
  0 2px 8px rgba(0,0,0,0.30),
  0 12px 32px rgba(0,0,0,0.40),
  0 32px 64px rgba(0,0,0,0.30);
```

---

## Lemon Accent on Light Background

Lemon `#E8FF3A` has ~1.2:1 contrast on cream — invisible as bare text.
Solution: dark chip technique. Lemon text inside `#18140E` dark pill.

**Stats chip (light theme):**
```css
background: #18140E;
color: #E8FF3A;
border-radius: 8px;      /* matches card corner language */
padding: 8px 14px;       /* optical balance: more vertical than horizontal */
font-size: 9px;
letter-spacing: 0.18em;
line-height: 1;
display: inline-block;
```

**Brand mark chip (light theme):**
```css
background: #18140E;
color: #E8FF3A;
border-radius: 6px;      /* slightly less than stats — hierarchy signal */
padding: 5px 11px;
font-size: 8px;
letter-spacing: 0.28em;
```

The chip radius should always relate to the card's own radius (24px).
Stats chip = 1/3 card radius. Brand chip = 1/4 card radius.

---

## Card Anatomy (top to bottom)

```
┌─────────────────────────────┐  ← 24px radius, shadow
│  EYEBROW LABEL              │  ← JetBrains Mono 8px, muted
│  ┌─────────────────────┐    │
│  │    HERO IMAGE        │    │  ← 296px, matte filter, 14px radius
│  └─────────────────────┘    │
│  "Pull quote here"          │  ← Poppins 700 italic 15px
│  [STATS CHIP]               │  ← dark chip with lemon (light) / bare lemon (dark)
│  ─────────────────────────  │  ← rule
│  ROLE LABEL     Name        │  ← grid, JetBrains Mono left / Inter right
│  ROLE LABEL     Name        │
│  ─────────────────────────  │
│  [HEPHZIBAH] © 2026         │  ← brand mark
└─────────────────────────────┘
```

---

## Render Tool

```
python scripts/render_card.py \
  --image PATH \
  --eyebrow "CLIENT × HEPHZIBAH — TYPE" \
  --quote "Brief or key line" \
  --stats "N units · N days · Result" \
  --role1 "Role" --name1 "Name" \
  --role2 "Role" --name2 "Name" \
  --theme both \
  --out Desktop
```

---

## Design Intent Notes

- Every post card must be **identifiable as Hephzibah** without reading the brand mark
- The matte newspaper quality comes from the filter + warm parchment bg, not from desaturation
- Lemon appears ONCE per card surface. If it appears twice it becomes wallpaper.
- The card floats — it does not touch the page edges. The page bg is visible as a border.
- Pills feel designed when their radius relates to the card. Random radii feel compensated.

## See Also

[[linkedin]] · [[brand]]
