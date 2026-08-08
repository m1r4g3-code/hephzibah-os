---
sensitivity: private
entity_type: system
name: Priority Queue
last_updated: 2026-07-27
---

# Priority Queue — Upwork OS

Single source of truth for what needs to happen next, sorted by priority score.
Read by `scripts/heartbeat.py` at every session start.
Update when items are created, resolved, or change state.

Priority score = urgency_weight × revenue_multiplier
- CRITICAL = 100 (blocks revenue / hard deadline <24h)
- HIGH     = 70  (time-sensitive, 24-72h window)
- MEDIUM   = 40  (important, this week)
- LOW      = 10  (backlog, no hard deadline)

Revenue multiplier: DIRECT=1.5 | INDIRECT=1.0 | MAINTENANCE=0.5

---

<!-- MACHINE-READABLE BLOCK — parsed by scripts/heartbeat.py -->
```json
[
  {
    "id": "q001",
    "action": "Resolve Upwork account restriction",
    "context": "RESOLVED 2026-08-05. Restriction lifted. Own account (011b48d2eabbfa6361) now active and being built.",
    "priority": "CRITICAL",
    "revenue_impact": "DIRECT",
    "deadline": "2026-07-29",
    "owner": "Emmanuel",
    "created": "2026-07-27",
    "state": "resolved",
    "platform": "Upwork",
    "next_action": "Done."
  },
  {
    "id": "q016",
    "action": "Complete cert sprint: all n8n Academy + Anthropic Education courses",
    "context": "James D. competitor analysis (2026-08-07) revealed he holds 18 certs — 4 n8n Academy + 14 Anthropic Education — all completed in August 2026. All free. Keyword density, credibility signals, verification links. n8n Academy: learn.n8n.io (QS101, N8N101, N8N102, N8N103). Anthropic Education: education.anthropic.com (14 courses). Emmanuel currently has 4 certs. Target: 18+.",
    "priority": "HIGH",
    "revenue_impact": "INDIRECT",
    "deadline": "2026-08-14",
    "owner": "Emmanuel",
    "created": "2026-08-07",
    "state": "open",
    "platform": "Upwork",
    "next_action": "Go to education.anthropic.com → complete all 14 courses. Then learn.n8n.io → complete N8N102 and N8N103. Add each cert to Upwork profile as you finish with verification link."
  },
  {
    "id": "q017",
    "action": "Set up Project Catalog — 2 items",
    "context": "James D. competitor analysis revealed Project Catalog is a geo-neutral discovery channel. Two items: (1) AI agent built in n8n that runs a real task in your business every day — $499, 7 days. (2) Diagnose your broken n8n workflow and give you a written repair plan — $149, 3 days. Both items submitted to review 2026-08-07.",
    "priority": "HIGH",
    "revenue_impact": "INDIRECT",
    "deadline": "2026-08-14",
    "owner": "Emmanuel",
    "created": "2026-08-07",
    "state": "resolved",
    "platform": "Upwork",
    "next_action": "Done. Both items sent to review 2026-08-07."
  },
  {
    "id": "q018",
    "action": "Rewrite overview: add Recent work section + update closing CTA",
    "context": "James D. analysis revealed two gaps: (1) No Recent work section — SERAMAN needs operational language: four n8n workflows, exactly-once job tracking, error routing with amber/red alert classification, human review gate, Creatomate rendering, Blotato multi-platform publishing, running in production. (2) Closing CTA is sales pitch not advisory. Target: 'Tell me what you are trying to automate and I will tell you the simplest honest way to get it done.'",
    "priority": "MEDIUM",
    "revenue_impact": "INDIRECT",
    "deadline": "2026-08-14",
    "owner": "Emmanuel",
    "created": "2026-08-07",
    "state": "open",
    "platform": "Upwork",
    "next_action": "Run /profile-audit to get current overview text. Rewrite Recent work section and CTA. Paste into Upwork overview editor."
  },
  {
    "id": "q010",
    "action": "Complete Upwork ID verification",
    "context": "Own account (011b48d2eabbfa6361) active. Profile fully built. ID verification not completed — blocks account from being fully active. Settings → Identity Verification.",
    "priority": "CRITICAL",
    "revenue_impact": "DIRECT",
    "deadline": "2026-08-07",
    "owner": "Emmanuel",
    "created": "2026-08-06",
    "state": "open",
    "platform": "Upwork",
    "next_action": "Settings → Identity Verification. Takes 10-15 min."
  },
  {
    "id": "q011",
    "action": "Add withdrawal method to Upwork",
    "context": "Cannot receive payment without this. Settings → Get Paid → add bank or Payoneer.",
    "priority": "CRITICAL",
    "revenue_impact": "DIRECT",
    "deadline": "2026-08-07",
    "owner": "Emmanuel",
    "created": "2026-08-06",
    "state": "open",
    "platform": "Upwork",
    "next_action": "Settings → Get Paid → add withdrawal method."
  },
  {
    "id": "q012",
    "action": "Record 3 portfolio Looms and upload to profile",
    "context": "Portfolio is the last major profile section not done. SERAMAN pipeline first (strongest — real client, 5-star, complex architecture). SavvySox second. One software project third. Format: WATCH THIS: [Topic]: Full n8n Breakdown!",
    "priority": "HIGH",
    "revenue_impact": "INDIRECT",
    "deadline": "2026-08-13",
    "owner": "Emmanuel",
    "created": "2026-08-06",
    "state": "open",
    "platform": "Upwork",
    "next_action": "Record SERAMAN Loom first. Show n8n canvas, each module, Claude AI node, Kie AI branch, Creatomate assembly, Blotato publishing."
  },
  {
    "id": "q013",
    "action": "Record and upload Upwork intro video",
    "context": "Script saved at outputs/strategy/2026-08-06-profile-intro-video-script.md. 60-90 seconds. Record like a Loom but for profile context.",
    "priority": "MEDIUM",
    "revenue_impact": "INDIRECT",
    "deadline": null,
    "owner": "Emmanuel",
    "created": "2026-08-06",
    "state": "open",
    "platform": "Upwork",
    "next_action": "Read script, record, upload to Upwork profile intro video section."
  },
  {
    "id": "q014",
    "action": "Follow up on 5 testimonials if not submitted by 2026-08-16",
    "context": "5 LinkedIn testimonials in motion: Cyrus, Rejoice, Oba, Bayonet, Samuel. All emailed with review text + Upwork recommendation requests sent. Takes 8-10 days to appear. Check by 2026-08-16.",
    "priority": "MEDIUM",
    "revenue_impact": "INDIRECT",
    "deadline": "2026-08-16",
    "owner": "Emmanuel",
    "created": "2026-08-06",
    "state": "open",
    "platform": "Upwork",
    "next_action": "Check profile by 2026-08-16. If any not submitted, WhatsApp the person directly."
  },
  {
    "id": "q015",
    "action": "Confirm payment terms with Bayonet before solar project",
    "context": "Bayonet called 2026-08-06 with solar calculator project (fuel spend → solar capacity recommendation). US client connection behind it. Emmanuel expressed interest. Must confirm: what is Bayonet paying Emmanuel, by when.",
    "priority": "HIGH",
    "revenue_impact": "DIRECT",
    "deadline": "2026-08-08",
    "owner": "Emmanuel",
    "created": "2026-08-06",
    "state": "open",
    "platform": "Direct",
    "next_action": "Reply to Bayonet: 'I'm in. Before committing fully — what's the payment structure on my side?'"
  },
  {
    "id": "q002",
    "action": "Chase Bayonet — payment number + logo PNG",
    "context": "Revamp Consulting build is blocked. Bayonet confirmed the project but hasn't sent payment WhatsApp number or logo file. No number = no invoice. No logo = no build.",
    "priority": "HIGH",
    "revenue_impact": "DIRECT",
    "deadline": "2026-07-28",
    "owner": "Emmanuel",
    "created": "2026-07-24",
    "state": "open",
    "platform": "Direct",
    "next_action": "WhatsApp Bayonet: 'Hey, just need your payment number and the logo PNG to kick off the build.'"
  },
  {
    "id": "q003",
    "action": "Follow up Petit Lit (Fradel Saks) if no reply",
    "context": "Reconnect email sent 2026-07-24 to sales@petitlitfurniture.com. If no reply by 2026-07-27, call 718.851.0367.",
    "priority": "HIGH",
    "revenue_impact": "DIRECT",
    "deadline": "2026-07-27",
    "owner": "Emmanuel",
    "created": "2026-07-24",
    "state": "open",
    "platform": "Direct",
    "next_action": "No email reply yet. Call 718.851.0367 or send follow-up email."
  },
  {
    "id": "q004",
    "action": "LinkedIn Post 3 — publish 8AM WAT",
    "context": "Hard schedule. Post 1: 2026-07-24 done. Post 2: 2026-07-26 done. Post 3: 2026-07-29. Must be online 60 min after posting. First comment within 60 seconds.",
    "priority": "HIGH",
    "revenue_impact": "INDIRECT",
    "deadline": "2026-07-29",
    "owner": "Emmanuel",
    "created": "2026-07-24",
    "state": "open",
    "platform": "LinkedIn",
    "next_action": "Prepare Post 3 content and card before 2026-07-29 8AM WAT."
  },
  {
    "id": "q005",
    "action": "Giovanni NGO project — scope the onboarding",
    "context": "Giovanni's partner is managing the NGO project. Pipeline probe sent. Partner onboarding is a paid deliverable — do not give it away as free support. Awaiting Giovanni's reply on what product they're running.",
    "priority": "HIGH",
    "revenue_impact": "DIRECT",
    "deadline": "2026-07-30",
    "owner": "Oba",
    "created": "2026-07-27",
    "state": "open",
    "platform": "Direct",
    "next_action": "Await Giovanni's reply. When he confirms product, scope the onboarding as part of NGO contract."
  },
  {
    "id": "q006",
    "action": "Gadget/phone sales OS — design and build",
    "context": "Emmanuel runs a gadget/phone sales operation. Needs: brand system, daily photo posting engine, posting strategy, n8n automation for cross-posting. 5 clarifying questions pending answers.",
    "priority": "MEDIUM",
    "revenue_impact": "INDIRECT",
    "deadline": null,
    "owner": "Emmanuel",
    "created": "2026-07-27",
    "state": "open",
    "platform": "Direct",
    "next_action": "Emmanuel to answer: (1) new/used/both stock, (2) brand name exists?, (3) units/week, (4) WhatsApp Business set up?, (5) current photo setup."
  },
  {
    "id": "q007",
    "action": "SERAMAN — normalize scene 1/8 volume to 200%",
    "context": "Scene 1 at 60%, scene 8 at 100%. Scenes 2-7 at 200%. Inconsistent. Giovanni flagged volume before. Low priority but should be fixed before next M2 job.",
    "priority": "MEDIUM",
    "revenue_impact": "MAINTENANCE",
    "deadline": null,
    "owner": "Emmanuel",
    "created": "2026-07-24",
    "state": "open",
    "platform": "n8n",
    "next_action": "Update Creatomate template for scene 1 and scene 8 volume to 200%."
  },
  {
    "id": "q008",
    "action": "SERAMAN — Gemini Omni switch pending Giovanni greenlight",
    "context": "A/B test run 2026-07-19. Gemini Omni fixes hand/joint defect, better VO, cheaper than Kling. 4-way comparison sent to Giovanni. Awaiting his approval to switch production workflow.",
    "priority": "MEDIUM",
    "revenue_impact": "MAINTENANCE",
    "deadline": null,
    "owner": "Oba",
    "created": "2026-07-19",
    "state": "open",
    "platform": "n8n",
    "next_action": "Follow up with Giovanni if no reply on the model comparison email."
  },
  {
    "id": "q009",
    "action": "OS Tier 2 + Tier 3 — full autonomous stack built",
    "context": "Tier 2 (heartbeat, pulse, queue) + Tier 3 (email_watcher, job_watcher, follow_up, outreach, prospector) all built and registered in Windows Task Scheduler. Playwright prospector tested successfully.",
    "priority": "MEDIUM",
    "revenue_impact": "INDIRECT",
    "deadline": "2026-07-27",
    "owner": "Emmanuel",
    "created": "2026-07-27",
    "state": "resolved",
    "platform": "OS",
    "next_action": "Done. Monitor logs/ directory for daemon errors. Run prospector as needed."
  }
]
```
<!-- END MACHINE-READABLE BLOCK -->

---

## Current Queue — Human View

| Priority | ID | Action | Owner | Deadline | State |
|---|---|---|---|---|---|
| 🔴 CRITICAL | q010 | Upwork ID verification | Emmanuel | 2026-08-07 | open |
| 🔴 CRITICAL | q011 | Add withdrawal method | Emmanuel | 2026-08-07 | open |
| 🟠 HIGH | q016 | Cert sprint: 14 Anthropic + 4 n8n Academy | Emmanuel | 2026-08-14 | open |
| ✅ DONE | q017 | Project Catalog: 2 items ($499 agent + $149 diagnostic) | Emmanuel | — | resolved |
| 🟠 HIGH | q012 | Record 3 portfolio Looms | Emmanuel | 2026-08-13 | open |
| 🟠 HIGH | q015 | Confirm Bayonet solar payment terms | Emmanuel | 2026-08-08 | open |
| 🟠 HIGH | q002 | Chase Bayonet — Revamp payment + logo | Emmanuel | — | open |
| 🟠 HIGH | q003 | Petit Lit follow-up | Emmanuel | — | open |
| 🟠 HIGH | q005 | Giovanni NGO — scope onboarding | Oba | — | open |
| 🟡 MEDIUM | q018 | Rewrite overview: Recent work section + CTA | Emmanuel | 2026-08-14 | open |
| 🟡 MEDIUM | q013 | Record + upload intro video | Emmanuel | — | open |
| 🟡 MEDIUM | q014 | Follow up testimonials by 2026-08-16 | Emmanuel | 2026-08-16 | open |
| 🟡 MEDIUM | q004 | LinkedIn posts 4-6 (overdue — reschedule) | Emmanuel | — | open |
| 🟡 MEDIUM | q006 | Gadget OS design | Emmanuel | — | open |
| 🟡 MEDIUM | q007 | SERAMAN scene 1/8 volume fix | Emmanuel | — | open |
| 🟡 MEDIUM | q008 | SERAMAN Gemini Omni greenlight | Oba | — | open |
| ✅ DONE | q001 | Upwork account restriction resolved | Emmanuel | — | resolved |
| ✅ DONE | q009 | OS Tier 2 + 3 build | Emmanuel | — | resolved |

---

## How to Maintain This File

- Add items: append to JSON block + add row to table
- Resolve items: change `"state": "open"` → `"state": "resolved"`, remove from table
- Escalate items: change priority level when deadline pressure increases
- heartbeat.py reads the JSON block automatically — keep it valid JSON
