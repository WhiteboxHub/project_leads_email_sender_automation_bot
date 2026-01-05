# Leads Email Sender Automation

Mass outreach bot with automated WBL activity logging.

## 🚀 Quick Start

1. **Setup Environment**:

   ```bash
   python -m venv venv
   # Windows: venv\Scripts\activate | Mac: source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure API & Env**:

   ```bash
   python setup_api.py
   ```

   _Follow prompts for WBL Email, Password, and Employee ID._

3. **Add Email Accounts**:
   Update `email_accounts.json` with your Gmail address and **App Password**.

   > [!IMPORTANT]
   > Use a [Gmail App Password](https://support.google.com/accounts/answer/185833), not your regular password.

4. **Run Bot**:
   ```bash
   python main.py
   ```

## 📂 Project Structure

- `main.py`: The main automation script.
- `leads_emails.csv`: Put your leads here (`email`, `full_name` headers).
- `logs/`: Check `sent_emails.csv` for delivery status.

## � Pro Tips

- **Delay**: Adjusted via `EMAIL_DELAY_SECONDS` in `.env`.
- **Errors**: If you get a "WebLoginRequired" error, ensure 2FA is on and you're using an App Password.
