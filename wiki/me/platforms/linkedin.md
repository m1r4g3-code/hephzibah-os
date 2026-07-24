---
sensitivity: public

aliases: []
entity_type: platform
handle: hephzibah-ifeoluwa-2ab82b2b7
last_audited: 2026-07-24
name: LinkedIn
platform: LinkedIn
relationships:
- first_seen: '2026-05-27'
  last_reinforced: '2026-07-24'
  strength: 3
  target: '[[middleman-lesson]]'
  type: mentioned_in
- first_seen: '2026-05-27'
  last_reinforced: '2026-07-24'
  strength: 2
  target: '[[builds-before-asking]]'
  type: mentioned_in
- first_seen: '2026-07-24'
  last_reinforced: '2026-07-24'
  strength: 1
  target: '[[linkedin-brand-system]]'
  type: implements
status: active — content publishing started 2026-07-24
type: platform-audit
url: https://www.linkedin.com/in/hephzibah-ifeoluwa-2ab82b2b7
---

## Current State (as of 2026-07-24)

Profile active. Content publishing started with SavvySox hologram post.
Custom URL not yet set — still using `2ab82b2b7` default suffix.

---

## What LinkedIn Success Looks Like

| Metric | Target |
|--------|--------|
| Connections | 500+ (first credibility milestone) |
| Profile completeness | 100% |
| Custom URL | `/in/hephzibah-ifeoluwa` |
| Headline | Role + who you help + result |
| About section | 3 paragraphs: what you build, proof, CTA |
| Featured section | Contra profile + best case study |
| Post frequency | 2–3x/week |

---

## Headline Formula

`[What you do] for [who] → [result they get]`

**Best option:** "AI Automation & Creative Systems | I build infrastructure for brands that move fast"

---

## Content Strategy — The Hephzibah Model

### Post Types (in order of priority)

**1. Project Post** ← primary format
Shows a completed project. Hook on the result → story of the brief → what it unlocked → infrastructure frame → engagement question.

Structure:
```
[Hook — 1 specific number or result. No context yet.]
[Client context — who reached out, for what]
[What we turned it into — the unexpected direction]
[Brief — exact words if possible]
[Delivery numbers — specific]
[The pivot moment — what the client asked next]
[What I'm building next — automation angle]
[Infrastructure frame — 1-2 lines on why this matters]
[Engagement question — business-specific, not generic]
```

Example (SavvySox, 2026-07-24):
> "I made 13 of these in 2 days.
> A sock brand in California reached out to Adelaja Obanijesu looking for product videos.
> We turned it into something else entirely.
> Brief: make the socks look like they're floating in space. Black background. Neon glow. 3D rotation.
> 13 styles. Every single one approved.
> Then the client asked: 'Can you do all 50 faster?'
> That's when we talked about automation.
>
> What I'm building next: drop a sock image into a Google Drive folder → finished hologram video appears automatically. No editor. No manual work. No waiting.
>
> For a product brand launching new designs monthly, that's not a feature.
> That's infrastructure.
> What's the most repetitive visual task in your business that nobody's thought to automate yet?"

**2. Build-in-Public Post**
Document something mid-build. Show the technical decision. Show the tradeoff. Not a finished product — a real moment in the process.

**3. Lesson Post**
One pattern extracted from recent client work. Framed as observation, not advice. Short. Ends with a reframe.

**4. Proof Post**
Before/after. Numbers only. No fluff. The image card carries the weight; text is minimal.

---

## Image Card System

Every post with a visual gets a branded card rendered via `scripts/render_card.py`.

See [[linkedin-brand-system]] for the full visual spec.

**Quick render command:**
```
python scripts/render_card.py \
  --image PATH_TO_HERO_IMAGE \
  --eyebrow "CLIENT × HEPHZIBAH — PROJECT TYPE" \
  --quote "Exact client brief or key line" \
  --stats "N deliverables · N days · Result" \
  --role1 "Creative direction" --name1 "Collaborator Name" \
  --role2 "Automation design" --name2 "Emmanuel Adekoya" \
  --theme both
```

Outputs `card_light.png` and `card_dark.png` to Desktop. Pick one to post.

---

## Post Angles Bank

1. *"I made 13 hologram product videos in 2 days for a sock brand. They asked for 50."* → SavvySox [[heygen]]
2. *"I built 4 automation workflows in 4 days for a German clinic. On day 5, the middleman cut me out."* → [[4-workflows-4-days]] + [[middleman-lesson]]
3. *"I rebuilt a NYC florist's entire website as a cold outreach demo — before they responded to a single message."* → [[builds-before-asking]]
4. *"We lost $12,500 in pipeline because I didn't have client contact info off-platform."* → platform diversification lesson
5. *"Why I stopped pitching my services and started building demos for people who hadn't asked."*

---

## Next Actions

1. **Set custom URL** — Edit Profile → Edit public profile & URL → `/in/hephzibah-ifeoluwa`
2. **Post SavvySox project post** — copy + card_light_v4.png, tag @Adelaja Obanijesu
3. **LinkedIn Projects section** — write 3 project descriptions: SERAMAN, Noryx Studio, SavvySox
4. **LinkedIn Recommendations** — request from 5+ contacts (Oba, Elbert, past clients)
5. **Post frequency** — 2x/week minimum going forward

## See Also

[[brand]] · [[linkedin-brand-system]] · [[github]] · [[contra]]
