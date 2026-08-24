---
name: research
description: Deep, context-aware research using Tavily. Reads Michael's current priorities, goals, and business context before searching — so findings are filtered and framed around what actually matters right now.
---

# Research Skill

Use this skill when Michael needs research that goes beyond a quick lookup — market intelligence, prospect background checks, AI tool deep-dives, industry analysis, or anything where business context should shape the results.

## When to Use This Skill

- Researching AI tools, trends, or competitors relevant to consulting
- Background on a prospect or industry before cold outreach
- Learning resources on a specific AI topic Michael is exploring
- Research to support a proposal, pitch, or service offering
- Any topic where "what does this mean for my business?" matters

## Workflow

### Step 1 — Load Context

Before running any research, read:

- `context/me.md`
- `context/work.md`
- `context/current-priorities.md`
- `context/goals.md`
- Any active project `README.md` files in `projects/`

This context is used to enrich the search query and frame the final output.

### Step 2 — Clarify the Request

If not already clear, ask:
1. What is the specific research question or topic?
2. What will the findings be used for? (prospecting, pitching, learning, building)
3. Quick overview or full analysis?
4. Any specific industries, companies, or angles to focus on?

### Step 3 — Run the Script

```bash
python .antigravity/skills/research/scripts/tavily_research.py --query "your research topic here"
```

To also save the output to `references/research/`:

```bash
python .antigravity/skills/research/scripts/tavily_research.py --query "your research topic here" --save
```

**Requirements:** `pip install tavily-python python-dotenv`
**API key:** Set `TAVILY_API_KEY` in `.env` at the workspace root.
**Free tier:** 1,000 credits/month — advanced search uses 2 credits per call (~500 searches/month).
**Get a key:** https://app.tavily.com

### Step 4 — Synthesize and Present

After receiving output from Tavily, structure and present findings as:

---

## Research: [Topic]

**Date:** YYYY-MM-DD
**Used for:** [prospecting / pitch / learning / etc.]
**Priority connection:** [how this ties to current priorities]

### Key Findings
-

### Actionable Takeaways
-

### Sources
-

---

### Step 5 — Save (Optional)

Significant research gets saved to:
- `references/research/YYYY-MM-DD-topic-name.md`
- Or inside the relevant project folder if a project is active

## API Config

| Setting | Value |
|---|---|
| Provider | Tavily AI |
| Search depth | `advanced` (richer results) |
| AI answer | Enabled (`include_answer=True`) |
| Key location | `.env` → `TAVILY_API_KEY` |
| Signup | https://app.tavily.com |

## Notes

- `.env` is git-ignored — never commit keys
- Keep context files current — they shape every research run
- If a research topic repeats (e.g., "competitor research"), build a sub-skill with a hardcoded prompt template
