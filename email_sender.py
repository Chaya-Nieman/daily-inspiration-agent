"""
email_sender.py

Handles sending the HTML email via Gmail SMTP using SSL on port 465.
Credentials are loaded from environment variables.
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(html_body: str) -> None:
    """
    Sends the inspirational HTML email via Gmail SMTP.

    Args:
        html_body: The complete HTML string to send as the email body.

    Raises:
        ValueError: If required environment variables are missing.
        smtplib.SMTPException: If the email fails to send.
    """
    # Load credentials from environment
    gmail_address = os.environ.get("GMAIL_ADDRESS")
    app_password = os.environ.get("GMAIL_APP_PASSWORD")
    recipient = os.environ.get("RECIPIENT_EMAIL")

    if not gmail_address:
        raise ValueError("GMAIL_ADDRESS is not set in environment variables.")
    if not app_password:
        raise ValueError("GMAIL_APP_PASSWORD is not set in environment variables.")
    if not recipient:
        raise ValueError("RECIPIENT_EMAIL is not set in environment variables.")

    # Build the email message
    message = MIMEMultipart("alternative")
    message["Subject"] = "✨ Your Daily Inspiration"
    message["From"] = gmail_address
    message["To"] = recipient

    # Attach the HTML body
    html_part = MIMEText(html_body, "html", "utf-8")
    message.attach(html_part)

    # Connect and send via Gmail SMTP with SSL
    print(f"📧 Sending email to {recipient}...")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_address, app_password)
        server.sendmail(gmail_address, recipient, message.as_string())

    print("✅ Email sent successfully!")
