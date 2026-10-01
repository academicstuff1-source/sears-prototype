---
name: cold-call-prep
description: >-
  Generates a high-conversion, psychology-backed cold call battlecard using Chris Voss's no-oriented questioning, Challenger Sale diagnostic structure, and Hormozi's value equation and offer clarity principles.
---

# Cold Call & Discovery Prep Skill (Pro)

Prepares Michael for high-stakes outbound calls by utilizing modern sales psychology (e.g., Chris Voss's "No-oriented" questions, Challenger Sale insights, Hormozi's offer framing). 

## When to Activate
- "Prep me for a cold call with [Name] at [Company]"
- "Build a battlecard for [Prospect]"

## Execution Algorithm

### Step 0: Offer Clarity Check (Hormozi Pass)
Before building the battlecard, identify:
- **Dream Outcome:** What does this prospect actually want?
- **Cost of Inaction:** What is the current cost (time, money, frustration) of not solving this?
- **Reduced Effort/Time:** How does our solution speed up the result and reduce their effort?

### Step 1: Context Ingestion
Locate the target in `references/research/account-briefs/` or execute a rapid search. Identify the core operational pain hypothesis.

### Step 2: Psychological Framework Application
1. **The Opener:** Must be pattern-interrupting and seek permission. (e.g., "I know I'm an interruption...")
2. **The Hook:** A direct statement of the problem we solve, tied to a peer example, quantifying the pain.
3. **The Questions:** Design "No-oriented" or deeply diagnostic questions that force the prospect to think about their workflow friction and cost of inaction.
4. **The Objections:** Prepare "Acknowledge & Pivot" responses. Never argue; validate and redirect.

### Step 3: Output Generation
Generate the brief and save to: `references/research/call-preps/YYYY-MM-DD-[company]-[name].md`

```markdown
# 📞 Cold Call Battlecard: [Name] at [Company]

**Goal:** Secure a 15-minute workflow mapping session.

---

## 1. The Context (10-Second Review)
- **Who:** [Name, Title]
- **The Angle:** [Core hypothesis, e.g., "They just opened a 2nd clinic; front desk is likely drowning in intake forms."]

## 2. The Human Override (Situational Awareness)
*(CRITICAL: Before you pitch, listen to their environment. Are they driving, actively lost, yelling at kids, or dealing with an emergency? If yes, DO NOT PITCH).*
> *"Oh wow, it sounds like you are in the middle of chaos right now. I am going to hang up and let you get sorted. I'll try you back tomorrow. Good luck!"*

## 3. Gatekeeper Strategy (Turning them into an Influencer)
*(CRITICAL RULE: Always verify identity first. Ask "Is this [Owner Name]?" Owner-operators often answer the phones themselves. Never run this play until you confirm they are NOT the owner).*

**The Ask:** *"Hey there, this is Michael. Is [Owner Name] around, or are they tied up on a call right now?"*
**The Pivot:** *"No worries. I work with independent [industry] owners to build operational playbooks. I imagine as the one managing the front, it’s about to get incredibly chaotic for you fielding repetitive questions and chasing down [specific admin task]?"*
**The Ask for Access:** *"That's exactly why I wanted to connect with them before it gets crazy. What is the best way for me to catch [Owner Name] so I can show them how to take that completely off your plate?"*

## 4. The Script
### Phase 1: Pattern Interrupt & Permission
> *"Hey [Name], it's Michael. I know I'm catching you in the middle of your day — do you have 30 seconds for me to tell you why I'm calling, and then you can hang up if it's not relevant?"*

### Phase 2: The Peer Hook (Specificity & Pain)
> *"I work with other [Industry] owners in DFW. A massive problem they're facing right now is their front desk getting bogged down with manual intake forms, appointment reminders, and CRM data entry. It's usually costing them roughly [X hours/week] or causing them to lose follow-ups on every third lead."*

### Phase 3: The Pivot (No-Oriented Question)
> *"Would it be a ridiculous idea to ask how your team is currently handling that volume?"*

## 5. High-Yield Discovery Questions
*(If they open up, ask these to widen the pain and surface the cost of inaction)*
1. *"When a lead comes in at 8 PM, what exactly happens between then and 8 AM the next day?"*
2. *"How much of your staff's week is spent just chasing people for missing paperwork or confirmations?"*
3. *"If you did nothing about this for the next 12 months, what does that actually cost you in lost revenue or wasted payroll?"*
4. *"What would it mean for your business if this bottleneck was completely solved in the next 30 days?"*

## 6. Objection Handling (Acknowledge & Pivot)

| Objection | The Play |
|---|---|
| **"We already have software."** | *"That makes total sense. Most clinics I speak with use [EHR/System]. We don't replace that—we build the 'glue' that stops your staff from having to manually move data in and out of it. How well is [System] handling your after-hours follow-ups?"* |
| **"We are too busy."** | *"I completely understand, and that’s exactly why I called. If you're slammed, it means manual admin is eating your margins. Would it be a terrible idea to put 15 minutes on the calendar next week when things cool down?"* |
| **"Send me an email."** | *"Happy to. So I don't send you generic spam, what is your biggest operational bottleneck right now: patient intake, or lead follow-up?"* |

## 7. The Close (Zero-Risk Diagnostic)
> *"I’d love to show you a 5-minute visual map of how a competitor solved this exact issue. The worst that happens is you get a free map of your workflow gaps to keep, and if it makes sense, we can talk about how to implement it. Do you have 15 minutes on [Day]?"*
```

---

## Frameworks Referenced
- Chris Voss — Never Split the Difference (no-oriented questions, tactical empathy)
- Challenger Sale — Insight-led selling, reframing the buyer's problem
- Alex Hormozi — $100M Offers (value equation, offer clarity), $100M Leads (lead gen hierarchy, DM strategy)
- See: `references/frameworks/hormozi.md`
