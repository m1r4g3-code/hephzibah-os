---
sensitivity: private
entity_type: company
name: "Axis Numérique"
platform: upwork
status: "prospect"
created: "2026-08-30"
updated: "2026-08-30"
off_platform_contacts:
  email: "info@axisnumerique.com"
  phone: "+1 438-533-5615"
  website: "https://axisnumerique.com"
  address: "4388 rue Saint-Denis, Suite 200, Montréal QC H2J 2L1 (virtual office — Montréal Cowork)"
  booking: "lien.axisnumerique.com/widget/booking/hAfUuNhdZIWR2KpDtoke"
  also_operates: "gohighlevelquebec.com (301 redirects to axisnumerique.com)"
founder_lead:
  name_signal: "R. Tremblay or R. Tremblay-Gagné (UNCONFIRMED — weak signal only)"
  note: "Website has no team page. Identity deliberately obscured. Do not use in proposal without verification."
---

# Prospect: Axis Numérique — AI Browser Agent Build

**Platform:** Upwork job posting
**Job URL:** https://www.upwork.com/jobs/~022093882211872096319
**Job budget:** $300 fixed (likely low for actual scope — budget conversation needed)
**Proposals at posting:** 8
**Connects cost:** 18
**Upwork client ID:** 7665664

---

## Company

**Axis Numérique**
- Website: axisnumerique.com (live, fully built)
- Also: gohighlevelquebec.com → 301 redirects to axisnumerique.com
- Domain registered: June 4, 2026 (Cloudflare registrar, WHOIS privacy-protected)
- gohighlevelquebec.com registered: February 17, 2026 (Hostinger)
- Both domains very new — either brand new company or rebrand. Upwork activity dates to September 2025, so they operated under a different name before.
- Core positioning: "Votre partenaire francophone exclusif pour l'écosystème HighLevel" — Quebec's exclusive French-language GoHighLevel partner.
- Market claim: 300+ HighLevel integrations, 48-hour deployment, 5x average ROI in 90 days, 94% customer satisfaction.
- White-label product possibly branded "ORA" (referenced in homepage testimonial).

**Address reality:** 4388 Saint-Denis is Montréal Cowork — a virtual office/coworking space in Plateau-Mont-Royal. Multiple other companies use this exact address. This is a 1-2 person operation working remotely, not a staffed office.

---

## Business Model

**GoHighLevel white-label SaaS reseller + implementation agency** serving Quebec's francophone SMB market.

Revenue streams:
1. Monthly GHL subscriptions resold at markup ($97+/month per client)
2. Done-for-you integration fees (one-time setup)
3. 2-day bootcamp training (priced on consultation)
4. Private coaching and monthly support retainers
5. Agency-in-agency white-label (other agencies reselling their platform)
6. Circle.so community membership (paid community, currently being automated with Claude)

Industries served: Real estate agencies, health clinics, professional services, construction/renovation, education/coaching, food service.

---

## Live Tech Stack (from Upwork contract history)

| Platform | Role |
|---|---|
| GoHighLevel | Core CRM/platform, white-labeled as "ORA" |
| n8n | Backend automation engine |
| Claude AI (Anthropic) | AI layer — autonomous SaaS operations |
| Circle.so | Paid community platform (being automated with Claude) |
| Zoho | Previous CRM for clients — migrating them to GHL |
| WordPress | Some client integrations |
| Voice AI (Retell or similar) | Voice bot product offering |

---

## Upwork Client Profile

| Metric | Value |
|---|---|
| Total jobs posted | 65 |
| Total spent | $11,920.53 |
| Total hires | 25 |
| Average per hire | ~$477 |
| Freelancer rating | 4.76 / 5 |
| Simultaneous active contracts | 3 (as of Aug 30 2026) |

**Spend pattern:** Posts many small, scoped tasks. Not large retainers. $300 is consistent with their hiring behavior. Nail the first job and there are multiple active projects to expand into.

**Recent contract history:**
- "GHL automation marketing, leads generation & conversion" (5 stars, ended Aug 17 2026)
- "n8n for data migration Zoho → GHL + autonomous AI marketing" (5 stars, ended Jul 31 2026)
- "GHL + WordPress integration" (ended Aug 14 2026 — freelancer gave client 1 star)
- "Voice AI Bot (SMS, webchat, email)" (ended Feb 2026, 4 stars)
- "Claude Code use AI to rank high on Google" (ended Sep 2025, 5 stars)

**Red flag:** One freelancer gave this client 1 star (GHL + WordPress contract). Watch for scope changes or difficult communication.

**Active now (3 contracts running simultaneously):**
1. GHL automation marketing / leads / conversion
2. Autonomous SaaS GHL + Circle.so with Claude AI
3. GHL + WordPress integration

---

## The Job: AI Browser Agent buildup

**Scope:**
- Build browser automation agent using Claude Agent SDK + computer-use/browser-use tools
- Implement the agent loop (tool call → execute action → return result → repeat)
- Sandboxed containerized execution environment (Docker)
- Front-end UI for triggering, monitoring, reviewing agent runs
- Guardrails: domain allowlisting, human confirmation checkpoints, prompt-injection safeguards
- Authentication, session management, deployment (hosting, CI/CD)
- Documentation

**Stack required:** Python or TypeScript/Node.js, LLM API integration, Playwright/Puppeteer, Docker.

**What they're likely using it for:** Automating browser-based actions inside GoHighLevel's UI (which doesn't expose API endpoints for everything), scraping sources without APIs, or automating client onboarding workflows that require a live browser. Could also be for lead generation automation.

**Budget reality:** $300 for a full Claude SDK computer-use agent with Docker, UI, guardrails, and docs is low. They may not understand market rate, or this is a scoping test. Propose Phase 1 as proof-of-concept (working agent loop in sandboxed environment), gate Phase 2 on that success.

---

## Founder Identity

**Not confirmed.** Website has no team page, no about page with names, no social profiles. Deliberately obscured.

Weak signal: "R. TremblayGagné" appeared in search excerpts from gohighlevelquebec.com — may be a testimonial or may be the founder. "Tremblay-Gagné" is a common Québécois surname. First initial "R." Do not use this in a proposal without confirming.

---

## Social Media

None found publicly. No LinkedIn company page, Facebook, Instagram, YouTube, TikTok. Solo operator — focused on direct sales through website, not content marketing.

---

## Proposal Strategy

**Kill shot / opening:**
"Your Claude + Circle.so automation contract is running right now — you're already building autonomous AI infrastructure on GHL. A browser agent using the computer-use API is the logical next layer: gets into GHL UI areas the API doesn't touch."

**Scope framing:**
"$300 for a full Claude SDK computer-use agent with Docker, guardrails, UI, and docs is tight. I'd structure this as Phase 1 (working agent loop in sandbox, proof the approach works) then Phase 2 (full build with UI and deployment) — that protects you from overcommitting budget before you know the agent performs."

**The francophone acknowledgment:**
Brief mention that you understand their market (Quebec francophone SMBs) without making it a centerpiece. Signals research.

**Their pattern:**
They post many small tasks. Win this one and there are 3 active contracts with room to grow. The real opportunity is relationship, not this single $300 job.

---

## Status Log

| Date | Event |
|---|---|
| 2026-08-30 | Job found on Upwork (8 proposals). Deep OSINT complete. Company identified as Axis Numérique. Website, email, phone, address confirmed. Business model mapped. Client node created. |
| 2026-08-30 | Cold email sent to info@axisnumerique.com. Subject: "GHL browser agent". Gmail Message ID: 1a0541a0e47d1919. Status: outreach_sent. |

---

## Next Action

Watch for reply to adekoyaafolasade29@gmail.com. If no reply in 72 hours, follow up or call +1 438-533-5615. When connects are available, also bid on the Upwork job. Frame Phase 1 as proof-of-concept to protect against the $300 budget ceiling.

[[financial-fragility]]
