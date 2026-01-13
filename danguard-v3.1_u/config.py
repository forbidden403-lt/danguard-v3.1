import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AZURE_CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
    AZURE_TENANT_ID = os.getenv("AZURE_TENANT_ID")
    AZURE_CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
    AZURE_SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID")

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")

    VERCEL_API_KEY = os.getenv("VERCEL_API_KEY")

    NETLIFY_API_KEY = os.getenv("NETLIFY_API_KEY")

    GCP_CREDENTIALS_PATH = os.getenv("GCP_CREDENTIALS_PATH")

    HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

    DATABASE_URL = os.getenv("DATABASE_URL")

    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")