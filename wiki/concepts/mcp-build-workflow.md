---
sensitivity: private
entity_type: concept
name: "mcp-build-workflow"
description: "Using Claude Code + MCP servers to build client projects faster — the accelerated development workflow"
tags: [mcp, claude-code, development, workflow, tools]
created: "2026-08-13"
---

# MCP Accelerated Build Workflow

Using Claude Code with MCP servers connected changes the development workflow from copy-paste debugging to a fully autonomous build loop. Claude writes files, runs them, reads errors, fixes them — without Emmanuel touching anything until review.

---

## The Shift

**Without MCP:**
Write code → run it → get error → copy error → paste into Claude → get fix → copy fix → paste back into file → run again

**With MCP:**
Tell Claude what to build → Claude writes the file, runs it, reads the error, fixes it, re-runs — all without you touching it

Emmanuel becomes the director. Claude is the hands.

---

## MCP Servers to Know

### 1. PostgreSQL MCP
Claude connects directly to a live database while building.

Use case: Setting up schemas, testing queries, debugging data issues, verifying storage — without copy-pasting SQL results back and forth.

Install:
```bash
npx @modelcontextprotocol/server-postgres "postgresql://localhost/dbname"
```

### 2. Fetch MCP
Claude makes real HTTP requests to test actual APIs while building.

Use case: Testing X API auth, Claude API responses, any endpoint — Claude reads the real response and fixes auth issues on the spot.

Install:
```bash
npx @modelcontextprotocol/server-fetch
```

### 3. Filesystem MCP
Claude reads and writes project files directly. Built into Claude Code — no install needed.

### 4. GitHub MCP (optional)
Claude commits working code, manages branches, pushes to repo.

Install:
```bash
npx @modelcontextprotocol/server-github
```

---

## CLAUDE.md in Every Client Project

Create a CLAUDE.md inside every client project folder. This is the briefing document Claude reads at the start of every session. Include:

- What the system does (1-2 sentences)
- Current milestone we're on
- Database schema (or where to find it)
- API credentials location (.env file)
- Tech stack summary
- Client's voice/brand rules (if generating content)
- What task we're building next

Without CLAUDE.md: every session starts cold.
With CLAUDE.md: Claude has full context immediately.

---

## Standard Project Setup

```bash
# Create project
mkdir client-project-name
cd client-project-name

# Create CLAUDE.md with project context

# Install MCP servers
npx @modelcontextprotocol/server-postgres "postgresql://localhost/dbname"
npx @modelcontextprotocol/server-fetch

# Open Claude Code — MCP servers now active in this session

# Work module by module
# Tell Claude what to build, review output, approve or redirect
```

---

## Speed Gain

A 30-day client project becomes 18-20 days with MCP assistance. This means:
- Finish before the client's deadline (over-deliver = 5-star review)
- Bandwidth for more concurrent clients
- Take on harder projects than solo skill level allows

---

## Positioning This to Clients

Don't say "I use AI to write my code."

Say: "I build AI-assisted development pipelines. The system writes, tests, and debugs itself while I direct the architecture and review outputs."

That's a real skill. Most freelancers don't have it. The judgment (what to build, how to wire it, how to review what's produced) is the actual craft being developed.

---

## Applied to Nick Gerli's Project

MCP servers for the Reventure automation build:

1. PostgreSQL MCP → connects to Reventure's housing database while building the Z-score detection module. Claude queries the real data, checks if anomalies are being calculated correctly, debugs schema issues.

2. Fetch MCP → tests real X API calls while building Tweepy integration. Claude authenticates, sends a test post, reads the real response, and fixes any issues immediately.

3. Filesystem → writes and edits all Python files directly.

Result: The data intelligence layer (Milestone 1) that might take 7 days solo takes 3-4 days with Claude Code + PostgreSQL MCP connected.

---

## Wikilinks

[[tool-first-rule]] · [[active-agent-mode]] · [[nick-twitter-automation]]
