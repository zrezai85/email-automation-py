# email-automation-py
# Python Email Sender

A simple Python script to send secure emails using Gmail SMTP server with SSL encryption.

## Features

- Connects securely to Gmail SMTP server using SSL  
- Authenticates with sender email and password  
- Sends plain text email to a specified receiver

## Prerequisites

- Python 3.x installed  
- Enable "App Password" in your Gmail account for secure login (recommended)  
- Internet connection

## Usage

1. Clone this repository or download the script file.  
2. Open the script file (e.g., `email_sender.py`).  
3. Enter your sender email and receiver email addresses in the script.  
4. Run the script. It will prompt you to enter your email password securely.  
5. The script will send a simple message via Gmail SMTP server.

```bash
python email_sender.py
Important Notes
Do NOT hardcode your password in the script; use secure methods like getpass or environment variables.

Make sure your Gmail account allows SMTP access and App Passwords are enabled.
This script sends plain text emails; you can extend it to support attachments or HTML emails.

---

کافیه همین متن رو در فایل `README.md` داخل ریشه پروژه‌ات ذخیره کنی.

اگر نیاز داشتی راهنمایی برای افزودن فایل کد یا کامیت کردن و پوش کردن به گیت‌هاب، بهم بگو.
