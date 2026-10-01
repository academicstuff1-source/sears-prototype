import streamlit as st
import json
import re
from google import genai

# --- AI Core Logic ---

def parse_web_alert_text_ai(raw_text, api_key):
    """Uses Gemini API to extract unstructured text into a bulletproof structured JSON."""
    client = genai.Client(api_key=api_key)
    # Using the fast & cheap model
    model = 'gemini-2.5-flash'
    
    prompt = f"""
    You are a data extraction assistant. Extract all clinical trial postings from the following text.
    Return a JSON list of objects. Each object MUST have exactly these keys (use "N/A" if missing):
    - "posting_id" (e.g. 0009-0895, CA48121-1, or N/A)
    - "timeline" (e.g. "Enrolling", "Starts in 12 Days", or N/A)
    - "project_name" (The study name or description, e.g. "Clinical Research Study...", "Backyard")
    - "compensation" (The dollar amount, e.g. "$7500", "Up to $7500", "$3,750", or N/A)
    - "location" (City/State or clinic name, e.g. "Salt Lake City, UT", "Lincoln")
    - "start_date" (If available, e.g. "Oct 05", otherwise "ASAP")
    - "end_date" (If available, e.g. "Oct 14", otherwise "TBD")
    - "demographics" (e.g. "Healthy Volunteers", "Male & Females")
    - "age_range" (e.g. "Age 18 - 55", "19 to 55 years of age", or N/A)

    Return ONLY a valid JSON list of objects. Do not include markdown formatting blocks like ```json.
    
    Text to parse:
    {raw_text}
    """
    
    response = client.models.generate_content(model=model, contents=prompt)
    text = response.text.strip()
    
    # Clean up potential markdown formatting from the LLM
    if text.startswith("```json"):
        text = text[7:-3]
    elif text.startswith("```"):
        text = text[3:-3]
        
    return json.loads(text.strip())


# --- Output Generators ---

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

st.set_page_config(page_title="Phase One Plug - AI Intake Parser", layout="wide")

# Securely grab the API key from Streamlit secrets so it isn't exposed on GitHub
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except (KeyError, FileNotFoundError):
    api_key = None

if not api_key:
    st.sidebar.title("AI Configuration")
    api_key = st.sidebar.text_input("Gemini API Key", type="password", help="Required for bulletproof AI parsing.")
    st.sidebar.warning("Please enter your API Key, or configure st.secrets in the Streamlit Cloud dashboard.")

st.title("Phase One Plug: AI Data Engine")
st.markdown("Paste your raw output from the **Web Alert App** below. The AI will instantly clean the formatting, extract the data regardless of the structure, and generate your Telegram posts and compliance emails.")

raw_input = st.text_area("Raw Web Alert Text", height=200, placeholder="Paste data here...")

if st.button("Process Data with AI", type="primary"):
    if not raw_input.strip():
        st.warning("Please paste some text first.")
    elif not api_key:
        st.error("AI Parsing requires a Gemini API Key. Please add it to your Streamlit Secrets.")
    else:
        with st.spinner("AI is analyzing and structuring the text..."):
            try:
                studies = parse_web_alert_text_ai(raw_input, api_key)
                
                if not studies:
                    st.error("The AI could not find any valid studies in the text provided.")
                else:
                    st.success(f"Successfully extracted {len(studies)} studies using AI!")
                    
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
                            
                            with st.expander("View Raw AI JSON Data"):
                                st.json(study)
                        
                        st.divider()
            except Exception as e:
                st.error(f"An error occurred during AI parsing: {e}")
