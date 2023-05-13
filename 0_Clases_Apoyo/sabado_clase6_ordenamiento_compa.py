def ordenar_lista(lista:list, orden:str ,clave:str, clave2:str):
    """"recibe la lista de personajes, el orden y dos claves en caso de que la primer clave sea igual 
    en dos personajes, usa la segunda clave como criterio de ordenamiento
    retorna una lista de personajes ordenada como pidio el usuario
    """

    bandera_swap = True
    while bandera_swap == True:
        bandera_swap = False
        for i in range(len(lista)-1):
            if (lista[i][clave] > lista[i+1][clave] and orden == "ascendente") or (lista[i][clave] < lista[i+1][clave] and orden == "descendente"):
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                bandera_swap = True
            if lista[i][clave] == lista[i+1][clave]:
                if lista[i][clave2] < lista[i+1][clave2]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera_swap = True
                    
                    
                    
'''
para debugear podemos usar pprint
import pprint solo para debugear
'''