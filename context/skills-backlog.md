# Skills to Build Backlog

Repeatable workflows that may become Antigravity skills.

**Do not build a skill until:**
1. The workflow has occurred more than once or is clearly recurring
2. Its inputs, desired output, and quality standards are clearly defined
3. Michael explicitly approves building it

---

## Backlog

### Now

| Skill | Problem it Solves | Trigger | Desired Output | Inputs Required | Approval Needed? |
|---|---|---|---|---|---|
| `prospect-research` | Time-consuming manual research on businesses and decision-makers | Starting outreach on a new account | Structured account brief: company overview, likely workflow pain points, key contacts, outreach angle | Company name, URL, or industry | No — internal use only |
| `session-summary` | Manual effort to capture session decisions, progress, and next steps | End of any working session | Filled session-summary.md filed in the right project or root | Conversation context | No |
| `cold-call-prep` | Inconsistent, under-prepared cold call and discovery call briefs | Before any outreach call | Call prep brief: contact background, company context, pain hypothesis, talk track notes, key questions | Contact name, company, call type | No — internal use only |

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
| `research` | `.agents/skills/research/` | Tavily-powered deep research, saves reports to `references/research/` |

---

## How to Add a Skill
1. Identify a workflow that repeats consistently
2. Add it to the appropriate priority tier above
3. When ready to build, say "let's build the [skill-name] skill" — then create `.agents/skills/skill-name/SKILL.md`
