---
name: social-outreach
description: >-
  Drafts high-converting, personalized social media outreach messages (LinkedIn, IG, Email) 
  by extracting operational pain signals from social content using the Insight-Observation-Question framework.
---

# Social Media Outreach Skill (Pro)

Transforms social media posts and profile bios into high-leverage conversation starters. It avoids generic AI fluff by utilizing the **Insight-Observation-Question (IOQ)** framework. 

## When to Activate
- "Draft a message for [Name] based on this LinkedIn post: [Text]"
- "Write an Instagram DM to this clinic owner."
- "Create an email hook referencing this YouTube video."

## Execution Algorithm

### Step 1: Signal Extraction
Analyze the provided content for implicit business signals:
- **Hiring:** "We are looking for an admin!" → *Signal: High volume, manual work, burnout risk.*
- **Growth:** "Opening our second location!" → *Signal: Scaling operations, existing systems might break.*
- **Venting/Frustration:** "Tech is so frustrating." → *Signal: Ripe for automation consulting.*

### Step 2: The IOQ Framework
Draft the message using this exact sequence:
1. **Insight:** A brief, personalized acknowledgment of their content (proves you actually read it).
2. **Observation:** Tying their content to an operational reality (the pivot to business).
3. **Question:** A low-friction, open-ended question that begs a reply, not a meeting.

### Step 3: Rules of Engagement
- **NO AI WORDS:** Do not use "delve," "navigate," "testament," "thrilled," or "synergy."
- **NO PITCHING:** The goal of the first message is a *reply*, not a meeting.
- **LENGTH:** Keep it under 4 sentences. Make it easily readable on a mobile screen.

### Step 4: Output Generation
Generate options and save to: `references/research/social-outreach/YYYY-MM-DD-[platform]-[name].md`

```markdown
# 📱 Social Outreach: [Name]

**Platform:** [Platform] | **Target:** [Name, Title]
**The Signal:** [What their post actually means operationally]

---

## Draft Options (For Review)

### Option 1: Direct IOQ (Best for LinkedIn DMs)
> "Hey [Name], loved your post on [Specific Detail]. 
> 
> Usually when I see [Clinics/Firms] expanding like you are, the front desk systems start to fracture under the new volume. 
> 
> Out of curiosity, are you guys still handling your [intake/scheduling/follow-ups] manually, or have you started automating that yet?"

### Option 2: The Soft Value-Add (Public Comment)
> "[Name], this is a great breakdown of [Topic]. The piece about [Detail] is spot on. Have you found that your team's bandwidth has been the main bottleneck there, or is it purely a systems issue?"

### Option 3: Ultra-Short (Best for Instagram/X)
> "Hey [Name] - saw the post about the new location. Congrats! Quick question: as you scale, are you guys still doing patient intake manually or have you automated that flow?"

---
**Status:** Awaiting Michael's approval.
```
