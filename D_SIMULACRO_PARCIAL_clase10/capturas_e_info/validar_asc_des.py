import re

def validar_respuesta(patron_re : str, texto : str )-> str | int:
    '''
    valida si un texto conincide con el patron
    Recibe: un texto a evaluar y un patron regex
    devuelve un int
    '''
    if(texto):
        if(re.match(patron_re, texto)):
            return texto
        return -1
    else:
        return -1
    
cadena = "5555"

respuesta_de_ordenamiento = validar_respuesta(r"^a[s]c$|^d[e][s]c$", cadena)
print(respuesta_de_ordenamiento)
