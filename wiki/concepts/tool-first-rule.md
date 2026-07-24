---
sensitivity: private

aliases: [tool-before-task, script-first, no-retry-loops]
entity_type: concept
last_updated: 2026-07-24
name: Tool-First Rule
relationships:
- first_seen: '2026-07-24'
  last_reinforced: '2026-07-24'
  strength: 1
  target: '[[hephzibah-os]]'
  type: governs
---

## The Rule

**Before attempting any task that involves rendering, image processing, file transformation, or multi-step data manipulation — check if a script exists. If it doesn't, build it first.**

Trying the task without the right tool = retry loop. Retry loops waste Emmanuel's time and mine.

---

## What Triggers This Rule

A task triggers this rule when it requires ANY of:
- HTML → image/PDF rendering
- Image loading, resizing, format conversion, base64 encoding
- Google Drive or external file downloads
- Audio/video extraction or processing
- Multi-step data transformation (scrape → parse → score)
- Repeating a creative output (card, PDF, proposal) with different content

---

## The Check (run this before starting)

```
1. Does scripts/ have a tool for this task?
   YES → use it. Pass --help if unsure of flags.
   NO  → build the script first, then use it.

2. Will this task need to run again with different data?
   YES → it's a tool, not a one-off. Build it properly.
   NO  → still build it if it's longer than 3 steps.
```

---

## Known Tools and What They Handle

| Task | Script |
|------|--------|
| LinkedIn brand card → PNG | `scripts/render_card.py` |
| Proposal → PDF | `scripts/proposal_renderer.py` |
| Handoff brief → PDF | `scripts/handoff_renderer.py` |
| Job URL → JSON | `scripts/scraper.py` |
| Job JSON → scores | `scripts/qualify.py` |
| Proposal draft → voice check | `scripts/voice.py` |
| Loom video → coaching report | `scripts/loom_coach.py` |
| Brain node read/write/commit | `scripts/vault.py` |
| Profile audit | `scripts/profile_audit.py` |
| Discovery call brief | `scripts/call_prep.py` |
| Pricing / SOW | `scripts/quote.py` |

---

## What Happened Without This Rule (2026-07 session)

Trying to render HTML → PNG:
1. Built artifact (wrong — user wanted an actual file)
2. Tried Canvas approach (blocked by browser security)
3. Tried writing raw HTML and viewing it (no PNG output)
4. Tried Playwright ad-hoc in scratchpad (finally worked, but 4th attempt)
5. Each attempt required re-building the same logic from scratch

**Cost:** ~45 minutes of retry loops. One `render_card.py` script built upfront = 2 minutes per future card.

Base64 injection for large images:
- Tried reading b64 into Claude context (200K chars = context overflow)
- Had to build PowerShell workaround to inject into HTML string
- **Tool fix:** `render_card.py` reads the image file directly and converts internally — b64 never enters Claude's context

---

## Building a New Tool — Standards

When the task needs a new script:
1. Put it in `scripts/`
2. Add argparse with `--help` documentation
3. Include a usage example in the module docstring
4. Add it to the Known Tools table above
5. Test it once with real data before reporting done

Don't put tools in scratchpad. Scratchpad is for throwaway. Scripts are for reuse.

---

## The Anti-Pattern to Avoid

```
❌  Try ad-hoc → fail → adjust → fail → adjust → fail → eventually build script
✓   Identify task → check scripts/ → build tool if missing → run once → done
```

The retry loop is not exploration. It's wasted time that could be a tool.

## See Also

[[hephzibah-os]] · [[claude-api]]
