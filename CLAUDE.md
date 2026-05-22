# Cold Outreach Brain — Agent Instructions

This is an LLM-maintained knowledge vault following the Karpathy LLM Wiki pattern.
The operator drops raw files into `sources/`. Claude Code reads, synthesizes, and maintains `wiki/`.
The operator browses. Claude Code writes.

Claude Code IS the intelligence engine. Python scripts are mechanical arms — they handle
I/O, file writes, data formatting. Claude Code handles all analysis, reasoning, and synthesis.

---

## Vault Layout

```
sources/           ← RAW INPUTS. Never edit these.
  calls/           ← call transcripts (.txt)
  prospects/       ← scraped lead data (.jsonl), intel cards
  research/        ← industry research, competitor analysis

wiki/              ← AI-MAINTAINED. Synthesized from sources.
  contacts/        ← one .md per person
  companies/       ← one .md per business
  objections/
    playbook.md    ← living objection playbook, ranked by frequency
  scripts/
    master_script.md   ← self-updating call script
  coaching/
    latest_roast.md    ← most recent coaching report

scripts/           ← Python engines (I/O only, Claude Code is the brain)
  lib/
    schemas.py     ← Pydantic models, single source of truth
    vault.py       ← Only writer to wiki/ (atomic, merge-safe)
    logger.py      ← Structured JSON logs to logs/
    utils.py       ← Path helpers, manifest R/W, env loader
  engines/
    call_intelligence_engine.py
    research_engine.py (M2)
    lead_engine.py (M2)
    qualification_engine.py (M3)
    personalization_engine.py (M3)
    coaching_engine.py (M4)
    learning_engine.py (M4)
    daily_brief_engine.py (M4)
  audio_to_transcript.py (M4)

config/
  scoring_rules.yaml    ← niche-specific lead scoring (M2, BLOCKED until niche confirmed)
  selectors.yaml        ← Google Maps CSS selectors (update when DOM changes)

pipeline/
  pipeline.md           ← deal stage kanban

daily/                  ← daily call logs + briefing cards

ME.md                   ← operator profile (loaded for personalization + coaching)
.env                    ← API keys (never committed)
logs/                   ← structured JSON engine logs
```

---

## Custom Commands

| Command | What I do |
|---------|-----------|
| `/analyze-call [file]` | Read transcript → extract all calls → write wiki → show coaching flags |
| `/roast-me [file\|all\|last-N]` | Load ME.md + transcripts → brutal coaching report → write to wiki/coaching/ |
| `/prep-call [company]` | Load company wiki + playbook + ME.md → generate intel card |
| `/score-lead [company\|--batch]` | Score lead against scoring_rules.yaml → update frontmatter |
| `/update-vault` | Process all new sources/ files → update wiki → summary |
| `/daily-brief` | Read pipeline + leads → generate prioritized call sheet |

---

## Core Rules

### When a new file lands in `sources/calls/`
1. Read the full transcript.
2. Split into individual calls (one conversation = one analysis unit).
3. For each call extract: prospect name/company/phone, outcome, objections (exact quotes),
   winning phrases, rapport moments, coaching flags (exact quotes, severity), close type,
   follow-up date/action.
4. Write `wiki/contacts/<name>.md` — create or merge (never overwrite call history).
5. Write `wiki/companies/<company>.md` — create or update stage + last_contact.
6. Append new objections to `wiki/objections/playbook.md` with exact quotes.
7. Update `sources/prospects/.processed_manifest.json`.

### When `/roast-me` is invoked
1. Load `ME.md` for operator context.
2. Read all specified transcripts.
3. Produce CoachingReport — cite exact quotes for every criticism, no generic feedback.
4. Write to `wiki/coaching/latest_roast.md` and `wiki/coaching/roast_<date>.md`.
5. Never soften output. The operator explicitly requested brutal feedback.

### When a new file lands in `sources/prospects/`
1. Parse as JSONL (one RawProspect or EnrichedProspect per line).
2. Create stub `wiki/companies/<company>.md` for each prospect.
3. If enriched: populate pain signals, website signals, social signals in frontmatter.
4. Set `stage: cold` in frontmatter.

### When a new file lands in `sources/research/`
1. Extract insights relevant to the operator's niche.
2. Update `wiki/scripts/` or `wiki/objections/playbook.md` if new language is found.

### Never
- Edit anything inside `sources/`
- Invent contact details not present in source files
- Mark outcome as "booked" unless transcript explicitly confirms a date/time
- Overwrite existing call history rows — always append

---

## Contact Note Template

```markdown
---
name:
company:
phone:
website:
stage: cold
last_contact:
follow_up_date:
tags: [prospect]
---

## Pain Signals
-

## Personalized Pitch Angle
-

## Call History
| Date | Outcome | Objections | Follow-up |
|------|---------|------------|-----------|

## Notes
```

---

## Company Note Template

```markdown
---
company:
owner:
phone:
website:
google_maps_url:
city:
state:
country:
lead_score:
tier:
stage: cold
last_contact:
follow_up_date:
tags: []
---

## Summary

## Pain Signals
-

## Opportunities
-

## Red Flags
-

## Call History
| Date | Contact | Outcome | Follow-up |
|------|---------|---------|-----------|
```

---

## Objection Playbook Entry Format

```markdown
### "[exact prospect quote]"
**Category:** budget | timing | no_need | trust | competitor | other
**Frequency:** N
**Caller response quality:** folded | weak_pivot | strong_pivot | closed
**Best response:** [the actual response that worked, or the correct response if caller folded]
**Source calls:** [transcript filenames]

---
```

---

## Pipeline Stages

| Stage | Meaning |
|-------|---------|
| cold | Identified, not yet contacted |
| attempted | Called or emailed, no response |
| contacted | Spoke to them, pitch delivered |
| nurturing | Interested but not ready — follow-up set |
| booked | Appointment confirmed with specific date/time |
| closed | Paying client |
| dead | Hard no or unresponsive after 3+ attempts |

---

## Coaching Flags to Always Detect

| Flag | What it means |
|------|--------------|
| `let_go_moment` | Prospect showed interest/warmth but caller accepted soft no without any pushback |
| `filler_density` | High um/uh/like/you know count — signals nervousness |
| `close_vague` | Call ended without a specific date and time confirmed |
| `over_explained` | Caller dumped full service description when one sentence would have done |
| `lost_frame` | Caller became nervous/needy, let prospect take control of pacing |
| `pitch_rushed` | Jumped to pitch before establishing any context or curiosity |

---

## ME.md Usage

Load `ME.md` when:
- Running `/roast-me` — calibrate feedback to known weaknesses
- Running `/prep-call` — calibrate intel card to operator's voice and background hooks
- Running `/analyze-call` — flag coaching issues relative to stated goals

Do NOT auto-load ME.md on every command — token discipline.
