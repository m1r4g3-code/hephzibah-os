---
sensitivity: public

entity_type: method
name: Workflow state-lineage bugs
aliases: [n8n debugging lessons, pairedItem lineage bug]
relationships:
- target: '[[n8n]]'
  type: applies_to
  strength: 8
  first_seen: '2026-07-26'
  last_reinforced: '2026-07-26'
- target: '[[hephzibah-os]]'
  type: learned_during
  strength: 6
  first_seen: '2026-07-26'
  last_reinforced: '2026-07-26'
---

Six recurring bug classes surfaced while building and hardening the Seraman n8n
pipeline (3-workflow handoff via a shared Google Sheet). None were algorithm
bugs — all were state/lineage bugs. General rules, not project-specific:

1. **Shared mutable store + multiple writers → use upsert, not append.**
   Any time more than one path (success/failure/retry/timeout) can write the
   same logical record, the write must be `appendOrUpdate`-shaped with an
   explicit matching key. Append is only safe if a record is provably written
   exactly once, ever.

2. **Whoever changes state must reset every field that gates downstream reads.**
   A status flag set by the original writer but never reset by a later writer
   (e.g. a regen path) causes downstream filters to fail closed — zero
   matching rows, no error, silent no-op. This is the worst bug shape because
   it produces no signal.

3. **`pairedItem` is data lineage, not cosmetic.** In n8n Code nodes,
   `.map()`-ing over `$input.all()` without setting `pairedItem: { item: idx }`
   per output item (or hardcoding `{ item: 0 }`) works with 1 input item and
   breaks with N. Any downstream `$('NodeName').item.json` reference depends
   on this being correct.

4. **HTTP success / duration-matched output is proof the pipeline ran, not
   proof it's correct.** Verify actual content (frame-diff a video, not just
   check its duration; read the actual row, not just the write ack) before
   declaring a generative/rendering pipeline fixed.

5. **API migrations that aren't applied to every code path diverge silently.**
   Two endpoints for the same capability can both return HTTP 200 with valid
   but differently-shaped JSON. A half-migrated system doesn't error — it
   quietly runs an older/worse path that looks like a content-quality issue
   from the outside.

6. **Hardcoded values that happen to resolve successfully are more dangerous
   than ones that error.** A hardcoded ID left over from manual testing
   (instead of a dynamic `{{ $json.field }}`) returns valid-looking data every
   time, just always the same data — nothing points at it until output is
   wrong for unrelated reasons.

**Appears in:** [[n8n]] · [[hephzibah-os]]
