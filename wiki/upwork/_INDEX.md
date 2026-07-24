---
sensitivity: private
entity_type: domain
name: Upwork OS — Domain Index
last_updated: 2026-05-27
relationships:
  - target: "[[identity]]"
    type: part_of
    strength: 10
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
  - target: "[[hephzibah-os]]"
    type: part_of
    strength: 10
    first_seen: "2026-05-27"
    last_reinforced: "2026-05-27"
---

# Upwork OS — Domain Index

Load this after `_CONTEXT.md`. This is the orientation document for the Upwork domain.

The Upwork OS is Emmanuel's freelancing operating system. It runs on the same brain architecture as all other OS projects. Claude Code is the engine. Python scripts are the mechanical arms. This domain is the memory layer.

---

## Active Status

- **Current niche:** See `[[upwork-niche]]` (`identity/niche.md`)
- **Active proposals:** See `performance/metrics.md`
- **Connects budget:** Track in `performance/metrics.md`

---

## Domain Map

```
upwork/
├── _INDEX.md                    ← this file
├── identity/
│   ├── profile.md               ← Upwork profile: JSS, badges, bio, portfolio gaps
│   ├── niche.md                 ← active niche + rotation log
│   ├── pricing.md               ← rate philosophy, anchor points, value stack
│   ├── voice.md                 ← writing style guide + calibration notes
│   ├── skills.md                ← Emmanuel's full skill set (automation + creative — read before scoring fit)
│   └── brand.md                 ← visual identity: colors, fonts, portfolio thumbnails, SOW template
├── market/
│   ├── intelligence.md          ← running market observations log
│   ├── niches/                  ← one .md per niche dossier
│   └── patterns/
│       ├── winning-signals.md   ← patterns from proposals that got replies/wins
│       ├── red-flags.md         ← client/job anti-patterns (JSS risks)
│       └── client-archetypes.md ← named client personalities + response playbooks
├── jobs/
│   ├── _template.md             ← job card schema
│   └── archive/                 ← evaluated job cards (YYYY-MM-DD-slug.md)
├── proposals/
│   ├── _template.md             ← proposal schema
│   ├── sent/                    ← all sent proposals (append-only, outcome logged)
│   └── best/                    ← hall of fame (proposals that won or got replies)
├── clients/
│   ├── _template.md             ← client quality card
│   └── active/                  ← active/past client nodes
├── playbooks/
│   ├── account-launch.md        ← OWN ACCOUNT cold start (Day 0-30 sequence) ← READ THIS FIRST when launching
│   ├── proposal-framework.md    ← master proposal methodology (6-pass pipeline)
│   ├── loom-strategy.md         ← Loom video proposal playbook (Pass 6)
│   ├── handoff.md               ← delivery brief + contract close + JSS engineering
│   ├── discovery-call.md        ← pre-call prep, question bank, close script, red flags
│   ├── objections.md            ← Upwork-specific objection library
│   ├── client-types.md          ← client archetypes + psychology
│   ├── profile-gravity.md       ← 90-day inbound engine build (profile → invited)
│   ├── niche-dossiers.md        ← niche-specific positioning intel
│   └── conversation-flows.md   ← post-proposal Upwork chat scripts
├── performance/
│   ├── metrics.md               ← live performance log
│   └── insights.md              ← weekly pattern synthesis
└── concepts/
    ├── elite-freelancer-model.md ← Ryan Ramshaw principles encoded
    ├── job-scoring.md            ← scoring methodology
    ├── client-quality-score.md  ← client evaluation framework
    ├── proposal-anatomy.md       ← what makes proposals convert
    ├── upwork-psychology.md      ← platform buyer psychology
    └── os-behavior-rules.md      ← Claude engine contract (run things, save to vault, memory vs vault)
```

---

## The OS Principles (Short Form)

Full principles in `CLAUDE.md` at OS root. Short form:

1. Elite consultant model — not mass applier
2. Bid gate: composite score ≥ 65 required, no exceptions
3. JSS is the moat — skip ambiguous scope always
4. Diagnose before prescribing — never pitch before you understand
5. Open conversations — proposals end with a question, not a plea
6. Selectivity is positioning — skip more than you bid
7. Voice first — every proposal sounds like Emmanuel, not AI

---

## Commands Quick Reference

| Command | Use when |
|---|---|
| `/job-qualify [url]` | You have a job to evaluate |
| `/write-proposal [job-file]` | Job is qualified, score ≥ 65 |
| `/daily-brief` | Start of day |
| `/client-intel [username]` | Need to deep-check a client |
| `/roast-proposal [file]` | Reviewing a sent or drafted proposal |
| `/analyze-conversation [chat]` | Upwork message thread to analyze |
| `/prep-job [url]` | Full intel before writing (complex jobs) |
| `/prep-call [job-file]` | Before every discovery call — generates pre-call brief |
| `/log-outcome [file] [result]` | After any outcome: reply, win, ghost |
| `/quote [project]` | Generate bid assessment + SOW pricing tiers |
| `/close-contract [client] [project]` | Handoff sequence — delivery brief + contract close |
| `/niche-radar [niche]` | Market intelligence check |
| `/gap-audit` | After 3+ skips — root cause diagnosis + fix priority list |
| `/strategy-review` | Weekly — what's working, what's not |
| `/reputation-brief` | Weekly — profile, portfolio, content |

---

## Wikilinks

[[upwork-niche]] · [[upwork-voice]] · [[upwork-pricing]] · [[elite-freelancer-model]] · [[proposal-anatomy]] · [[upwork-psychology]] · [[job-scoring]] · [[client-quality-score]]
