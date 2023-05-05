'''
10- Crea una función que reciba como parámetros una lista 
de palabras y devuelva la palabra más larga.
'''
lista_de_palabras = ["Mate", "Yerba", "Azucar", "Café", "Matecocido", "Yerba mate Pachamama", "Té"]

def buscar_palabra_mas_larga(lista):
    '''
    busca la palabra mas larga
    recibe una lista
    devuelve la palabra mas larga
    '''
    palabra_mas_larga = "0"
    for palabra in lista:
        if len(palabra) > len(palabra_mas_larga): #compara el len() de dos str
            palabra_mas_larga = palabra
        
    return palabra_mas_larga

print(buscar_palabra_mas_larga(lista_de_palabras))