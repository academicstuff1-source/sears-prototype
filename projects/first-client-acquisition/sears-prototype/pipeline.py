import re
import json

def parse_web_alert_text(raw_text):
    """Parses the raw unstructured text from the Web Alert app into structured data."""
    # Clean up the raw text: remove empty lines and [...] markers
    lines = [line.strip() for line in raw_text.split('\n')]
    clean_lines = [line for line in lines if line and not '[…]' in line]
    
    studies = []
    current_study = {}
    
    # We iterate through the lines looking for anchor points. 
    # A reliable anchor is "Starts in X Days" or the Compensation "$X,XXX*"
    
    i = 0
    while i < len(clean_lines):
        line = clean_lines[i]
        
        # Heuristic: the study block consistently starts with a Project Name (e.g., "Backyard")
        # immediately followed by "Starts in X Days"
        if i + 1 < len(clean_lines) and re.match(r'Starts in \d+ Days', clean_lines[i+1], re.IGNORECASE):
            # We found the start of a block!
            current_study = {
                "project_name": line,
                "timeline": clean_lines[i+1]
            }
            
            # Now we try to safely grab the next expected fields based on the pattern:
            # ID, Location, Start Date, End Date, Demographics, Comp, Age
            try:
                current_study["posting_id"] = clean_lines[i+2]
                current_study["location"] = clean_lines[i+3]
                current_study["start_date"] = clean_lines[i+4]
                current_study["end_date"] = clean_lines[i+5]
                current_study["demographics"] = clean_lines[i+6]
                
                # Clean up compensation (remove asterisks)
                comp_raw = clean_lines[i+7]
                current_study["compensation"] = comp_raw.replace('*', '')
                
                # Age requirement
                current_study["age_range"] = clean_lines[i+8]
                
                studies.append(current_study)
                # Advance the index past this block
                i += 9
                continue
                
            except IndexError:
                # We hit the end of the text before finishing a block
                break
        
        # If it doesn't match our start anchor, move to the next line
        i += 1
        
    return studies

def generate_approval_email(study):
    """Generates the compliant approval request email using the extracted data."""
    email_template = f"""Subject: Request to share approved research-study recruitment materials (Ref: {study.get('posting_id', 'N/A')})

Hello {study.get('location', 'Clinic')} Team,

I operate an opt-in community in the DFW area for adults interested in learning about legitimate research-study opportunities. We do not conduct medical screening, make eligibility decisions, provide medical advice, or guarantee enrollment.

I recently learned from your public posting that your organization is recruiting for the '{study.get('project_name', 'Study')}' trial starting {study.get('start_date', 'soon')}. Before sharing any information with our audience, I would like to use only your current approved recruitment materials and official participant contact route.

Could you please provide:
- The current IRB-approved flyer, recruitment copy, or approved study landing page
- Confirmation that we may share it through our community channel
- The official phone number, email, or landing page for prospective participants
- Any channel restrictions, required disclaimers, and the expiration or enrollment-close date

Thank you,
Thank you,
Christopher Sears
Study Scoops
"""
    return email_template

def generate_telegram_message(study):
    """Formats the structured study data into a clean Telegram message."""
    message = f"""[NEW STUDY ALERT: {study.get('project_name', 'Unknown')}]

Location: {study.get('location', 'TBD')}
Compensation: {study.get('compensation', 'TBD')}
Demographics: {study.get('demographics', 'TBD')}
Age Range: {study.get('age_range', 'TBD')}
Dates: {study.get('start_date', 'TBD')} to {study.get('end_date', 'TBD')}

Reference ID: {study.get('posting_id', 'N/A')}
Timeline: {study.get('timeline', 'N/A')}

Next Steps: Ensure you mention the Reference ID when contacting the clinic!"""
    return message

def mock_publish_to_telegram(study):
    """Simulates pushing the formatted message to the Telegram Bot API."""
    import time
    print("\n[SYSTEM] Connecting to Telegram API (Mock)...")
    time.sleep(1)
    print(f"[SYSTEM] POST https://api.telegram.org/bot<TOKEN>/sendMessage")
    print(f"[SYSTEM] Payload delivered to Chat ID: -100XXXXXXX")
    print("\n--- TELEGRAM MESSAGE PREVIEW ---")
    print(generate_telegram_message(study))
    print("--------------------------------\n")

def mock_publish_to_website(study):
    """Simulates pushing the structured study to a WordPress/Web CMS API."""
    import time
    print("\n[SYSTEM] Connecting to Website CMS API (Mock)...")
    time.sleep(1)
    
    # Generate an SEO-friendly title
    title = f"Paid Clinical Trial in {study.get('location', 'DFW')} - {study.get('compensation', '$$')}"
    
    # Generate the HTML body for the website post
    html_content = f"""<h2>{study.get('project_name', 'Unknown')} - Paid Clinical Trial</h2>
<ul>
    <li><strong>Location:</strong> {study.get('location', 'TBD')}</li>
    <li><strong>Compensation:</strong> {study.get('compensation', 'TBD')}</li>
    <li><strong>Demographics:</strong> {study.get('demographics', 'TBD')}</li>
    <li><strong>Age Range:</strong> {study.get('age_range', 'TBD')}</li>
    <li><strong>Dates:</strong> {study.get('start_date', 'TBD')} to {study.get('end_date', 'TBD')}</li>
</ul>
<p><strong>Status:</strong> {study.get('timeline', 'N/A')}</p>
<p>If you are interested in participating, please reference ID: <strong>{study.get('posting_id', 'N/A')}</strong> when contacting the clinic.</p>"""
    
    payload = {
        "title": title,
        "content": html_content,
        "status": "publish",
        "categories": ["Paid Trials", study.get('location', 'DFW')]
    }
    
    print(f"[SYSTEM] POST https://studyscoops.com/wp-json/wp/v2/posts")
    print("\n--- WEBSITE CMS PAYLOAD PREVIEW ---")
    print(json.dumps(payload, indent=2))
    print("-----------------------------------\n")

if __name__ == "__main__":
    print("Reading raw Web Alert data...")
    with open('raw_input.txt', 'r', encoding='utf-8') as f:
        raw_data = f.read()
        
    extracted_studies = parse_web_alert_text(raw_data)
    
    print(f"Successfully extracted {len(extracted_studies)} complete studies from the unstructured text.\n")
    
    for idx, study in enumerate(extracted_studies, 1):
        print(f"=== STUDY #{idx} STRUCURED DATA ===")
        print(json.dumps(study, indent=2))
        
        # Phase 1: B2B Compliance Email
        print("\n--- AUTO-GENERATED COMPLIANCE EMAIL ---")
        print(generate_approval_email(study))
        print("---------------------------------------")
        
        # Phase 2: Telegram Push
        mock_publish_to_telegram(study)
        
        # Phase 3: Website CMS Push
        mock_publish_to_website(study)
        
        print("=" * 60)
        print("\n")
