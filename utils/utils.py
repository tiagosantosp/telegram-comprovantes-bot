import re
import unicodedata


def _strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    return normalized.encode("ASCII", "ignore").decode("ASCII")


def sanitize(text):
    text = (text or "").upper().strip()
    text = _strip_accents(text)
    text = text.replace(" ", "_")
    text = re.sub(r'[^A-Z0-9_-]', '', text)
    return text
