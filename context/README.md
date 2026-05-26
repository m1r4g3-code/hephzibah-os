# Shared Brain — Integration Guide

This directory is the portable memory layer of the Second Brain OS.
It exports the operator's identity, voice, concepts, and patterns into a format
any AI system can consume — on this machine or anywhere else.

---

## Files

| File | Size | Purpose |
|------|------|---------|
| `os_context.md` | ~2,000 tokens | Full brain state — load in other Claude Code projects |
| `system_prompt.txt` | ~400 tokens | Compact — paste into any AI system prompt |

---

## Keeping It Current

Run after any update to `wiki/me/`, `wiki/concepts/`, or `ME.md`:

```bash
python scripts/export_context.py
```

Or run the slash command from Claude Code:

```
/export-context
```

---

## Wiring Into Another Claude Code Project

Create a new Claude Code project for a different domain (e.g. a startup OS, a learning OS).
In that project's `CLAUDE.md`, add:

```markdown
## Shared Operator Context

At the start of any session involving operator identity, coaching, personalization,
or cross-domain reasoning, read:

C:\Users\HomePC\Documents\Cold Outreach Brain\context\os_context.md

This is the shared brain. It contains who the operator is, their voice, their
known patterns, their concept network, and their current goals.
```

That's it. The new project now has full context without you explaining yourself again.

---

## Wiring Into Any Other AI System

Copy the contents of `system_prompt.txt` and paste it as the system prompt in:
- Claude.ai (Project instructions)
- GPT-4 / ChatGPT (Custom instructions)
- Any API call's `system` message
- An n8n AI node's system prompt field
- A custom agent's persona config

---

## What Updates Automatically

| Source | What it feeds |
|--------|--------------|
| `wiki/me/identity.md` | Core story, inner circle, personal rules |
| `wiki/me/brand.md` | Positioning, voice, strengths, weaknesses |
| `wiki/me/goals.md` | Financial, lifestyle, education, physical targets |
| `ME.md` | Offer, non-negotiables, known sales weaknesses |
| `wiki/concepts/*.md` | The 12 concept nodes compressed into one block |

---

## The Pattern

One brain. Multiple projects tap into it.

```
Cold Outreach Brain/context/os_context.md
         │
         ├── Cold Outreach OS (this project) — active
         ├── Startup OS (future project)      — reads same brain
         ├── Learning OS (future project)     — reads same brain
         └── Any AI chat, API call, agent     — paste system_prompt.txt
```
