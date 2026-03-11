import json
import urllib.request
from config.config import BASE_URL, FILE_URL


def send_message(chat_id, text):

    url = f"{BASE_URL}/sendMessage"

    payload = json.dumps({
        "chat_id": chat_id,
        "text": text
    }).encode()

    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"}
    )

    urllib.request.urlopen(req)


def get_file_url(file_id):

    url = f"{BASE_URL}/getFile?file_id={file_id}"

    response = urllib.request.urlopen(url)

    data = json.loads(response.read())

    file_path = data["result"]["file_path"]

    return f"{FILE_URL}/{file_path}"
