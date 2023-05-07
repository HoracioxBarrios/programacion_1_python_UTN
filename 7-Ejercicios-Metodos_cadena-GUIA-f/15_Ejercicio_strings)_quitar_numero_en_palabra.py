'''
15.Escribir una función que tome una cadena de texto y devuelva 
solo los caracteres alfabéticos, eliminando cualquier número o 
símbolo (sólo son válidos letras y espacios), por 
ejemplo: "H0l4, m4nd0!" -> "Hl mnd”

'''
palabra_ejemplo = "H0l4, m4nd0!"


def quitar_numeros(palabra: str) -> str:
    '''
    quita los numeros las palabras
    recibe una cadena
    devuelve una nueva cadena
    
    '''
    caracteres_alfabeticos = []
    for caracter in palabra:
        if caracter.isalpha() or caracter.isspace():
            print(caracter)
            caracteres_alfabeticos.append(caracter)
    nueva_palabra = ''.join(caracteres_alfabeticos) # join recibe una lista y devuelve un string
    return nueva_palabra

palabra_limpia = quitar_numeros(palabra_ejemplo)
print(palabra_limpia)
