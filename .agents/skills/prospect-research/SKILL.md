---
name: prospect-research
description: >-
  Conducts deep, strategic account research for outbound prospecting. Identifies operational scale, 
  tech stack signals, workflow bottlenecks, and key decision-makers. Outputs an executive Account Brief 
  optimized for consultative selling.
---

# Prospect Research Skill (Pro)

An advanced intelligence-gathering workflow. It moves beyond basic firmographics to uncover operational friction, technological debt, and organizational structure, providing Michael with the exact leverage needed to book a discovery call.

## When to Activate
- "Research [Company Name / URL]"
- "Give me a breakdown of [Company]"
- "Qualify this target: [URL]"

## Execution Algorithm

### Step 1: Context & Constraints Setup
1. Read `context/work.md` and `context/current-priorities.md`.
2. Anchor the research goal: **Identify manual workflow friction** (intake, scheduling, follow-ups, CRM data entry) that Michael's low-code/no-code AI solutions can solve.

### Step 2: Deep Web Reconnaissance
Use available search/web tools to investigate:
- **Firmographics:** Headcount, locations, years in business.
- **Tech Stack Markers:** Do they use a visible patient portal? Booking widgets (Calendly, Acuity, local EHR)? Are they running ads (signals budget)?
- **Digital Footprint:** Reviews mentioning slow response times, bad customer service, or long waits (prime automation targets).
- **Leadership:** Identify the Practice Manager, Operations Director, Managing Partner, or Owner.

### Step 3: Synthesis & Hypothesis Generation
Apply the "Why Change? Why Now?" framework:
- **Why Change?** What is the cost of their current manual process (e.g., lost leads, staff burnout)?
- **Why Now?** Did they recently expand? Are they hiring for admin roles? (Signals bandwidth limits).

### Step 4: Output Generation
Generate the brief and save to: `references/research/account-briefs/YYYY-MM-DD-[company-slug].md`

```markdown
# 🎯 Account Intelligence: [Company Name]

**Target URL:** [URL] | **Industry:** [Niche] | **Est. Size:** [Headcount/Locations]

---

## 1. Operational Snapshot
[Brief executive summary of their business model, target demographic, and market positioning. How do they make money?]

## 2. Tech & Friction Signals
- **Visible Tech Stack:** [EHR, CRM, booking tools]
- **Friction Indicators:** [e.g., "Reviews mention long wait times," "No online booking available," "Currently hiring for front desk / data entry"]

## 3. High-Probability Pain Points
1. **[Pain 1 - e.g., After-Hours Lead Leakage]:** [Why they likely suffer from this]
2. **[Pain 2 - e.g., Staff Bottlenecks]:** [Why manual intake is costing them money]

## 4. Key Decision Makers
- **[Name]** — [Title] (Primary target)
- **[Name]** — [Title] (Secondary target / Champion)

## 5. Recommended Strategic Angles
- **Angle A (Growth):** "How to handle your recent expansion without doubling front-desk headcount."
- **Angle B (Efficiency):** "Plugging the holes in patient intake so providers spend less time on admin."
```
