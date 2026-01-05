# ------------Leads Email Automation------------


import json
import smtplib
import os
import csv
import time
import shutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from datetime import datetime
from job_activity_logger import JobActivityLogger

# Load environment variables
load_dotenv()

# Initialize API logger
api_logger = JobActivityLogger()

# Load email accounts from JSON file
with open(os.getenv("EMAIL_ACCOUNTS_FILE"), 'r') as f:
    email_accounts = json.load(f)

current_account_index = 0
emails_sent_with_current_account = 0
MAX_EMAILS_PER_ACCOUNT = 100

# Other configurations
SMTP_HOST = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
REPLY_TO_EMAIL = os.getenv("REPLY_TO_EMAIL")
EMAIL_DELAY_SECONDS = int(os.getenv("EMAIL_DELAY_SECONDS", 2))

# Database/File Configuration
CSV_FILE = "leads_emails.csv"
LOG_FILE = "logs/sent_emails.csv"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def get_next_email_account():
    global current_account_index, emails_sent_with_current_account

    if emails_sent_with_current_account >= MAX_EMAILS_PER_ACCOUNT:
        current_account_index = (current_account_index + 1) % len(email_accounts)
        emails_sent_with_current_account = 0
        print(f"\nSwitching to email account: {email_accounts[current_account_index]['EMAIL_USER']}\n")

    account = email_accounts[current_account_index]
    emails_sent_with_current_account += 1
    return account

def log_sent(email, name, sender_email):
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(["Sender Email", "Recipient Email", "Name", "Timestamp"])
        writer.writerow([sender_email, email, name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

def send_email(to_email, to_name):
    account = get_next_email_account()

    subject = "New Batch Alert! Join our AI & ML Training Program!"

    html_body = f"""
      <html>
        <body style="font-family: Arial, sans-serif; font-size: 15px; color: #333; line-height: 1.6; margin: 0; padding: 0; background-color: #f6f8fa;">
            <div style="max-width: 600px; margin: auto; padding: 20px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="https://www.whitebox-learning.com/_next/static/media/wbl-dark.364b4e0a.png"
                    alt="Whitebox Learning Logo"
                    style="height: 50px; display: block; margin: auto;">
                <h2 style="margin: 10px 0 0 0; color: #1b1f23;">Whitebox Learning</h2>
            </div>

            <p>Hi {to_name or 'there'},</p>
            <p>Sorry for spamming  — just wanted to make sure you don’t miss this last chance to join Whitebox Learning.</p>

            <p><strong> Last Batch Of The Year 2025</strong> Don’t miss your chance to join Whitebox Learning’s <strong>AI & ML Training Program</strong>. This is your opportunity to explore your career path in the <strong>AI/ML. Join our orientation for more for free </strong>

            <!-- 🔥 NEW CONTENT ADDED HERE -->
            <p style="font-weight:bold; text-align:center;">
                <p><strong>October Month Highlights:</strong></p>
                    <ul>
                        <li><strong>67+ Interviews Scheduled</strong></li>
                        <li><strong>Out of 10 Marketing Candidates 4 Got Placed </strong></li>
                        <li><strong>Currently 50+ Candidates In Preparation and Training</strong></li>
                        <li><strong>20+ Interviews Happening This Week</strong></li>
                    </ul>
                 Join now and explore your future in the AIML way
                (Don’t let this chance slip — treat this as your last reminder!)
              </p>

            <!-- 🔥 END NEW CONTENT -->

            <p><strong>Orientation Date:</strong> January 10th, 2026 </p>
            <p><strong>Time:</strong> 10:00 AM to 12:00 PM PST</p>
            <p><strong>Register Online at:</strong> <a href="https://attendee.gotowebinar.com/register/5522842960170307676">Register Here</a></p>
            <p><strong>Batch Starts:</strong> January 10th, 2026 </p>

            <p><strong>Topics Covered:</strong></p>
              <li>Data Analysis</li>
               <li>Machine Learning</li>
               <li>Deep Learning</li>
               <li>Gen AI</li>
               <li>RAG</li>
               <li>Agentic AI</li>
               <li>MLOps</li>
           </ul>

            <p><strong>Join WhatsApp Group for announcements:</strong> <a href="https://chat.whatsapp.com/CKn3I9NbPSRKfFLJndcld9">Join Here</a></p>
            <p><strong>In-person orientation:</strong> 6500 Dublin Blvd., Ste. 218, Dublin, CA 94568</p>
            <p>If you know someone who’s still deciding, remind them too — this is the <strong>last call</strong> for this batch!</p>
            <p><strong>Earn up to $50 Amazon gift card</strong> as a referral bonus for each successful enrollment (T&C apply).</p>

            <p><strong>📞 Contact:</strong> +1 925-557-1053</p>
            <p><a href="tel:+919966566721">Gautam</a> or <a href="tel:+917993041323">Jafar</a> for details.</p>

            <div style="text-align: center; margin-top: 30px;">
                <a href="https://www.facebook.com/WBLAIML" target="_blank" style="background-color:#3b5998; color:#fff; padding:8px 16px; text-decoration:none; border-radius:5px; display:inline-block; margin:5px;">
                <img src="https://cdn-icons-png.flaticon.com/24/145/145802.png" alt="Facebook" style="height: 18px; vertical-align: middle; margin-right: 6px;"> Facebook
                </a>
                <a href="https://www.linkedin.com/company/107532599/admin/dashboard/" target="_blank" style="background-color:#0077b5; color:#fff; padding:8px 16px; text-decoration:none; border-radius:5px; display:inline-block; margin:5px;">
                <img src="https://cdn-icons-png.flaticon.com/24/145/145807.png" alt="LinkedIn" style="height: 18px; vertical-align: middle; margin-right: 6px;"> LinkedIn
                </a>
            </div>

            <p style="margin-top:20px; text-align:center; font-weight:bold; color:#d9534f;">
                Don’t wait. Join now and explore your future in the AIML, See you in class!
            </p>

            <hr style="margin-top: 30px; border: none; border-top: 1px solid #ddd;">
            <p style="font-size: 12px; color: #888; text-align: center;">
                Don’t want to hear from us again?
                <a href="https://www.whitebox-learning.com/leads_unsubscribe?email={to_email}" style="color:#888;">Unsubscribe</a>
            </p>
            </div>
        </body>
    </html>



    """

    msg = MIMEMultipart("related")
    msg["Subject"] = subject
    msg["From"] = f"Whitebox Learning <{account['EMAIL_USER']}>"
    msg["To"] = to_email
    msg["Reply-To"] = REPLY_TO_EMAIL
    msg_alternative = MIMEMultipart("alternative")
    msg.attach(msg_alternative)
    msg_alternative.attach(MIMEText(html_body, "html", "utf-8"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(account['EMAIL_USER'], account['EMAIL_PASS'])
        server.send_message(msg)

    return account['EMAIL_USER']

def run():
    print(f"Reading from {CSV_FILE}...")
    
    # Read all rows
    all_rows = []
    fieldnames = []
    try:
        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            all_rows = list(reader)
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} not found.")
        return

    # Identify candidates
    leads_to_email = []
    for row in all_rows:
        # Check conditions: massemail_unsubscribe != 1 (True) AND massemail_email_sent != 1 (True)
        # CSV values are strings "1"/"0"
        is_unsubscribed = row.get("massemail_unsubscribe", "0") == "1"
        is_sent = row.get("massemail_email_sent", "0") == "1"
        
        if not is_unsubscribed and not is_sent:
            leads_to_email.append(row)
    
    # Limit to 800
    leads_to_process = leads_to_email[:800]
    
    if not leads_to_process:
        print("No emails to send.")
        return

    print(f"Found {len(leads_to_process)} leads to email (Limit: 800). Starting batch...")

    successful_sends = 0

    for lead in leads_to_process:
        email = lead.get("email", "").strip()
        name = lead.get("full_name", "").strip()

        if not email or '@' not in email:
            print(f"Skipping invalid email: {email}")
            continue

        try:
            sender_email = send_email(email, name)
            
            # Update status in memory
            lead["massemail_email_sent"] = "1"
            # Note: "last_modified" column logic from SQL is skipped as it doesn't appear to be in CSV headers 
            # (only "Entry Date", "Closed Date" etc are present). We only verify Sent flag.

            log_sent(email, name, sender_email)
            print(f"Sent to {email} using {sender_email}")
            successful_sends += 1
        except Exception as e:
            print(f"Failed to send to {email}: {e}")

        # Add delay between email attempts
        if EMAIL_DELAY_SECONDS > 0:
            print(f"Waiting {EMAIL_DELAY_SECONDS} seconds before next email...")
            time.sleep(EMAIL_DELAY_SECONDS)

    # Save changes back to CSV if any emails sent
    if successful_sends > 0:
        print("Saving updates to CSV...")
        # Create a temp file first to be safe
        temp_file = CSV_FILE + ".tmp"
        try:
            with open(temp_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(all_rows)
            
            # Replace original
            shutil.move(temp_file, CSV_FILE)
            print("CSV updated successfully.")
        except Exception as e:
            print(f"Error saving CSV: {e}")
            if os.path.exists(temp_file):
                os.remove(temp_file)

    # Log activity to WBL API
    if successful_sends > 0:
        notes = f"Mass email campaign sent to {successful_sends} leads from CSV"
        logging_success = api_logger.log_activity(successful_sends, notes)
        if logging_success:
            print(f"\nCampaign complete: {successful_sends} emails sent successfully")
        else:
            print(f"\nCampaign complete: {successful_sends} emails sent successfully, but activity logging failed")
    else:
        print("\nNo emails were sent successfully")

if __name__ == "__main__":
    run()
