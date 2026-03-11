import base64
import mimetypes
import json
from openai import OpenAI
from config.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def analisar_comprovante(file_bytes, filename, descricao=""):

    mime_type, _ = mimetypes.guess_type(filename)

    arquivo_base64 = base64.b64encode(file_bytes).decode()

    prompt = f"""
Analise este comprovante de pagamento.

Descrição do usuário:
{descricao}

Extraia:

empresa
valor
data
categoria

Responda apenas JSON.
"""

    content = [{"type": "input_text", "text": prompt}]

    if mime_type == "application/pdf":

        content.append({
            "type": "input_file",
            "filename": filename,
            "file_data": f"data:application/pdf;base64,{arquivo_base64}"
        })

    else:

        content.append({
            "type": "input_image",
            "image_url": f"data:{mime_type};base64,{arquivo_base64}"
        })

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[{
            "role": "user",
            "content": content
        }]
    )

    return json.loads(response.output_text)
