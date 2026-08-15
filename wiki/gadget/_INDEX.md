---
sensitivity: private
entity_type: domain
name: Gadget OS — Domain Index
last_updated: 2026-08-08
relationships:
  - target: "[[identity]]"
    type: part_of
    strength: 10
    first_seen: "2026-08-08"
    last_reinforced: "2026-08-08"
  - target: "[[hephzibah-os]]"
    type: part_of
    strength: 10
    first_seen: "2026-08-08"
    last_reinforced: "2026-08-08"
  - target: "[[yemi]]"
    type: partner_in
    strength: 9
    first_seen: "2026-08-08"
    last_reinforced: "2026-08-08"
  - target: "[[lagos]]"
    type: operates_in
    strength: 10
    first_seen: "2026-08-08"
    last_reinforced: "2026-08-08"
---

# Gadget OS — Domain Index

Load this after `_CONTEXT.md`. This is the orientation document for the gadget business domain.

Hephzibah Gadgets is Emmanuel's consumer electronics business, run with [[yemi]] as operating partner. This domain is its memory layer. Claude Code is the engine. The Python scripts in `scripts/` are the mechanical arms. Nothing about this business should be decided from vibes — every stock decision, every price, every supplier commitment is scored and logged here.

**This is the third suit in the hephzibah-OS architecture.** Same brain, same engine, new domain. It does not get its own memory — it reads and writes here, alongside `upwork/`, `outreach/`, and `fiverr/`.

---

## Operating Context

| Fact | Value |
|---|---|
| Market | Lagos, Nigeria — primary. Nationwide via courier. |
| Sourcing hub | Computer Village, Ikeja + direct import (China/UK/US) |
| Primary currency | NGN (₦). COGS on imports tracked in USD, converted at PO date. |
| Sales channels | WhatsApp Status/Broadcast · Instagram · X (Twitter) · Jiji · direct referral |
| Operating partner | [[yemi]] — sourcing, physical handling, profit split |
| Fulfilment | Hand delivery (Lagos) · GIG/Kwik courier (nationwide) |

**Assumption flag:** The Nigerian/Lagos framing above is inferred from `me/identity.md` (Yemi = gadget business partner, phone swap deals, Lagos base). If Hephzibah Gadgets actually operates a different market — correct `identity/niche.md` first, then re-run `/pricing-strategy` on all active products. Every margin number in this domain assumes NGN retail against USD-or-NGN COGS.

---

## Domain Map

```
gadget/
├── _INDEX.md                     ← this file
├── _QUEUE.md                     ← gadget priority queue (heartbeat.py reads this)
├── _PIPELINE.md                  ← all products across all stages
├── _SESSION.md                   ← session checkpoint (read first, write at end)
├── identity/
│   ├── brand.md                  ← Hephzibah Gadgets brand, voice, values
│   ├── niche.md                  ← categories in / categories out
│   └── pricing.md                ← margin targets, pricing philosophy, FX policy
├── market/
│   ├── intelligence.md           ← running market observation log
│   ├── competitors.md            ← competitor tracking
│   └── patterns/
│       ├── winning-products.md   ← patterns from products that sold well
│       └── dead-stock.md         ← patterns from products that did not
├── products/
│   ├── _template.md              ← product node schema
│   └── active/                   ← live product nodes (one per SKU)
├── suppliers/
│   ├── _template.md              ← supplier node schema
│   └── active/                   ← supplier relationship nodes
├── playbooks/
│   ├── product-qualification.md  ← the 5-dimension scoring rubric
│   ├── listing-framework.md      ← how a Hephzibah listing is built
│   └── content-strategy.md       ← content angles per product type
├── performance/
│   ├── metrics.md                ← live business metrics
│   └── insights.md               ← weekly synthesis
└── concepts/                     ← atomic gadget-domain concept nodes
```

---

## Why State Files Live Here, Not At Brain Root

The brain root already has `_QUEUE.md`, `_PIPELINE.md`, and `_SESSION.md` — they belong to the Upwork OS and are full of proposal and client items.

**Decision:** the gadget OS keeps its own `_QUEUE.md` / `_PIPELINE.md` / `_SESSION.md` inside `gadget/`. Two operating systems writing to one queue file produces merge conflicts on every session and forces the operator to read freelancing items while thinking about stock. The brain is shared; the state machine is per-domain.

`scripts/heartbeat.py` reads `gadget/_QUEUE.md` first and falls back to the root file only if the gadget one is missing. Cross-domain items (things that affect both businesses — cash position, Yemi's time, shared shipping) get written into **both** queues with the same `id` prefix so they stay linked.

---

## The Five Gates

Every decision in this domain passes through these. They are in `../CLAUDE.md` in full. Short version:

| Gate | Rule |
|---|---|
| **Product** | Composite score < 65 → SKIP. No exceptions. |
| **Margin** | Gross margin < 35% → do not stock. |
| **Supplier** | Never sole-source a top-5 product. |
| **Quality** | Sample before bulk PO. Always. |
| **Brand** | If it cheapens the Hephzibah name, the margin does not matter. |

---

## Entry Points

- **New product idea** → `/product-qualify` → writes to `products/active/` if it passes
- **New supplier contact** → `/supplier-intel` → writes to `suppliers/active/`
- **Product cleared to sell** → `/write-listing` → `outputs/listings/`
- **Weekly** → `/daily-brief` + update `performance/insights.md`
- **Anything with real downside** → `/war-room`

---

## Linked Concepts

[[hephzibah-os]] · [[lagos]] · [[yemi]] · [[middleman-lesson]] · [[financial-fragility]] · [[strategic-frameworks]] · [[specificity-as-credibility]] · [[tool-first-rule]] · [[active-agent-mode]]
