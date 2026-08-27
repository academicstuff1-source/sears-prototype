---
name: session-summary
description: >-
  Acts as the operational memory of the workspace. Triggered at the end of a session to 
  extract decisions, update project READMEs, log material changes, and write a summary artifact.
---

# Session Summary Skill (Pro)

The most critical skill in the workspace. It ensures that the "Second Brain" never degrades. It acts as an autonomous clerk, capturing the delta between the start of the session and the end, and updating the source-of-truth files.

## When to Activate
- "Wrap up"
- "Session summary"
- "Log what we did today"
- At the natural conclusion of a multi-turn work block.

## Execution Algorithm

### Step 1: Conversation Parsing
Review the entire transcript of the current session. Identify:
- **Completed Actions:** What tasks from ClickUp or Project READMEs were finished?
- **New Artifacts:** What files/research were generated?
- **Material Decisions:** Did Michael change strategy, tool preference, target demographic, or priority?
- **Next Steps:** What is left undone?

### Step 2: Autonomous Workspace Updates
You must explicitly update these files if applicable:
1. **Projects:** Open `projects/[name]/README.md`. Mark tasks as `[x]`. Add new tasks.
2. **Context:** If a preference was stated (e.g., "I don't want to use Zapier"), update `context/work.md` or `.agents/rules/`.
3. **Decisions:** If a strategic pivot occurred, append it to `decisions/log.md` using the standard schema.

### Step 3: Summary Generation
Generate the summary and save to: `references/session-summaries/YYYY-MM-DD-summary.md`

```markdown
# 📝 Session Summary: YYYY-MM-DD

## 1. Executive Snapshot
- **Core Focus:** [What did we spend time on?]
- **Velocity:** [e.g., 2 accounts researched, 1 cold email drafted]

## 2. File Updates Executed
- `projects/[name]/README.md` (Updated next actions)
- `decisions/log.md` (Logged decision regarding [Topic])

## 3. Decisions & Epiphanies Captured
- [Decision 1]
- [Preference 1]

## 4. Next Actions (Queued for Next Session)
- [ ] [Action 1]
- [ ] [Action 2]
```

### Step 4: Final Confirmation
Present a brief message to Michael confirming that the session has been logged and the workspace files have been updated.
