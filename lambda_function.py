import json
import urllib.request

from telegram_service import send_message, get_file_url
from openai_service import analyze_receipt
from s3_service import upload_file, file_exists
from utils import sanitize


def download_file(url):

    response = urllib.request.urlopen(url)

    return response.read()


def lambda_handler(event, context):

    body = json.loads(event["body"])

    message = body.get("message")

    if not message:
        return {"statusCode": 200}

    chat_id = message["chat"]["id"]

    caption = message.get("caption", "")

    file_id = None
    file_unique_id = None
    filename = "file"

    if "photo" in message:

        file_id = message["photo"][-1]["file_id"]
        file_unique_id = message["photo"][-1]["file_unique_id"]

        filename = "comprovante.jpg"

    elif "document" in message:

        file_id = message["document"]["file_id"]
        file_unique_id = message["document"]["file_unique_id"]

        filename = message["document"]["file_name"]

    else:

        send_message(chat_id, "Envie um comprovante em imagem ou PDF.")

        return {"statusCode": 200}

    file_url = get_file_url(file_id)

    file_bytes = download_file(file_url)

    dados = analyze_receipt(file_bytes, filename, caption)

    unique_prefix = sanitize(file_unique_id or "arquivo")
    new_filename = f"{unique_prefix}-{filename}"

    if not file_exists(new_filename):
        upload_file(new_filename, file_bytes)

    resposta = f"""
✅ Comprovante registrado

Empresa: {dados.get("empresa")}
Valor: R${dados.get("valor")}
Categoria: {dados.get("categoria")}
Data: {dados.get("data")}
"""

    send_message(chat_id, resposta)

    return {
        "statusCode": 200,
        "body": "ok"
    }
