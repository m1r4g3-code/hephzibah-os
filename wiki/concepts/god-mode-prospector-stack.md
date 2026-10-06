---
name: god-mode-prospector-stack
description: Full tool acquisition map for god-mode cold outreach. Tier 1 (free now), Tier 2 (when scaling), Tier 3 (when revenue supports it).
type: reference
created: 2026-09-02
sensitivity: private
---

# God-Mode Prospector — Tool Stack

## What god-mode actually means

Not more messages. Right person + right pain + right moment + right message.
The tools below either (a) find people who are ALREADY searching for a solution, or
(b) make every message land harder. Both matter.

---

## Tier 1 — Get These Today (Free or Near-Free)

### Hunter.io
- Site: hunter.io
- Cost: Free (25 domain searches/month)
- Why: Email finder. Give it a domain, get the best email for the company.
- Setup: Register, copy API key, paste into `config.py` as `HUNTER_API_KEY`
- Impact: HIGH — unlocks email finding for all prospector sources

### Apollo.io
- Site: apollo.io
- Cost: Free (50 credits/month). Each credit = 1 person enriched.
- Why: Finds decision-maker emails + LinkedIn + job titles. More powerful than Hunter alone.
  Returns CEO/Founder emails directly. 50 credits = 50 verified leads/month for free.
- Setup: Register, go to Settings > API Keys, copy key into `config.py` as `APOLLO_API_KEY`
- Impact: HIGH — signal_hunter.py and prospector.py both use this automatically when key is set

### Adzuna Job API
- Site: developer.adzuna.com
- Cost: Free (50,000 API calls/month free tier)
- Why: Job board API. Gives structured job post data — company name, salary, location, description.
  Powers the signal_hunter.py job-signal prospecting alongside RemoteOK.
- Setup: Register at developer.adzuna.com, get App ID + App Key, add to config.py
- Impact: MEDIUM — expands signal_hunter.py results beyond RemoteOK (which is US remote-only)

### BuiltWith Free API
- Site: builtwith.com/free-api
- Cost: Free (limited calls)
- Why: Detects tech stack for any website. If a prospect is on Zapier, pitch n8n as a replacement.
  If they have no scheduling tool, that's a gap. Already partially built in prospector.py.
- Setup: Register, get free API key
- Impact: MEDIUM — improves observation quality in the prospector website analysis

---

## Tier 2 — When Revenue Starts ($50-150/month range)

### Apollo.io Basic ($49/month)
- Cost: $49/month for 240 credits
- Why: 240 verified decision-maker emails per month. At 10 outreach/day, 30 days = 300 sends.
  Apollo Basic covers nearly all of that with verified emails (vs scraping guesses).
- When to get: When free 50 credits run out consistently each month

### Hunter.io Starter ($49/month)
- Cost: $49/month for 500 domain searches
- Why: Covers gaps Apollo misses. Different data sources = higher hit rate when used together.
- When to get: When Apollo + Hunter free tiers are both maxed

### Instantly.ai or Smartlead ($37-39/month)
- Sites: instantly.ai | smartlead.ai
- Why: Email deliverability. When sending 20+ cold emails/day from Gmail,
  deliverability drops. These tools warm the domain and rotate inboxes.
  Without this, emails go to spam at scale.
- When to get: When daily volume consistently hits 15+ emails/day

### Apify ($5-10/month for usage)
- Site: apify.com
- Why: Cloud-based scraping. Has pre-built LinkedIn Job Scraper actor.
  Finds job posts without running Playwright locally. Pay per result.
- When to get: If signal_hunter.py RemoteOK + Adzuna aren't enough volume.
  LinkedIn job posts = 100x the volume of RemoteOK.
- Impact: HIGH — LinkedIn has millions of job posts. This unlocks that.

---

## Tier 3 — When Revenue Supports It ($150-400/month)

### Clay ($149/month Explorer)
- Site: clay.com
- Why: THE tool serious SDR teams use. Waterfall enrichment across 50+ data sources.
  If Apollo doesn't have an email, it tries Hunter. If Hunter fails, it tries Clearbit.
  If that fails, it tries Snov.io. One row in a Clay table can pull from all of them
  automatically. 90%+ email find rate vs 50-60% with one source alone.
  Also has an AI research column that writes personalised emails per row.
  This replaces the custom enrichment code in the prospector entirely.
- When to get: When revenue supports it. This is the final form of the prospector.

### LinkedIn Sales Navigator ($99/month)
- Site: linkedin.com/sales/
- Why: Advanced LinkedIn search + signal tracking. Get notified when someone at
  a target company changes jobs (high-intent signal). Filter by company growth signals.
  Post intent signals (people who liked/commented on specific content).
  The algorithm that powers signal_hunter.py becomes 10x more targeted with Sales Nav.
- When to get: When Tier 1-2 tools are maxed out and LinkedIn signals are the bottleneck.

### Lemlist ($59/month)
- Site: lemlist.com
- Why: Multi-channel outreach sequences. Send email on day 1, LinkedIn DM on day 3,
  email follow-up on day 5 — all from one place. Currently doing each channel manually.
  Lemlist automates the sequence management while keeping personalisation.
- When to get: When volume requires sequence automation (50+ prospects in active sequences)

---

## LinkedIn MCP — Does It Exist?

There is no official LinkedIn MCP.
Community implementations exist but violate LinkedIn TOS and are unstable.
The safe approach: use Apify's LinkedIn Job Scraper (cloud-based, managed, TOS-compliant for research).

---

## The Current vs God-Mode Stack Comparison

| What | Current | God-Mode |
|---|---|---|
| Prospect finding | Google Maps, DesignRush | + RemoteOK, Adzuna, Apify LinkedIn, Clay |
| Email finding | Scraping only (no key set) | Apollo (50/mo free) + Hunter fallback |
| Email quality | Observation-based | + Competitive intelligence hooks |
| Deliverability | Gmail API direct | + Instantly/Smartlead domain warming |
| Sequences | Manual per prospect | + Lemlist multi-channel sequences |
| Rhythm tracking | None | daily_tracker.py (built) |
| Signal targeting | Location/category only | + Job-posting intent signals (signal_hunter.py) |

---

## What to Do Right Now (Today, Free, 30 Minutes)

1. Go to hunter.io — register, copy API key, paste into config.py as HUNTER_API_KEY
2. Go to apollo.io — register, go to Settings > API Keys, paste into config.py as APOLLO_API_KEY
3. Go to developer.adzuna.com — register, get App ID + App Key, paste into config.py
4. Test: `python scripts/signal_hunter.py --list-roles`
5. First run: `python scripts/signal_hunter.py --role social-media --limit 5 --dry-run`
6. Full scan: `python scripts/signal_hunter.py --scan --limit 3`

That's 24+ signal-based prospects per scan. Run it daily.

---

## The Math (Why This Works)

10 messages/day x 5 days/week x 20 weeks (Q4) = 1,000 outreach messages.
At 3% response-to-call rate = 30 discovery calls.
At 40% close rate on calls = 12 new clients.
At $2,000 average project = $24,000 Q4 revenue from outreach alone.

The math works. The question is: does the daily rhythm hold?
That's what daily_tracker.py tracks. That's what heartbeat surfaces every session.
