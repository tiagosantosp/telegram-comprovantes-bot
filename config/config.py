import os

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
S3_BUCKET = os.environ["S3_BUCKET"]

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"
FILE_URL = f"https://api.telegram.org/file/bot{TELEGRAM_TOKEN}"