"""
main.py

Entry point for the Daily Inspiration Agent.
Run this script manually to generate and send today's inspirational email.

Usage:
    python main.py
"""

import asyncio
import sys

# Load environment variables from .env file before anything else
from dotenv import load_dotenv
load_dotenv()

import os
# Disable OpenAI Agents SDK tracing entirely — we don't need it
# and it causes noise when openai.com is blocked by network filters
os.environ["OPENAI_AGENTS_DISABLE_TRACING"] = "1"

from agent import generate_inspiration
from template import build_email_html_raw
from email_sender import send_email


async def main() -> None:
    print("🚀 Starting Daily Inspiration Agent...")

    # Step 1: Generate inspirational HTML content via Gemini agent
    print("✨ Generating inspirational content via Gemini...")
    try:
        content_snippet = await generate_inspiration()
        print("✅ Content generated successfully.")
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Agent error: {e}")
        sys.exit(1)

    # Step 2: Wrap the content in the full email HTML template
    html_body = build_email_html_raw(content_snippet)

    # Step 3: Send the email via Gmail SMTP
    try:
        send_email(html_body)
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        sys.exit(1)

    print("🌷 Have a wonderful day!")


if __name__ == "__main__":
    asyncio.run(main())
