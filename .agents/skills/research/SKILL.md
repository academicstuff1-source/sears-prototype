---
name: research
description: >-
  Use this skill when Michael asks for research on any topic related to his AI
  consulting business. Accepts a research query, loads live business context
  (priorities, goals, active projects), calls the Tavily Search API at advanced
  depth, and saves a structured markdown report to references/research/.
  Activate for: competitive analysis, prospect research, industry deep-dives,
  AI tool evaluation, cold outreach prep, or any research where business context
  should shape the results.
engine: tavily
engine-tier: advanced
output: references/research/YYYY-MM-DD-slug.md
requires:
  env: TAVILY_API_KEY
  packages:
    - tavily-python
    - python-dotenv
---

# Research Skill

Deep, context-aware research powered by Tavily Search.
Loads Michael's live workspace context before every run so results are filtered
and framed around what matters right now — landing clients, understanding the
DFW AI consulting market, and building a repeatable business.

## When to Activate

- Competitive analysis on AI consultants or adjacent firms
- Background research on a prospect or industry before outreach
- AI tool or trend evaluation for consulting use cases
- Research to support a proposal, pitch, or service offering
- Any query where "what does this mean for my business?" matters

## Workflow

### Step 1 — Load Context

Read these files before running any research:

- `context/me.md`
- `context/work.md`
- `context/current-priorities.md`
- `context/goals.md`
- Any active `projects/*/README.md`

These are automatically injected into the Tavily request by the script.

### Step 2 — Clarify (if needed)

If the query is ambiguous, ask:
- What is the specific research question?
- What will the findings be used for?
- Quick overview or full analysis?

### Step 3 — Run

```bash
# Standard run
python .agents/skills/research/scripts/tavily_research.py --query "your topic"

# Run and save to references/research/
python .agents/skills/research/scripts/tavily_research.py --query "your topic" --save
```

**Install once:** `pip install tavily-python python-dotenv`

### Step 4 — Present Findings

Structure output as:

```
## Research: [Topic]
**Date:** YYYY-MM-DD
**Used for:** [prospecting / pitch / learning / etc.]

### AI Summary
### Key Findings
### Sources
### Actionable Takeaways
```

### Step 5 — Save

Significant research → `references/research/YYYY-MM-DD-topic.md`
Project-related research → inside the relevant `projects/*/` folder

## Notes

- `.env` is git-ignored — never commit the API key
- Free tier: 1,000 Tavily credits/month; advanced search uses 2 credits per call
- Get a key: https://app.tavily.com
- Keep context files current — they shape every research run
