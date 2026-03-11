import re


def limpar_nome(texto):

    texto = texto.upper()

    texto = re.sub(r'[^A-Z0-9_-]', '', texto)

    return texto

def sanitize(text):

    return text.upper().replace(" ", "_")