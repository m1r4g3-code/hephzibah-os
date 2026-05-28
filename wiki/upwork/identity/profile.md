---
sensitivity: private
entity_type: concept
name: Upwork Profile State
aliases:
- upwork-profile
- profile-optimization
last_updated: '2026-05-28'
relationships:
- target: '[[identity]]'
  type: part_of
  strength: 9
  first_seen: '2026-05-27'
  last_reinforced: '2026-05-27'
- target: '[[social-proof-gap]]'
  type: reinforces
  strength: 8
  first_seen: '2026-05-27'
  last_reinforced: '2026-05-27'
---

# Upwork Profile State

Current state of Emmanuel's Upwork profile. Track all profile metrics here. Update after each week of activity.

---

## Current Profile Status

**Profile last reviewed:** 2026-05-27 (initial setup)
**Account status:** New / Building

### Metrics (update weekly)

| Metric | Current | Target (30d) | Target (90d) |
|---|---|---|---|
| JSS | — | — | 90%+ |
| Reviews | 0 | 1+ | 5+ |
| Hourly rate set | — | $35–50 | $60–80 |
| Profile completion | — | 100% | 100% |
| Top Rated status | No | No | Working toward |
| Portfolio pieces | 0 | 2+ | 5+ |
| Specializations | None | 1 set | 2 set |

---

## Profile Optimization Checklist

### Bio / Title
- [ ] Title: specific, not generic ("AI Workflow Engineer — n8n · Claude API · Full-Stack" not "Software Developer")
- [ ] First paragraph of bio: specific outcome + specific proof (not "I'm passionate about technology")
- [ ] Bio includes: who I help, what I build, one specific proof point
- [ ] Bio does NOT include: "I am passionate", skills list, generic claims

### Skills Section
- [ ] AI automation skills listed: n8n, Claude API, OpenAI, workflow automation
- [ ] Full-stack skills: Next.js, React, TypeScript, Python, PostgreSQL
- [ ] Niche skills: no deprecated or irrelevant ones

### Portfolio
- [ ] At least 2 portfolio items before first bid
- [ ] Each portfolio item: real outcome, specific numbers, tech used

**CRITICAL FLAG — What can and cannot be used:**
The German medical clinic workflows (4 workflows, 4 days) were done as a middleman under another person's Upwork account. They CANNOT be listed as Upwork portfolio items (Upwork will find the mismatch). They can be referenced verbally ("I built similar workflows in a prior engagement") but not documented on the profile.

**Real portfolio items available (from GitHub — all verifiable):**

| Item | What to show | Proof angle |
|---|---|---|
| `Distill` | URL → structured JSON for AI pipelines | AI data engineering, n8n-ready outputs — his own project |
| `n8n-Aigent-app` | Webhook-driven n8n workflow manager | n8n expertise, real system — his own project |
| `yct-exam-nav-system` | Graph coloring + Dijkstra shortest path | CS fundamentals, TypeScript depth — his own project |
| `Viral-ShortsAi` | AI-powered shorts from long video | AI product thinking — his own project |
| `Habit-Tracker` | Mood-aware gamified habit tracker | Full-stack React/TypeScript depth — his own project |

Note: Arroxy, hyperframes, open-design, tradingview-mcp-jackson are FORKS. Do not present as his own work on Upwork profile.

**Priority for portfolio build:**
1. Create a demo video (Loom) of n8n workflow in action — most relevant to AI automation niche
2. Document Distill with a real use case (e.g., "feed any URL into an n8n node as structured data")
3. Screenshot/record open-design as a technical depth signal

### Tests / Certifications
- [ ] Upwork Skill Certifications (if offered in niche)

---

## Profile Narrative

This is what the bio should communicate (update as actual bio is written):

"I build AI-native automation systems that replace the manual work your team is doing every day. Not wrappers around ChatGPT — full workflow architectures using n8n, Claude API, and your existing stack.

Recent: built 4 production AI workflows for a German medical admin team in 4 days. Admin time on [specific task] dropped from [X] hours to [Y] minutes.

I work with SaaS founders, agencies, and operations teams who have systems that should be automated but aren't."

---

## Review Engineering Log

After each successful project, use this protocol:
1. Deliver beyond scope on one small thing (unexpected bonus)
2. Send end-of-project summary: what was delivered, key decisions made, how to extend it
3. 3 days after delivery, ask for review: "If our work together met your expectations, I'd really appreciate a review on Upwork — it helps me get in front of clients who need similar work."
4. Do NOT ask for 5 stars specifically. Do NOT ask before delivery confirmation.

| Date | Client | Review received | Score | Notes |
|---|---|---|---|---|
| — | — | — | — | — |

---

## Wikilinks

[[identity]] · [[social-proof-gap]] · [[4-workflows-4-days]] · [[builds-before-asking]]

### Profile Audit — Cross-Platform Roast 2026-05-28 — 2026-05-28 09:14

## Portfolio Site (v0-portfolio-website-plan-indol.vercel.app) — RATING: 3/10

### CRITICAL ISSUES (fix today)

1. **Fake testimonials** — Sarah Chen/NexaStream, Marcus Thorne/Peak Logistics, Elena Rodriguez/ScaleUp AI, Priya N./FinEdge, Daniel K./CloudWorks — all AI-generated names and fake companies. Only Cyrus is real. A client who Googles any of these and finds nothing will blacklist Emmanuel and warn others.

2. **'Trusted by Industry Leaders' logo strip** — Microsoft, Google Cloud, Salesforce, Shopify etc. Emmanuel has NOT worked with these companies. This is an unmodified template. Any serious client sees this and thinks fraud.

3. **Broken live metrics showing 0** — '0hrs Hours Saved | 0 Active Automations | 0 Projects Delivered | 0.0% System Uptime' — counters that were never configured. Worse than not having them.

4. **'7+ years building production AI systems'** — He is 20. Started Nov 2025. This is a lie. Will destroy trust the moment any client checks.

5. **'Shipped 50+ automation workflows for global clients'** — Real number: 4 (German clinic, under another account). The gap is not rounding — it is a character issue.

6. **'Former engineer at high-growth B2B SaaS companies'** — False. No employment history backs this.

### What's good on the site
- Tech stack is accurate and specific (n8n, Claude API, Make.com, Supabase, VAPI, Twilio)
- Process section (Analyze → Design → Engineer → Optimize) is clean
- Contact info visible (email + Telegram)

---

## GitHub (m1r4g3-code) — RATING: 7/10

**Strongest asset, undersold everywhere.**

Real and compelling: yct-exam-nav-system (DSatur + Dijkstra), Distill (URL→JSON for AI pipelines), n8n-Aigent-app + n8n-workflow-app (real n8n depth), Viral-ShortsAi, Habit-Tracker, 40+ repos total.

**Issues:**
- Forks (n8n main, ComfyUI, LangFlow, excalidraw etc.) sitting in profile dilute signal — unstar/unpin
- Most repos have no README, no screenshot, no one-line description
- Ramshaw principle: first 10 seconds must communicate value. Currently just raw code.

---

## Immediate Action List (priority order)

1. TODAY: Remove all fake testimonials except Cyrus
2. TODAY: Remove 'Trusted by Industry Leaders' logo strip
3. TODAY: Fix or hide broken live metrics (0hrs, 0 automations, 0 projects)
4. THIS WEEK: Replace '7+ years' with the real story — 40+ shipped GitHub projects, freelancing since 2025, fast and technical
5. THIS WEEK: Add READMEs to Distill, n8n-Aigent-app, yct-exam-nav-system (one paragraph + screenshot)
6. THIS WEEK: Upwork profile to 100% — bio, title, skills, 2+ portfolio items
7. THIS WEEK: Loom video of n8n workflow running — highest ROI action for Upwork portfolio

---

## The Real Story (stronger than the fake one)

20-year-old in Lagos, 40+ shipped GitHub projects, deep n8n expertise proven by building workflow apps for himself, full AI stack (Claude API, n8n, TypeScript, Python, Supabase, VAPI), built 4 production workflows for a real client in 4 days, learning sales psychology and negotiation in parallel.

This story — told honestly — is more compelling to the right client than '7+ years, 50+ workflows.' The fake credentials attract wrong clients and repel right ones.