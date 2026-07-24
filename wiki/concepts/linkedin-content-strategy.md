---
sensitivity: private

aliases: [linkedin-posts, content-calendar, post-sequence]
entity_type: concept
last_updated: 2026-07-24
name: LinkedIn Content Strategy
relationships:
- first_seen: '2026-07-24'
  last_reinforced: '2026-07-24'
  strength: 2
  target: '[[linkedin]]'
  type: implements
- first_seen: '2026-07-24'
  last_reinforced: '2026-07-24'
  strength: 1
  target: '[[linkedin-brand-system]]'
  type: uses
---

## What We're Exploiting

### Algorithm Psychology
- LinkedIn boosts posts that get comments in first 60 minutes — engineer the question at end of every post
- Short paragraphs + white space = high dwell time = reach multiplier
- No external links in post body — LinkedIn suppresses them. Link goes in FIRST COMMENT only
- Native visual content (screenshots, workflow images) = 3-5x more reach than text only
- Multiple images (2-3) > single image — more scroll time = more dwell time signal
- Posting 3x per week tells algorithm account is active — consistency beats volume
- Reply velocity in first 60 minutes is the single biggest algorithm lever — reply to EVERY comment with substance, not just "thanks"

### Human Psychology Levers
- Before/after contrast — brain is wired to notice transformation
- Specific numbers — "13 videos in 2 days" beats "fast delivery" every time
- Scroll-stop visual — one striking image buys 3 extra seconds of attention
- Vulnerability/confession — "I made this mistake" outperforms bragging every time
- Identity confirmation — "if your business still does X manually..." makes them feel seen
- Curiosity gap — first 2 lines must create a question BEFORE "see more" cuts off
- **War story question** — "What's the most [adjective] [experience] you've had?" gets more comments than "what do you think?" because it asks for personal experience, not opinion
- **"What it actually is" reframe** — flip the expected narrative. "Most people think automation is building the cool thing. It's actually the 80% debugging silent failures." Contrarian honesty = comments from peers who feel seen
- **Hyper-specific failure details** — "A casing mismatch between 'Link' and 'link'" is more credible than "I debugged an issue." Specificity = proof of real work = trust from clients AND peers
- **Debugging transparency** — showing what broke and why outperforms showing what succeeded. Silent failures angle is particularly powerful in the automation community

### New Learnings (from competitor analysis 2026-07-24)
Source: Chukwukaidibia Onyekwere (n8n Ambassador) — 157 reactions, 32 comments on a debugging post

What drove the numbers:
1. The engagement question asked for a **personal war story**, not an opinion — "What's the most deceptive bug you've debugged?" = everyone has one = 32 comments
2. He **replied to every single comment with substance** — not "thanks" but actual technical engagement. This kept the thread alive for 3 days.
3. Three workflow screenshots (not one) — maximum dwell time
4. **"What it actually is" frame** was the hook — the 80/20 flip on what automation work really is
5. **Specific failure details** were the credibility signal — clients reading it trusted him immediately

---

## Content Pillars

| Pillar | What it does | Source material |
|--------|--------------|-----------------|
| Case study proof | Shows real client work with real outcomes | SERAMAN, SavvySox, Revamp, German surgeon |
| Process transparency | Shows how you think and build | Workflow screenshots, Looms, architecture |
| Debugging honesty | Shows the real work — what broke and why | Any real build has this |
| Contrarian take | Generates comments, signals positioning | Pricing, niche, AI opinions |
| Personal story | Builds parasocial connection | Lagos → global clients journey |

---

## Hard Schedule

Post 1 was live 2026-07-24 (Thursday). Schedule from there:

| Post | Date | Day | Time (WAT) | Topic | Status |
|------|------|-----|-----------|-------|--------|
| Post 1 | 2026-07-24 | Thu | Posted | SavvySox hologram | ✓ LIVE |
| Post 2 | 2026-07-26 | Sat | 8:00 AM WAT | SERAMAN — what it actually took | Build now |
| Post 3 | 2026-07-29 | Tue | 8:00 AM WAT | Lagos → global, outcome pricing | Ready |
| Post 4 | 2026-07-31 | Thu | 8:00 AM WAT | SERAMAN deep case study | Pending |
| Post 5 | 2026-08-02 | Sat | 8:00 AM WAT | Hot take — AI automation | Pending |
| Post 6 | 2026-08-05 | Tue | 8:00 AM WAT | Behind the scenes build | Pending |

**Time:** 8AM WAT every post. Overlaps with UK morning (8AM BST), US East night (3AM EST — LinkedIn indexes overnight, surfaces at scroll-time). Consistent time trains algorithm and audience.

**Revamp post** — shelved until build is complete and has real screenshots. Will replace Post 4 or 5 when ready.

---

## Post 1 — SavvySox (LIVE 2026-07-24)

See `content/posts/2026-07-24-savvysox-hologram.md`

---

## Post 2 — SERAMAN: What It Actually Took (2026-07-26, 8AM WAT)

**Pillar:** Debugging honesty + Process transparency
**Psychology:** The "what it actually is" reframe. Clients see real engineering. Peers feel seen. War story question at the end pulls comments.
**Images:** SERAMAN workflow screenshots — `outputs/assets/workflow-main.png` + `outputs/assets/workflow-edit.png`

**Copy:**
```
Building an AI video pipeline sounds clean on paper.

Then you actually build it.

I spent 3 weeks on a system for an Italian furniture brand — 
automated product video generation, end to end.

Here's what nobody shows you:

→ HeyGen renders completed. Script said success. Video was blank.
→ Google Sheets auto-mapping silently wrote to the wrong column for 2 days.
→ The polling loop hit the API rate limit at exactly frame 7 of 8. Every time.

None of them threw errors. All of them looked like the workflow ran clean.

This is 80% of what automation engineering actually is. Not wiring nodes together — 
that's the easy part. It's sitting with a system asking: 
"Is this actually true, or does it just look true?"

The client now has a pipeline that takes a product image + description, 
generates a full Italian-language video in 3 AI voices, 
and publishes to Instagram, TikTok, and YouTube automatically.

But between spec and that — it looked like it was working 
about a dozen times before it actually was.

What's the most convincing "it's working" lie a system ever told you?
```

**Card:** Branded card with SERAMAN workflow screenshot as hero image
**First comment:** `#n8n #AIAutomation #BuildInPublic #Automation #AIVideoGeneration — I build automation pipelines for product brands. Work: [portfolio link]`

---

## Post 3 — Lagos → Global (2026-07-29, 8AM WAT)

**Pillar:** Personal story + Contrarian take
**Psychology:** Identity + vulnerability + aspirational reframe. Nigerian developer community engages hard. Clients see someone who prices differently.
**Images:** None needed — text post lands harder with no image here

**Copy:**
```
Lagos. No connections. No referrals. $0.

That was me 18 months ago.

Today I'm building automation systems for brands in Italy, California, and the UK. From my room.

Not because I'm exceptional. Because I stopped competing on price.

Most developers from Nigeria charge $5-10/hour. I charge $40-50. I get hired over them.

The difference isn't skill level. It's what you're selling.

"I'll work for you hourly" — you're selling time. Time is cheap everywhere.
"Your manual process, automated, running in 2 weeks" — you're selling an outcome. Outcomes are expensive.

The market doesn't care where you're from. It cares what problem goes away when you show up.

I figured that out later than I should have.

If you're a developer still charging by the hour — what would change if you priced the outcome instead?
```

**First comment:** `#Freelancing #AIAutomation #n8n #NigerianDeveloper #RemoteWork — I build automation systems for businesses. Work: [portfolio link]`

---

## Posting Rules — Non-Negotiable

1. **Hard time:** 8AM WAT every post — no exceptions, no "I'll post later"
2. **Stay online 60 minutes after posting** — reply to EVERY comment with a real sentence. Not "thanks." Not an emoji. A real response that keeps the thread alive.
3. **War story engagement** — when someone shares their experience in comments, ask one follow-up question. Keeps them in thread, boosts algorithm.
4. **No hashtags in post body** — hashtags in first comment only, posted immediately after
5. **First comment template:** `#[Tag1] #[Tag2] #[Tag3] — I build [thing] for [who]. Work: [link]` — live within 60 seconds of the post going up
6. **Never post two days in a row** — minimum 48 hours between posts (schedule above enforces this)
7. **No external links in post body** — LinkedIn suppresses reach. All links in comments.
8. **Multiple images where possible** — 2-3 native images beats 1 every time

---

## Performance Tracking

Log to `content/posts/YYYY-MM-DD-slug.md` at 1h, 24h, and 7d:
- Comment count + what the engagement question attracted
- Reaction count
- DMs / profile visits spike
- 7-day reach
- Any leads generated

## See Also

[[linkedin]] · [[linkedin-brand-system]] · [[active-agent-mode]]
