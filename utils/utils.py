import re

def sanitize(text):
    text = (text or "").upper().strip()
    text = text.replace(" ", "_")
    text = re.sub(r'[^A-Z0-9_-]', '', text)
    return text
