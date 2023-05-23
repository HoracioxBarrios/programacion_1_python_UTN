def validacion_respuesta(texto: str, patron: str, posibles_keys: list) -> str | int:
    if texto:
        if re.match(patron, texto) and texto in posibles_keys:
            return texto
        return -1
    else: return -1