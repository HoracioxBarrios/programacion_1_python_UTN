def capitalizar_palabras(cadena: str) -> str:
    '''
    capitaliza palabras
    Recibe una cadena str.
    devuelve dicho string en el cual todas y cada una de las palabras 
    que contenga, deberán estar capitalizadas.
    '''
    lista_palabras = cadena.split()
    lista_palabras_capitalizadas = []
    for palabra in lista_palabras:
        palabra_capitalizada = palabra.capitalize()
        lista_palabras_capitalizadas.append(palabra_capitalizada)
    return ' '.join(lista_palabras_capitalizadas)