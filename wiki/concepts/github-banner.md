---
name: github-banner
description: Animated pixel art GitHub profile banner — lemon character, personality + laptop animation. Script and live URL.
metadata:
  type: reference
---

# GitHub Profile Banner — Pixel Art Character

**Live URL:** `https://raw.githubusercontent.com/m1r4g3-code/m1r4g3-code/master/banner.gif`
**Repo:** `m1r4g3-code/m1r4g3-code` (profile README repo)
**Script:** `scripts/make_banner_final.py` in Upwork OS project
**Last render:** 2026-07-22

## Animation breakdown

66 frames, 7.6s loop. Two phases:

**Phase 1 — Personality (standalone character):**
Idle hold, glance right + wink, wave 3 pumps, glance left, double blink, double hop x2 with squint eyes.

**Phase 2 — Typing at laptop:**
Laptop snaps in on landing. Character stands on keyboard, legs type.
Screen is rendered behind the character — lemon code builds through the leg gaps (cols 0,1,3,5,7,9,10 visible between leg cells). Key glows appear on keyboard as each leg position presses.
Ends: fast burst fills screen, ENTER clears, idle hold.

## Technical specs

- Grid: 10 rows x 11 cols, P=26px
- Canvas: 1500 x 400px, BG=(13,17,23)
- Lemon: (232,255,58), Screen: (6,6,6), Keys: (145,150,155)
- CHAR_Y=60, LAP_Y=268 (screen bezel behind leg rows 8-9, keyboard at y=320)
- Fonts: Poppins-ExtraBold 90pt, JetBrainsMono-SemiBold 28/18pt
- Quantize: colors=64, MEDIANCUT, no dither

## To regenerate

```
cd "C:\Users\HomePC\Documents\Upwork OS"
python scripts/make_banner_final.py
# Then push: get SHA, write payload via Python, gh api PUT
```

See push instructions in scripts/make_banner_final.py comments or session history.
