---
title: HyperFrames Video Editor
type: concept
tags: [tools, video, hyperframes, heygen, design]
sensitivity: private
created: 2026-08-08
---

# HyperFrames Video Editor

## What it is

HyperFrames by HeyGen — write HTML/CSS/JS, render MP4. Installed as Claude Code skills via `npx skills add heygen-com/hyperframes --full-depth`. 25 skills live at `.agents/skills/` and `.claude/skills/`.

The OS workflow: **talking-head-recut** — take existing footage, layer timed graphic cards (GSAP timeline), render to MP4 frame-by-frame via headless Chrome.

## Status

Confirmed working as of 2026-08-08. Test render: 6-card Hephzibah Terminal Precision composition, 1920×1080, 63s, from Italian test clip.

## Design System — Hephzibah Terminal Precision

- **Background:** `#080808` matte
- **Accent:** `#E8FF3A` LEMON
- **Foreground:** `#F0F0F0`
- **Fonts:** Inter 400/700 + Caveat 400/700
- **Cards:** `border-radius: 14-16px`, glass matte, `rgba(255,255,255,0.035)` surfaces
- **Borders:** `rgba(232,255,58,0.22)` LEMON tint on glass elements

## Render Command

```powershell
$env:HYPERFRAMES_BROWSER_PATH = "C:\Program Files\Google\Chrome\Application\chrome.exe"
npx hyperframes render "videos/<project>/public" --skill=talking-head-recut -o "videos/<project>/output.mp4" --fps 30
```

## Composition Requirements (critical — causes blank/broken render if missing)

The root composition element (`#stage` div) MUST have:
```html
data-composition-id="talking-head-recut"
data-width="1920"
data-height="1080"
data-duration="63"
```

The `<video>` element MUST have:
```html
data-start="0"
data-duration="63"
```

The GSAP timeline MUST be registered matching the composition ID:
```js
window.__timelines['talking-head-recut'] = tl;
```

DO NOT use imperative `video.currentTime` control — HyperFrames owns video sync via `data-start`.

## Card Structure

Each card is a standalone HTML fragment in `public/cards/card-XX.html`. Loaded async into slot divs. All styles scoped with `[data-card-id="card-XX"]` selector.

## 6-Card Layout Plan (Intro Video)

| Card | Time | Layout | Content |
|------|------|--------|---------|
| 01 | 0.5–8.5s | Fullscreen overlay | "EMMANUEL" kinetic title, LEMON eyebrow, accent bar |
| 02 | 8.5–19s | Lower-third pill | Tech stack: n8n, Claude AI, Python, Playwright, Telegram |
| 03 | 19–30s | Stack (video top 548px) | "WHAT I BUILD" — n8n / AI / API grid |
| 04 | 30–43s | PiP (video 420×316 bottom-right) | "Systems that run while you sleep." + 3 feature cards |
| 05 | 43–53s | Fullscreen overlay | Count-up stat: "5+" production systems |
| 06 | 53–63s | Full dark outro | HEPHZIBAH wordmark + accent line + "Emmanuel Adekoya" |

## Video Layout Transitions (GSAP on `#video-wrap`)

- **Overlay:** wrap at 1920×1080, x/y 0
- **Stack:** wrap height tweens to 548px (top half)
- **PiP:** wrap tweens to x:1460, y:720, 420×316, border-radius:16
- **Full-bleed restore:** tween back to 0/0/1920×1080

## Source Files

```
videos/test-clip/
├── public/
│   ├── index.html          ← main composition
│   ├── input-video.mp4     ← re-encoded source (dense keyframes)
│   ├── cards/card-01..06.html
│   ├── fonts/              ← Inter + Caveat woff2
│   └── vendor/gsap.min.js
├── metadata.json
├── transcript.json
└── output.mp4              ← rendered (gitignored)
```

## Dependencies

- Node.js v22+, npx
- FFmpeg 8.1+ (audio extraction, re-encoding)
- Chrome at `C:\Program Files\Google\Chrome\Application\chrome.exe`
- Python + faster-whisper (transcription)

## Next Use

For the actual Upwork intro video: record Emmanuel on camera, run through the same pipeline with updated card content (real portfolio items, real stats). The composition HTML is the reusable template.
