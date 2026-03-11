import json
import boto3
import gspread
from google.oauth2.service_account import Credentials
from config.config import (
    ID_PLANILHA,
    GOOGLE_CREDENTIALS_S3_BUCKET,
    GOOGLE_CREDENTIALS_S3_KEY,
)

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def connect():

    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket=GOOGLE_CREDENTIALS_S3_BUCKET, Key=GOOGLE_CREDENTIALS_S3_KEY)
    raw = obj["Body"].read().decode("utf-8")

    if not raw:
        raise ValueError("Google credentials not set. Provide S3 bucket/key.")

    creds_info = json.loads(raw)
    creds = Credentials.from_service_account_info(creds_info, scopes=SCOPES)

    client = gspread.authorize(creds)

    sheet = client.open_by_key(ID_PLANILHA).sheet1

    return sheet


def add_row(empresa, valor, categoria, data, filename, link):

    sheet = connect()

    sheet.append_row([empresa, valor, categoria, data, filename, link])
