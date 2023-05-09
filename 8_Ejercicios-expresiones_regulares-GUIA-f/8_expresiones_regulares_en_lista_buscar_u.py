'''
8. Crear una función que reciba una lista de palabras y devuelva 
otra lista con las palabras que comienzan con la letra "U"
'''
import re
lista_de_frutas = ["Uva", "Uvaya", "uxi", "pera", "manzana", "naranjucha"]

def comiezan_con_u(lista: list)-> list:
    '''
    busca las palabras que empeizan con u
    '''
    nueva_lista_palabras_con_u = []
    for fruta in lista:
        if re.match(r'^[Uu]+', fruta):
            nueva_lista_palabras_con_u.append(fruta)
            
    return nueva_lista_palabras_con_u

print(comiezan_con_u(lista_de_frutas))