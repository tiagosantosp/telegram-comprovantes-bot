import json
import gspread
from google.oauth2.service_account import Credentials
from config.config import ID_PLANILHA, GOOGLE_CREDENTIALS

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def connect():

    creds_info = json.loads(GOOGLE_CREDENTIALS)
    creds = Credentials.from_service_account_info(creds_info, scopes=SCOPES)

    client = gspread.authorize(creds)

    sheet = client.open_by_key(ID_PLANILHA).sheet1

    return sheet


def add_row(empresa, valor, categoria, data, filename, link):

    sheet = connect()

    sheet.append_row([empresa, valor, categoria, data, filename, link])
