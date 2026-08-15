---
sensitivity: private
entity_type: domain
name: Price Ranges — Real Vendor Data
last_updated: 2026-08-08
---

# Price Ranges — Real Vendor Data

Actual vendor prices from posts Emmanuel receives. Append-only. **Vendor cost, not selling price** — the sell side gets logged separately once deals are done.

Every price is dated because these move. A price without a date is not data.

---

## 2026-08-08 — First real batch

| Item | Spec | Condition | Vendor ₦ | Notes |
|---|---|---|---|---|
| iPhone 17 | 256GB, **eSIM locked** | **Non-active** | **700,000** | Never activated |
| iPhone 17 | 256GB, **eSIM locked** | **Active, 87–91BH** | **670,000** | −₦30k vs non-active |
| Samsung S26 Ultra | 256GB, **physical + eSIM** | **not stated** | **1,120,000** | ⚠ condition omitted |
| HP ProBook 440 G6 | i5 8th gen, 8GB, 256GB SSD, backlit | not stated | **270,000** | 2 units. Photo recirculated |
| iPhone 12 | 128GB, **factory unlocked** | **87% BH, graded** | **300,000** | ⭐ inspection label on unit |

---

## What This Batch Establishes

### The tier gap is the whole business problem

| Vendor ₦ | Sell at | Spread | Buyers in Emmanuel's pool |
|---|---|---|---|
| 1,120,000 | ~1,175,000 | ~₦52k | **almost none** |
| 700,000 | ~735,000 | ~₦32k | **very few** |
| 300,000 | ~320,000 | ~₦20k | **many** |
| 270,000 | ~292,000 | ~₦19k | **many** |

Emmanuel's stated problem is that customers come and cannot afford the phones. This table is that problem in numbers, and it also contains the answer.

**A ₦320,000 iPhone 12 is not "selling cheap." It is the correct tier for the audience he actually has.** Three of those in a week is ₦60,000. One iPhone 17 that nobody in his contact list can buy is ₦0.

The instinct to protect margin by chasing the expensive units is backwards while the audience is what it is. Sell the tier they can reach now; the high-ticket units become viable once the channel reaches people with the budget for them — see the war-room output of 2026-08-08.

### The ₦300k band looks like the sweet spot

Reachable for a young Lagos buyer, still a phone worth wanting, still a real spread. **This is where the volume is, and volume is the missing variable at 1–3 deals a week.**

### Laptops are a genuinely separate market worth testing

The ProBook at ₦270k → ~₦292k is a ₦19k spread, and it sells to a different buyer: students and small offices, not phone upgraders. Emmanuel studies at Miva; his network is disproportionately students, who need a working laptop more than they need a current-generation iPhone.

Untested, but the audience fit looks stronger than anything else in this batch. Two units available means it can be tried without commitment.

---

## Price Drivers Observed

Decoded in full in [[vendor-dynamics]].

| Driver | Measured effect | Confidence |
|---|---|---|
| Non-active vs active | **−₦30,000** (−4.3%) on a ₦700k phone | 1 observation |
| eSIM-only vs physical+eSIM | Discount — vendor flags it as a qualifier, and advertises physical SIM as a feature | 2 observations |
| Factory unlocked | Premium state — no carrier restriction | 1 observation |
| Graded with an inspection label | Lower risk. FMI off, data cleared, functionality passed, all documented | 1 observation |
| Battery health | 87% and 91% both seen. Price effect not yet isolable | insufficient |

---

## The Inspection Label — Worth More Than It Costs

The iPhone 12 arrived with a printed grading label stuck to the back showing, in readable form: model and part number, **Other (Unlocked)**, **FMI / Lock OFF**, **Data Cleared PASS**, **Functionality PASS**, **Testing Finished YES**, plus a serial, barcode and QR.

**FMI OFF is the single most important line on it.** An iCloud-locked iPhone is worthless and is the classic Lagos burn. A label that documents it is exactly the verified information this brand sells — already produced, already attached, and currently being thrown away by everyone who reposts the phone without it.

**Photograph the label. Every time.** It is free, it is falsifiable, and no competitor reposting group images can show one.

---

---

# THE PRICE LADDER — Yemzy Gadgets, Apr–Aug 2026

Extracted from a full WhatsApp export of the *Yemzy Gadgets deals* group by
`scripts/parse_whatsapp.py`. **128 priced products across 4 months.**

Coverage is honest: 560 messages → 242 noise, 133 without a price, 57 with a
price but no model the parser recognised. So this is roughly 70% of the priced
posts, not all of them. Medians on `n=1` or `n=2` are anecdotes, not prices.

**All figures are VENDOR COST — what Yemzy asks. Not what Hephzibah sells for.**

| Model | n | Low | Median | High |
|---|---|---|---|---|
| MacBook Air | 3 | ₦2.02m | ₦2.03m | ₦7.44m |
| MacBook Pro | 2 | ₦2.02m | ₦2.02m | ₦2.02m |
| Samsung S26 | 1 | ₦1.32m | — | — |
| iPhone 17 Pro Max | 5 | ₦1.06m | **₦1.16m** | ₦1.73m |
| Samsung S26 Ultra | 1 | ₦1.12m | — | — |
| iPhone 17 Pro | 2 | ₦1.00m | ₦1.02m | ₦1.05m |
| iPhone 16 Plus | 3 | ₦670,000 | ₦930,000 | ₦960,000 |
| iPhone 15 Pro Max | 4 | ₦740,000 | **₦850,000** | ₦970,000 |
| HP EliteBook 840 G7 | 1 | ₦840,000 | — | — |
| HP EliteBook 830 G7 | 3 | ₦830,000 | ₦830,000 | ₦830,000 |
| iPhone 17 | 7 | ₦520,000 | **₦820,000** | ₦1.05m |
| iPhone 17e | 2 | ₦560,000 | ₦780,000 | ₦1.00m |
| iPhone 16 | 5 | ₦600,000 | **₦780,000** | ₦955,000 |
| iPhone 15 Pro | 2 | ₦720,000 | ₦755,000 | ₦790,000 |
| iPhone 14 Pro Max | 4 | ₦520,000 | ₦682,500 | ₦820,000 |
| Apple Watch Ultra 2 | 1 | ₦640,000 | — | — |
| iPhone 15 | 5 | ₦420,000 | **₦610,000** | ₦870,000 |
| iPhone 14 Pro | 6 | ₦400,000 | **₦600,000** | ₦620,000 |
| iPhone 16 Pro | 2 | ₦540,000 | ₦590,000 | ₦640,000 |
| iPad 11th gen | 4 | ₦480,000 | ₦510,000 | ₦590,000 |
| HP ProBook 440 G6 | 1 | ₦440,000 | — | — |
| iPhone 13 Pro | 1 | ₦430,000 | — | — |
| iPad Air | 2 | ₦400,000 | ₦410,000 | ₦420,000 |
| iPhone 13 Pro Max | 4 | ₦310,000 | ₦365,000 | ₦390,000 |
| iPhone 14 | 2 | ₦300,000 | ₦350,000 | ₦400,000 |
| iPhone 12 Pro | 3 | ₦220,000 | ₦330,000 | ₦385,000 |
| iPhone 11 Pro Max | 2 | ₦240,000 | ₦295,000 | ₦350,000 |
| **iPhone 13** | **10** | **₦180,000** | **₦280,000** | **₦400,000** |
| **iPhone 12** | **8** | **₦170,000** | **₦225,000** | **₦300,000** |
| iPhone 11 Pro | 2 | ₦180,000 | ₦185,000 | ₦190,000 |
| **iPhone 11** | **6** | **₦150,000** | **₦182,500** | ₦250,000 |
| **iPhone XR** | **9** | **₦125,000** | **₦165,000** | ₦200,000 |
| iPhone SE | 1 | ₦145,000 | — | — |
| iPhone X | 2 | ₦90,000 | ₦95,000 | ₦100,000 |
| iPhone 8 | 1 | ₦80,000 | — | — |
| iPhone 7 | 3 | ₦75,000 | ₦85,000 | ₦85,000 |

**Note the ProBook 440 G6 at ₦440,000 here versus ₦270,000 quoted elsewhere on 2026-08-08.** Same model, ₦170,000 apart, different sources. Either different specs, or a genuine sourcing edge worth understanding. Worth chasing — this is exactly the vendor-versus-vendor comparison the OS has been missing.

---

# WHY THE SAME PHONE COSTS DIFFERENT MONEY

**The iPhone 13 128GB — ten posts, one group, four months:**

| Price | Flags |
|---|---|
| **₦180,000** | locked · **IBM** (battery replaced) |
| **₦180,000** | locked · 75% battery |
| **₦190,000** | factory unlocked — but **NO FACE ID** |
| ₦260,000 | locked · eSIM · mint · US |
| ₦270,000 | locked · eSIM · mint · US |
| ₦290,000 | eSIM · **IDM** (screen replaced) · US |
| ₦300,000 | used · 75% battery |
| ₦345,000 | UK standard |
| ₦350,000 | *(no flags — clean)* |
| **₦400,000** | **non-boosted** · US |

**₦180,000 to ₦400,000. A ₦220,000 spread — 122% — on one model and one storage size.**

Nothing about the phone changed. Only what is wrong with it, and whether the vendor said so.

## What each flag is worth

Median price change against other posts of the same model and storage:

| Flag | Seen | Effect | What it means |
|---|---|---|---|
| **NO-FACE-ID** | 5 | **−24%** | Face ID dead. Usually a screen replaced badly. |
| **locked** | 19 | **−16%** | Carrier locked. The most common discount by far. |
| MDM-LOCK | 2 | −7% | Corporate lock. **Skip these entirely.** |
| WIFI-ONLY | 4 | −5% | No SIM tray + carrier locked = not a phone |
| IBM-battery | 7 | −3% | Battery replaced, non-genuine |
| IDM-display | 6 | −3% | Screen replaced, non-genuine |
| factory-unlocked | 9 | 0% | Baseline expectation, not a premium |
| physical+esim | 6 | +2% | Mild premium |
| used | 8 | +6% | *(artefact — "used" posts skew to better models)* |
| **non-boosted** | 2 | **+21%** | **See below. The most important flag here.** |

Small samples throughout. Direction is trustworthy; the exact percentages are not.

## ⚠ "Boosted" — batteries with faked health readings

The single most valuable thing in this export.

A vendor writing **"Non Boosted"** as a selling point, and commanding roughly +21% for it, means the default assumption in this market is that a battery health figure **may have been tampered with.** "Boosting" makes a worn battery report a high percentage.

**Consequences that change how Hephzibah operates:**

1. **A battery health screenshot alone is not proof.** The number can be manufactured. The brand has been treating that screenshot as the core proof — it is necessary but no longer sufficient.
2. **Cycle count is the harder number to fake.** `cc 762` in a vendor post is charge cycles. A phone claiming 100% health with 700+ cycles is lying. **Always ask for cycles alongside battery health** — the pair together is much harder to fake than either alone.
3. **"Non Boosted" is worth asking for by name.** It is vendor language, they recognise it, and it costs nothing to ask.
4. **This is a content post waiting to be written.** Most buyers in Lagos have never heard of battery boosting. Explaining it — and showing how to check cycles — is the highest-trust content available, and it advertises exactly the checking Hephzibah does.

---

## Gaps

- Still **no selling prices** — everything above is vendor cost. Every spread the OS quotes is modelled until real sales are logged.
- 57 priced posts had no recognisable model — mostly accessories and Samsung variants. Parser coverage could improve.
- No like-for-like comparison between Matte and Yemzy on the same model, except the ProBook discrepancy noted above.
- Samsung S26 Ultra condition never stated — **ask before quoting it.**
- No sense of how fast any of this stock actually moves.

---

## Linked

[[gadget-index]] · [[vendor-dynamics]] · [[broker-model]] · [[trust-as-margin]] · [[gadget-learning]]
