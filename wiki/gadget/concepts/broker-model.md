---
sensitivity: private
entity_type: concept
name: Broker Model
last_updated: 2026-08-08
relationships:
  - target: "[[trust-as-margin]]"
    type: tensions_with
    strength: 10
    first_seen: "2026-08-08"
    last_reinforced: "2026-08-08"
  - target: "[[capital-velocity]]"
    type: supersedes
    strength: 9
    first_seen: "2026-08-08"
    last_reinforced: "2026-08-08"
---

# Broker Model

**Hephzibah Gadgets does not hold stock.** Units are posted from [[yemi-group]] and [[matte]]; money moves only when a buyer commits. Nothing sits on a shelf.

This is the single most important structural fact about the business, and getting it wrong makes every number downstream wrong. The OS was initially built for a stockist and had to be corrected — this node is the correction.

---

## What Changes

| | Stockist | **Broker (actual)** |
|---|---|---|
| Capital at risk | full unit cost, for weeks | **~zero** |
| The killer failure | dead stock — capital trapped | **the unit is gone when the buyer commits** |
| Margin floor logic | risk buffer for trapped capital | **is this deal worth the trip across Lagos** |
| Right unit of margin | percentage | **absolute naira per deal** |
| FX exposure | full, across the holding period | minimal — cost and sale are near-simultaneous |
| Launch-window risk | severe | mild — no inventory to devalue |
| Scale constraint | available capital | **time, trust, and attention** |

**The margin floor must be an absolute number, not a percentage.** With no capital tied up, "35% gross" is meaningless — there is nothing to buffer. What actually has to be covered is the trip to Ikeja, the trip to the buyer, the hours of messaging, and the risk of carrying a problem that is not yours. A ₦40k spread on a ₦450k phone is 8.9% and a good day. The same 8.9% would be ruinous for a stockist and is entirely fine here.

Conversely a ₦12k spread is a bad deal at any percentage, because a day spent crossing Lagos for ₦12k is not a business, it is an errand.

---

## The Gates, Restated for a Broker

| Gate | Broker form |
|---|---|
| **Product** | composite ≥ 65 — unchanged, but demand matters even more: a broker has no shelf, so a slow unit is wasted attention rather than wasted capital |
| **Margin** | **≥ ₦15,000 absolute AND ≥ 8%** — both must clear. Defaults, not measurements. Calibrate after 10 logged deals. |
| **Supplier** | unchanged and *more* binding — with no stock, the supplier **is** the inventory |
| **Quality** | sample-before-bulk does not apply. Replaced by **inspect-before-handover**, which is stricter |
| **Brand** | unchanged, and under more strain — see below |

---

## The Trust Problem — The Real One

[[trust-as-margin]] says the product is verified information and the device is the delivery mechanism. The whole premium rests on the buyer knowing more from a Hephzibah listing than from holding the phone in a shop.

**A broker posting from a group is selling a device he has never held.**

Battery health, IMEI status, the nick on the frame — none of it is knowable at posting time. Publishing those numbers anyway, taken from a group post, is exactly the unverifiable claim the brand exists to stand against. Doing it once and being caught costs more than the margin on every deal that month.

This is not a small tension. It is the central operational risk of the model.

### The resolution

Do not fake the verification. **Move it, and say where it is.**

The listing states plainly what is confirmed and what is not, and when the verification happens:

> iPhone 13 128GB — UK Used, at my vendor in Ikeja
>
> What I know now: 128GB, UK used, seller states battery 91%.
> What I have not done yet: I have not held this unit. Battery, IMEI and body are unverified until I collect it.
>
> How it works: you commit, I collect it and run the full check — battery screen, IMEI, every port, every lens. I send you the photos before I set out to you. If anything is off, the deal is off and you have paid nothing.
>
> ₦470,000. Lagos delivery, inspect before you pay.

That is more honest than every competing listing and **more persuasive**, because it names a risk the buyer already suspects and then removes it. The buyer's exposure is genuinely zero. The market's normal offer is "trust me"; this is "you don't have to."

### The three rules this produces

1. **Never publish a spec as verified that has not been personally checked.** Attribute it: *"seller states 91%"* is honest. *"Battery 91%"* on an unheld unit is a lie with a number on it.
2. **No money before the check.** The inspection happens before the buyer's cash moves, always. This is what makes rule 1 survivable — an unverified listing is fine precisely because nobody is exposed.
3. **Pull the post the moment the unit is gone.** A live listing for a sold phone is indistinguishable from bait.

---

## The Broker Failure Modes

Ranked by how often they will actually happen.

**1. The unit is gone.** Group stock is shared with everyone in the group. A buyer commits and the phone sold an hour ago. → Confirm availability **before** taking money, never after. Track how often it happens per supplier; repeated occurrences are a supply-reliability problem, not luck.

**2. The price moved.** Quoted ₦420k, arrive at Ikeja, it is ₦435k. The spread is gone and the buyer has been given a number. → Get the price-hold window in writing, per vendor. Build a small buffer into the asking price for vendors whose prices move.

**3. Condition is worse than described.** Rule 2 above makes this survivable rather than fatal — walk away, nobody has paid. But it costs the trip and the buyer relationship. → Track it per supplier; it is the clearest quality signal available.

**4. Both hands, no control.** The buyer relationship, the reputation, and the delivery risk are all Emmanuel's. The stock, the price, and the availability are all the vendor's. That asymmetry is the permanent condition of brokering. → The only real hedges are multiple vendors and the fact that Emmanuel owns the buyer relationship, which is the more durable asset.

---

## What Scales, and What Does Not

A stockist scales by adding capital. **A broker scales by adding buyers, and is capped by hours.** Every deal costs roughly the same time regardless of value — same messaging, same trip, same handover.

Two consequences:

- **Higher-ticket units are strictly better.** A ₦60k spread and a ₦20k spread cost the same day. Push toward the top of the range.
- **The audience is the actual asset.** Capital compounds for a stockist; here the thing that compounds is the number of people who come to Emmanuel first. That is what makes content ([[gadget-content-strategy]]) the growth engine and not a side activity.

**The path out** is that broker margins fund selective stock-holding later. When a SKU proves it moves reliably, buying a unit outright captures the full margin instead of the spread. That is a graduation, not a pivot — and it is the point at which the original 35% stockist gate becomes live again for those units.

---

## ⚠ THE 50/50 SPLIT — Halve Every Number

**Emmanuel and Yemi split deal profit in half.** Confirmed 2026-08-08.

Every figure this OS produced before that date quoted the gross spread as though he kept it. **His actual take is half of every spread shown.** A ₦20,000 spread is ₦10,000 in his hand — and that ₦10,000 still has to cover his own transport to Ikeja and to the buyer.

`qualify.py` now prints both. `PARTNER_SPLIT = 0.50`.

**RESOLVED 2026-08-08 — the split is symmetric and runs both ways.** Emmanuel takes half of Yemi's own deals exactly as Yemi takes half of his, including deals Emmanuel plays no part in. This is a genuine pooled partnership, not a sourcing fee, and an earlier reading of it here as a possible "tax" was wrong.

**The operating structure, confirmed:** each partner sources independently, closes independently, and works his own deals alone. Neither needs the other's involvement to trade. All profit is pooled and halved regardless of who did the work. Close friends; the arrangement runs on understanding rather than paperwork.

**What this means for how the OS should think:** there is no "my deal" and "his deal" — there is one book with two people writing into it. Emmanuel's deal count is not a personal scoreboard, it is his contribution to a shared P&L. And because either partner can trade without the other, **the ceiling on the business is simply how many deals the two of them start**, not how well any single deal is executed.

### What symmetry actually implies

**1. The partner who closes more subsidises the one who closes less.** Emmanuel closed two deals in 2026; Yemi "closed the most deals" last year. On a symmetric split that makes Emmanuel the **net receiver** so far. Nothing wrong with that between partners — but it is the honest frame, and it sharpens two things:

- The outstanding ₦25,000 is owed to the partner who has been producing more. That is worth clearing on those grounds alone.
- The single highest-leverage variable Emmanuel controls is **his own deal count.** It is the only side of the ledger he can move.

**2. Yemi is not merely a supplier — he is an investor in Emmanuel's deal flow.** He earns from every deal Emmanuel closes, whether or not he touches it. That inverts how Emmanuel should be treating the relationship:

- Asking Yemi for the best price is not an imposition; Yemi profits from the sale either way
- Asking Yemi for help, coaching, introductions or leads costs nothing and pays Yemi directly
- Yemi has a **direct financial stake** in Emmanuel getting better at closing

Emmanuel has been treating Yemi as a vendor to negotiate against. The structure says he is a partner to recruit. *"Help me close more — you earn from it too"* is a true statement, and it is almost certainly an unspent asset.

**3. It makes the two-vendor process cleaner than it looked.** Price-checking [[matte]] against Yemzy is not disloyalty — a better price means a bigger pot, and Yemi takes half of that pot regardless of where the unit came from. Both partners gain from Emmanuel sourcing well.

---

## The Real Deal History — 2026

Two closed deals this year. This is the entire revenue record.

### Deal 1 — Oyin (coursemate), swap
`iPhone 11 Pro Max 256GB → iPhone 14 128GB`
**Gross profit ₦50,000 · Emmanuel's half ₦25,000**

The ₦25,000 has not yet been paid to Yemi — Emmanuel's phone was stolen around that period ([[financial-fragility]]). **Spoken about and acknowledged between them (2026-08-08); Emmanuel has told Yemi he will pay.** Close friends, understood on both sides. Recorded here as an open balance, not as a problem — the OS should not raise it again unless it is still open in a month.

### Deal 2 — Aunt's husband, laptop repair
HP laptop — screen and keyboard replaced.
**Gross profit ₦24,000 · split ₦12,000 each**

Not a resale at all. A **repair service** — a revenue line the OS did not know existed and has no schema for.

### What the two deals actually say

| | Deal 1 | Deal 2 |
|---|---|---|
| Source | coursemate | aunt's husband |
| Channel | **personal relationship** | **personal relationship** |
| Type | **swap** | **repair** |
| Gross | ₦50,000 | ₦24,000 |

**Neither came from WhatsApp Status.** Both came from someone who already knew and trusted him. The posting has produced zero closed deals.

**Both were also non-standard.** Not "buy phone, sell phone" — a swap and a repair. The two things that actually worked were the two things that were not straight reselling.

**2026 totals: ₦74,000 gross · ₦37,000 his share · ₦12,000 actually in hand** once the unpaid ₦25,000 is set against it.

---

## Confirmed Operating Facts

From Emmanuel directly, 2026-08-08. These are stated, not inferred — everything else in this node is reasoning built on top of them.

| Fact | Value | What it changes |
|---|---|---|
| **Margin added** | ₦10,000 and above | The hard floor. An earlier build guessed ₦15k + 8% and would have rejected his entire book. |
| **Does it scale with ticket?** | **Yes** — more on expensive phones | Produces the expected-spread bands below, as guidance rather than a gate. |
| **Does he hold the phone?** | **Sometimes** — depends on the deal | The central brand risk. See the rule below. |
| **Transport per deal** | ₦2,000–₦4,000 | The ₦3,000 default is right. On a ₦10k spread that is 30% of the profit. |
| ~~**Volume**~~ | ~~1–3 deals per week~~ | **SUPERSEDED — see below** |
| **Volume (actual)** | **2 closed deals in 2026** | Changes everything again. |
| **Profit split** | **50/50 with Yemi** | Halves every number the OS produces |
| **Vendor process** | Price-check **both** Matte and Yemzy per deal | A real competitive process — see below |

### The volume correction

An earlier answer put volume at 1–3 deals a week. The deal history shows **two closed deals in roughly eight months.** The first figure was probably read as *how much stock moves through the group*, not *how many deals Emmanuel closes*.

This is the third time a working assumption has been corrected by real data, and it is the largest correction of the three. Treat every remaining unverified number here as provisional in the same way.

**What it changes:** the business is not "low volume." It is pre-revenue. The OS should stop optimising deal quality — two deals a year does not have a quality problem — and concentrate entirely on **deal count**. Gates, scorecards and margin discipline are defending capital that is not at risk and time that is not scarce.

### The vendor price-check — the one process that already works

When a buyer appears, Emmanuel:
1. Asks **Yemi** for the current price
2. Asks **Matte (Matthew)** for his price
3. Compares the two
4. Takes whichever leaves the better margin

This is genuinely good practice and it is already habit. It is also the reason the two-vendor position matters beyond the supplier gate: **competing quotes per deal is a margin lever, not just a redundancy measure.** Worth logging both quotes each time — the record of who wins on which model becomes real sourcing intelligence, and there is one visible discrepancy already (the ProBook 440 G6 at ₦270k versus ₦440k).

### Expected spread by ticket — guidance, not a gate

| Sell price | Expected spread |
|---|---|
| under ₦150k | ₦10,000 |
| ₦150k – ₦400k | ₦15,000 |
| ₦400k – ₦800k | ₦25,000 |
| ₦800k+ | ₦40,000 |

**The hard floor stays ₦10,000 everywhere.** A deal below its band still passes — it is flagged as underpriced for the work, not rejected. Rejecting a real ₦12k deal on a ₦435k phone would repeat exactly the mistake the ₦15k guess made.

These bands are **inferred from "it scales", not stated.** Emmanuel has not given the actual numbers per tier. Recalibrate from logged deals — queue `g007`.

---

## The Volume Read — What 1–3 Deals A Week Actually Means

**The constraint on this business is demand, not time and not capital.**

At 1–3 deals a week, Emmanuel is not running out of hours and he is not running out of stock — Ikeja has effectively unlimited supply. He is running out of **buyers**.

This inverts the OS's natural priorities. Most of the machinery built into it — sourcing discipline, supplier scorecards, margin gates — optimises a constraint he does not currently have. They are still worth keeping because they stop bad deals, but they are not where the growth is.

What follows from it:

1. **Content is the highest-return activity available, by a wide margin.** Not a side activity. Every hour not spent on a live deal should be building the audience that produces the next one. `playbooks/content-strategy.md` is the growth document; the qualification rubric is merely the defence.
2. **Thin deals are less bad than they look.** At 8+ deals a week, a ₦10k deal crowds out a ₦40k one and should be refused. At 1–3, there is nothing being crowded out — the alternative is an idle day. Take it, and note it.
3. **Raising the floor is the wrong first move.** The instinct at low volume is to protect margin. The correct move is to widen the top of the funnel; margin discipline matters once there is competition for the hours.
4. **A single repeat buyer is worth more than a better vendor price.** Referral share is the metric that compounds here.
5. **Higher-ticket units are the cheapest growth available.** Same work, more spread. Moving from ₦400k phones to ₦800k phones roughly doubles the week without adding a single deal.

**When this flips:** at roughly 8 deals a week the constraint becomes time, and every point above reverses. That is also the point at which holding stock starts to pay.

---

## The "Sometimes I Hold It" Rule

Emmanuel collects the phone himself on some deals; on others the vendor delivers straight to the buyer. That mixed reality is the most dangerous version, because the same brand voice ends up covering two very different levels of knowledge.

**The rule: verification status is a property of the deal, and the listing must match it.**

| Deal type | What may be published |
|---|---|
| **He collects and checks it** | Verified specs, stated flatly: *"Battery 91%, checked today"* + the battery screenshot. Full Hephzibah position. |
| **Vendor delivers direct** | **Attributed claims only:** *"Seller states battery 91% — I have not held this unit."* No verified-spec table. No inspection photos. |

Never publish a spec as checked on a unit that was never held. One buyer discovering that costs more than the margin on every deal that month — see [[trust-as-margin]].

**And the flag has to be recorded**, not just remembered: every pipeline row and product node carries `verified: true|false`. When a complaint arrives, the first question is which kind of deal it was, and that has to be answerable from the record rather than from memory.

**The strategic version of this question:** direct-delivery deals are the ones that can end the business, and they are worth the least defending. The natural resolution as volume grows is to collect personally on high-ticket deals — where the spread justifies the trip — and be plainly honest about the rest.

---

## Linked

[[gadget-index]] · [[trust-as-margin]] · [[capital-velocity]] · [[gadget-pricing]] · [[matte]] · [[yemi-group]] · [[middleman-lesson]]
