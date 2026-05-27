---
sensitivity: public
entity_type: domain
name: Hephzibah OS Brain — Context Document
last_updated: 2026-05-27
---

# Load This First

You are the intelligence engine of **Hephzibah OS** — an AI-maintained multi-domain knowledge OS built and operated by Emmanuel Adekoya Hephzibah Ifeoluwa (alias: `m1r4g3-code`, `mirage`). This document is your orientation. Read it once. The rest of the brain compounds from here.

---

## The Operator

**Emmanuel Adekoya Hephzibah Ifeoluwa**
- Lagos-native, 20s. Builds AI agents, n8n automation workflows, full-stack web apps.
- Sells done-for-you AI automation and engineering services to Western businesses via cold calling.
- Price point: ~$2,000–$5,000 per engagement (exact rates in `me/goals.md`, sensitivity: sensitive).
- GitHub: `m1r4g3-code`. Git email: `adekoyaemmanuel15@gmail.com`. Always use these for any git operations.
- Platforms: Contra (primary), LinkedIn, GitHub, Fiverr.
- Inner circle: Cyrus (strategic thinking partner), Oba, Yemi (gadget/tech).
- Spiritual identity: "Hephzibah Ifeoluwa" — "my delight is in her / God's will."

**Core beliefs (encoded as concept nodes):**
- [[builds-before-asking]] — show up with proof before being hired. Research → identify pain → build demo → call.
- [[specificity-as-credibility]] — generic pitches fail. The more specific the insight, the more trust it generates.
- [[pain-before-pitch]] — diagnose before prescribing. Never jump to the offer.
- [[challenger-reframe]] — don't agree with the prospect's framing. Reframe toward urgency.
- [[geographic-edge]] — Lagos-native context is a permanent moat for West African markets.
- [[compound-discipline]] — consistency compounds. No shortcuts.
- [[financial-fragility]] — under cash pressure, decisions distort. Build a buffer. The lesson is structural, not personal.
- [[middleman-lesson]] — never work without a signed contract and 50% deposit. Trust without contract is exposure.

---

## The OS Architecture

```
hephzibah-OS/              ← private GitHub repo (m1r4g3-code/hephzibah-os)
  wiki/                    ← the brain (Obsidian vault, Karpathy pattern)
    _CONTEXT.md            ← this file — load first
    me/                    ← identity hub
    concepts/              ← atomic concept nodes
    outreach/              ← cold outreach intelligence (active domain)
    content/               ← content strategy (scaffold)
    learning/              ← course notes, books (scaffold)
    startup/               ← product/SaaS research (scaffold)
    clients/               ← active + closed clients (scaffold)
    disciplines/           ← fitness, spiritual, habits (scaffold)
  sources/                 ← raw inputs (immutable — never edit)
  scripts/                 ← Python engines + CLI
  config/                  ← per-domain config (active_niche.yaml, etc.)
  CLAUDE.md                ← full agent instructions
  ME.md                    ← operator profile (load for coaching + personalization)
```

**Claude Code is the engine. Scripts are mechanical arms.**
Claude Code handles all analysis, synthesis, reasoning. Python handles I/O, file writes, data formatting.

---

## The Brain — Two Repos

The `wiki/` folder lives in two places simultaneously:

| Repo | Visibility | Contents | Who uses it |
|---|---|---|---|
| [`hephzibah-brain`](https://github.com/m1r4g3-code/hephzibah-brain) | Private | Full brain — all nodes including private/sensitive | Trusted OS instances, Emmanuel's own agents |
| [`hephzibah-brain-public`](https://github.com/m1r4g3-code/hephzibah-brain-public) | Public | `sensitivity: public` nodes only | External agents, anonymous collaborators |

**Sensitivity tiers:**
- `public` — concepts, tools, methods, platforms, index files. Safe for any agent.
- `private` — outreach companies, contacts, sales scripts, coaching notes. Trusted agents only.
- `sensitive` — identity, financial goals, inner circle contacts. Full brain only.

**Sharing the brain with a new OS project:**

```bash
# Clone full brain (trusted agent)
git clone https://github.com/m1r4g3-code/hephzibah-brain.git wiki

# OR clone public brain (external agent)
git clone https://github.com/m1r4g3-code/hephzibah-brain-public.git wiki
```

Once cloned, the new project writes new memory nodes to `wiki/`, commits, and pushes back. The brain grows bidirectionally.

---

## The Typed Knowledge Graph

Every node has a structured entity schema:

```yaml
---
sensitivity: public|private|sensitive
entity_type: person|company|tool|concept|platform|skill|place|domain
name: ""
aliases: []
relationships:
  - target: "[[node-slug]]"
    type: uses|built|knows|works_at|sells_to|pain_signal|identity_on|embodies|reinforces|part_of|competes_with|opposes|teaches|mentioned_in
    strength: 1-10
    first_seen: "YYYY-MM-DD"
    last_reinforced: "YYYY-MM-DD"
---
```

**Relationship types:**

| Type | Meaning |
|---|---|
| `uses` | actively uses a tool/platform |
| `built` | created something |
| `knows` | personal relationship |
| `works_at` | person at company |
| `sells_to` | targets this niche |
| `competes_with` | competitor relationship |
| `pain_signal` | company has this documented pain |
| `identity_on` | has presence on platform |
| `part_of` | belongs to category/group |
| `embodies` | demonstrates/lives this concept |
| `reinforces` | strengthens another concept |
| `opposes` | resists/contradicts |
| `teaches` | learning from |
| `mentioned_in` | referenced (weak, default) |

**Strength 1–10:** increments each time the relationship appears in a new source. 9–10 = defining. 1–2 = inferred once.

**Bidirectional auto-wiring:** when the graph engine writes A→B, it also writes the inverse B→A automatically via `INVERSE_TYPE` map in `scripts/modules/brain/graph_engine.py`.

**Obsidian graph view:** driven by `[[wikilinks]]` in body text — NOT by YAML frontmatter. Always put wikilinks in the body.

---

## Active Domain — Cold Outreach (AI Automation Sales)

**Offer:** Done-for-you AI automation + engineering. AI agents, n8n workflows, full-stack web apps.

**Channels:** Cold calling primary. Cold email secondary.

**Niche rotation (weekly):** doctors → SaaS startups → marketing agencies → law firms → florists.
Current active niche: see `config/outreach/active_niche.yaml`.

**Pipeline stages:** cold → attempted → contacted → nurturing → booked → closed → dead.

**Call flow:** pain-before-pitch → challenger-reframe → specificity-as-credibility → close with date+time.

**Key coaching flags to always catch:**
- `let_go_moment` — showed interest but caller accepted soft no
- `close_vague` — ended without specific date+time confirmed
- `over_explained` — dumped full service when one sentence needed
- `lost_frame` — let prospect control pacing
- `pitch_rushed` — jumped to offer before establishing context

---

## Custom Commands

| Command | What happens |
|---|---|
| `/analyze-call [file]` | Read transcript → extract all calls → write wiki → show coaching flags |
| `/roast-me [file\|all\|last-N]` | Brutal coaching report with exact quote citations |
| `/prep-call [company]` | Intel card — company wiki + playbook + operator context |
| `/score-lead [company\|--batch]` | Score lead, update frontmatter |
| `/update-vault` | Process all new sources/ files → update wiki |
| `/daily-brief` | Prioritized call sheet from pipeline + leads |

---

## Graph Engine Commands

```bash
# Extract entities + relationships from any text
python scripts/modules/brain/graph_engine.py --text "raw text here"

# Enrich an existing node by slug
python scripts/modules/brain/graph_engine.py --enrich identity

# Run migration scripts
python scripts/migrate_to_graph.py        # add entity schema to all nodes
python scripts/migrate_sensitivity.py     # add sensitivity tiers to all nodes
python scripts/push_public.py             # push public nodes to brain-public repo
```

---

## Brain Sync Commands

```bash
# Push wiki/ to hephzibah-brain (full, private)
git subtree push --prefix=wiki brain main

# Pull new memory from hephzibah-brain
git subtree pull --prefix=wiki brain main --squash

# Push filtered public nodes to hephzibah-brain-public
python scripts/push_public.py
```

---

## Key Node Index

**Operator:** `[[identity]]` (me/identity.md) — central hub, 24+ typed relationships

**Inner circle:** `[[cyrus]]` · `[[oba]]` · `[[yemi]]`

**Tools used:** `[[n8n]]` · `[[claude-api]]` · `[[heygen]]`

**Platforms:** `[[github]]` · `[[contra]]` · `[[linkedin]]` · `[[fiverr]]`

**Key concepts:** `[[builds-before-asking]]` · `[[specificity-as-credibility]]` · `[[pain-before-pitch]]` · `[[challenger-reframe]]` · `[[geographic-edge]]` · `[[compound-discipline]]` · `[[financial-fragility]]` · `[[middleman-lesson]]` · `[[4-workflows-4-days]]`

**Active outreach domain:** `[[cold-outreach]]` · `[[doctor-admin-pain]]` · `[[social-proof-gap]]`

**OS itself:** `[[hephzibah-os]]` · `[[lagos]]`

---

## Rules for Any Agent Writing to This Brain

1. **Pull before push.** Always. Never overwrite without syncing first.
2. **Never delete existing nodes or relationships.** Append only. Increment strength.
3. **Always add `sensitivity` to new nodes.** Default to `private` when unsure.
4. **Wikilinks go in the body, not just frontmatter.** Obsidian graph needs them.
5. **Bidirectional.** Write A→B, then write B→A with inverse type.
6. **Commit message format:** `domain: action — detail` (e.g., `outreach: add balcones-psychiatry — stage cold`)
7. **New entity nodes go in:** `wiki/concepts/` (tools, concepts, places), `wiki/outreach/contacts/` (people), `wiki/outreach/companies/` (companies).
