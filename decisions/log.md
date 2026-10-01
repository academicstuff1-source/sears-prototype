# Decision Log

This file is append-only.

Log decisions that materially affect priorities, strategy, operations, tools, projects, clients, financial commitments, or team execution.

Use this format:

[YYYY-MM-DD] DECISION: ...
REASONING: ...
CONTEXT: ...
OWNER: ...

***

[2026-08-27] DECISION: Connected ClickUp as project management dashboard for AI Consulting OS
REASONING: Needed a visual, day-to-day task dashboard to complement the Antigravity workspace files. REST API approach used after MCP connection could not be established in current session.
CONTEXT: Space "AI Consulting OS" created in Michael's Workspace (team ID 90141541221). 7 project folders and 25 tasks built via ClickUp REST API, mirroring the project READMEs in projects/. Token stored in mcp_config.json only (outside git repo). Token should be regenerated after initial setup.
OWNER: Michael

***

[2026-09-02] DECISION: Shifted initial sales angle away from 'Intake Fragmentation' to 'Speed-to-Lead & API Glue'.
REASONING: Call #1 (Viva Day Spa) revealed that major EHRs (like Zenoti) handle digital intake seamlessly. However, hesitation on the call highlighted that our lack of a concrete, defined offer caused a loss of confidence. The new angle positions us as the 'glue' between their closed-loop EHRs and their top-of-funnel marketing/social channels.
CONTEXT: First cold call rep completed. Pivot required to increase confidence and bypass EHR objections.
OWNER: Michael

***

[2026-09-03] DECISION: Shifted outbound focus from cold local Med Spas to Warm Network List (Fortrea alumni and local church/neighbor contacts).
REASONING: Cold outreach to Med Spas revealed high gatekeeper friction and competing cheap human labor ('social media girls'). Pivoting to warm contacts (past colleagues) immediately bypassed trust barriers and resulted in the first booked discovery meeting.
CONTEXT: Hit gatekeepers on 3 cold calls. Pulled a warm list. Call #1 on warm list yielded a booked meeting.
OWNER: Michael

***

[2026-09-03] DECISION: Reserve generic 20-question intake forms exclusively for cold inbound leads. Use hyper-targeted 3-question emails/forms for warm post-discovery prospects.
REASONING: Sending a generic form after a highly specific 30-minute discovery call breaks the illusion of a personalized relationship and signals poor listening.
CONTEXT: Follow-up prep for Christopher Sears.
OWNER: Michael

***

[2026-09-08] DECISION: Reframed the Sears opportunity as a B2B patient recruitment infrastructure play, not a consumer Telegram automation tool.
REASONING: Perplexity Pro analysis revealed that the real economic buyers are research sites, CROs, and recruitment vendors, not Telegram subscribers. Companies like Antidote, SubjectWell/Reify, and Clariness validate the B2B referral model (per consented referral, per prescreen, monthly retainer) at scale. Consumer subscriptions are a supplemental revenue stream at best.
CONTEXT: Pre-call prep for Christopher Sears discovery meeting (Sept 10). This reframe changes the pitch from 'workflow automation tool' to 'compliant participant recruitment infrastructure.' Significant implications for how Michael scopes and prices any engagement coming out of this call. Full research brief saved to references/research/2026-09-08-sears-clinical-trial-recruitment-model.md.
OWNER: Michael

***

[2026-09-08] DECISION: Rejected fully automated voice-to-Telegram broadcast architecture in favor of an approval-gated pipeline for the Sears build.
REASONING: Perplexity Pro analysis identified that any Telegram post containing eligibility criteria, compensation, and a CTA is legally classified as recruitment advertising subject to IRB oversight. Auto-publishing AI-generated posts based solely on phone calls, without written authorization from the research site or CRO, creates material compliance exposure that could destroy B2B partnership potential before it starts.
CONTEXT: Safe architecture: Voice memo to AI transcription to internal CRM record to approval-request email to written authorization to human-reviewed draft to human clicks publish. AI accelerates internal intake and drafting only. Full compliant workflow documented in references/research/2026-09-08-sears-clinical-trial-recruitment-model.md.
OWNER: Michael

***

[2026-09-09] DECISION: Anchored Christopher Sears 30-day pilot build at $1,500 one-time MVP setup and incorporated hybrid intake architecture (scraper + call center voice memos).
REASONING: Sears confirmed he scrapes 35 CRO websites and uses ChatGPT daily, alongside his manual call-center calls and voice memos. His bottleneck is not data collection, but unifying fragmented inputs and monetizing compliantly. Anchoring the initial pilot at $1,500 gives a concrete, low-friction entry point for Michael's first paid consulting engagement while avoiding vague revenue-share commitments early on.
CONTEXT: Discovery call preparation for Sept 10 Sears meeting. Visual slide deck created and saved to references/sears-presentation.html.
OWNER: Michael Anyanwu

***

[2026-09-10] DECISION: Proceed with prototyping phase for Christopher Sears (B2B Clinical Trial Recruitment Infrastructure).
REASONING: Discovery call confirmed alignment on shifting from consumer subscriptions to B2B CRO contracts. Sears lacks the technical execution to modernize the visual interface (Gen Z demographic) and data cleanup. Building a mock website and data pipeline prototype demonstrates our capability to surpass competitor 'Study Scoops' and provides leverage for future B2B negotiations.
CONTEXT: Outcome of Sept 10 discovery meeting. Agreed to a 1-week timeline to review the prototype privately.
OWNER: Michael Anyanwu

***

[2026-09-11] DECISION: Deferred social media content marketing push indefinitely.
REASONING: Outreach has been inconsistent this week. Staying focused on the top priority: qualified sales conversations and pattern recognition from reps. Social media is a long-game channel that produces no signal at this stage and risks diluting outreach effort. Will revisit after outreach rhythm is consistent and client conversations are producing signal.
CONTEXT: Evaluated whether to build a dedicated Social Media Manager assistant. Decided against it. current-priorities.md already flagged this as a 'What Not to Prioritize' item.
OWNER: Michael

***

***

[2026-09-14] DECISION: Transitioned Melanie Powell to active pipeline (discovery meeting booked for Friday 10 AM).
REASONING: Cold call succeeded. Discovered she currently manages 'think about it' prospect follow-ups manually and wants to automate this (and build a lead magnet funnel) to free up time for top-of-funnel marketing like Facebook ads.
CONTEXT: Second active prospect in the pipeline. We need to build a 5-min visual map of an automated discovery-to-close pipeline for Friday's meeting.
OWNER: Michael


***

[2026-09-14] DECISION: Disqualified David Grice (Epiphany Dermatology) from outreach pipeline.
REASONING: Cold call reached the office manager, who curtly stated all systems are handled by corporate and refused engagement. Validates hypothesis that recently acquired practices have high gatekeeper friction and zero local buying autonomy.
CONTEXT: First call from the church/neighbor warm list that failed. Moving on to targets with clear local ownership.
OWNER: Michael


***

[2026-09-14] DECISION: Reframed A. Cheray Scott (CS InsureWise) from standard AI consulting prospect to a consulting-led play â€” build the call triage system/playbook, not fill the human receptionist role.
REASONING: Cold call conversation revealed she is deeply AI-averse (confirmed twice on the call) and has built her entire business on a white-gloves, human concierge model for Medicare-age senior clients. She has a real, confirmed pain: call overflow and no one to triage repetitive client questions during open enrollment. She pivoted the conversation toward hiring Michael as a part-time human call screener. Declined that framing in the moment; instead positioning as the consultant who *builds the triage system* so that whoever she hires (human) can operate it effectively. This preserves the consulting engagement model. Follow-up text sent with reframe.
CONTEXT: Call #3 from warm church/neighbor list. Two-attempt call (she hung up on call 1 thinking Michael was AI). Reached full conversation on call 2. She asked Michael to text his info for a callback. Key intelligence: she pays her current VA ~\$25/hr for CRM/newsletters; is approaching 60 and wants more work-life balance; open enrollment is her crunch period; her client base is loyalty-driven seniors who screen all calls.
OWNER: Michael

***

[2026-09-17] DECISION: Rejected clinicaltrials.gov as a viable data source for the Christopher Sears project.
REASONING: The platform's information lags behind sponsor pages, and the dense, scientific formatting is poorly suited for the target demographic (Gen Z).
CONTEXT: Sears follow-up meeting (Sept 17).
OWNER: Michael

***

[2026-09-17] DECISION: Approved Phase One Plug dark color scheme (blues/purples/black) for the participant portal.
REASONING: White backgrounds were rejected by Sears in favor of an HBO Max / Mac aesthetic. Spelled out "One" per final adjustment.
CONTEXT: Sears follow-up meeting (Sept 17) prototype review.
OWNER: Michael

***

[2026-09-17] DECISION: Committed to building an automation script tailored specifically to clean and format output from the "Web Alert" mobile app.
REASONING: Sears currently manually removes spaces, asterisks, and periods from the Web Alert output before posting to Telegram. Automating this exact cleanup process provides immediate, tangible value for his workflow.
CONTEXT: Sears follow-up meeting (Sept 17).
OWNER: Michael

***

[2026-09-18] DECISION: Advanced Melanie Powell (Little Flower Birth Services) to proposal stage.
REASONING: Diagnostic call confirmed two concrete, unautomated pain points: (1) post-discovery "think about it" follow-up sequence is fully manual despite prior attempts with an IT guide; (2) lead magnet funnel emails exist but the end-to-end pipeline lacks automation. She confirmed both would be a no-brainer to solve. Requested a formal proposal.
CONTEXT: 12-minute Google Meet diagnostic call (Sept 18, 10 AM). Proposed automation: Day 1 value add â†’ Day 3 soft SMS check-in â†’ Day 7 objection handling â†’ hot lead ping to Melanie when ready. Follow-up proposal review meeting booked for Wednesday, Sept 23 at 10 AM. Email: melanie.powell@littleflowerbirthservices.com.
OWNER: Michael

***

[2026-09-21] DECISION: Capped the Christopher Sears project at Phase 3 (Intake script, pipeline, participant website). Categorizing the work strictly as a portfolio case study, not a path to a paying engagement.
REASONING: Sears is a frequent trial participant himself and floated an LLC partnership in lieu of payment—classic signals of an unfunded prospect. Furthermore, the B2B model (Phases 4-6) requires a formal legal entity, IRB/healthcare attorneys, BAA compliance, and real research site relationships to execute safely. A solo consultant cannot vibe-code a compliant B2B clinical trial recruitment network.
CONTEXT: Capping at Phase 3 allows Michael to walk away with a highly tangible, impressive automation case study ('Built an automated clinical trial opportunity intake and distribution pipeline') without taking on legal risk or wasting time chasing a prospect with no budget.
OWNER: Michael

[2026-09-22] DECISION: Abandoned HubSpot CRM in favor of managing pipeline entirely within the workspace via markdown files.
REASONING: Single-player speed and minimizing friction. Using a separate SaaS tool for a handful of prospects violated the core goal of optimizing for reps. Antigravity will manage the pipeline.md file natively.
CONTEXT: Michael naturally operated out of the terminal; the HubSpot requirement was a legacy assumption from the original project files.
OWNER: Michael

[2026-09-22] DECISION: Pivot Christopher Sears Oct 1 presentation strategy.
REASONING: Intelligence revealed his Telegram audience is only 43 people and he is an older operator unsuited for complex social media. Automation value proposition shifts from 'handling volume' to 'freeing up time for low-tech marketing (Email/Facebook/Nextdoor)' to build a viable B2B audience.
CONTEXT: Phase 1/2 python parser built. Needed to align the technical build with a realistic business model for his demographic.
OWNER: Michael

[2026-09-23] DECISION: Refined targeting to focus on 'The Overwhelmed Owner-Operator' in low-friction health sub-niches.
REASONING: Corporate healthcare (e.g. Epiphany Dermatology) has insurmountable IT and gatekeeper friction. Shifted to cash-pay PT, mobile wellness, concierge medicine, and independent health insurance brokers (especially approaching Q4 Open Enrollment). These owners have severe hands-on time constraints, manual intake pain, and lack corporate gatekeepers.
CONTEXT: A high-volume cold calling sprint revealed that mobile IV owners often already have systems, but solo insurance brokers and cash-pay therapists are highly vulnerable to missed calls and manual paperwork.
OWNER: Michael

***

[2026-09-24] DECISION: Shifted Independent Broker pitch to the Anti-AI 'Triage Playbook'.
REASONING: Target audience (Medicare brokers) serves seniors who expect white-glove human touch. Framing automation as 'AI' triggers rejection. Framing it as a bulletproof blueprint/playbook for their human receptionist/VA lands perfectly.
CONTEXT: Validated during calls with Cheray Scott and other independent brokers facing the Oct 15 AEP rush.
OWNER: Michael

***

[2026-09-24] DECISION: Disqualified high-touch solo operators who use repetitive calls as relationship builders.
REASONING: Not all solo operators view missed calls or repetitive questions as a pain point. Some (like Lamonica Thomas) intentionally use them to build trust and loyalty with seniors. Automation here is viewed as a threat to their retention model.
CONTEXT: Audio intelligence gathered from Lamonica Thomas call.
OWNER: Michael

[2026-09-25] DECISION: Added 'Phase 0: The Human Override' to all cold call scripts.
REASONING: Calling prospects while they are driving, lost, or dealing with emergencies and proceeding to pitch destroys trust instantly. By prioritizing situational awareness and giving them an 'out', we behave like operational partners rather than telemarketers.
CONTEXT: Hit an agency owner (Arlene) while she was driving and lost looking for a rental place. Pitched anyway, got hung up on.
OWNER: Michael

***

[2026-09-28] DECISION: Capped Sears technical build at the Telegram Headless CMS (bot.py). Rejected building the fully automated Make.com+Distill cloud stack and Google Sheets API integration for the hand-off.
REASONING: The 'Consultant's Trap'. Handing over a complex SaaS architecture or cloud webhook server for a free pro-bono project traps the consultant into permanent IT support. The Telegram bot isolates the risk, solves the immediate data-entry pain, requires zero training, and secures the portfolio case study without scope creep.
CONTEXT: Preparing for the Oct 1 Sears presentation.
OWNER: Michael

[2026-09-30] DECISION: Formally added 'Independent Medicare/Health Insurance Brokers' to the top-tier cold call target profile (through October) to capitalize on the urgency of the upcoming Oct 15th AEP (Annual Enrollment Period) crunch.
REASONING: The 'AEP crunch' is a proven, highly validated pain point (heavy inbound call volume of repetitive questions + tedious Medical Intake/SOA collection) that creates massive urgency. 
CONTEXT: This demographic perfectly matches the 'Overwhelmed Owner-Operator' thesis, but requires a very specific pitch. We merged the 'Shield from repetitive noise' concept with the 'Medical Intake Protocol' into a unified 'Triage Playbook' pitch.
OWNER: Michael

***

[2026-10-01] DECISION: The AI-driven parsing engine (LLM) is the primary production solution for the Sears Prototype. The Regex parser is strictly a fallback mechanism.
REASONING: The AI engine reads dynamically like a human, which is mandatory for production use where the scraped text format changes unpredictably. The temporary pivot to Regex on Oct 1 was strictly to bypass a live API outage (503 error) during a demo window. 
CONTEXT: Michael clarified that the tool must be built for real-world client use, not just a controlled demo. We will build both: the AI engine runs point, and the Regex engine serves as an offline failsafe.
OWNER: Michael

***

[2026-10-01] DECISION: Designed Multi-Model Fallback Routing for Phase 2 architectures.
REASONING: Using multiple keys for the same LLM (e.g., Gemini) does not protect against server-side capacity outages (503s). True failsafe architecture requires catching the provider error and routing to a completely different LLM provider (e.g., OpenAI or Anthropic).
CONTEXT: Sparked by the Gemini 503 outage during Sears prep. This will be pitched as an 'Enterprise-grade reliability' feature for paid Phase 2 engagements.
OWNER: Michael
