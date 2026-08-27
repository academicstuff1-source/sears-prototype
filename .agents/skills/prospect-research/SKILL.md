---
name: prospect-research
description: >-
  Use this skill to research a target company, prospect URL, or niche business before outreach.
  Analyzes business model, operational size, probable workflow bottlenecks (intake, scheduling, follow-ups, billing, reporting),
  identifies key decision-maker titles, and produces a structured Account Brief with tailored outreach angles.
---

# Prospect Research Skill

Generates structured, actionable Account Briefs for outbound prospecting in under 5 minutes. Formatted specifically for Michael's AI automation consulting positioning — focusing on practical, high-friction workflow problems rather than generic AI hype.

## When to Activate

- "Research [Company Name / URL / Practice]"
- "Find workflow pain points for [Company]"
- "Build an account brief for [Prospect]"
- Pre-outreach account qualification and angle identification

## Workflow

### Step 1 — Load Context
Read Michael's positioning in `context/work.md` and target preferences in `context/current-priorities.md`.
Ensure focus remains on practical, low-code/no-code AI workflow improvements (intake, scheduling, reminder sequences, CRM synchronization, document processing, customer follow-up).

### Step 2 — Investigate Target Account
Using search tools or provided URLs, analyze:
1. **Core Business:** What they do, specialty, primary services, customer base.
2. **Operations & Size:** Estimated staff count, number of locations, tools used (visible booking widgets, EHRs, CRM, contact forms).
3. **Likely Workflow Bottlenecks:**
   - Patient/Client Intake & Onboarding (manual form handling, data re-entry)
   - Appointment Scheduling & No-Show Reduction (manual follow-up calls, reminders)
   - Lead Follow-up & Response Time (missed website inquiries, after-hours capture)
   - Billing, Invoicing & Documentation (repetitive admin tasks)
   - Internal Reporting & Team Hand-offs
4. **Key Decision-Makers:** Owners, Managing Partners, Practice Administrators, Operations Directors, Clinic Managers.

### Step 3 — Formulate Value Hypothesis & Outreach Angles
Craft 2–3 distinct outreach angles:
- **Angle 1 (Speed/Response):** Solving slow lead/patient response or after-hours intake.
- **Angle 2 (Manual Friction):** Eliminating double-data entry, manual paperwork, or repetitive admin tasks.
- **Angle 3 (Capacity/Retention):** Helping front desk or staff handle higher volume without hiring.

### Step 4 — Generate & Save Account Brief
Save the report to:
`references/research/account-briefs/YYYY-MM-DD-[company-slug].md`

#### Account Brief Structure:
```markdown
# Account Brief: [Company Name]

**Date:** YYYY-MM-DD  
**Website / Location:** [URL / City, State]  
**Industry / Niche:** [e.g., Physical Therapy / Dental / SMB]  
**Estimated Size:** [e.g., 2 locations, 12 staff]  

---

## 1. Company Overview
[2-3 sentences on what they do, who they serve, and how they operate.]

## 2. Likely Workflow Pain Points
- **[Pain Area 1, e.g., Patient Intake]:** [Specific bottleneck description]
- **[Pain Area 2, e.g., Appointment Confirmation & No-Shows]:** [Specific bottleneck description]
- **[Pain Area 3, e.g., Repetitive Staff Admin]:** [Specific bottleneck description]

## 3. Decision-Maker Profiles
- **Primary:** [Title / Name if found, e.g., Owner, Managing Partner, Practice Administrator]
- **Secondary:** [e.g., Office Manager, Operations Lead]

## 4. Recommended Outreach Angles
1. **[Angle Title 1]:** [1-2 sentences on how to frame the problem]
2. **[Angle Title 2]:** [1-2 sentences on how to frame the problem]

## 5. Tailored Openers (Ready for Cold Call / Email)
- **Call Opener:** "[Specific, conversational opening hook]"
- **Email Subject Line:** [Concise, non-spammy subject line]
- **Email Hook:** "[Direct, 2-line problem statement]"
```
