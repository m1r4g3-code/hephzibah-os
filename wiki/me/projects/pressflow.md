---
sensitivity: private
entity_type: project
name: PressFlow
status: shipped
last_updated: '2026-05-31'
relationships:
- target: '[[identity]]'
  type: built_by
  strength: 10
  first_seen: '2026-05-31'
  last_reinforced: '2026-05-31'
- target: '[[builds-before-asking]]'
  type: embodies
  strength: 10
  first_seen: '2026-05-31'
  last_reinforced: '2026-05-31'
---

# PressFlow

Local-first, always-on speech-to-text desktop utility for Windows.
Hold a hotkey anywhere → speak → release → transcribed text pasted at cursor in 2 seconds.
No cloud. No account. No subscription.

## What it is

WhisperFlow / Superwhisper clone, built from scratch. Solves the problem that
WhisperFlow is paid and Superwhisper is macOS-only. This version is offline,
open-source, and owned.

## Stack

- **faster-whisper** — local Whisper inference (small model, ~244MB, CPU)
- **sounddevice** — mic capture to numpy float32 buffer, no temp files
- **keyboard** — global hotkey listener (system-wide, not just focused window)
- **pyautogui + pyperclip** — clipboard save → inject → restore
- **PyQt6** — floating pill UI + system tray + settings window

## Key design decisions

- Audio stays in memory (numpy buffer). Zero disk writes during recording.
- Model loaded at boot, not on first use — eliminates first-use latency.
- Floating pill UI matches WhisperFlow: states are RECORDING (waveform + timer),
  TRANSCRIBING (spinner), DONE (green check, fades), ERROR (red X, fades).
- Clipboard preserved: saves before paste, restores 500ms after.
- Hotkey falls back to F13 if Right Alt is already claimed by another process.

## PRD

Full specification at: `Upwork OS/pressflow-prd.txt`

## Built

2026-05-31. Went from PRD to shipped in one session.
