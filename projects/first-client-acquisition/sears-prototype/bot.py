import os
import re
import json
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# import gspread # Uncomment when running with Google Sheets credentials
# from oauth2client.service_account import ServiceAccountCredentials

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# --- CORE PARSING LOGIC ---
def parse_web_alert_text(raw_text):
    """Parses raw text from Web Alert into structured JSON."""
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
                current_study["compensation"] = clean_lines[i+7].replace('*', '')
                current_study["age_range"] = clean_lines[i+8]
                studies.append(current_study)
                i += 9
                continue
            except IndexError:
                break
        i += 1
    return studies

# --- GENERATORS ---
def generate_telegram_post(study):
    return f"""🚨 **NEW STUDY: {study.get('project_name', 'Unknown')}** 🚨

📍 **Location:** {study.get('location', 'TBD')}
💰 **Compensation:** {study.get('compensation', 'TBD')}
👥 **Demographics:** {study.get('demographics', 'TBD')} (Ages {study.get('age_range', 'TBD')})
📅 **Dates:** {study.get('start_date', 'TBD')} to {study.get('end_date', 'TBD')}

*Reference ID: {study.get('posting_id', 'N/A')}*
*Timeline: {study.get('timeline', 'N/A')}*

👉 **Next Steps:** Call the clinic and mention the Reference ID!"""

def generate_compliance_email(study):
    return f"""*Compliance Email Draft:*
-------------------------
Subject: Request to share approved research-study materials (Ref: {study.get('posting_id', 'N/A')})

Hello {study.get('location', 'Clinic')} Team,

I operate an opt-in community in the DFW area for adults interested in research studies. I recently learned from your public posting about the '{study.get('project_name', 'Study')}' trial. Before sharing any information with our audience, I would like to use your approved recruitment materials.

Could you please provide the IRB-approved flyer and confirmation we may share it?

Thank you,
Christopher Sears
Study Scoops
-------------------------"""

# --- GOOGLE SHEETS INTEGRATION (MOCKED FOR DEMO) ---
def push_to_google_sheets(study):
    """
    In production, this uses gspread to append a row to the Google Sheet.
    The website (index.html) reads directly from this sheet.
    """
    # scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    # creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    # client = gspread.authorize(creds)
    # sheet = client.open("Phase_One_Plug_Database").sheet1
    # row = [study['project_name'], study['location'], study['compensation'], ...]
    # sheet.append_row(row)
    
    logger.info(f"Mock: Successfully appended '{study.get('project_name')}' to Google Sheets Database.")
    return True

# --- TELEGRAM BOT HANDLERS ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    welcome_message = (
        "🤖 **Phase One Plug CMS Bot Online.**\n\n"
        "Chris, just paste your raw Web Alert text here. "
        "I will instantly generate your Telegram post, draft your IRB approval email, "
        "and automatically push the live listing to your website."
    )
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def process_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Process pasted text, format it, reply, and update website."""
    raw_text = update.message.text
    
    # Send a quick acknowledgment
    status_msg = await update.message.reply_text("🔄 *Processing Web Alert data...*", parse_mode='Markdown')
    
    studies = parse_web_alert_text(raw_text)
    
    if not studies:
        await status_msg.edit_text("❌ *Error:* No valid study format found. Make sure the text includes the 'Starts in X Days' anchor.", parse_mode='Markdown')
        return
        
    await status_msg.edit_text(f"✅ *Extracted {len(studies)} studies. Pushing to Website Database...*", parse_mode='Markdown')
    
    for study in studies:
        # 1. Update the Website (Google Sheets)
        push_to_google_sheets(study)
        
        # 2. Generate the outputs for Telegram forwarding
        tg_post = generate_telegram_post(study)
        email_draft = generate_compliance_email(study)
        
        # 3. Send back to Chris
        await update.message.reply_text(tg_post, parse_mode='Markdown')
        await update.message.reply_text(email_draft, parse_mode='Markdown')
        
    await update.message.reply_text("🌐 *Website has been updated! You can now forward the posts above to the VIP channel.*", parse_mode='Markdown')

def main() -> None:
    """Start the bot."""
    BOT_TOKEN = "8944569446:AAFL_6bejvz1Gpb3pVrCIjZy68bdcqGVGak"
    
    if BOT_TOKEN == "YOUR_BOT_TOKEN":
        print("WARNING: Please set the TELEGRAM_BOT_TOKEN environment variable.")
        return

    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    # on non command i.e message - process the text
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_text))

    # Run the bot until the user presses Ctrl-C
    print("Bot is polling...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
