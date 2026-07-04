---
sensitivity: private
entity_type: concept
name: OS Behavior Rules — Claude Engine Contract
last_updated: 2026-05-29
relationships:
  - target: "[[hephzibah-os]]"
    type: part_of
    strength: 10
    first_seen: "2026-05-29"
    last_reinforced: "2026-05-29"
---

# OS Behavior Rules — Claude Engine Contract

These are non-negotiable behaviors Emmanuel has explicitly set. They apply in every session without being re-stated.

---

## Rule 1: Run It, Don't Delegate It

Claude is the engine. Emmanuel is the operator. If a script exists and can be run, Claude runs it — not Emmanuel.

**Why:** Emmanuel's exact words: "u are the engine why telling me to run this, dat u should be d one to nau." Delegating runnable commands to the user breaks the OS contract.

**How to apply:**
- Script exists + can be executed → run it, show output
- Output needs saving to brain/vault → save it in the same work block
- Exception: commands that require Emmanuel's physical action (browser login, Playwright --setup opening a window). Even then — run the command, let the browser open, do not ask him to run it himself.

---

## Rule 2: Save to Vault — Not Only to Memory

Every new framework, decision, playbook addition, or insight from a conversation must be written to the brain vault (`hephzibah-brain-temp/upwork/`).

**Why:** Emmanuel's exact words: "any new thing we talk abt dont forget to always add them to vault be it from my prompt or ur message." And: "AND REMIND URSELF TO ALWAYS SAVE IN VAULT TO NOT ONLY MEMORY."

The brain is the living memory of the OS. If it is not in the vault it does not exist in the next session.

**How to apply:**
- New framework or methodology → new or updated .md node in brain
- New OS decision → append to relevant playbook or concept node
- New market insight, client type pattern, pricing decision → write to appropriate brain section
- Commit immediately after writing: `upwork: add/update [what] — [detail]`
- Do not batch saves — write to vault as part of the same work block, not at the end
- Claude memory (MEMORY.md) is NOT a substitute for vault saves
  - Memory = cross-session pointer (local to this machine only)
  - Vault = the actual content node (synced to GitHub, survives system changes)

---

## Rule 3: Memory Is Local — Vault Is Permanent

Claude memory files live at `C:\Users\HomePC\.claude\projects\...\memory\` — local machine only. They do NOT sync to new systems or different Claude accounts.

The vault (`hephzibah-brain-temp/`) is a GitHub-synced git repo. It survives machine changes, account changes, and OS reinstalls. Clone it anywhere and the full brain is back.

**How to apply:**
- Any insight worth keeping across sessions → vault first, memory pointer second
- If Emmanuel gets a new machine: `git clone` the brain repo → full context is back. Memory files would need manual copy from old machine.
- Whenever a meaningful conversation produces a reusable rule, decision, or playbook addition → vault it before the session ends.

---

## Rule 4: Profile.md Is the Source of Truth for Account State

`hephzibah-brain-temp/upwork/identity/profile.md` is the authoritative record of the active Upwork account. `qualify.py` reads it at score time.

**How to apply:**
- Profile rate changed → update `rate_usd` in profile.md
- New review received → update `total_reviews`, `total_earned_usd`
- New portfolio item added → add entry to `portfolio_items` list
- Account switches → update `account_owner`, reset/update all fields
- Do not assume profile state from memory — read the file

---

## Wikilinks

[[hephzibah-os]] · [[upwork-os]] · [[vault]] · [[profile]]
