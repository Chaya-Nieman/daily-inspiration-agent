# Daily Inspiration Agent

A simple Python agent that generates a beautiful inspirational email and sends it via Gmail SMTP. Powered by the **OpenAI Agents SDK** with **Google Gemini** as the model provider.

---

## What It Does

When you run `python main.py`, the agent will:

1. Connect to Google Gemini using your API key
2. Generate an inspirational email containing:
   - One authentic quote from a well-known philosopher, scientist, leader, or author
   - The author's name
   - A short, thoughtful reflection (2–3 sentences) connecting the quote to everyday life
3. Wrap the content in a modern, Gmail-compatible HTML email design
4. Send the email to your recipient via Gmail SMTP
5. Print success or error messages to the console

> **No scheduling or automation** — the email is only sent when you manually run the script.

---

## Project Structure

```
daily-inspiration-agent/
├── main.py              # Entry point — orchestrates the full flow
├── agent.py             # Agent logic — configures and runs the Gemini-powered agent
├── email_sender.py      # Email delivery — sends HTML email via Gmail SMTP
├── template.py          # HTML template — wraps agent output in a styled email layout
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (never commit this file)
├── .env.example         # Example env file for reference
└── README.md            # This file
```

---

## Prerequisites

- Python 3.11 or higher
- A Google AI Studio API key (for Gemini)
- A Gmail account with an App Password enabled

---

## Setup Instructions

### 1. Get a Google AI Studio API Key

1. Go to [https://aistudio.google.com](https://aistudio.google.com)
2. Sign in with your Google account
3. Click **"Get API key"** → **"Create API key"**
4. Copy the key — you'll need it for your `.env` file

### 2. Create a Gmail App Password

Gmail requires an App Password (not your regular Gmail password) when using SMTP with 2-Step Verification.

1. Go to your Google Account → [https://myaccount.google.com](https://myaccount.google.com)
2. Navigate to **Security** → **2-Step Verification** (enable it if not already)
3. Under **2-Step Verification**, scroll down to **App passwords**
4. Select app: **Mail** | Select device: **Other (custom name)** → type "Daily Inspiration Agent"
5. Click **Generate** and copy the 16-character password

### 3. Clone or Download the Project

```bash
git clone <your-repo-url>
cd daily-inspiration-agent
```

Or simply place all the project files in a folder on your machine.

### 4. Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the `.env` File

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

Open `.env` and fill in:

```env
GOOGLE_API_KEY=your_google_ai_studio_api_key_here
GMAIL_ADDRESS=your_gmail_address@gmail.com
GMAIL_APP_PASSWORD=your_16_character_app_password
RECIPIENT_EMAIL=recipient@example.com
```

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | Your Google AI Studio API key for Gemini |
| `GMAIL_ADDRESS` | The Gmail account used to send the email |
| `GMAIL_APP_PASSWORD` | The 16-character App Password (not your Gmail login password) |
| `RECIPIENT_EMAIL` | The email address that will receive the inspiration email |

> ⚠️ **Never commit your `.env` file to version control.** It contains sensitive credentials.

---

## Running the Application

### Manually (run anytime)

```bash
python main.py
```

Expected console output:

```
🚀 Starting Daily Inspiration Agent...
✨ Generating inspirational content via Gemini...
✅ Content generated successfully.
📧 Sending email to recipient@example.com...
✅ Email sent successfully!
🌷 Have a wonderful day!
```

### Automatically (daily schedule via GitHub Actions)

The project includes a GitHub Actions workflow that runs every day at **8:00 AM Israel time** automatically — even when your computer is off.

**Setup:**
1. Push the code to GitHub
2. Go to your repo → **Settings** → **Secrets and variables** → **Actions**
3. Add these 4 secrets: `GOOGLE_API_KEY`, `GMAIL_ADDRESS`, `GMAIL_APP_PASSWORD`, `RECIPIENT_EMAIL`
4. The workflow runs automatically every day

**To trigger manually from GitHub:**
1. Go to your repo → **Actions** tab
2. Click **"Daily Inspiration Email"**
3. Click **"Run workflow"**

**To change the send time:**
Edit `.github/workflows/daily-inspiration.yml` and update the cron line:
```yaml
- cron: '0 5 * * *'  # 05:00 UTC = 08:00 Israel time
```
Format: `minute hour * * *` (always use UTC time)

---

## Email Design

The generated email features:

- Centered card layout with rounded corners
- Soft, calming color palette
- Large title: **✨ Daily Inspiration ✨**
- Prominently displayed quote
- Styled author attribution
- Reflection paragraph
- Footer: *Have a wonderful day 🌷*

The HTML is fully compatible with Gmail.

---

## Dependencies

See `requirements.txt` for the full list. Key packages:

| Package | Purpose |
|---|---|
| `openai-agents` | OpenAI Agents SDK (pinned to `>=0.18,<1.0` — gets updates automatically, but won't break on a future major version) |
| `python-dotenv` | Load environment variables from `.env` |

## GitHub Actions Workflow

The file `.github/workflows/daily-inspiration.yml` contains the automation schedule. It:
- Runs every day at 8am Israel time (5am UTC)
- Can also be triggered manually from the GitHub Actions tab
- Uses your GitHub secrets as environment variables — your credentials never appear in the code

---

## Troubleshooting

**`Authentication failed` on SMTP**
- Make sure you're using an App Password, not your regular Gmail password
- Verify 2-Step Verification is enabled on your Google account

**`API key not valid` from Gemini**
- Double-check your `GOOGLE_API_KEY` in `.env`
- Make sure the key is from [Google AI Studio](https://aistudio.google.com), not Google Cloud

**`ModuleNotFoundError`**
- Make sure your virtual environment is activated
- Run `pip install -r requirements.txt` again

**Email not received**
- Check your spam/junk folder
- Verify `RECIPIENT_EMAIL` is spelled correctly in `.env`

---

## License

MIT — free to use and modify for personal or commercial projects.
