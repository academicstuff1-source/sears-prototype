---
name: cold-call-prep
description: >-
  Generates a high-conversion, psychology-backed cold call battlecard. 
  Includes permission-to-pitch openers, diagnostic pain questions, and empathy-led objection handlers.
---

# Cold Call & Discovery Prep Skill (Pro)

Prepares Michael for high-stakes outbound calls by utilizing modern sales psychology (e.g., Chris Voss's "No-oriented" questions, Challenger Sale insights). 

## When to Activate
- "Prep me for a cold call with [Name] at [Company]"
- "Build a battlecard for [Prospect]"

## Execution Algorithm

### Step 1: Context Ingestion
Locate the target in `references/research/account-briefs/` or execute a rapid search. Identify the core operational pain hypothesis.

### Step 2: Psychological Framework Application
1. **The Opener:** Must be pattern-interrupting and seek permission. (e.g., "I know I'm an interruption...")
2. **The Hook:** A direct statement of the problem we solve, tied to a peer example.
3. **The Questions:** Design "No-oriented" or deeply diagnostic questions that force the prospect to think about their workflow friction.
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

## 2. The Script

### Phase 1: Pattern Interrupt & Permission
> *"Hey [Name], it's Michael. I know I'm catching you in the middle of your day — do you have 30 seconds for me to tell you why I'm calling, and then you can hang up if it's not relevant?"*

### Phase 2: The Peer Hook
> *"I work with other [Industry] owners in DFW. A massive problem they're facing right now is their front desk getting bogged down with manual intake forms, appointment reminders, and CRM data entry. They’re basically paying skilled staff to do copy-paste work."*

### Phase 3: The Pivot (No-Oriented Question)
> *"Would it be a ridiculous idea to ask how your team is currently handling that volume?"*

## 3. High-Yield Discovery Questions
*(If they open up, ask these to widen the pain)*
1. *"When a lead comes in at 8 PM, what exactly happens between then and 8 AM the next day?"*
2. *"How much of your staff's week is spent just chasing people for missing paperwork or confirmations?"*
3. *"If you could instantly automate one administrative headache tomorrow, what would it be?"*

## 4. Objection Handling (Acknowledge & Pivot)

| Objection | The Play |
|---|---|
| **"We already have software."** | *"That makes total sense. Most clinics I speak with use [EHR/System]. We don't replace that—we build the 'glue' that stops your staff from having to manually move data in and out of it. How well is [System] handling your after-hours follow-ups?"* |
| **"We are too busy."** | *"I completely understand, and that’s exactly why I called. If you're slammed, it means manual admin is eating your margins. Would it be a terrible idea to put 15 minutes on the calendar next week when things cool down?"* |
| **"Send me an email."** | *"Happy to. So I don't send you generic spam, what is your biggest operational bottleneck right now: patient intake, or lead follow-up?"* |

## 5. The Close
> *"I’d love to show you a 5-minute visual map of how a competitor solved this exact issue. If it makes sense, great. If not, you can steal the strategy. Do you have 15 minutes on [Day]?"*
```
