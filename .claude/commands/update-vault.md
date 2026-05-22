# SKILL: update-vault
# Invocation: /update-vault
# Mission: Scan sources/ for everything unprocessed and run the right engine for each.
# The morning sweep — run this before /daily-brief to make sure the vault is current.

---

## EXECUTION

**Step 1 — Discover unprocessed files**

Check `.processed_manifest.json` against actual files:

```
python scripts/engines/call_intelligence_engine.py --batch
```

This identifies any transcript in `sources/calls/` not yet in the manifest.

**Step 2 — Process new transcripts**

For each unprocessed transcript found:
1. Run the call intelligence engine to load context
2. Analyze with /analyze-call logic
3. Write wiki entries (contacts, companies, objections)

**Step 3 — Process new lead files**

Scan `sources/prospects/` for:
- `leads_*.jsonl` files without a corresponding `enriched_*.jsonl` → run research_engine
- `enriched_*.jsonl` files without a corresponding `scored_*.jsonl` → run qualification_engine

```
python scripts/engines/research_engine.py --all
python scripts/engines/qualification_engine.py --all
```

**Step 4 — Run learning engine**

After any new call data is processed:
```
python scripts/engines/learning_engine.py
```

If `should_update_script` is true in the output context, read `logs/_learning_context.json`
and update `wiki/scripts/master_script.md` with evidence-based script improvements.

**Step 5 — Report**

Print a structured summary:
```
VAULT UPDATE — [timestamp]
─────────────────────────────────────────────
Transcripts processed:     [N] new
Contacts updated:          [N]
Companies updated:         [N]
Objections added:          [N]
Leads enriched:            [N]
Leads scored:              [N]
Script updated:            yes / no
─────────────────────────────────────────────
Next: /daily-brief
```

---

## RULES

- If nothing is new, say so clearly — don't pretend work was done.
- If a transcript has already been processed, skip it (check manifest).
- Never run the scraper (`lead_engine.py`) — that's operator-initiated, not vault maintenance.
- If the learning engine says `should_update_script: true`, actually update the script. Don't defer it.
