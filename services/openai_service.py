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

    output_text = (response.output_text or "").strip()
    if not output_text:
        # Fallback: some SDK responses expose text inside output content
        try:
            output_items = response.output or []
            for item in output_items:
                for part in (item.get("content") or []):
                    if part.get("type") == "output_text" and part.get("text"):
                        output_text = part["text"].strip()
                        break
                if output_text:
                    break
        except Exception:
            output_text = ""

    if not output_text:
        raise ValueError("OpenAI response has no output_text to parse as JSON.")

    try:
        return json.loads(output_text)
    except json.JSONDecodeError:
        # Try to salvage JSON if the model added extra text
        start = output_text.find("{")
        end = output_text.rfind("}")
        if start != -1 and end != -1 and end > start:
            return json.loads(output_text[start:end + 1])
        raise
