# Danguard v3.1

<p align="center">
  <strong>Automated Subdomain Takeover Suite</strong>
</p>

<p align="center">
A fast, offensive security tool for identifying and verifying subdomain takeover vulnerabilities.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/license-internal-red.svg" alt="License">
</p>

## Quick Start

Get up and running in under a minute.

```bash
# 1. Clone the repo
git clone https://github.com/your-team/danguard-v3.1.git
cd danguard-v3.1

# 2. Setup a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure your API keys
cp .env.example .env
# Edit .env with your credentials

# 5. Add your targets to domains.txt and run
python main.py

Configuration
All operational keys are managed in the .env file. Copy .env.example to .env and fill it with your credentials.

# Example: Vercel
VERCEL_API_KEY="your_vercel_api_key"

# Example: Azure
AZURE_CLIENT_ID="your_azure_client_id"
AZURE_CLIENT_SECRET="your_azure_client_secret"
AZURE_TENANT_ID="your_azure_tenant_id"
AZURE_SUBSCRIPTION_ID="your_subscription_id"

# ...and so on for all providers

⚠️ Critical: The .env file is in .gitignore. Never commit your keys to the repository.

Usage
Run the tool against a list of domains.
# Use the default target list (domains.txt)
python main.py

# Specify a custom target list
python main.py path/to/your/targets.txt
Features
🔍 Multi-Provider Support: Azure, Vercel, AWS, Netlify, and more.
⚡ Automated Claiming: Doesn't just find vulnerabilities; it verifies them by actively claiming the subdomain.
📢 Real-Time Notifications: Get instant alerts in your team's Telegram on a successful takeover.
👥 Team Authentication: Built-in login system ensures only authorized operators can run an operation.
📊 JSON Reporting: All findings are exported to a structured JSON file for easy analysis.
Telegram Notifications
To receive Telegram alerts, your Chat ID must be registered by your team lead.

Start a chat with the team's Telegram bot.
Get your Chat ID from a bot like @myidbot.
Send your Chat ID to your team lead to be added to the operator database.
OpSec & Rules
This is an offensive tool. You are responsible for its use.

Authorization is mandatory. Only operate against assets you own or have explicit permission to test.
Protect your keys. If you suspect a compromise, revoke them immediately.
License
Internal Use Only. Distribution outside the team is prohibited.
```



