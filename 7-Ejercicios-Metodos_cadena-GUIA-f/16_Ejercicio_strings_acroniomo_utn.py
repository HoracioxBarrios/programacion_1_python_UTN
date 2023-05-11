'''

16.Escribir una función que tome una cadena de texto y la 
convierta en un acrónimo, tomando la primera letra de cada 
palabra, por ejemplo:
"Universidad Tecnológica Nacional Facultad Regional Avellaneda" ->
"UTNFRA”.

'''
nombre_de_la_universidad = "universidad tecnológica nacional facultad regional avellaneda"


def convertir_a_acronimo(cadena: str) -> str:
    '''
        toma una cadena de texto y la convierte en un acronimo
        recibe una cadena
        devuelve una nueva cadena
    '''
    palabras = cadena.split()  # Separar la cadena en palabras
    acronimo = ""
    for palabra in palabras:
        acronimo += palabra[0].upper()  # Agregar la primera letra de cada palabra en mayúscula al acrónimo
    return acronimo

print(convertir_a_acronimo(nombre_de_la_universidad))
