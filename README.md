# Leads Mass Email Sender

This program sends mass emails to leads from a MySQL database using a rotating pool of email accounts.

## Prerequisites

- Python 3.x
- MySQL database
- Required packages: python-dotenv, mysql-connector-python, smtplib (built-in), csv (built-in), email (built-in), datetime (built-in), os (built-in)

## Setup

1. Ensure all files are in the same directory:
   - `main.py`
   - `.env`
   - `email_accounts.json`
   - `logs/` directory

2. Configure your environment variables in `.env`:
   - `DB_HOST=your-db-host`
   - `DB_USER=your-db-user`
   - `DB_PASS=your-db-password`
   - `DB_NAME=your-db-name`
   - `EMAIL_ACCOUNTS_FILE=email_accounts.json`
   - `SMTP_SERVER=smtp.gmail.com`
   - `SMTP_PORT=587`
   - `REPLY_TO_EMAIL=your-reply-email@example.com`

3. Update `email_accounts.json` with your email accounts in the format:
   ```json
   [
     {
       "EMAIL_USER": "your-email@gmail.com",
       "EMAIL_PASS": "your-app-password"
     }
   ]
   ```

4. Ensure your MySQL database has a `lead` table with columns: `id`, `full_name`, `email`, `massemail_unsubscribe`, `massemail_email_sent`

## Running the Program

```bash
python main.py
```

## Expected Output

- Connects to database and fetches up to 800 leads that haven't been emailed and aren't unsubscribed
- Cycles through email accounts (up to 100 emails per account)
- Sends HTML emails with unsubscribe links
- Updates database to mark emails as sent
- Logs sent emails to `logs/sent_emails.csv`
- Prints sending status for each email

## Notes

- Uses Gmail SMTP by default
- Automatically switches accounts when limit is reached
- Skips leads with invalid emails
- Only sends to leads where `massemail_unsubscribe != 1` and `massemail_email_sent != 1`
