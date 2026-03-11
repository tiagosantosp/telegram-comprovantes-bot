import os

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
S3_BUCKET = os.environ["S3_BUCKET"]
ID_PLANILHA = os.environ["ID_PLANILHA"]
GOOGLE_CREDENTIALS_S3_BUCKET = os.environ["GOOGLE_CREDENTIALS_S3_BUCKET"]
GOOGLE_CREDENTIALS_S3_KEY = os.environ["GOOGLE_CREDENTIALS_S3_KEY"]

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"
FILE_URL = f"https://api.telegram.org/file/bot{TELEGRAM_TOKEN}"
