---
description: Analyze a call transcript and update the wiki with structured intelligence
---

Analyze the call transcript: $ARGUMENTS

**Step 1 — Locate the file**
If $ARGUMENTS is empty, use the most recently modified file in `sources/calls/`.
If $ARGUMENTS is a filename (not a full path), look in `sources/calls/<filename>`.
If $ARGUMENTS is "all", process every .txt file in `sources/calls/`.

**Step 2 — Run the engine**
```
python scripts/engines/call_intelligence_engine.py $ARGUMENTS
```
This writes `logs/_analysis_context.json` with the full transcript and split segments.

**Step 3 — Read and analyze**
Read `sources/calls/<filename>` directly. The transcript may contain multiple calls in sequence.

For EACH distinct call in the transcript, extract:
- Prospect name, company, phone
- Outcome (voicemail / hung_up / gatekeeper_blocked / interested / callback_scheduled / booked / rejected / dead)
- Every objection with the EXACT words the prospect used, the caller's response, and quality (folded / weak_pivot / strong_pivot / closed)
- Winning phrases — exact lines that kept the prospect on the call
- Rapport moments — specific moments of genuine connection
- Coaching flags — specific delivery problems, each citing an exact quote:
  - let_go_moment: prospect showed warmth/interest but caller accepted a soft no without pushing back
  - filler_density: unusually high um/uh/like/you know count
  - close_vague: call ended without confirming a specific date/time
  - over_explained: caller dumped the full pitch when one sentence would do
  - lost_frame: caller became nervous/needy and let prospect take control of the conversation
- Close attempted? If yes: specific_datetime / vague / no_attempt
- Follow-up date and action if mentioned

**Step 4 — Write to vault**
Call `write_analysis_results()` via the engine, OR write directly using vault.py functions:
- `wiki/contacts/<prospect-name>.md` — create or update with call history row
- `wiki/companies/<company-name>.md` — create or update with stage + last_contact
- `wiki/objections/playbook.md` — append each new objection

**Step 5 — Report to operator**
Print a structured summary:
1. How many calls processed, list of [company → outcome]
2. New contacts/companies added to wiki
3. Top 3 coaching flags (most severe first) with exact quotes
4. New objections added to playbook
5. Follow-ups scheduled

Be direct. Do not soften coaching flags. Cite the exact moment.

**Idempotency:** If transcript was already processed and --force was not passed, say so and skip.
