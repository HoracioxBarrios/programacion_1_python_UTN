def reemplazar(texto: str) -> str:
    signos = [",", ".", ":", ";"]
    for signo in signos:
        texto = texto.replace(signo, "")
    return texto