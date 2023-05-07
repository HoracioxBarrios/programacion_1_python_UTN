'''
18.Escribir una función que tome una cadena de caracteres y 
reemplace todas las letras mayúsculas por letras minúsculas 
y todas las letras minúsculas por letras mayúsculas, por 
ejemplo: "HoLa" -> "hOlA"
'''
cadena = "pELOTA"
def cambiar_mayusculas_y_minusculas(cadena :str)-> str:
    '''
    toma una cadena de caracteres y reemplaza todas 
    las letras mayúsculas por letras minúsculas y todas
    las letras minúsculas por letras mayúsculas.
    recibe una cadena 
    '''
    resultado = ""
    for caracter in cadena:
        if caracter.isupper():
            resultado += caracter.lower()
        elif caracter.islower():
            resultado += caracter.upper()
        else:
            resultado += caracter
    return resultado

print(cambiar_mayusculas_y_minusculas(cadena))




cadena = "Pelota"
def cambiar_mayusculas_y_minusculas_v2(cadena : str)-> str:
    '''
    toma una cadena de caracteres y reemplaza todas 
    las letras mayúsculas por letras minúsculas y todas
    las letras minúsculas por letras mayúsculas.
    recibe una cadena 
    '''
    return cadena.swapcase()

print(cambiar_mayusculas_y_minusculas_v2(cadena))
