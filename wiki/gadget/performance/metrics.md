---
sensitivity: private
entity_type: system
name: Gadget Business Metrics
last_updated: 2026-08-08
period: "2026-08"
---

# Live Business Metrics

Read by `scripts/pulse.py` and `scripts/heartbeat.py`. Updated at every session end and after every sale.

> **⚠️ Baseline is zeroed — these are not real numbers yet.** Queue item `g002`. Until actual cash and stock figures are entered, `pulse.py` reports an empty business and the OS will recommend stocking things that cannot be funded.

---

<!-- MACHINE-READABLE BLOCK — parsed by scripts/pulse.py. Keep it valid JSON. -->
```json
{
  "as_of": "2026-08-08",
  "currency": "NGN",
  "cash": {
    "available_capital": 0,
    "committed_to_stock": 0,
    "receivables": 0,
    "fx_rate_ngn_usd": 0
  },
  "inventory": {
    "active_skus": 0,
    "units_held": 0,
    "stock_value_at_cost": 0,
    "stock_value_at_retail": 0,
    "dead_stock_value": 0
  },
  "sales_30d": {
    "units_sold": 0,
    "revenue": 0,
    "gross_profit": 0,
    "avg_margin_pct": 0,
    "avg_days_to_sell": 0,
    "returns": 0
  },
  "sales_all_time": {
    "units_sold": 0,
    "revenue": 0,
    "gross_profit": 0
  },
  "pipeline": {
    "products_researching": 0,
    "products_qualified": 0,
    "products_sampling": 0,
    "products_sourcing": 0,
    "listings_pending": 0
  },
  "suppliers": {
    "active": 0,
    "on_probation": 0,
    "sole_source_exposures": 0,
    "avg_reliability": 0
  },
  "content": {
    "posts_last_7d": 0,
    "posts_due_this_week": 0,
    "target_per_week": 8
  },
  "channels": {
    "whatsapp_contacts": 0,
    "instagram_followers": 0,
    "x_followers": 0
  }
}
```

---

## The Six Numbers That Matter

Everything above is instrumentation. These six are the business.

**1. Gross margin % (target: 42%+)**
Below 35% on the blended average means the gate is being broken somewhere. Find where.

**2. Days to sell (target: under 21)**
The velocity number. Capital that turns four times a year at 40% beats capital that turns once at 60%. This is the metric most gadget businesses never track and it is the one that decides whether the business grows or just cycles.

**3. Capital efficiency — gross profit ÷ average capital deployed**
The real return. A business making ₦400k profit on ₦2m of stock is doing better than one making ₦500k on ₦4m.

**4. Dead stock as % of stock value (target: under 10%)**
Above 15% means qualification is failing. The rubric needs revisiting, not the sales effort.

**5. Return rate (target: under 5%)**
Every return is a failure of inspection or of description. Above 5% means the condition reports are not honest enough, which is the one thing this brand cannot afford.

**6. Referral share of sales (target: 30%+)**
The compounding number. Referral buyers negotiate less, return less, and cost nothing to acquire. A rising referral share means the trust position is real. A falling one means the brand is talking, not working.

---

## Health Thresholds

`pulse.py` flags these automatically.

| Condition | Signal | Action |
|---|---|---|
| Available capital < ₦100k | 🔴 Cash constrained | No new POs. Clear existing stock first. |
| Dead stock > 15% of stock value | 🔴 Qualification failing | Run `/war-room`. Revisit the rubric. |
| Avg margin < 35% | 🔴 Gate broken | Find which SKUs are dragging. Re-price or clear. |
| Return rate > 5% | 🔴 Inspection failing | Audit the last 5 condition reports against what came back. |
| Zero sales in 14 days | 🔴 Demand or visibility problem | `/daily-brief` then `/content-brief` — usually visibility, not demand. |
| Sole-source exposures > 0 on top-5 | 🟠 Supplier gate breach | Find a backup. Queue item. |
| Posts last 7d < 4 | 🟠 Content behind | Content builds the buyers for next month. |
| Listings pending > 3 | 🟠 Bottleneck at listing | Finished stock nobody can buy. Highest-ROI fix available. |
| Products in sourcing > 14d | 🟠 Capital in limbo | Chase the supplier or release the capital. |

---

## Monthly Snapshot

Appended on the 1st. Never overwritten — the trend is the point.

| Month | Units | Revenue ₦ | Gross profit ₦ | Margin % | Days to sell | Dead stock % | Referral % |
|---|---|---|---|---|---|---|---|
| 2026-08 | — | — | — | — | — | — | — |

---

## Linked

[[gadget-index]] · [[gadget-insights]] · [[gadget-pricing]]
