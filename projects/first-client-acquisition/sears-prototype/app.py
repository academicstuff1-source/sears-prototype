import streamlit as st
import re
import json

# --- Core Logic from pipeline.py ---

def parse_web_alert_text(raw_text):
    """Parses the raw unstructured text from the Web Alert app into structured data."""
    lines = [line.strip() for line in raw_text.split('\n')]
    clean_lines = [line for line in lines if line and not '[…]' in line]
    
    studies = []
    
    i = 0
    while i < len(clean_lines):
        line = clean_lines[i]
        
        if i + 1 < len(clean_lines) and re.match(r'Starts in \d+ Days', clean_lines[i+1], re.IGNORECASE):
            current_study = {
                "project_name": line,
                "timeline": clean_lines[i+1]
            }
            
            try:
                current_study["posting_id"] = clean_lines[i+2]
                current_study["location"] = clean_lines[i+3]
                current_study["start_date"] = clean_lines[i+4]
                current_study["end_date"] = clean_lines[i+5]
                current_study["demographics"] = clean_lines[i+6]
                
                comp_raw = clean_lines[i+7]
                current_study["compensation"] = comp_raw.replace('*', '')
                current_study["age_range"] = clean_lines[i+8]
                
                studies.append(current_study)
                i += 9
                continue
                
            except IndexError:
                break
        
        i += 1
        
    return studies

def generate_approval_email(study):
    return f"""Subject: Request to share approved research-study recruitment materials (Ref: {study.get('posting_id', 'N/A')})

Hello {study.get('location', 'Clinic')} Team,

I operate an opt-in community in the DFW area for adults interested in learning about legitimate research-study opportunities. We do not conduct medical screening, make eligibility decisions, provide medical advice, or guarantee enrollment.

I recently learned from your public posting that your organization is recruiting for the '{study.get('project_name', 'Study')}' trial starting {study.get('start_date', 'soon')}. Before sharing any information with our audience, I would like to use only your current approved recruitment materials and official participant contact route.

Could you please provide:
- The current IRB-approved flyer, recruitment copy, or approved study landing page
- Confirmation that we may share it through our community channel
- The official phone number, email, or landing page for prospective participants
- Any channel restrictions, required disclaimers, and the expiration or enrollment-close date

Thank you,
Christopher Sears
Study Scoops"""

def generate_telegram_message(study):
    return f"""[NEW STUDY ALERT: {study.get('project_name', 'Unknown')}]

Location: {study.get('location', 'TBD')}
Compensation: {study.get('compensation', 'TBD')}
Demographics: {study.get('demographics', 'TBD')}
Age Range: {study.get('age_range', 'TBD')}
Dates: {study.get('start_date', 'TBD')} to {study.get('end_date', 'TBD')}

Reference ID: {study.get('posting_id', 'N/A')}
Timeline: {study.get('timeline', 'N/A')}

Next Steps: Ensure you mention the Reference ID when contacting the clinic!"""

def generate_website_html(study):
    return f"""<h2>{study.get('project_name', 'Unknown')} - Paid Clinical Trial</h2>
<ul>
    <li><strong>Location:</strong> {study.get('location', 'TBD')}</li>
    <li><strong>Compensation:</strong> {study.get('compensation', 'TBD')}</li>
    <li><strong>Demographics:</strong> {study.get('demographics', 'TBD')}</li>
    <li><strong>Age Range:</strong> {study.get('age_range', 'TBD')}</li>
    <li><strong>Dates:</strong> {study.get('start_date', 'TBD')} to {study.get('end_date', 'TBD')}</li>
</ul>
<p><strong>Status:</strong> {study.get('timeline', 'N/A')}</p>
<p>If you are interested in participating, please reference ID: <strong>{study.get('posting_id', 'N/A')}</strong> when contacting the clinic.</p>"""


# --- Streamlit UI ---

st.set_page_config(page_title="Phase One Plug - Intake Parser", layout="wide")

st.title("Phase One Plug: Data Formatting Engine")
st.markdown("Paste your raw output from the **Web Alert App** below. This tool will instantly clean the formatting, extract the data, and generate your Telegram posts and compliance emails.")

raw_input = st.text_area("Raw Web Alert Text", height=200, placeholder="Paste data here...")

if st.button("Process Data", type="primary"):
    if not raw_input.strip():
        st.warning("Please paste some text first.")
    else:
        studies = parse_web_alert_text(raw_input)
        
        if not studies:
            st.error("No valid study formats found. Please make sure the text contains the 'Starts in X Days' anchor.")
        else:
            st.success(f"Successfully extracted {len(studies)} studies!")
            
            for idx, study in enumerate(studies, 1):
                st.subheader(f"Study #{idx}: {study.get('project_name', 'Unknown')}")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Telegram Ready Post**")
                    st.code(generate_telegram_message(study), language="text")
                    
                    st.markdown("**Website HTML Payload**")
                    st.code(generate_website_html(study), language="html")
                
                with col2:
                    st.markdown("**Compliance Approval Request (Email Draft)**")
                    st.code(generate_approval_email(study), language="text")
                    
                    with st.expander("View Raw JSON Data"):
                        st.json(study)
                
                st.divider()
