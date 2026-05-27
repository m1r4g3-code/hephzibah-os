---
sensitivity: public
---

# hephzibah-brain

> **New here?** Read [`_CONTEXT.md`](_CONTEXT.md) first. One file. Full picture.

The shared memory layer for every OS I build.

Not documentation. A living knowledge graph — an Obsidian vault maintained by AI, growing with every call made, every lesson extracted, every concept wired. Built on Karpathy's LLM wiki pattern.

The problem it solves: every AI OS I build should already know who I am, what I've shipped, what I've learned. Without me re-explaining from scratch. This repo is that shared context. Clone it in any project and the AI has full memory.

---

## How it fits

Each OS is a mech suit. The AI engine inside reads and writes to this brain. When one OS learns something — a sharper objection response, a new concept node, a coaching pattern that works — it pushes that node here. Every OS that pulls gets smarter from work it didn't do itself.

```
hephzibah-OS/wiki/ ←→ git subtree ←→ hephzibah-brain (this repo) ←→ git clone/push ←→ OS-2, OS-3...
```

One brain. Multiple suits. All converging.

---

## Structure

```
me/                     identity layer
  identity.md           full story, inner circle, personal rules
  brand.md              positioning, voice, real strengths
  goals.md              financial, physical, spiritual targets
  startup.md            webapp vision, name shortlist
  platforms/            github.md, contra.md, linkedin.md

concepts/               atomic concept nodes — wired across all domains
                        one file per named concept, wikilinked everywhere it appears

outreach/               cold outreach intelligence
  companies/            one .md per business — stage, call history, pain signals
  contacts/             one .md per person — objections, rapport notes, follow-up
  objections/
    playbook.md         living objection playbook, ranked by frequency, auto-updated
  scripts/
    master_script.md    self-updating call script, rebuilt after every learning cycle
  coaching/
    latest_roast.md     most recent coaching report — exact quotes, no softening
  examples/             study material, not live prospects

content/                brand content notes
learning/               book highlights, course notes, extracted lessons
startup/                product research, competitor docs
clients/                active and closed client notes
disciplines/            fitness, spiritual, habits
```

---

## Two repos — one brain

The brain ships in two versions:

| Repo | Visibility | Contents |
|---|---|---|
| [`hephzibah-brain`](https://github.com/m1r4g3-code/hephzibah-brain) | **Private** | Full brain — all nodes. Trusted OS instances only. |
| [`hephzibah-brain-public`](https://github.com/m1r4g3-code/hephzibah-brain-public) | **Public** | `sensitivity: public` nodes only. Safe for external agents. |

Every wiki node has a `sensitivity` field in its frontmatter:
- `public` — concepts, tools, methods, platforms. Any agent can read this.
- `private` — outreach companies, contacts, sales scripts, coaching notes. Trusted only.
- `sensitive` — identity, financial goals, inner circle. Full brain only.

**After adding new nodes, sync the public brain:**
```bash
python scripts/push_public.py
```

---

## hephzibah-OS — the home OS

`wiki/` inside `hephzibah-OS` is linked here via git subtree. Files live there locally. Two commands keep them in sync.

**After committing new wiki nodes in hephzibah-OS, push to brain:**
```bash
git subtree push --prefix=wiki brain main
```

**Pull memory nodes written by other OS projects into wiki/:**
```bash
git subtree pull --prefix=wiki brain main --squash
```

Run these after every significant session. Don't let the brain drift from what's on disk.

**First-time setup in hephzibah-OS** (already done — for reference):
```bash
git remote add brain https://github.com/m1r4g3-code/hephzibah-brain.git
```

---

## Starting a new OS project

Choose your access level:

**Full brain (trusted agent):**
```bash
git clone https://github.com/m1r4g3-code/hephzibah-brain.git wiki
```

**Public brain (external agent):**
```bash
git clone https://github.com/m1r4g3-code/hephzibah-brain-public.git wiki
```

**First thing after cloning — load context:**
```
Read wiki/_CONTEXT.md
```

The cloned root IS the brain. Point Obsidian here. Your AI reads from these files directly.

When the AI writes new memory nodes, commit and push back:
```bash
git pull origin main        # always pull first
git add .
git commit -m "brain: add concepts/new-concept-name"
git push origin main
```

That node is now in the shared brain. Next time hephzibah-OS runs a subtree pull, it lands in `wiki/`.

---

## Rules

**Pull before every push.**
Two OS projects can write to the same domain simultaneously. Conflicts happen. Pull first, every time.

```bash
git pull origin main
```

**Never delete existing nodes.**
Call history, concept definitions, old coaching reports — they're part of the permanent record. The brain only grows. Append, never replace.

**Call history rows are immutable.**
Every row in a contact's call history table stays. Add new rows at the bottom. Never edit past entries.

**Raw source data stays in the OS repo.**
Transcripts, scraped JSONL, API keys, engine logs — none of that belongs here. Only synthesized wiki nodes. If it's a raw input, it goes in `sources/` inside the OS. If it's extracted intelligence, it goes here.

**Commit message format:**
```
brain: add [what you added]
brain: update [what you updated]
brain: merge [domain] from [project]
```

Examples:
```
brain: add concepts/social-proof-gap
brain: update outreach/companies/zamora-medical-center stage booked
brain: merge outreach nodes from sales-os-v2
brain: add me/goals — Q3 targets
```

---

## Full command reference

| Scenario | Command |
|---|---|
| hephzibah-OS → push wiki to full brain | `git subtree push --prefix=wiki brain main` |
| hephzibah-OS → pull full brain into wiki | `git subtree pull --prefix=wiki brain main --squash` |
| hephzibah-OS → push filtered public nodes | `python scripts/push_public.py` |
| New OS → clone full brain (trusted) | `git clone https://github.com/m1r4g3-code/hephzibah-brain.git wiki` |
| New OS → clone public brain (external) | `git clone https://github.com/m1r4g3-code/hephzibah-brain-public.git wiki` |
| Any OS → pull latest before writing | `git pull origin main` |
| Any OS → push new node | `git add . && git commit -m "brain: add [node]" && git push origin main` |
| hephzibah-OS → verify remotes | `git remote -v` |
| Any OS → check what changed in brain | `git log --oneline origin/main` |

---

## What lives here vs. what doesn't

| Belongs here | Doesn't belong here |
|---|---|
| Synthesized contact/company notes | Raw call transcripts |
| Objection playbook entries | Scraped prospect JSONL |
| Concept nodes | Engine logs |
| Coaching reports | API keys or .env files |
| Identity, brand, goals | In-progress drafts |
| Daily brief outputs | Python scripts or engines |

---

Built by [m1r4g3-code](https://github.com/m1r4g3-code).
