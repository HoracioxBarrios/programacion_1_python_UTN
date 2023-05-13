'''
1. Crea una función que ordene una lista de números enteros 
de menor a mayor. Puedes utilizar cualquier método de 
ordenamiento que conozcas
'''
lista_de_numeros = [5, 10, 30, 50, 100, 150, 600]

def ordenar_numeros_bubble_sort(lista : list):
    range_de_lista = len(lista) -1
    for indice in range(range_de_lista):
        if(lista[indice] > lista[indice + 1]):
            aux = lista[indice]
            lista[indice] = lista[indice + 1]
            lista[indice + 1] = aux
        range_de_lista -= 1
    print(lista)

ordenar_numeros_bubble_sort(lista_de_numeros)


def ordenar_numeros_bubble_sort_v2(lista : list):
    flag_swap = True
    while(flag_swap):
        flag_swap = False
    for indice in range(len(lista)-1):
        if(lista[indice] > lista[indice + 1]):
            aux = lista[indice]
            lista[indice] = lista[indice + 1]
            lista[indice + 1] = aux
            flag_swap = True
        
    print(lista)

ordenar_numeros_bubble_sort_v2(lista_de_numeros)
