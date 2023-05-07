'''

16.Escribir una función que tome una cadena de texto y la 
convierta en un acrónimo, tomando la primera letra de cada 
palabra, por ejemplo:
"Universidad Tecnológica Nacional Facultad Regional Avellaneda" ->
"UTNFRA”.

'''
nombre_de_la_universidad = "universidad tecnológica nacional facultad regional avellaneda"


def convertir_a_acronimo(cadena : str)-> str:
    '''
    toma una cadena de texto y la convierte en un acrónimo
    recibe una cadena
    devuelve una nueva cadena
    '''
    lista = cadena.split() # creamos una lista desde la cadena
    nueva_lista_palabras = [] # nueva lista para cada palabra
    for palabra in lista:
        palabra_capitalized = palabra.capitalize() 
        nueva_lista_palabras.append(palabra_capitalized) #agregamos la palabra corregida a a nueva lista
    nueva_palabra = " ".join(nueva_lista_palabras) # unimos las palabras con un espacio como separador
    return nueva_palabra
print(convertir_a_acronimo(nombre_de_la_universidad))