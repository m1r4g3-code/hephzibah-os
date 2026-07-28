# Hephzibah OS — Agent Instructions

This is an AI-maintained multi-domain knowledge vault following the Karpathy LLM Wiki pattern.
The operator drops raw files into `sources/<domain>/`. Claude Code reads, synthesizes, and maintains `wiki/<domain>/`.
The operator browses. Claude Code writes.

Claude Code IS the intelligence engine. Python scripts are mechanical arms — they handle
I/O, file writes, data formatting. Claude Code handles all analysis, reasoning, and synthesis.

## Shared Brain — Two Repos

`wiki/` ships as two GitHub repos with tiered access:

| Repo | Visibility | Contents |
|---|---|---|
| `hephzibah-brain` | **Private** | Full brain. Trusted OS instances only. |
| `hephzibah-brain-public` | **Public** | `sensitivity: public` nodes only. External/anonymous agents. |

**Sensitivity tiers on every wiki node:**
- `public` — concepts, tools, platforms, methods. Safe for any agent.
- `private` — outreach intel, contacts, sales scripts. Trusted only.
- `sensitive` — identity, financials, inner circle. Full brain only.

**Load context first in any new session:**
```
Read wiki/_CONTEXT.md
```

```bash
# Push wiki to full brain (after committing)
# NOT git subtree push — that permanently non-fast-forwards once the brain
# has commits from any other OS instance. Use the file-copy sync:
python scripts/push_brain.py

# Pull brain into wiki (file-copy sync, tracks last pull in .brain_last_pull)
python scripts/pull_brain.py

# Sync public-only nodes to hephzibah-brain-public
python scripts/push_public.py

# Clone full brain in a new OS project (trusted)
git clone https://github.com/m1r4g3-code/hephzibah-brain.git wiki

# Clone public brain in a new OS project (external agent)
git clone https://github.com/m1r4g3-code/hephzibah-brain-public.git wiki
```

---

## Architecture — Domain-Driven

Each life domain is self-contained under a shared namespace pattern:

```
sources/<domain>/          ← raw inputs for that domain (immutable)
wiki/<domain>/             ← AI-maintained outputs for that domain
scripts/modules/<domain>/  ← engines that serve that domain
config/<domain>/           ← config specific to that domain
```

Shared layers (above all domains):
- `wiki/me/` — identity hub: story, brand, goals, platforms, startup
- `wiki/concepts/` — atomic concept nodes linked across all domains
- `scripts/lib/` — shared Python libs used by all engines
- `ME.md` — operator profile loaded for coaching + personalization

---

## Vault Layout

```
sources/
  outreach/          <- cold outreach raw inputs
    calls/           <- call transcripts (.txt)
    prospects/       <- scraped lead data (.jsonl), intel cards
    research/        <- industry + competitor research
  content/           <- content drafts, post ideas (scaffold)
  learning/          <- course notes, book highlights (scaffold)
  startup/           <- product research, competitor docs (scaffold)

wiki/
  me/                <- identity hub (above all domains)
    identity.md      <- story, inner circle, personal rules
    brand.md         <- positioning, voice, real strengths
    goals.md         <- financial, physical, spiritual targets
    startup.md       <- webapp vision, name shortlist
    platforms/       <- github.md, contra.md, linkedin.md
  concepts/          <- shared atomic concept nodes (cross-domain)
  outreach/          <- cold outreach intelligence (active)
    companies/       <- one .md per business
    contacts/        <- one .md per person
    objections/
      playbook.md    <- living objection playbook, ranked by frequency
    scripts/
      master_script.md  <- self-updating call script
    coaching/
      latest_roast.md
    examples/        <- study material, not live prospects
  content/           <- brand content notes (scaffold)
  learning/          <- learning notes (scaffold)
  startup/           <- startup research (scaffold)
  clients/           <- active + closed client notes (scaffold)
  disciplines/       <- fitness, spiritual, habits (scaffold)

scripts/
  lib/               <- shared libraries (all domains import from here)
    schemas.py       <- Pydantic models, single source of truth
    vault.py         <- Only writer to wiki/ (atomic, merge-safe)
    logger.py        <- Structured JSON logs to logs/
    utils.py         <- DOMAIN_PATHS registry, manifest R/W, env loader
  modules/
    outreach/        <- engines for the outreach domain
      call_intelligence_engine.py
      research_engine.py
      lead_engine.py
      qualification_engine.py
      personalization_engine.py
      coaching_engine.py
      learning_engine.py
      daily_brief_engine.py
      email_engine.py

config/
  outreach/          <- outreach-specific config
    active_niche.yaml
    selectors.yaml
    niches/

pipeline/
  pipeline.md        <- deal stage kanban

daily/               <- daily call logs + briefing cards
logs/                <- structured JSON engine logs

ME.md                <- operator profile (loaded by /prep-call, /roast-me)
CLAUDE.md            <- this file
.env                 <- API keys (never committed)
```

---

## Custom Commands

| Command | Domain | What I do |
|---------|--------|-----------|
| `/analyze-call [file]` | outreach | Read transcript -> extract all calls -> write wiki -> show coaching flags |
| `/roast-me [file\|all\|last-N]` | outreach | Load ME.md + transcripts -> brutal coaching report -> write to wiki/outreach/coaching/ |
| `/prep-call [company]` | outreach | Load company wiki + playbook + ME.md -> generate intel card |
| `/score-lead [company\|--batch]` | outreach | Score lead against scoring_rules.yaml -> update frontmatter |
| `/update-vault` | outreach | Process all new sources/ files -> update wiki -> summary |
| `/daily-brief` | outreach | Read pipeline + leads -> generate prioritized call sheet |
| `/write-email [company]` | outreach | Write cold/follow-up email -> push to Gmail as draft |
| `/write-linkedin [company]` | me | LinkedIn connection request or DM |
| `/build-case-study [company]` | me | Case study from closed client |
| `/write-proposal [company]` | me | Scoped proposal with ROI framing |
| `/strategize [situation]` | me | Full move-by-move breakdown of a business/negotiation situation using all six [[strategic-frameworks]] |

---

## Strategic Reasoning — Applies Across All Domains

On any business, negotiation, pricing, or client-relationship decision — not just when `/strategize` is invoked — default to multi-step strategic thinking before recommending an action. Check who a move actually benefits and what it costs downstream before suggesting it, not after the operator has to catch it.

Six standing frameworks, each covering a blind spot the others have. Full detail in `wiki/concepts/strategic-frameworks.md` and its children:

| Framework | Covers | Node |
|---|---|---|
| Chess thinking | Sequential lookahead when the board is visible | `[[chess-thinking]]` |
| Poker under uncertainty | Acting well when the other side's real position isn't known | `[[poker-under-uncertainty]]` |
| BATNA | Knowing your own fallback before any deal conversation | `[[batna]]` |
| OODA loop | Moving faster than the other side's decision cycle | `[[ooda-loop]]` |
| Voss negotiation | What to actually say — tactical empathy, calibrated questions, labeling | `[[voss-negotiation]]` |
| Red-team inversion | Attacking your own plan before it ships, catching costly "helpful" moves | `[[red-team-inversion]]` |

Depth scales with stakes: a quick gut-check on routine questions, full explicit move/countermove sequencing (`/strategize`) when the operator asks for it directly or real money/scope/a fragile relationship is on the line. This does not apply to purely technical questions — it's a lens for business judgment, not a mandate to over-analyze everything.

### When `/strategize` is invoked
1. Load the relevant contact/company wiki note for full context (e.g. `wiki/outreach/contacts/<name>.md`)
2. Apply each of the six frameworks explicitly: current read of the position (chess), the other side's likely range of intent (poker), our own fallback (BATNA), speed/timing considerations (OODA), the actual language to use (Voss), and a self-attack pass on the recommended plan (red-team) before presenting it
3. Present as named moves/branches, not a single linear guess — flag the fork points that would change the recommendation
4. Log the resulting posture to the contact's wiki note under a "Negotiation posture" section, and to memory if it's a standing pattern likely to recur

---

## Core Rules

### When a new file lands in `sources/outreach/calls/`
1. Read the full transcript.
2. Split into individual calls (one conversation = one analysis unit).
3. For each call extract: prospect name/company/phone, outcome, objections (exact quotes),
   winning phrases, rapport moments, coaching flags (exact quotes, severity), close type,
   follow-up date/action.
4. Write `wiki/outreach/contacts/<name>.md` — create or merge (never overwrite call history).
5. Write `wiki/outreach/companies/<company>.md` — create or update stage + last_contact.
6. Append new objections to `wiki/outreach/objections/playbook.md` with exact quotes.
7. Update `sources/outreach/prospects/.processed_manifest.json`.

### When `/roast-me` is invoked
1. Load `ME.md` for operator context.
2. Read all specified transcripts from `sources/outreach/calls/`.
3. Produce CoachingReport — cite exact quotes for every criticism, no generic feedback.
4. Write to `wiki/outreach/coaching/latest_roast.md` and `wiki/outreach/coaching/roast_<date>.md`.
5. Never soften output. The operator explicitly requested brutal feedback.

### When a new file lands in `sources/outreach/prospects/`
1. Parse as JSONL (one RawProspect or EnrichedProspect per line).
2. Create stub `wiki/outreach/companies/<company>.md` for each prospect.
3. If enriched: populate pain signals, website signals, social signals in frontmatter.
4. Set `stage: cold` in frontmatter.

### When a new file lands in `sources/outreach/research/`
1. Extract insights relevant to the operator's niche.
2. Update `wiki/outreach/scripts/` or `wiki/outreach/objections/playbook.md` if new language is found.

### Never
- Edit anything inside `sources/`
- Invent contact details not present in source files
- Mark outcome as "booked" unless transcript explicitly confirms a date/time
- Overwrite existing call history rows — always append

---

## Wikilink Resolution

Obsidian resolves `[[filename]]` by scanning all `.md` files recursively — path is irrelevant.
`[[balcones-psychiatry]]` works whether the file is in `wiki/outreach/companies/` or anywhere else.
Moving files within the vault never breaks wikilinks.

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
| `filler_density` | High um/uh/like/you know count -- signals nervousness |
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

---

## Adding a New Domain

1. Create `sources/<domain>/` for raw inputs
2. Create `wiki/<domain>/` with a `_index.md` stub
3. Create `scripts/modules/<domain>/` for any domain-specific engines
4. Add the domain to `DOMAIN_PATHS` in `scripts/lib/utils.py`
5. Document the domain's custom commands in this file
