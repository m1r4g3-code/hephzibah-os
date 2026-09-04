---
sensitivity: private
entity_type: company
name: Seraman
aliases: [seraman-tactical]
tags: [active-client, italian, tactical-gear]
stage: active
last_contact: '2026-06-28'
last_updated: '2026-06-28'
relationships:
- target: '[[giovanni]]'
  type: employs
  strength: 10
  first_seen: '2026-06-28'
  last_reinforced: '2026-06-28'
- target: '[[identity]]'
  type: targeted_by
  strength: 9
  first_seen: '2026-06-28'
  last_reinforced: '2026-06-28'
- target: '[[4-workflows-4-days]]'
  type: mentioned_in
  strength: 3
  first_seen: '2026-06-28'
  last_reinforced: '2026-06-28'
---

# Seraman

**Italian tactical gear brand.** Active client. Owner: [[giovanni]].

The Seraman project is Emmanuel's most complex active build — a six-workflow n8n AI video production pipeline producing automated tactical gear content for social publishing.

## What Emmanuel Is Building

Full automated content pipeline:

```
Tally form (brief input)
  → Claude Script Agent (scriptwriting + cleaning)
  → Kie AI Veo 3.1 (video generation)
  → Creatomate (video assembly)
  → Google Sheets (tracking)
  → Blotato (social publishing)
```

Six total workflows. Approval gate: social publishing only fires after explicit client approval.

## Why This Client Matters

- Highest complexity build Emmanuel has shipped
- First clean direct-client AI video automation engagement (no middleman)
- Establishes Kie AI + Creatomate + Blotato stack knowledge
- Proof point for the AI video automation offer in ME.md

## Call History

| Date | Contact | Outcome | Follow-up |
|------|---------|---------|-----------|
| 2026-08-26 | Giovanni (async, email) | Aquatabs corrected video shipped and delivered. Real K9 Tourniquet job (M1MozPE) ran through the pipeline for real — images clean, video blocked on Kie credit exhaustion. Two real production bugs found and fixed (row-collision on new-job writes, stale caption/image inheritance). Full detail in [[giovanni]] and `wiki/upwork/clients/active/2026-06-22-giovanni-seraman.md`. | Awaiting Giovanni's confirmation Aquatabs is clean (retainer-conversation trigger); Kie top-up needed before K9 video/30-product launch can proceed. |

## Wikilinks

[[giovanni]] · [[n8n]] · [[claude-api]] · [[identity]]
