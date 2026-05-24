# Second Brain OS

> A multi-domain AI-maintained knowledge system. Cold outreach is one module. Every domain gets smarter over time.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square)
![Claude Code](https://img.shields.io/badge/Powered_by-Claude_Code-orange?style=flat-square)
![Status](https://img.shields.io/badge/Outreach_Module-M4_Complete-green?style=flat-square)
![Repo](https://img.shields.io/badge/Visibility-Private-red?style=flat-square)

---

## What This Is

A personal AI operating system built on two ideas:

**The Karpathy Vault Pattern** — Raw inputs live in `sources/<domain>/` and are immutable. All synthesized intelligence lives in `wiki/<domain>/`, which is AI-maintained. The operator reads. The AI writes.

**The Mech Suit Model** — Claude Code is the intelligence engine. Python scripts are mechanical arms that handle I/O, file writes, and data formatting. No separate AI API calls are made from scripts — Claude Code does all analysis, reasoning, and synthesis directly.

Cold outreach is the active module. As new domains are added — content, startup, clients, learning — they slot into the same pattern without touching anything that already works.

---

## Domain Map

| Domain | Status | What it tracks |
|--------|--------|---------------|
| `outreach` | Active (M4 complete) | Cold outreach — leads, calls, scripts, coaching, emails |
| `me` | Active | Identity, brand, goals, startup vision, platform audits |
| `concepts` | Active | Shared atomic concept nodes linked across all domains |
| `content` | Scaffold | Posts, threads, brand content, case studies |
| `learning` | Scaffold | Books, courses, skills |
| `startup` | Scaffold | Product decisions, market research, roadmap |
| `clients` | Scaffold | Active engagements, SOWs, delivery |
| `disciplines` | Scaffold | Fitness, spiritual practice, habits |

---

## Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                          OPERATOR                                  │
│         Reads Obsidian vault · Makes calls · Drops files          │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│                  Claude Code (Intelligence Engine)                 │
│    Runs slash commands · Analyzes transcripts · Writes wiki       │
└────────────────────────┬─────────────────────────────────────────┘
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
┌──────────────────┐    ┌──────────────────────────────────────────┐
│  Obsidian (UI)   │    │         Python Scripts (I/O Arms)         │
│  wiki/**/*.md    │    │  scripts/modules/outreach/*.py            │
│  Graph view      │    │  scripts/lib/ (shared)                    │
│  Pipeline kanban │    └──────────────────────────────────────────┘
└──────────────────┘
```

### Domain-Driven Directory Pattern

Every domain follows the same convention:

```
sources/<domain>/         ← immutable raw inputs
wiki/<domain>/            ← AI-maintained synthesized outputs
scripts/modules/<domain>/ ← engines specific to that domain
config/<domain>/          ← config for that domain
```

Shared above all domains:
- `wiki/me/` — operator identity hub
- `wiki/concepts/` — atomic concept nodes wired across domains
- `scripts/lib/` — schemas, vault writer, logger, utils

---

## Outreach Module — The Intelligence Loop

```
① /daily-brief          → Prioritized call sheet: who to call, in what order
② /prep-call [company]  → Intel card + personalized human script, ready in 90 seconds
③ Operator makes call   → Records audio
④ Drop audio/transcript → sources/outreach/calls/
⑤ /analyze-call         → Wiki updated: contact, company, objections, coaching flags
⑥ /roast-me             → Brutal coaching report with exact quotes
⑦ /write-email [company]→ Email written + Gmail draft created — operator approves, clicks Send
⑧ Loop repeats          → Script evolves, playbook grows, next call is smarter
```

---

## Command Suite

| Command | Domain | What it does |
|---------|--------|-------------|
| `/analyze-call [file\|all]` | outreach | Transcript → wiki entries + coaching flags |
| `/roast-me [file\|all\|last-N]` | outreach | Brutal post-call coaching — exact quotes, no softening |
| `/prep-call [company]` | outreach | Full intel card + personalized human script |
| `/write-email [company] [type]` | outreach | Cold or follow-up email — 120 words max, sounds human |
| `/write-proposal [company]` | me | Scoped proposal with ROI framing |
| `/build-sequence [company]` | outreach | 5-touchpoint 8-day outreach sequence |
| `/write-linkedin [company] [type]` | me | Connection request or DM |
| `/daily-brief` | outreach | Morning call sheet — ranked by priority |
| `/pipeline-report` | outreach | Revenue snapshot + deal health audit |
| `/competitor-intel [niche]` | outreach | Battle cards per niche |
| `/build-case-study [company]` | me | One-liner + email + full version from closed client |

---

## Project Structure

```
Second Brain OS/
│
├── wiki/
│   ├── me/                    # Identity hub — above all domains
│   │   ├── identity.md
│   │   ├── brand.md
│   │   ├── goals.md
│   │   ├── startup.md
│   │   └── platforms/
│   ├── concepts/              # Shared atomic concept nodes
│   ├── outreach/              # Cold outreach (active domain)
│   │   ├── companies/         # One .md per business
│   │   ├── contacts/          # One .md per person
│   │   ├── objections/
│   │   │   └── playbook.md    # Living objection playbook
│   │   ├── scripts/
│   │   │   └── master_script.md
│   │   ├── coaching/
│   │   └── examples/
│   ├── content/               # Scaffold
│   ├── learning/              # Scaffold
│   ├── startup/               # Scaffold
│   ├── clients/               # Scaffold
│   └── disciplines/           # Scaffold
│
├── sources/
│   ├── outreach/
│   │   ├── calls/             # Call transcripts (.txt)
│   │   ├── prospects/         # Scraped lead data (.jsonl), intel cards
│   │   └── research/
│   ├── content/               # Scaffold
│   ├── learning/              # Scaffold
│   └── startup/               # Scaffold
│
├── scripts/
│   ├── lib/                   # Shared libraries — import from here
│   │   ├── schemas.py         # Pydantic v2 data models
│   │   ├── vault.py           # Only writer to wiki/
│   │   ├── logger.py          # Structured JSON logging
│   │   └── utils.py           # DOMAIN_PATHS, manifest R/W, env loader
│   └── modules/
│       └── outreach/          # Outreach domain engines
│           ├── call_intelligence_engine.py
│           ├── research_engine.py
│           ├── lead_engine.py
│           ├── qualification_engine.py
│           ├── personalization_engine.py
│           ├── coaching_engine.py
│           ├── learning_engine.py
│           ├── daily_brief_engine.py
│           └── email_engine.py
│
├── config/
│   └── outreach/
│       ├── active_niche.yaml  # Change this to rotate verticals
│       ├── selectors.yaml     # Google Maps CSS selectors
│       └── niches/            # One config per vertical
│
├── .claude/
│   └── commands/              # Slash command skill files
│
├── pipeline/
├── daily/
├── logs/
│
├── CLAUDE.md                  # Agent operating instructions
├── ME.md                      # Operator profile
└── .env                       # API keys (gitignored)
```

---

## Setup

### Prerequisites

```
Python 3.13+
Claude Code CLI
Obsidian (for wiki browsing — point vault at the repo root)
```

### Install dependencies

```bash
pip install pydantic pyyaml filelock python-dotenv rich tenacity aiohttp beautifulsoup4 youtube-transcript-api
```

### Configure environment

```bash
cp .env.example .env
# Add your OpenAI API key for Whisper audio transcription
# OPENAI_API_KEY=sk-...
```

### Open in Obsidian

Point Obsidian at the repo root as the vault. Enable the **Dataview** community plugin for pipeline queries. The graph view will show the full concept network across all domains.

### Verify setup

Drop a call transcript `.txt` into `sources/outreach/calls/` and run:

```
/analyze-call
```

Entries appear in `wiki/outreach/contacts/`, `wiki/outreach/companies/`, and `wiki/outreach/objections/playbook.md`.

---

## Configuration

### Rotating niches

Edit one line in `config/outreach/active_niche.yaml`:

```yaml
active_niche: doctors  # saas_startups | doctors | marketing_agencies | law_firms | florists
```

### Operator profile

Fill in `ME.md` with your offer, pricing, voice, and known weaknesses. Loaded by `/prep-call` and `/roast-me`. Keep under 400 words.

### Adding a new domain

1. Create `sources/<domain>/` and `wiki/<domain>/` with a `_index.md` stub
2. Create `scripts/modules/<domain>/` for domain engines
3. Add the domain to `DOMAIN_PATHS` in `scripts/lib/utils.py`
4. Document commands in `CLAUDE.md`

---

## Email Funnel Setup

The email engine writes a personalized cold email and pushes it to Gmail as a draft. You review and click Send. Nothing is ever sent automatically.

### One-time Gmail configuration

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a project → Enable the Gmail API
3. Create OAuth 2.0 credentials (Desktop App) → download as `credentials.json`
4. Place `credentials.json` in vault root
5. First run opens browser for authorization → token saved to `.gmail_token.json`

Both files are gitignored and stay local.

---

## Vault Write Safety

All writes to `wiki/` go through `scripts/lib/vault.py`:

- **Atomic writes** — write to `.tmp`, then `os.replace()` — no partial corruption
- **File locking** — prevents collisions from concurrent engines
- **Merge, never overwrite** — call history rows always preserved, new rows appended
- **YAML frontmatter** — Obsidian-compatible read/update/render

Direct writes to `wiki/` outside `vault.py` are a bug.

---

## Outreach Milestones

| Milestone | Status | What it unlocks |
|-----------|--------|----------------|
| **M0** — Foundation | Done | Vault structure, CLAUDE.md, yt_transcript.py |
| **M1** — Intelligence Loop | Done | analyze-call, roast-me, prep-call + all writing commands |
| **M2** — Lead Engine | Done | Google Maps scraper, website + social enrichment |
| **M3** — Qualification | Done | Lead scoring, personalization engine, intel cards |
| **M4** — Full Automation | Done | Audio transcription, coaching engine, learning engine, daily brief |

---

## Principles

**Sources are immutable.** Never edit files in `sources/`. The entire `wiki/` can be regenerated from `sources/` by re-running the engines.

**Claude Code is the brain.** Python scripts handle I/O only. All analysis, synthesis, and reasoning is done by Claude Code.

**Schema is the contract.** `scripts/lib/schemas.py` is the single source of truth for every data shape. Never define a model outside it.

**Domain isolation.** Each domain owns its sources, wiki, engines, and config. Changing the outreach domain touches nothing in content or learning.

---

## License

Private repository. Not licensed for redistribution.
