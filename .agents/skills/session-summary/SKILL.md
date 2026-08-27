---
name: session-summary
description: >-
  Use this skill whenever Michael says "wrap up", "session summary", or indicates the end of a working session.
  Captures decisions, progress, new learnings, and next actions, updates project READMEs, logs material decisions,
  and saves a structured session summary to archives/session-summaries/ or root.
---

# Session Summary Skill

Ensures no context is lost between working sessions. At the conclusion of any active session, this skill parses the conversation trajectory, extracts durable information, updates relevant workspace files, and outputs a concise session summary.

## When to Activate

- Trigger phrases: "wrap up", "session summary", "end session", "let's log what we did today"
- When ending a productive work block with new decisions, progress, or project changes

## Workflow

### Step 1 — Review the Session
Inspect the full conversation to extract:
1. **What got done:** Completed tasks, research conducted, drafts created, files modified.
2. **Decisions made:** Any strategy, tooling, pricing, client, or prioritization decisions.
3. **Open items & next steps:** Immediate next actions for active workstreams.
4. **Context updates:** Any new preferences learned ("Remember that I..."), priority shifts, or stakeholder notes.

### Step 2 — Update Project Files
- Open the relevant `projects/<project-name>/README.md` files.
- Mark completed actions as checked `[x]`.
- Append new current next actions to `Current Next Actions`.
- Update project status or key dates if changed.

### Step 3 — Append Material Decisions (if any)
If a material decision was made affecting priorities, strategy, projects, tools, or commitments:
- Append an entry to `decisions/log.md` using the standard format:
```markdown
[YYYY-MM-DD] DECISION: [What was decided]
REASONING: [Why it was decided]
CONTEXT: [Relevant situation, constraints, alternatives, or linked project]
OWNER: Michael

***
```

### Step 4 — Update Context Files (if needed)
- If durable preferences were expressed, update `context/me.md` or `.agents/rules/`.
- If priority order or time-sensitive items changed, update `context/current-priorities.md`.

### Step 5 — Generate and Save Summary
Format the output based on `templates/session-summary.md` and save it to:
`references/session-summaries/YYYY-MM-DD-session-summary.md` (or present directly to Michael).

Output format:
```markdown
# Session Summary — YYYY-MM-DD

**Primary focus:** [Topic]
**Related project(s):** [Project names]

## What Got Done
- [Item 1]
- [Item 2]

## Decisions Made
- [Decision 1 (logged in decisions/log.md)]

## Open Items / Next Steps
- [Next action 1]

## Context Updates
- Preferences learned: [None / details]
- Priorities updated: [None / details]
- Project files updated: [List of modified READMEs]
```
