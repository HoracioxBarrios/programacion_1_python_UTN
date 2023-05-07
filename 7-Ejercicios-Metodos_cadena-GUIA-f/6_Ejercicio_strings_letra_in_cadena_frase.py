'''
6. Escribir una función que tome un string y un carácter y devuelva 
una lista con todas las palabras en el string que contienen ese 
carácter
'''

frase = "El camino del necio es recto ante sus propios ojos, pero el que escucha el consejo es sabio."

caracter_buscado = "e"

def encontrar_palabra_en_cadena_segun_caracter(cadena : str, caracter : str)-> list:
    '''
    Busca el caracter en una cadena de palabras
    recibe una cadena (una frase por ejemplo) y un caracter a buscar
    devuelve en caso de encontrar coincidencias: una lista con las palabras que 
    contiene el caracter.
    sino avisa que no se encontro coincidencias
    '''
    lista_de_palabras =  cadena.split(" ")
    lista_de_coincidencias = []
    for palabra in lista_de_palabras:
        if caracter in palabra:
            lista_de_coincidencias.append(palabra)
            
    
    if(len(lista_de_coincidencias) > 0):
        return lista_de_coincidencias
    else:
        return "No se encontró coincidencias"

print(encontrar_palabra_en_cadena_segun_caracter(frase, caracter_buscado))

