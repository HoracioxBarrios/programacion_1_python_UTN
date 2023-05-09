import re
'''
9. Crear una función que reciba un texto y devuelva una lista 
con las palabras que contienen entre 3 y 6 caracteres de largo
'''
palabra = "Hola me gustaria saber si esto cumple con la condicion"

def palabras_entre_3_y_6_caracteres(texto):
    patron = r'(?:^|\s)([a-zA-Z0-9]{3,6})(?=\s|$)'
    palabras = re.findall(patron, texto)
    return palabras


print(palabras_entre_3_y_6_caracteres(palabra))

'''
En este patrón, utilizamos (?:^|\s) para buscar el inicio de una 
palabra (o del texto completo) sin incluirlo en el resultado, y 
(?=\s|$) para buscar el final de una palabra (o del texto completo) 
sin incluirlo en el resultado. Entre estas dos partes, buscamos una 
cadena de caracteres que contenga entre 3 y 6 letras o números, y 
la capturamos utilizando paréntesis.
'''