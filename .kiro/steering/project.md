# Daily Inspiration Agent — Project Steering

## What This Project Does

A Python script that uses the OpenAI Agents SDK with Google Gemini as the model provider to generate a beautiful inspirational email and send it via Gmail SMTP. Run manually with `python main.py` — no scheduling or automation.

---

## Tech Stack

- **Python 3.12**
- **OpenAI Agents SDK** (`openai-agents==0.0.19`)
- **Google Gemini** via Google AI Studio (OpenAI-compatible endpoint)
  - Base URL: `https://generativelanguage.googleapis.com/v1beta/openai/`
  - Model: `gemini-2.5-flash`
- **Gmail SMTP** — host `smtp.gmail.com`, port `465`, SSL
- **python-dotenv** for environment variable loading

---

## Project Structure

```
Daily Inspiration Agent/
├── main.py           # Entry point — orchestrates the full flow
├── agent.py          # Agent logic — Gemini-powered via OpenAI Agents SDK
├── email_sender.py   # Gmail SMTP delivery
├── template.py       # HTML email template wrapper
├── requirements.txt  # Pinned dependencies
├── .env              # Secrets (never commit)
├── .env.example      # Reference template
└── README.md         # Full setup guide
```

---

## Environment Variables

All loaded from `.env` via `python-dotenv`:

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | Google AI Studio API key for Gemini |
| `GMAIL_ADDRESS` | Gmail account used as sender |
| `GMAIL_APP_PASSWORD` | 16-character Gmail App Password (not login password) |
| `RECIPIENT_EMAIL` | Email address to receive the inspiration email |

---

## Agent Behavior

- Agent name: `Daily Inspiration Agent`
- Returns an HTML snippet (not a full page) containing:
  - `<blockquote>` — the quote text
  - `<p class="author">` — the author's name
  - `<p class="reflection">` — 2–3 sentence reflection
- The snippet is embedded into the full email template in `template.py`

---

## Email Design

- Centered card layout, rounded corners
- Soft gradient header (blue to purple)
- Title: ✨ Daily Inspiration ✨
- Quote in a styled blockquote with left border
- Author right-aligned in purple
- Reflection paragraph below a divider
- Footer: "Have a wonderful day 🌷"
- Gmail-compatible HTML (table-based layout, inline styles)

---

## How to Run

```bash
py main.py
```

Expected output:
```
🚀 Starting Daily Inspiration Agent...
✨ Generating inspirational content via Gemini...
✅ Content generated successfully.
📧 Sending email to recipient@example.com...
✅ Email sent successfully!
🌷 Have a wonderful day!
```

---

## Constraints

- No scheduling, cron jobs, or automatic execution
- Email only sends on manual script run
- Uses Gmail App Password — NOT the regular Gmail login password
- `.env` must never be committed to version control

---

## Dependencies Already Installed

Run on Python 3.12. Install with:
```bash
py -3.12 -m pip install -r requirements.txt
```
