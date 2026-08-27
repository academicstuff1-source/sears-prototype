# Skills to Build Backlog

Repeatable workflows that may become Antigravity skills.

**Do not build a skill until:**
1. The workflow has occurred more than once or is clearly recurring
2. Its inputs, desired output, and quality standards are clearly defined
3. Michael explicitly approves building it

---

## Backlog

### Next

| Skill | Problem it Solves | Trigger | Desired Output | Inputs Required | Approval Needed? |
|---|---|---|---|---|---|
| `outreach-draft` | Writing personalized cold emails and follow-ups takes significant time | Starting outreach to a prospect | Draft outreach email or sequence for Michael's review | Account brief, contact info, outreach goal | Yes — before sending |
| `discovery-call-summary` | Post-call notes are inconsistent; insights get lost | After a discovery or sales call | Structured call summary: pain points, context, next steps, CRM update suggestions | Call notes or transcript | No for summary; Yes for CRM changes |
| `crm-hygiene` | HubSpot contact and pipeline data degrades over time | Weekly or on request | Suggested contact updates, pipeline stage corrections, and follow-up tasks for review | HubSpot export or record list | Yes — before any CRM changes |
| `tool-evaluation` | Comparing AI, automation, and no-code tools takes research time | Evaluating a new tool | Comparison table: cost, capabilities, learning curve, implementation fit, recommendation | Tool names, use case, budget constraints | No |

### Later

| Skill | Problem it Solves | Trigger | Desired Output | Inputs Required | Approval Needed? |
|---|---|---|---|---|---|
| `client-proposal` | First-draft proposals from a brief take significant effort | After a qualified discovery call | Draft proposal or scope-of-work document | Discovery call summary, proposed solution, pricing hypothesis | Yes — before sending |
| `social-media-content` | Creating consistent content is time-consuming | Content creation request | Draft posts or captions aligned with AI consulting positioning | Topic, platform, audience | Yes — before publishing |
| `case-study-capture` | Lessons and client results get lost after delivery | After completing client work | Structured case study draft: problem, approach, result, testimonial prompt | Project notes, client outcome data | Yes — before sharing externally |
| `weekly-review` | No consistent rhythm for reviewing priorities, pipeline, and next actions | Weekly, Monday or Friday | Weekly review doc: pipeline status, top priorities, blockers, planned actions | Current-priorities.md, project READMEs, CRM status | No |

---

## Already Built

| Skill | Location | Notes |
|---|---|---|
| `research` | `.agents/skills/research/` | Tavily-powered deep market and competitive research → `references/research/` |
| `session-summary` | `.agents/skills/session-summary/` | Auto-captures session progress, updates project READMEs, logs decisions |
| `prospect-research` | `.agents/skills/prospect-research/` | Generates 5-minute structured Account Briefs with tailored outreach angles |
| `cold-call-prep` | `.agents/skills/cold-call-prep/` | Generates 1-page tactical call sheets with talk track, questions & objection handlers |
| `social-outreach` | `.agents/skills/social-outreach/` | Analyzes LinkedIn/IG/YT posts and drafts high-converting conversational messages |

---

## How to Add a Skill
1. Identify a workflow that repeats consistently
2. Add it to the appropriate priority tier above
3. When ready to build, explicitly approve it — then create `.agents/skills/skill-name/SKILL.md`
