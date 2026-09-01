---
name: social-outreach
description: >-
  Drafts high-converting, personalized social media outreach messages (LinkedIn, IG, Email) 
  by extracting operational pain signals from social content using the I-V-Q framework and Hormozi's give-first lead gen principles from $100M Leads.
---

# Social Media Outreach Skill (Pro)

Transforms social media posts and profile bios into high-leverage conversation starters. It avoids generic AI fluff by utilizing the **Insight-Value-Question (I-V-Q)** framework. 

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

### Step 2: The I-V-Q Framework
Draft the message using this exact sequence:
1. **Insight:** A brief, personalized acknowledgment of their content (proves you actually read it).
2. **Value-add (The Give):** Offer one specific, free insight or observation that proves expertise before pivoting to their operational problem. It should feel like consulting, not selling.
3. **Question:** A low-friction, open-ended question that begs a reply, not a meeting.

### Step 3: Rules of Engagement
- **NO AI WORDS:** Do not use "delve," "navigate," "testament," "thrilled," or "synergy."
- **NO PITCHING:** The goal of the first message is a *reply*, not a meeting.
- **LENGTH:** Keep it under 4 sentences. Make it easily readable on a mobile screen.
- **BE SPECIFIC:** Vague compliments ("loved your content!") are filtered out. Name the exact thing. Specificity signals you actually paid attention.
- **GIVE BEFORE ASKING:** If the message doesn't contain at least one genuinely useful observation or insight, it's a cold pitch disguised as a conversation.
- **NO STACKING:** One question only. Multiple questions create friction and signal desperation.

### Step 4: Output Generation
Generate options and save to: `references/research/social-outreach/YYYY-MM-DD-[platform]-[name].md`

```markdown
# 📱 Social Outreach: [Name]

**Platform:** [Platform] | **Target:** [Name, Title]
**The Signal:** [What their post actually means operationally]

---

## Draft Options (For Review)

### Option 1: Direct I-V-Q (Best for LinkedIn DMs)
> "Hey [Name], loved your post on [Specific Detail]. 
> 
> Usually when I see [Clinics/Firms] expanding like you are, the front desk systems start to fracture under the new volume. 
> 
> Out of curiosity, are you guys still handling your [intake/scheduling/follow-ups] manually, or have you started automating that yet?"

### Option 2: The Soft Value-Add (Public Comment)
> "[Name], this is a great breakdown of [Topic]. The piece about [Detail] is spot on. Have you found that your team's bandwidth has been the main bottleneck there, or is it purely a systems issue?"

### Option 3: Ultra-Short (Best for Instagram/X)
> "Hey [Name] - saw the post about the new location. Congrats! Quick question: as you scale, are you guys still doing patient intake manually or have you automated that flow?"

### Option 4: The Free Insight (Hormozi Give-First)
> "Hey [Name] — saw the post about [Specific Detail].
> 
> One thing I've seen work really well for [Clinic/Firm] owners at your stage: automating the [intake/follow-up/scheduling] step so your staff isn't manually chasing paperwork after a certain volume threshold. It usually frees up 5–8 hours a week almost immediately.
> 
> Is that something you've looked into, or is the manual process still working okay for now?"

---
**Status:** Awaiting Michael's approval.
```

---

## Frameworks Referenced
- I-V-Q (Insight-Value-Question) — evolved from original IOQ framework
- Alex Hormozi — $100M Leads (give-first lead gen, DM strategy, specificity as credibility signal)
- See: `references/frameworks/hormozi.md`
