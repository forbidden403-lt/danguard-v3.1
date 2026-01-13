# Danguard v3.1 - Subdomain Takeover Suite

> A fast, automated tool for identifying and verifying subdomain takeover vulnerabilities.

Danguard is a command-line suite designed for red teams and security researchers. This tool automates the process of scanning for dangling DNS records and verifying subdomain takeover vulnerabilities across various cloud providers. If you can point a CNAME at it, Danguard can test it.

## 🎯 Core Features

-   **Multi-Vector Scanning:** Full support for Azure, Vercel, AWS, and other providers.
-   **Automated Verification:** Doesn't just point out vulnerabilities; it actively attempts to claim them for definitive proof.
-   **Real-Time Comms:** Get instant notifications in your team's Telegram the moment a target is successfully compromised.
-   **Team-Based Ops:** Built-in authentication system ensures only authorized operators can execute an operation.
-   **Structured Reporting:** All findings are exported to a clean JSON format for easy parsing and integration with other tools.

## ⚠️ Operational Security & Rules of Engagement

This is a powerful tool. With power comes responsibility.

-   **Authorization Only:** Danguard is strictly for use on assets you own or have explicit, written permission to test. Scanning or taking over assets without permission is illegal.
-   **Handle with Care:** You are solely responsible for how you use this tool. The development team is not responsible for misuse.
-   **Protect Your Keys:** **NEVER**, under any circumstances, commit your `.env` file or share your API keys. If you suspect your keys have been compromised, revoke them immediately.

## 🚀 Setup & Deployment

### 1. Prerequisites
-   Python 3.8+
-   Git

### 2. Deployment
Clone the repository and navigate into the project directory.
```bash
git clone https://github.com/forbidden403-lt/danguard-v3.1.git
cd danguard-v3.1

### **3. Environment**
We use a virtual environment to keep dependencies clean and isolated.
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

### **4. Install Dependencies**
Install all required Python packages from the requirements.txt file.
```bash
pip install -r requirements.txt

## ⚙️ **Configuration**
Your operational API keys and tokens are managed via a .env file.

1. Copy the example template to create your local configuration file.
```bash
cp .env.example .env
