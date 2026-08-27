---
name: cold-call-prep
description: >-
  Use this skill to prepare a 1-page tactical cold call and discovery call brief for a specific prospect or business owner.
  Generates a natural talk track, pain hypothesis, high-yield discovery questions, objection responses, and target next steps.
---

# Cold Call & Discovery Call Prep Skill

Produces a crisp, 1-page call preparation sheet in under 2 minutes. Designed to eliminate hesitation, ensure Michael sounds natural and informed (without sounding overly scripted), and steer early conversations toward pattern recognition, workflow discovery, and booking a paid audit/pilot.

## When to Activate

- "Prep me for a call with [Name] at [Company]"
- "Generate a call cheat-sheet for [Company]"
- "How should I open a cold call to [Industry/Prospect]?"

## Workflow

### Step 1 — Review Account Context
Check `references/research/account-briefs/` for existing research or run a quick scan of the prospect's business, location, and decision-maker name/role.

### Step 2 — Construct Call Strategy
1. **Target Call Outcome:** What is the specific goal of this call? (e.g., Book a 15-minute workflow audit, identify who handles office operations, or test problem resonance).
2. **Opening Hook:** Conversational, direct, respectful of time, non-pitchy.
3. **Pain Hypothesis:** 1 concrete operational problem they almost certainly face.
4. **Diagnostic / Discovery Questions:** 3–4 questions that uncover how they currently handle that workflow.
5. **Objection Handling (Top 3):**
   - *"We already have software / an IT person for that."*
   - *"We're too busy right now / not interested."*
   - *"Just send me an email."*

### Step 3 — Output & Save Call Prep Sheet
Save the generated sheet to:
`references/research/call-preps/YYYY-MM-DD-[company-slug]-[contact-slug].md`

#### Call Prep Sheet Template:
```markdown
# Call Prep: [Contact Name] — [Company Name]

**Date:** YYYY-MM-DD  
**Target:** [Contact Name, Title]  
**Company:** [Company Name, Location, Specialty]  
**Goal:** [e.g., Book 15-min discovery call / Confirm if intake workflow is manual]  

---

## 1. Fast Context (20-Second Glance)
- **Who they are:** [Brief summary]
- **Key hypothesis:** [e.g., Front desk spends 10+ hours/week manually chasing appointment confirmations]

## 2. Opening Talk Track
> *"Hi [First Name], this is Michael. I know you're in the middle of running things, so I'll keep this brief. I work with [healthcare practices / local businesses] here in [DFW / Texas] helping them automate [repetitive task, e.g., patient intake & reminder follow-ups]. I noticed [specific observation about company] and wanted to ask: who currently manages your [specific workflow]?"*

## 3. Core Discovery Questions (Pick 2-3)
1. *"When a new [patient/client] reaches out after hours or through your website, what is the exact process for getting them on the schedule?"*
2. *"How much time is your front desk spending each week manually calling or texting for confirmations and paperwork?"*
3. *"Where does your team experience the most friction between receiving info and getting it into your [EHR / CRM / practice management software]?"*
4. *"If you could eliminate one repetitive manual task from your desk tomorrow, what would it be?"*

## 4. Objection Battlecard
| Objection | Natural Response |
|---|---|
| *"We already have a system / software."* | *"Totally understand — most practices I talk to have [EHR/System]. We don't replace that; we usually just connect the gaps where staff are still doing manual copy-pasting or phone tag. What system are you running?"* |
| *"We're too busy right now."* | *"That's exactly why I called — if your team is slammed, manual tasks are what's eating their bandwidth. I'd love to show you a 5-minute example next week when things are calmer. How does Tuesday morning look?"* |
| *"Just send me an email."* | *"Happy to. So I don't send generic fluff, which area is a bigger headache right now: [intake paperwork] or [missed appointment follow-ups]?"* |

## 5. Next Step Close
> *"Look [First Name], I'd love to take 15 minutes to show you a quick map of how other [practices/businesses] streamline this. Even if we never work together, you'll walk away with a clear picture of what can be automated. Do you have 15 minutes this Thursday afternoon or Friday morning?"*
```
