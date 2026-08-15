---
sensitivity: private
entity_type: product
name: "[Product name — model, storage, condition]"
sku: "[slug-form-sku]"
category: "[phones|audio|power|wearables|laptops|accessories]"
stage: "researching"
stage_entered: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"

# Scores — from scripts/qualify.py
score_demand: null
score_margin: null
score_competition: null
score_fit: null
score_logistics: null
score_composite: null
decision: null          # STOCK | WATCHLIST | SKIP
forced_stock: false     # true if stocked against the gate — marks the outcome data

# Economics — all NGN unless stated
supplier: null          # must match a slug in suppliers/active/
invoice_cost: null
fx_rate_at_po: null     # NGN per USD/GBP actually paid. Required on any import.
landed_cost: null       # invoice + freight + clearing + inspection + provision
target_price: null
floor_price: null       # lowest acceptable after negotiation — do not go below
gross_margin_pct: null
units_ordered: 0
units_held: 0
units_sold: 0
capital_committed: 0

channels: []            # whatsapp | instagram | x | jiji | referral
relationships: []
---

# [Product Name]

## What It Is

[Two sentences. The device, the configuration, the condition. Written the way it would be said to a buyer who knows devices.]

---

## Qualification

Run: `python scripts/qualify.py --name "[product]" --category [cat] --demand N --margin N --competition N --fit N --logistics N`

| Dimension | Score | Reasoning |
|---|---|---|
| Market demand (30%) | — | [what the demand evidence actually was] |
| Margin potential (25%) | — | [cost basis vs achievable price] |
| Competition (20%) | — | [how crowded — inverted, higher score = less crowded] |
| Brand fit (15%) | — | [against identity/niche.md] |
| Logistics (10%) | — | [weight, fragility, import complexity, warranty exposure] |
| **Composite** | **—** | |

**Decision:** [STOCK / WATCHLIST / SKIP]
**Rationale:** [Two sentences. Honest. If this is a close call, say which way it could go wrong.]

---

## Condition Report

*Required before any used unit is listed. This section is the product.*

| Attribute | Value |
|---|---|
| Grade | [A / A- / B — Hephzibah does not stock below B] |
| Battery health | [%] |
| IMEI status | [clean — checked YYYY-MM-DD via (source)] |
| iCloud / FRP | [clear / locked — locked is not stocked] |
| Screen | [original / replaced — original quality if replaced] |
| Back glass / body | [specific description of every mark, with location] |
| Ports and buttons | [all tested — list anything not working] |
| Cameras | [front and rear tested] |
| Face ID / fingerprint | [working / not] |
| Speakers and mic | [tested] |
| Network | [unlocked / carrier-locked to X] |
| In the box | [exact contents] |
| Known flaws | [every one, named and located. If none found, write "none found on inspection YYYY-MM-DD" — never write "perfect"] |

**Inspected by:** [name] **on** [date]

---

## Economics

```
Invoice cost           ₦
FX rate at PO           (if imported)
Freight per unit       ₦
Clearing per unit      ₦
Inbound transport      ₦
Inspection (₦2,000)    ₦
Included accessories   ₦
Loss provision (N%)    ₦
─────────────────────────
LANDED COST            ₦

Target price           ₦
Floor price            ₦
Gross margin           %      ← must be ≥35%
Margin per unit        ₦
```

---

## Positioning

**Who buys this:** [specific — not "everyone who wants a phone"]
**What they are afraid of:** [the actual fear this listing has to remove]
**The one-line pitch:** [how it gets described in a WhatsApp status]
**Bundle attach:** [what goes with it at point of sale]

---

## Listing

**Status:** [not written / draft / approved / published]
**File:** `outputs/listings/YYYY-MM-DD-[sku].md`
**Published:** [date + channels]

---

## Content

| Angle | Format | Status |
|---|---|---|
| | | |

Brief: `outputs/strategy/YYYY-MM-DD-[sku]-content-brief.md`

---

## Sales Log

| Date | Units | Price | Channel | Buyer type | Negotiated? | Notes |
|---|---|---|---|---|---|---|

---

## Outcome

*Fill when the SKU sells out, is retired, or hits dead stock. This section feeds `market/patterns/`.*

**Result:** [sold out / retired / dead stock]
**Days to clear:** [first listed → last unit sold]
**Realised margin:** [% — actual, after every discount given]
**Return rate:** [N of M units]
**What worked:**
**What did not:**
**Would stock again:** [yes / no / yes but at a different cost]
**Pattern candidate:** [trait this shares with other products, or "none"]

---

## Linked

[[gadget-index]] · [[supplier-slug]] · [[gadget-pricing]]
