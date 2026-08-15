---
sensitivity: private
entity_type: concept
name: Vendor Dynamics — Why Prices Differ
last_updated: '2026-08-13'
---

# Vendor Dynamics — Why One Phone Is Cheaper Than Another

The judgement the OS cannot reason its way to. Built from real vendor posts Emmanuel receives, decoded one at a time.

**Status: 3 data points.** Early. Every rule below is provisional until it has been seen three times.

---

## The Price Drivers, As They Actually Appear

### 1. SIM type — the biggest one seen so far

Two posts from the same vendor, same day, make this explicit:

| Post | SIM line | Signal |
|---|---|---|
| iPhone 17 256GB | **"Esim Locked"** | stated as a *limitation* |
| Samsung S26 Ultra 256GB | **"Physical & Esim"** | stated as a *feature* |

The vendor volunteers "Physical & eSIM" as a selling point and flags "eSIM Locked" as a qualifier. That asymmetry is the tell: **physical SIM support carries a premium in this market, and eSIM-only carries a discount.**

**CORRECTION 2026-08-08 — the first explanation written here was wrong.** It said Nigerian eSIM support is patchy. It is not: MTN, Airtel, Glo and 9mobile all support eSIM, Glo since March 2025. Emmanuel's own read was closer, and researching it produced a much worse answer than the one being replaced.

**What "eSIM Locked" actually means, and why it is severe:**

Two separate facts combine into one problem.

1. **US iPhones from the 14 onward have no physical SIM tray at all.** eSIM is the only way in.
2. **A carrier lock covers the eSIM chip, not just the SIM slot.** A phone locked to AT&T or Verizon will refuse any other carrier's eSIM — the profile may appear to install and then simply never connect.

Put together on a US model: **no SIM tray + cannot accept an MTN, Airtel, Glo or 9mobile eSIM = no cellular service in Nigeria at all.** No calls, no SMS, no mobile data. A very expensive iPod touch.

That is the real reason it is ₦30k+ cheaper, and it is not a discount — it is the market pricing a device that cannot do the main thing a phone does.

**The check, before ever quoting one:**
`Settings → General → About → Carrier Lock`
- **"No SIM Restrictions"** → genuinely unlocked, any Nigerian eSIM will work. Fine.
- **"SIM Locked"** → locked to a foreign carrier. On an eSIM-only body, WiFi only.

Ninety seconds, on the unit, before any money moves. There is no way to establish this from a photo or a group post.

**Consequence for Hephzibah:** this is the single most dangerous unit type seen so far. A buyer paying ₦735,000 for a phone that cannot take their line is not a complaint — it is a refund, a public thread, and the end of the trust position ([[trust-as-margin]]). If one is ever sold it must say, in plain words above the price: *"This phone cannot use a Nigerian SIM or eSIM. WiFi only."*

Better rule while volume is low: **do not touch eSIM-locked units.** The spread is not worth the exposure.

---

### 4. Apple "Important Message" codes — IBM / ICM / IDM

Vendor shorthand that appears in group posts, usually unexplained. Emmanuel flagged these; researched 2026-08-08.

| Code | Full name | What was replaced |
|---|---|---|
| **IBM** | **I**mportant **B**attery **M**essage | Battery |
| **ICM** | **I**mportant **C**amera **M**essage | Camera |
| **IDM** | **I**mportant **D**isplay **M**essage | Screen |

They appear when iOS cannot verify a component as a genuine Apple part — i.e. **the phone has been opened and repaired with an aftermarket part.** Anything not fitted by Apple or an Apple Authorised Service Provider triggers it.

**Where to see it:** `Settings → General → About → Parts and Service History`

**The honest assessment, both directions:**

*Not as bad as it sounds:* calls, messages, apps and browsing all work normally. Aftermarket parts are often functionally fine. The message itself breaks nothing.

*Worse than the vendor implies:* the phone has been opened. Something was damaged badly enough to need replacing. A replaced display can lose True Tone; a replaced camera or Face ID assembly can lose functions outright. Resale value drops hard and permanently, so **the discount transfers to the next seller too** — the buyer inherits it.

**Why this matters more than the price:** these units are posted cheap precisely because of the flag, and vendors typically do not explain unless asked. A buyer sees a good deal, buys, and finds the warning in Settings later. That is the exact dynamic this brand exists to invert.

**Rule: an IBM/ICM/IDM unit can be sold — but the code goes in the listing, translated into plain words, with the discount explained.**

> "Screen was replaced with a non-Apple part, so the phone shows an Important Display Message in settings. Everything works and it's ₦40k under a clean one because of it."

That is the flaw-first listing doing its job, and on this category it is worth more than on any other — because every competitor is hiding exactly this.

**Also worth checking on the same screen: MDM.** A corporate/school management lock. `Settings → General → About` and an IMEI check will show it. An MDM-locked phone can be remotely wiped or bricked by the organisation that owns it. That one is not a discount — it is a skip.

### 2. Activation status — worth ₦30,000 on a ₦700k phone

Same model, same storage, same lock status, one vendor, one post:

| | Price | Difference |
|---|---|---|
| **Non-Active** (never switched on) | ₦700,000 | — |
| **Active, 91% battery health** | ₦670,000 | **−₦30,000 (−4.3%)** |

"Non-Active" means the warranty clock has never started and nobody has used it. "Active" means it has been registered and carries real battery wear.

**₦30k ≈ 4.3% is the measured price of activation status + 9 points of battery health, on a current-generation flagship.** One observation, not yet a rule.

**The buying read:** the ₦30k saved is real money, and 91% on a recent phone is genuinely fine for most users. For a buyer who wants the phone rather than the box, the active unit is often the better purchase — and saying so out loud is exactly the "recommend against the more expensive option" move that builds credibility.

### 3. Condition stated vs condition omitted

The Samsung S26 Ultra post gives **model, storage, SIM type, price** — and no condition at all. Sealed? Non-active? Used? Battery health? Not stated.

On a **₦1,120,000** phone that is the single most important missing fact, and it is worth roughly the entire spread.

**Rule: never repost a unit whose condition was not stated. Ask first.** An unstated condition is not a neutral gap; it usually means the answer is not the good one.

---

## Vendor Post Shorthand — Decoder

| Shorthand | Means | Matters because |
|---|---|---|
| `BH` / `91BH` | Battery health % | The main used-value driver on iPhone |
| `Non-Active` | Never activated, warranty unstarted | Premium — commands ~4% over an active unit |
| `Active` | Registered and used | Discount |
| `Esim Locked` | eSIM only (confirm exact meaning) | **Discount — smaller buyer pool. Must be disclosed.** |
| `Physical & Esim` | Takes a normal SIM too | Premium — vendor states it unprompted |
| `HMU` | "Hit me up" — contact to claim | Signals limited quantity |
| `2 above` | Two units available | Quantity on hand |
| **`IBM`** | Important **Battery** Message | Battery replaced, non-genuine |
| **`ICM`** | Important **Camera** Message | Camera replaced, non-genuine |
| **`IDM`** | Important **Display** Message | Screen replaced, non-genuine |
| `MDM` | Mobile Device Management lock | **Skip.** Corporate-owned, can be remotely bricked |
| `FMI` | Find My iPhone / Activation Lock | Must read **OFF**. On = iCloud locked = worthless |
| `Mint` | Vendor's cosmetic grade | Unstandardised. Means nothing until inspected |
| `Factory Unlock` | No carrier restriction | **Premium state.** Any network, any SIM |

**The pattern across IBM / ICM / IDM / Mint:** these are the codes that make a phone cheap, and vendors post them without explanation. A buyer reads the low price, not the three letters. That gap is the business.

## The Three-Screen Check

Everything above resolves on the unit in about two minutes. This is the routine, and it runs on every phone regardless of who it came from.

| Screen | Path | Pass |
|---|---|---|
| **Carrier lock** | Settings → General → About → Carrier Lock | "No SIM Restrictions" |
| **Parts history** | Settings → General → About → Parts and Service History | No Important Messages, or they are known and priced |
| **Battery** | Settings → Battery → Battery Health | Number recorded, screenshotted |

Plus the IMEI check for FMI, MDM and blacklist status.

**Photograph all three.** They are the condition report, they take two minutes, and they are the entire difference between Hephzibah and a stall.

---

## ⚠️ Vendor Photos Are Not Always The Unit

The most important operational finding so far, because it sits directly on top of the brand's only real asset.

**Vendor-shot, appears genuine** — the iPhone and Samsung posts share one wooden backdrop, one black-gloved hand, and the same Apple Watch display behind. A consistent studio setup on their own stock.

**Recirculated, almost certainly** — the HP ProBook post:
- Completely different environment from the same vendor's phone shots
- Shows a stack of roughly ten laptops when **two** are offered
- Desktop icons in a non-English script
- The Windows taskbar appears to read **10/30/2023** — a photo close to three years old

**The rule this produces:** a vendor photo is a *catalogue* image. It shows the model, not the unit.

For a brand whose entire position is verified information, reposting a catalogue image as though it were the unit in hand is the same failure as publishing an unverified spec — and it is the more visible one, because the buyer compares the photo to the phone at handover.

**What follows:**
1. Vendor photos are fine for the *offer* stage — showing what the model is.
2. **The unit must be photographed by Emmanuel at collection**, and those photos are what a buyer sees before paying.
3. If a unit is never collected personally, say the photo is the vendor's. Never imply it is the unit.

This is also the practical answer to the branded-card question: the card is built around **his own photo of the actual unit**, which is precisely what no competitor reposting group images can copy.

---

## Still Unknown

- Why the *same model* differs between Matte and Yemi's group — not yet observed side by side
- Whether Matte's own stock prices differently from his boss's
- How fast these prices move, and what moves them (FX? new stock? launch cycles?)
- What "UK used" means from these specific vendors
- Whether a quoted price holds, and for how long

---

## Linked

[[gadget-index]] · [[price-ranges]] · [[broker-model]] · [[trust-as-margin]] · [[matte]] · [[yemi-group]]

### CORRECTION — eSIM-only is a US-MARKET variant, not 'a phone from America' — 2026-08-13 11:44

Emmanuel checked this independently on 2026-08-13 and the earlier note here was imprecise in a way that matters commercially.

**What is actually true:**

- **US-market** iPhone 14 and later are eSIM-only, with no physical SIM tray. Apple documents this: units purchased in the US can only be activated with eSIM.
- **Non-US regional variants of the same model** commonly have a nano-SIM tray AND eSIM.
- Some China, Hong Kong and Macau variants carry two physical SIMs.

**Why the distinction is the whole point in Lagos:** "US used" here almost always means *imported from the United States*, not *built as the US hardware variant*. A phone can have spent its life in America and still be a regional variant with a tray. Emmanuel's example: **A2889 is not the US variant** (the US iPhone 14 Pro is A2650); A2889 covers markets including Canada, Japan, Mexico, Saudi Arabia and Guam. An A2889 with a SIM tray is completely normal and not a sign of anything.

**The definitive check:** `Settings > General > About > Model Number`, the one ending in `/A`. That code names the region the phone was built for, regardless of what the seller says or where it was shipped from.

**What this changes in practice:**

1. Do not tell a buyer that a phone is eSIM-only because it came from America. Look at the side of the device, or read the model number.
2. The carrier-lock check still matters on every unit either way. A tray gives a fallback; a lock still refuses the buyer's line.
3. The carousel published 2026-08-13 was corrected before posting. Slide 06 now separates market variant from import origin, and slide 07 teaches the model-number check.

**Also worth noting on our own stock:** the HAIKUO labels on the ten iPhone Air units show A3260 and A3280. Worth confirming which regions those are before describing any of them as a US or non-US version.
