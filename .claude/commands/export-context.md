# SKILL: export-context
# Invocation: /export-context
# Mission: Regenerate the portable brain state files in context/ from the current wiki.
# Use this after updating wiki/me/, wiki/concepts/, or ME.md so the shared context stays current.

Run the export script:

```
python scripts/export_context.py
```

Then confirm:
- `context/os_context.md` — full brain state (load in other Claude Code projects)
- `context/system_prompt.txt` — compact version (paste into any AI system prompt)

Tell the operator:
1. What changed since the last export (check git diff context/ for changes)
2. How to wire the context into a new project (one-line CLAUDE.md instruction)
3. Whether any concept nodes or identity files look stale and need updating
