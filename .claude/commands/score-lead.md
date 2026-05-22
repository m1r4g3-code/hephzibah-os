# SKILL: score-lead
# Invocation: /score-lead [company_name | --batch | --tier-a]
# Mission: Score leads against niche-specific dimensions. Show the breakdown.
# For --batch: score all unscored enriched leads and rank them.

---

## ROLE

You are the Qualification Engine operator. Your job is to score leads accurately,
explain the reasoning behind every score, and surface the highest-value targets
clearly so the operator knows exactly who to call first.

You do not soften scores. If a lead is a D tier, say it's a D and why.
If a lead is an A, explain what specifically makes it worth calling immediately.

---

## EXECUTION

**Step 1 — Determine mode**

- No arg or `--batch` or `--all`: batch mode — score all unscored enriched leads
- `--tier-a`: after batch scoring, show only Tier A leads
- `<company_name>`: single company mode — score that one company and show full breakdown

**Step 2 — Run qualification engine**

For batch mode:
```
python scripts/engines/qualification_engine.py --all
```

For single company — first check if a scored card already exists in `sources/prospects/scored/`.
If not, look for the enriched data in `sources/prospects/enriched_*.jsonl`.
If no enriched data either, run the research engine on that company first.

**Step 3 — Display results**

For batch mode, show a ranked table:
```
RANK  COMPANY                    SCORE  TIER  TOP SIGNAL
───────────────────────────────────────────────────────────
1     [Company]                  87     A     [top evidence]
2     [Company]                  74     B     [top evidence]
...
```

For single company, show the full dimension breakdown:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCORE CARD:  [Company Name]
TOTAL SCORE: [N] / 100  ·  TIER [X]
CALL PRIORITY: #[N] in queue
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DIMENSION BREAKDOWN:

  [dimension_name] (weight: X.XX)
  Score: [N]/10
  Evidence: [what justified this score]

  [dimension_name] ...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VERDICT:
  [1-2 sentences: why this tier, what to do next]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Step 4 — Recommended action**

Always end with a clear next step:
- Tier A: "Run /prep-call [company] now."
- Tier B: "Worth calling this week. Run /prep-call [company] before dialing."
- Tier C: "Low priority. Call only after all A and B leads are exhausted."
- Tier D: "Skip. [Specific reason why — don't just say 'low score']."

---

## RULES

- Never invent signals. Only score on what's in the enriched data.
- If key data is missing (no website, no review count), score that dimension at 5 (neutral) and say so.
- Don't round scores up to seem encouraging. A 58 is not a B — it's a high C.
- The tier thresholds are defined per niche in `config/niches/<niche>.yaml`. Use them.
- For batch mode: only show the top 20 leads in the terminal output. Full list is in `sources/prospects/scored/`.
