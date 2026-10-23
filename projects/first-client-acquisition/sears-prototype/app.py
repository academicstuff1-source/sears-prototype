import streamlit as st
import streamlit.components.v1 as components
import re
import os
import json
from bs4 import BeautifulSoup
from google import genai
from google.genai import types
from pydantic import BaseModel

# --- Component Setup ---
component_path = os.path.join(os.path.dirname(__file__), "rich_paste_component")
rich_paste = components.declare_component("rich_paste", path=component_path)

# --- Core Logic ---

def clean_web_alert_html(raw_html):
    """
    Parses raw clipboard HTML, strips elements containing strikethroughs or red markers, 
    and returns clean text alongside debug metrics.
    """
    soup = BeautifulSoup(raw_html, "html.parser")
    removed_count = 0
    
    # 1. Defensively strip deleted/old text
    for tag in soup.find_all(True):
        remove = False
        
        # Safely get attributes since tag.attrs can occasionally be None
        attrs = getattr(tag, 'attrs', {})
        if attrs is None:
            attrs = {}
            
        # Check standard strikethrough tags
        if tag.name in ['del', 's', 'strike']:
            remove = True
            
        # Safely extract style
        style = attrs.get('style', '')
        if isinstance(style, list):
            style = ' '.join(style)
        style = style.lower()
        
        if 'line-through' in style:
            remove = True
        
        # Check explicit color attributes (red/darkred)
        if 'color: red' in style or 'color:red' in style or '#ff0000' in style:
            remove = True
            
        color_attr = attrs.get('color', '')
        if isinstance(color_attr, list):
            color_attr = ' '.join(color_attr)
        color_attr = color_attr.lower()
        
        if color_attr == 'red' or color_attr == '#ff0000':
            remove = True
            
        if remove:
            tag.decompose()
            removed_count += 1

    # 2. Preserve surviving <a href="..."> links inline before extracting plain text
    for a_tag in soup.find_all('a', href=True):
        href = str(a_tag.get('href', '')).strip()
        if href and not href.lower().startswith(('javascript:', 'mailto:', '#')):
            link_text = a_tag.get_text(strip=True)
            a_tag.replace_with(f"{link_text} ({href})" if link_text else href)

    # 3. Tag inserted/green elements with [NEW/UPDATED: ...] so the AI can distinguish changed studies from unchanged ones
    for ins_tag in soup.find_all(['ins', 'span', 'font']):
        if ins_tag.find_parent('div', class_='header-bar'):
            continue
        is_ins = ins_tag.name == 'ins'
        if not is_ins:
            attrs = getattr(ins_tag, 'attrs', {}) or {}
            style = str(attrs.get('style', '')).lower()
            color_attr = str(attrs.get('color', '')).lower()
            if any(g in style for g in ('#52ff52', '#113b11', 'color: green', 'color:green', '#00ff00')) or color_attr in ('green', '#00ff00', '#52ff52'):
                is_ins = True
        if is_ins:
            inner_text = ins_tag.get_text()
            if inner_text.strip():
                ins_tag.replace_with(f"[NEW/UPDATED: {inner_text}]")
            
    # 4. Extract surviving text
    clean_text = soup.get_text(separator='\n')
    
    # Post-process: collapse multiple newlines
    clean_text = re.sub(r'\n\s*\n', '\n\n', clean_text).strip()
    return clean_text, removed_count

class StudyModel(BaseModel):
    posting_id: str | None
    project_name: str | None
    timeline: str | None
    location: str | None
    start_date: str | None
    end_date: str | None
    return_visits: str | None
    demographics: str | None
    smoking_status: str | None
    childbearing_status: str | None
    compensation: str | None
    age_range: str | None
    study_url: str | None

class StudiesResponse(BaseModel):
    studies: list[StudyModel]

def infer_smoking_status(text):
    """Infers smoking requirement from study text if not explicitly separated."""
    if not text:
        return "Not Specified"
    lower = text.lower()
    if "non / ex-smoker" in lower or "non/ex-smoker" in lower:
        return "Non / Ex-smoker only"
    if "smokers & non-smokers" in lower or "smokers and non-smokers" in lower:
        return "Smokers & Non-Smokers"
    if "non-smoker" in lower or "non smoker" in lower or "nonsmoker" in lower:
        return "Non-smoker"
    if "smoker" in lower:
        return "Smokers Permitted"
    return "Not Specified"

def infer_childbearing_status(demographics_text):
    """Infers childbearing / non-childbearing requirement from demographics text."""
    if not demographics_text:
        return "Not Specified"
    lower = demographics_text.lower()
    if "non-childbearing" in lower or "non childbearing" in lower or "sterile" in lower or "postmenopausal" in lower or "post-menopausal" in lower:
        return "Non-Childbearing Potential Required"
    if "childbearing" in lower:
        return "Childbearing Potential Permitted"
    if ("male" in lower or "men" in lower) and "female" not in lower and "women" not in lower:
        return "N/A (Males Only)"
    return "Not Specified (Verify with Clinic)"

def extract_fallback_url(raw_text):
    """Finds the first explicit https:// URL or bare domain (e.g. helpresearch.com) in the text."""
    url_match = re.search(r'https?://[^\s\)\"\'\<\>]+', raw_text, re.IGNORECASE)
    if url_match:
        return url_match.group(0)
    domain_match = re.search(r'\b([a-z0-9-]+\.(?:com|org|net|edu|gov|io|co\.uk))(?:/[^\s\)\"\'\<\>]*)?', raw_text, re.IGNORECASE)
    if domain_match:
        return f"https://{domain_match.group(0)}"
    return "TBD"

def parse_web_alert_text_regex(raw_text):
    """Fallback: rigid positional parser."""
    fallback_url = extract_fallback_url(raw_text)
    lines = [line.strip() for line in raw_text.split('\n')]
    clean_lines = [line for line in lines if line and not '[?]' in line]
    
    studies = []
    i = 0
    while i < len(clean_lines):
        line = clean_lines[i]
        
        # Format 1: Triggered by "Starts in X Days"
        if i + 1 < len(clean_lines) and re.match(r'Starts in \d+ Days', clean_lines[i+1], re.IGNORECASE):
            current_study = {"project_name": line, "timeline": clean_lines[i+1], "study_url": fallback_url}
            try:
                current_study["posting_id"] = clean_lines[i+2]
                current_study["location"] = clean_lines[i+3]
                current_study["start_date"] = clean_lines[i+4]
                current_study["end_date"] = clean_lines[i+5]
                current_study["demographics"] = clean_lines[i+6]
                current_study["childbearing_status"] = infer_childbearing_status(clean_lines[i+6])
                current_study["compensation"] = clean_lines[i+7].replace('*', '')
                current_study["age_range"] = clean_lines[i+8]
                studies.append(current_study)
                i += 9
                continue
            except IndexError:
                break
                
        # Format 2: Triggered by "Enrolling" immediately after an ID
        elif i + 1 < len(clean_lines) and clean_lines[i+1].lower() == 'enrolling':
            current_study = {"posting_id": line, "timeline": clean_lines[i+1], "study_url": fallback_url}
            try:
                current_study["demographics"] = clean_lines[i+2]
                current_study["childbearing_status"] = infer_childbearing_status(clean_lines[i+2])
                current_study["project_name"] = clean_lines[i+3]
                current_study["compensation"] = clean_lines[i+4]
                current_study["location"] = clean_lines[i+5]
                current_study["start_date"] = "ASAP"
                current_study["end_date"] = "TBD"
                
                age_range = "TBD"
                for j in range(i+6, min(i+12, len(clean_lines))):
                    if "Age" in clean_lines[j]:
                        age_range = clean_lines[j]
                        break
                current_study["age_range"] = age_range
                
                studies.append(current_study)
                i += 5
                continue
            except IndexError:
                break
        
        i += 1
        
    return studies

def get_active_api_key():
    """Returns custom API key from sidebar if provided, otherwise falls back to Streamlit secrets."""
    custom_key = st.session_state.get("custom_api_key", "").strip()
    if custom_key:
        return custom_key
    try:
        return st.secrets.get("GEMINI_API_KEY")
    except Exception:
        return None

def parse_web_alert_text(raw_text):
    """Primary: AI parsing using Gemini. Fallback: Regex parsing."""
    api_key = get_active_api_key()
    if not api_key:
        st.warning("No Gemini API key found in Secrets or Sidebar. Falling back to Regex parser.")
        return parse_web_alert_text_regex(raw_text)
        
    client = genai.Client(api_key=api_key)
    prompt = f"""
    You are a data extraction assistant for clinical trials. 
    Extract active clinical trial study opportunities from the following unstructured text.

    CRITICAL FILTERING & DIFF RULES:
    1. Plain-Text Diff Protection: If the text comes from a plain-text diff where two conflicting values appear back-to-back on the same line (e.g. 'Cohort A2 A3', 'October 22 to 26, November 16 to 20, 2026', or '(CB3)(B3)'), Web Alert always puts the old deleted value first and the new added value second. ALWAYS pick the SECOND (newer) value.
    2. Only New/Updated Studies: If '[NEW/UPDATED: ...]' markers appear anywhere in the text, ONLY extract studies that contain at least one '[NEW/UPDATED: ...]' marker (skip studies on the page that had zero changes). Be sure to strip the '[NEW/UPDATED: ]' wrapper from your output values. If no '[NEW/UPDATED: ...]' markers appear anywhere in the text, extract all active studies.
    3. Skip Closed Studies & Generic Sign-Up Cards:
       - Do NOT extract any study marked 'Recruitment Complete', 'Recruitment Closed', or 'Full'.
       - Do NOT extract generic clinic database/newsletter sign-up cards that are not specific trials (e.g. 'Overweight Participants' with compensation 'To be confirmed' and 'Receive alerts for future study opportunities').

    For each valid active study, carefully identify the following. If completely missing, use "TBD" or null.
    - posting_id: Unique ID or cohort name (e.g. '7080413 Cohort A3')
    - project_name: What the study is about (e.g. 'Asthma', 'SAD 6', 'Investigational medication')
    - timeline: Status or timeline (e.g. 'Recruiting now.', 'Recruiting soon.')
    - location: City or clinic (e.g. 'Miami')
    - start_date: Specific start date or 'ASAP' (e.g. '4 Nov', 'November 16')
    - end_date: Specific end date or 'TBD' (e.g. '21 Nov', 'November 20, 2026')
    - return_visits: Any mention of overnight stays, return visits, or follow-up visits (e.g. '0 return visits', '7 return visits', '1 overnight stay (4 nights) and 1 return visit'). If not mentioned in the text, use null.
    - demographics: Who the study is looking for — gender/health group ONLY (e.g. 'Men and surgically sterile or postmenopausal women', 'Healthy Male Participants'). Do NOT include return visits or smoking status here.
    - smoking_status: Explicit smoking requirement (e.g. 'Non-smoker', 'Non / Ex-smoker only', 'Smokers & Non-Smokers'). If not mentioned in the text, use 'Not Specified'.
    - childbearing_status: Explicit childbearing/fertility status indicator (e.g. 'Non-Childbearing Potential Required', 'Childbearing Potential Permitted', 'N/A (Males Only)', or 'Not Specified (Verify with Clinic)')
    - compensation: Payment amount (e.g. '$2,280')
    - age_range: Required ages (e.g. '18 to 65')
    - study_url: Official study link or source website URL (e.g. 'https://helpresearch.com' or specific study href). If only a domain name like 'helpresearch.com' appears in the text, format it as 'https://helpresearch.com'. If completely missing, use 'TBD'.
    
    Raw text to parse:
    {raw_text}
    """
    
    model_candidates = [
        'gemini-3.6-flash',
        'gemini-3.5-flash',
        'gemini-3.5-flash-lite',
        'gemini-3.1-flash-lite',
        'gemini-3.8-flash',
    ]
    
    try:
        response = None
        last_error = None
        for idx, model_name in enumerate(model_candidates):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                        response_schema=StudiesResponse,
                        temperature=0.1
                    ),
                )
                break
            except Exception as e:
                last_error = e
                if ("503" in str(e) or "429" in str(e)) and idx + 1 < len(model_candidates):
                    next_model = model_candidates[idx + 1]
                    st.warning(f"⚠️ {model_name} is experiencing high demand (503). Auto-routing to {next_model}...")
                    continue
                raise e
        
        if response is None and last_error is not None:
            raise last_error

        data = json.loads(response.text)
        studies = data.get("studies", [])
        
        # Convert objects to dicts so the rest of the app doesn't break
        fallback_url = extract_fallback_url(raw_text)
        studies_dict = []
        for s in studies:
            d = s if isinstance(s, dict) else s.copy()
            if not d.get("study_url") or d.get("study_url") in ("TBD", "null", "None"):
                d["study_url"] = fallback_url
            if not d.get("smoking_status") or d.get("smoking_status") in ("TBD", "null", "None"):
                d["smoking_status"] = infer_smoking_status(d.get("demographics", ""))
            if not d.get("childbearing_status") or d.get("childbearing_status") in ("TBD", "null", "None"):
                d["childbearing_status"] = infer_childbearing_status(d.get("demographics", ""))
            studies_dict.append(d)
            
        if not studies_dict and len(raw_text.strip()) > 50:
            return parse_web_alert_text_regex(raw_text)
            
        return studies_dict
    except Exception as e:
        st.error(f"AI parsing failed: {e}. Falling back to Regex parser.")
        return parse_web_alert_text_regex(raw_text)

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

def format_dates_with_visits(study):
    start = study.get('start_date') or 'TBD'
    end = study.get('end_date') or 'TBD'
    visits = study.get('return_visits')
    
    if end and str(end).upper() not in ('TBD', 'NONE', 'NULL', '') and end != start:
        date_str = f"{start} to {end}"
    else:
        date_str = str(start)
        
    if visits and str(visits).upper() not in ('TBD', 'NONE', 'NULL', ''):
        return f"{date_str} ({visits})"
    return date_str

def generate_telegram_message(study):
    study_url = study.get('study_url') or 'TBD'
    smoking = study.get('smoking_status') or infer_smoking_status(study.get('demographics', ''))
    cb_status = study.get('childbearing_status') or infer_childbearing_status(study.get('demographics', ''))
    dates_line = format_dates_with_visits(study)
    return f"""[NEW STUDY ALERT: {study.get('project_name', 'Unknown')}]

Location: {study.get('location', 'TBD')}
Compensation: {study.get('compensation', 'TBD')}
Looking For: {study.get('demographics', 'TBD')}
Smoking Status: {smoking}
Childbearing Status: {cb_status}
Ages: {study.get('age_range', 'TBD')}
Dates: {dates_line}

Reference ID: {study.get('posting_id', 'N/A')}
Timeline: {study.get('timeline', 'N/A')}
Official Study Link: {study_url}

Next Steps: Ensure you mention Phase One Plug and Reference ID ({study.get('posting_id', 'N/A')}) when contacting the clinic!"""

def generate_website_html(study):
    study_url = study.get('study_url') or 'TBD'
    smoking = study.get('smoking_status') or infer_smoking_status(study.get('demographics', ''))
    cb_status = study.get('childbearing_status') or infer_childbearing_status(study.get('demographics', ''))
    dates_line = format_dates_with_visits(study)
    link_html = f'<a href="{study_url}" target="_blank" rel="noopener noreferrer">{study_url}</a>' if str(study_url).startswith('http') else study_url
    return f"""<h2>{study.get('project_name', 'Unknown')} - Paid Clinical Trial</h2>
<ul>
    <li><strong>Location:</strong> {study.get('location', 'TBD')}</li>
    <li><strong>Compensation:</strong> {study.get('compensation', 'TBD')}</li>
    <li><strong>Looking For:</strong> {study.get('demographics', 'TBD')}</li>
    <li><strong>Smoking Status:</strong> {smoking}</li>
    <li><strong>Childbearing Status:</strong> {cb_status}</li>
    <li><strong>Ages:</strong> {study.get('age_range', 'TBD')}</li>
    <li><strong>Dates:</strong> {dates_line}</li>
    <li><strong>Official Study Link:</strong> {link_html}</li>
</ul>
<p><strong>Status:</strong> {study.get('timeline', 'N/A')}</p>
<p>If you are interested in participating, please mention <strong>Phase One Plug</strong> and reference ID: <strong>{study.get('posting_id', 'N/A')}</strong> when contacting the clinic.</p>"""


# --- Streamlit UI ---

st.set_page_config(page_title="Phase One Plug - Intake Parser", layout="wide", initial_sidebar_state="collapsed")

with st.sidebar:
    st.header("⚙️ Settings")
    with st.expander("🔑 API Key Settings", expanded=False):
        st.text_input(
            "Custom Google Gemini API Key (Optional)",
            type="password",
            key="custom_api_key",
            help="Leave blank to use the default backend key, or paste your own free key from Google AI Studio.",
        )
        st.caption("Get a free key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey)")

st.title("Phase One Plug: Data Formatting Engine")
st.markdown("Paste one or multiple pages from **Web Alert** below to build your batch, then click **Process Batch** to format everything at once.")

# Initialize session state for Batch Queue
if "batch_queue" not in st.session_state:
    st.session_state.batch_queue = []
if "last_paste_ts" not in st.session_state:
    st.session_state.last_paste_ts = None
if "processed_studies" not in st.session_state:
    st.session_state.processed_studies = []
if "has_processed" not in st.session_state:
    st.session_state.has_processed = False

# 1. Capture Raw HTML from Clipboard via custom component
raw_event = rich_paste()

if raw_event:
    if isinstance(raw_event, dict):
        raw_input = raw_event.get("content", "")
        paste_ts = raw_event.get("timestamp")
    else:
        raw_input = str(raw_event)
        paste_ts = hash(raw_input)

    if raw_input and paste_ts != st.session_state.last_paste_ts:
        st.session_state.last_paste_ts = paste_ts
        is_html = bool(re.search(r'<[a-z][\s\S]*>', raw_input, re.IGNORECASE))

        if not is_html:
            clean_text = raw_input
            removed_count = 0
        else:
            clean_text, removed_count = clean_web_alert_html(raw_input)

        source_label = extract_fallback_url(clean_text)
        if source_label == "TBD":
            first_lines = [l.strip() for l in clean_text.split('\n') if l.strip()]
            source_label = first_lines[0][:40] if first_lines else "Pasted Page"

        st.session_state.batch_queue.append({
            "id": paste_ts,
            "source": source_label,
            "raw_html": raw_input,
            "clean_text": clean_text,
            "removed_count": removed_count,
            "is_html": is_html,
        })

# 2. Display Batch Queue Controls
if st.session_state.batch_queue:
    st.subheader(f"📋 Batch Queue ({len(st.session_state.batch_queue)} {'Page' if len(st.session_state.batch_queue) == 1 else 'Pages'} Ready)")

    for idx, item in enumerate(st.session_state.batch_queue):
        q_col1, q_col2 = st.columns([6, 1])
        with q_col1:
            if not item["is_html"]:
                status_badge = "⚠️ Plain text pasted (using plain-text diff fallback)"
            elif item["removed_count"] == 0:
                status_badge = "ℹ️ 0 deleted elements detected (all new or unchanged)"
            else:
                status_badge = f"✅ Stripped {item['removed_count']} deleted/old elements"
            st.markdown(f"**Page #{idx + 1}:** `{item['source']}` — {status_badge}")
        with q_col2:
            if st.button("✖ Remove", key=f"remove_{item['id']}_{idx}"):
                st.session_state.batch_queue.pop(idx)
                st.rerun()

    btn_col1, btn_col2, _ = st.columns([2, 1, 4])
    with btn_col1:
        process_clicked = st.button(
            f"🚀 Process Batch ({len(st.session_state.batch_queue)} {'Page' if len(st.session_state.batch_queue) == 1 else 'Pages'})",
            type="primary",
            use_container_width=True,
        )
    with btn_col2:
        if st.button("🗑️ Clear Batch", use_container_width=True):
            st.session_state.batch_queue = []
            st.session_state.processed_studies = []
            st.session_state.has_processed = False
            st.rerun()

    if process_clicked:
        all_studies = []
        progress_bar = st.progress(0, text="Processing batch...")
        total_pages = len(st.session_state.batch_queue)
        for idx, item in enumerate(st.session_state.batch_queue, 1):
            progress_bar.progress(
                (idx - 1) / total_pages,
                text=f"Formatting Page {idx} of {total_pages} ({item['source']})...",
            )
            page_studies = parse_web_alert_text(item["clean_text"])
            for s in page_studies:
                s["_batch_page"] = f"Page #{idx} ({item['source']})"
            all_studies.extend(page_studies)
        progress_bar.progress(1.0, text="Batch complete!")
        progress_bar.empty()
        st.session_state.processed_studies = all_studies
        st.session_state.has_processed = True

# 3. Display Extracted Studies
if st.session_state.has_processed:
    studies = st.session_state.processed_studies
    if not studies:
        st.error("❌ The parser could not extract any active new/updated studies from the queued batch.")
    else:
        st.success(f"✅ Successfully extracted {len(studies)} active studies across {len(st.session_state.batch_queue)} queued {'page' if len(st.session_state.batch_queue) == 1 else 'pages'}!")

        for idx, study in enumerate(studies, 1):
            source_tag = f" — [{study['_batch_page']}]" if study.get("_batch_page") else ""
            st.subheader(f"Study #{idx}: {study.get('project_name', 'Unknown')}{source_tag}")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Telegram Ready Post**")
                st.code(generate_telegram_message(study), language="text", wrap_lines=True)

                with st.expander("View Website HTML Payload"):
                    st.code(generate_website_html(study), language="html", wrap_lines=True)

            with col2:
                st.markdown("**Compliance Approval Request (Email Draft)**")
                st.code(generate_approval_email(study), language="text", wrap_lines=True)

                with st.expander("View Raw JSON Data"):
                    st.json(study)

            st.divider()

# 4. Developer Debug View (tucked at the very bottom)
if st.session_state.batch_queue:
    with st.expander("🛠️ Debug View: Queued Raw HTML & Cleaned Text"):
        for idx, item in enumerate(st.session_state.batch_queue, 1):
            st.markdown(f"### Page #{idx}: `{item['source']}`")
            st.markdown("**1. Raw HTML Received from Clipboard:**")
            st.code(item["raw_html"], language="html")
            st.markdown("**2. Clean Plain Text Passed to Parser:**")
            st.code(item["clean_text"], language="text")
            st.divider()
