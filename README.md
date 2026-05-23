# Outbound OS

> A closed-loop cold outreach intelligence system. Every call makes the next one smarter.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square)
![Claude Code](https://img.shields.io/badge/Powered_by-Claude_Code-orange?style=flat-square)
![Status](https://img.shields.io/badge/Milestone-M4_Complete-green?style=flat-square)
![Repo](https://img.shields.io/badge/Visibility-Private-red?style=flat-square)

---

## The Problem

Cold outreach fails for one consistent reason: **information asymmetry**. The caller knows nothing about the prospect before dialing. After the call, every signal — what objection killed the deal, what phrase kept them on the line, what the prospect actually cared about — evaporates. The next call starts from zero.

Most outreach systems solve the volume problem (make more calls). This system solves the intelligence problem (get smarter after every call).

---

## What This Is

Outbound OS is a personal AI-powered outreach intelligence system built on two core ideas:

**The Karpathy Vault Pattern** — Raw inputs live in `sources/` and are immutable. All synthesized intelligence lives in `wiki/`, which is AI-maintained. The operator reads. The AI writes.

**The Mech Suit Model** — Claude Code is the intelligence engine. Python scripts are mechanical arms that handle I/O, file writes, and data formatting. No separate AI API calls are made from scripts — Claude Code does all analysis, reasoning, and synthesis directly.

The result: a system that researches prospects before you call, generates a personalized call script, records what happened, coaches you on mistakes, and evolves the script over time based on real call data.

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        OPERATOR                                  │
│         Reads Obsidian vault · Makes calls · Drops files        │
└───────────────────┬─────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Claude Code (Intelligence Engine)              │
│   Runs slash commands · Analyzes transcripts · Writes wiki      │
└───────────────────┬─────────────────────────────────────────────┘
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
┌──────────────────┐  ┌──────────────────────────────────────────┐
│  Obsidian (UI)   │  │           Python Scripts (I/O Arms)       │
│  wiki/*.md       │  │  call_intelligence_engine.py              │
│  Graph view      │  │  research_engine.py        (M2)           │
│  Pipeline kanban │  │  lead_engine.py             (M2)          │
│  Daily briefings │  │  qualification_engine.py    (M3)          │
└──────────────────┘  │  personalization_engine.py  (M3)          │
                      │  coaching_engine.py          (M4)          │
                      │  learning_engine.py          (M4)          │
                      │  audio_to_transcript.py      (M4)          │
                      │  email_engine.py             (M4)          │
                      └──────────────────────────────────────────┘
```

---

## The Outreach Loop

```
① /daily-brief          → Prioritized call sheet: who to call, in what order
② /prep-call [company]  → Intel card + personalized human script, ready in 90 seconds
③ Operator makes call   → Records audio
④ Drop audio/transcript → sources/calls/
⑤ /analyze-call         → Wiki updated: contact, company, objections, coaching flags
⑥ /roast-me             → Brutal coaching report with exact quotes
⑦ /write-email [company]→ Email written + Gmail draft created — operator approves, clicks Send
⑧ Loop repeats          → Script evolves, playbook grows, next call is smarter
```

Each loop iteration compounds. Call 50 is statistically better than call 1 because every objection, winning phrase, and close attempt gets absorbed into the system.

---

## Command Suite

| Command | What it does |
|---------|-------------|
| `/analyze-call [file\|all]` | Read transcript → extract all calls → write wiki entries → surface coaching flags |
| `/roast-me [file\|all\|last-N]` | Brutal post-call coaching — cites exact quotes, no softening |
| `/prep-call [company]` | Full intel card + personalized human script before you dial |
| `/write-email [company] [type]` | Cold or follow-up email — 120 words max, sounds human |
| `/write-proposal [company]` | Scoped proposal with ROI framing — 600 words max |
| `/build-sequence [company]` | 5-touchpoint 8-day outreach sequence, every word written |
| `/write-linkedin [company] [type]` | Connection request or DM that passes the "is this a bot?" test |
| `/daily-brief` | Morning call sheet — ranked by priority, flagged, with openers |
| `/pipeline-report` | Revenue snapshot + deal health audit + leakage analysis |
| `/competitor-intel [niche]` | Battle cards per niche + differentiation statement |
| `/build-case-study [company]` | One-liner + email + full version from a closed client |

---

## Project Structure

```
outbound-os/
│
├── .claude/
│   └── commands/           # Slash command skill files (loaded by Claude Code)
│       ├── analyze-call.md
│       ├── prep-call.md
│       ├── roast-me.md
│       ├── write-email.md
│       ├── write-proposal.md
│       ├── build-sequence.md
│       ├── write-linkedin.md
│       ├── daily-brief.md
│       ├── pipeline-report.md
│       ├── competitor-intel.md
│       └── build-case-study.md
│
├── config/
│   ├── active_niche.yaml   # Change this to rotate verticals
│   └── niches/             # One config per target vertical
│       ├── saas_startups.yaml
│       ├── doctors.yaml
│       ├── marketing_agencies.yaml
│       ├── law_firms.yaml
│       └── florists.yaml
│
├── scripts/
│   ├── lib/                # Shared libraries — import from here, never duplicate
│   │   ├── schemas.py      # Pydantic v2 data models — single source of truth
│   │   ├── vault.py        # Only writer to wiki/ — atomic, merge-safe
│   │   ├── logger.py       # Structured JSON logging to logs/
│   │   └── utils.py        # Path constants, manifest R/W, env loader
│   └── engines/
│       ├── call_intelligence_engine.py   # ✅ M1 — transcript analysis
│       ├── research_engine.py            # ✅ M2 — website + social enrichment
│       ├── lead_engine.py                # ✅ M2 — Google Maps scraper
│       ├── qualification_engine.py       # ✅ M3 — lead scoring
│       ├── personalization_engine.py     # ✅ M3 — intel card generation
│       ├── coaching_engine.py            # ✅ M4 — cross-call pattern analysis
│       ├── learning_engine.py            # ✅ M4 — script evolution
│       ├── daily_brief_engine.py        # ✅ M4 — prioritized call sheet
│       └── email_engine.py              # ✅ M4 — Gmail draft creator
│
├── wiki/                   # AI-maintained. Claude Code writes. Operator reads.
│   ├── contacts/           # One .md per person contacted
│   ├── companies/          # One .md per business
│   ├── objections/
│   │   └── playbook.md     # Living objection playbook — self-updating
│   ├── scripts/
│   │   └── master_script.md # Self-updating call script
│   ├── coaching/
│   │   └── latest_roast.md # Most recent coaching report
│   └── examples/           # Study material — not live prospects
│
├── sources/                # Raw inputs — never edit these (gitignored)
│   ├── calls/              # Call transcripts (.txt)
│   └── prospects/          # Scraped lead data (.jsonl), intel cards
│
├── drafts/                 # Email drafts — operator reviews before sending (gitignored)
├── daily/                  # Daily call briefs — generated each morning
├── logs/                   # Structured engine logs (gitignored)
│
├── CLAUDE.md               # Agent operating instructions for Claude Code
├── ME.md                   # Operator profile — loaded for coaching + personalization
├── .env                    # API keys (gitignored — never committed)
├── credentials.json        # Gmail OAuth2 credentials (gitignored — see Email Funnel Setup)
└── yt_transcript.py        # YouTube transcript fetcher (free, no API cost)
```

---

## Setup

### Prerequisites

```
Python 3.13+
Claude Code CLI
Obsidian (for wiki browsing)
```

### Install dependencies

```bash
pip install pydantic pyyaml filelock python-dotenv rich tenacity aiohttp beautifulsoup4 youtube-transcript-api
```

### Configure environment

```bash
cp .env.example .env
# Add your OpenAI API key (used for Whisper audio transcription — M4 only)
# OPENAI_API_KEY=sk-...
```

### Open the vault in Obsidian

Point Obsidian to the `wiki/` folder as a vault. Enable the **Dataview** community plugin for pipeline queries.

### Verify setup

Drop a call transcript `.txt` file into `sources/calls/` and run:

```
/analyze-call
```

The system should write entries to `wiki/contacts/`, `wiki/companies/`, and `wiki/objections/playbook.md`.

---

## Configuration

### Rotating niches

Edit one line in `config/active_niche.yaml`:

```yaml
active_niche: doctors  # saas_startups | doctors | marketing_agencies | law_firms | florists
```

All engines pick up the active niche automatically. Niche configs live in `config/niches/` — each one defines pain signals, scoring dimensions, opener templates, and known objections for that vertical.

### Operator profile

Fill in `ME.md` with your offer, pricing, voice, and known weaknesses. This file is loaded by `/prep-call` and `/roast-me` to calibrate scripts and coaching to your specific situation. Keep it under 400 words — it's loaded per-command, not globally.

### Adding a new niche

Copy any existing niche config and edit the fields:

```bash
cp config/niches/doctors.yaml config/niches/accountants.yaml
# Edit: niche, display_name, pain_angle, search_queries, pain_signals, dimensions, openers, known_objections
```

---

## Email Funnel Setup

The email funnel writes a personalized cold email and pushes it to Gmail as a draft. You review it in Gmail and click Send. Nothing is ever sent automatically.

### One-time Gmail configuration

**Step 1** — Go to [console.cloud.google.com](https://console.cloud.google.com)

**Step 2** — Create a project (or select an existing one)

**Step 3** — Enable the Gmail API:
- APIs & Services -> Enable APIs -> search "Gmail API" -> Enable

**Step 4** — Create OAuth credentials:
- APIs & Services -> Credentials -> Create Credentials -> OAuth 2.0 Client ID
- Application type: **Desktop App**
- Download the JSON file

**Step 5** — Save the file as `credentials.json` in the vault root (same folder as CLAUDE.md)

**Step 6** — First run opens a browser tab for authorization. Approve once. A token is saved to `.gmail_token.json` — you never need to authorize again.

Both `credentials.json` and `.gmail_token.json` are gitignored and never leave your machine.

### How it works

When you run `/write-email [company]`:

1. Claude Code reads company wiki + ME.md and writes the email
2. `email_engine.py` creates a Gmail draft automatically
3. A markdown copy is saved to `drafts/<company>_<date>_<type>.md` for review in Obsidian
4. The terminal shows a direct link to the Gmail draft
5. You open it, review, and click Send

If Gmail is not configured, the markdown draft is still saved — no email is lost.

### Skip Gmail (markdown-only mode)

If you don't want Gmail integration, simply don't create `credentials.json`. The engine detects its absence and saves the draft locally. You can copy-paste from `drafts/` into any email client.

---

## Data Model

All data models are defined once in `scripts/lib/schemas.py` (Pydantic v2). Every engine imports from here. Changing a field in schemas propagates everywhere — no duplication.

Key models: `RawProspect`, `EnrichedProspect`, `LeadScoreCard`, `CallAnalysis`, `ObjectionInstance`, `CoachingFlag`, `CoachingReport`, `EmailDraft`.

---

## Vault Write Safety

All writes to `wiki/` go through `scripts/lib/vault.py`. It implements:

- **Atomic writes** — write to `.tmp`, then `os.replace()` — no partial file corruption
- **File locking** — `filelock` prevents collisions if multiple engines run concurrently
- **Merge, never overwrite** — existing call history rows are always preserved; new rows are appended
- **YAML frontmatter parsing** — Obsidian-compatible frontmatter is read, updated, and re-rendered

Direct file writes to `wiki/` from outside `vault.py` are a bug.

---

## Milestones

| Milestone | Status | What it unlocks |
|-----------|--------|----------------|
| **M0** — Foundation | ✅ Done | Vault structure, CLAUDE.md, yt_transcript.py |
| **M1** — Intelligence Loop | ✅ Done | analyze-call, roast-me, prep-call + all writing commands |
| **M2** — Lead Engine | ✅ Done | Google Maps scraper, website + social enrichment, 50 leads in < 5 min |
| **M3** — Qualification | ✅ Done | Lead scoring, personalization engine, intel cards from real scraped data |
| **M4** — Full Automation | ✅ Done | Audio transcription, coaching engine, learning engine, daily brief engine |

---

## Principles

**Sources are immutable.** Never edit files in `sources/`. They are the ground truth. The entire `wiki/` can be regenerated from `sources/` by re-running the engines. If the vault is ever corrupted, `sources/` is the recovery point.

**Claude Code is the brain.** Python scripts handle I/O only — reading files, writing files, formatting output, managing manifests. All analysis, synthesis, and reasoning is done by Claude Code directly. No LLM API calls from scripts.

**Schema is the contract.** `scripts/lib/schemas.py` is the single source of truth for every data shape in the system. Never define a data model outside of it.

**One niche at a time.** The `active_niche.yaml` file controls which niche the entire system is calibrated for. All scoring weights, pain signals, openers, and objection reframes are niche-specific. Rotate weekly.

---

## License

Private repository. Not licensed for redistribution.
