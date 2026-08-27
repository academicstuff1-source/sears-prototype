---
name: social-outreach
description: >-
  Use this skill when Michael finds a prospect on social media (LinkedIn, YouTube, Instagram, X) or wants to draft a personalized message/comment based on a post, video, or profile.
  Extracts operational pain signals from content, formulates conversational conversation-starters (DMs, comments, or follow-up emails), and aligns with Michael's non-salesy AI automation positioning.
---

# Social Media Outreach & Engagement Skill

Analyzes social media posts, videos, comments, or profile bios to identify genuine business and workflow pain signals, then drafts high-converting, human, non-spammy outreach messages.

## When to Activate

- "Draft a message for [Name] — here's their LinkedIn post: [content]"
- "Here's an Instagram post / reel from a clinic owner: [description/text], write a DM"
- "Analyze this YouTube video / channel and write an outreach message"
- "Draft a LinkedIn connection request or comment for [Person]"

## Workflow

### Step 1 — Ingest & Analyze Social Content
Review the provided post, video summary, or profile context. Look for implicit or explicit operational signals:
- **Hiring & Bandwidth:** Complaints about being short-staffed, hiring admin roles, or team burnout.
- **Growth & Bottlenecks:** Opening new locations, taking on more patients/clients, scaling pains.
- **Tech & Tool Friction:** Frustrations with existing software, manual spreadsheets, or messy systems.
- **Workflow Highlights:** Videos showing daily routine, office tours, or backend operations.

### Step 2 — Determine Channel Strategy
Select the appropriate format based on channel:
- **LinkedIn DM / InMail:** 3–5 sentences max. Reference specific post insight → connect to practical workflow → low-friction open question.
- **LinkedIn Public Comment:** Thoughtful observation that adds value publicly without pitching.
- **Instagram DM:** Casual, short (2–3 sentences), conversational tone.
- **Email Follow-up Referencing Social Post:** Professional bridge from their public post to a private conversation.

### Step 3 — Apply Non-Negotiable Rules
- **Never sound like a generic AI bot** (no "I came across your inspiring post and was blown away!").
- **Reference a specific detail** that proves you actually watched/read their content.
- **Do not hard-pitch AI services in the first message.** Pitch curiosity and pattern recognition around their problem.
- **Always require Michael's review & explicit approval** before sending externally.

### Step 4 — Generate Draft Options & Save Record
Save output to:
`references/research/social-outreach/YYYY-MM-DD-[platform]-[name-slug].md`

#### Output Format:
```markdown
# Social Outreach: [Prospect Name] — [Platform]

**Date:** YYYY-MM-DD  
**Platform:** [LinkedIn / Instagram / YouTube / X]  
**Prospect:** [Name, Title, Company, Profile URL]  
**Source Content Analyzed:** [Summary/quote of post or video]  
**Observed Signal / Pain Point:** [e.g., Struggling to manage front desk volume during expansion]  

---

## Recommended Angles

### Option A: Direct DM (Conversational & Value-Focused)
> *"Hey [First Name], saw your post about [specific topic/detail from post]. Really liked your point on [specific insight].*
>
> *Curious — as you guys are [expanding/handling that volume], how are you managing the [repetitive workflow, e.g., intake paperwork / lead follow-up] without overwhelming your team?*
>
> *I build simple automation workflows for [practices/businesses] in [DFW/Texas] to take that off the front desk's plate. Would love to swap notes sometime if you're open to it."*

### Option B: Public Comment (Builds Rapport First)
> *"[Insightful, value-add comment directly addressing the post's core topic without a sales pitch — establishing Michael as a knowledgeable peer in operations]."*

### Option C: Short / Casual (Instagram or Quick LinkedIn DM)
> *"Hey [First Name] — loved the reel showing your clinic's backend setup. Quick question: is your team still doing [specific manual step] manually, or have you already automated that piece?"*

---

## Next Steps
- [ ] Review and adjust draft
- [ ] Send via [Platform]
- [ ] Log contact in HubSpot upon response
```
