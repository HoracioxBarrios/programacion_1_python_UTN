'''
13- Crear una función que recibe una lista de palabras y 
devuelve un diccionario con las palabras como llaves(Key) y su 
longitud como valores (Value).
'''
lista_de_palabras = ["alfajor", "bonobon", "Chocolate"]

def largo_de_palabra(lista_str):
    '''
    crea un diccionario en base a una lista de palabras, con la palabra como key y la longitud de la misma como valor
    recibe una lista de palabras
    devuelve un diccionario con palabra como keys, y sus respectivas longitudes
    '''
    dicc_palabras = dict()
    for palabra in lista_str:
        dicc_palabras[palabra] = len(palabra)
    return dicc_palabras

nuevo_diccionario_palabras = largo_de_palabra(lista_de_palabras)

print(nuevo_diccionario_palabras)






'''dimplemente es esto, nomas que pepe se reemplaza por la palabra 
en esa posicion en ese momento'''
# nuevo_dic = {}
# nuevo_dic["Pepe"] = len("Pepe")
# print(nuevo_dic)  #imprime : {'Pepe': 4}











# def longitud_palabras(lista_palabras):
#     """Esta función recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores"""
#     diccionario = {}
#     for palabra in lista_palabras:
#         diccionario[palabra] = len(palabra)
#     return diccionario

# long = longitud_palabras(lista_de_palabras)
# print(long)