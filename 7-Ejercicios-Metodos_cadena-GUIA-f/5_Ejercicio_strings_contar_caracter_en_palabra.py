'''
5. Escribir una función que tome un string y un carácter y devuelva 
el número de veces que aparece ese carácter en el string.

'''

palabra = "avion"
letra = "i"

def contar_caracter_en_palabra(palabra :str, caracter : str)-> int:
    '''
    cuenta el caracter buscado en una palabra
    recibe una palabra y un caracter
    devuelve el nuero de veces que se encontró el caracter en la palabra
    '''
    return palabra.count(caracter)
    

    
print("las veces que aparece la letra: {0} en la palabra: {1} es: {2}".format(
        letra, palabra, contar_caracter_en_palabra(palabra, letra)))