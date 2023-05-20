import copy

'''
1. Crea una función que ordene una lista de números enteros 
de menor a mayor. Puedes utilizar cualquier método de 
ordenamiento que conozcas
'''
lista_de_numeros = [5, 10, 30, 50, 100, 150, 600]

lista_de_numeros_2 = copy.copy(lista_de_numeros)

lista_de_numeros_3 = lista_de_numeros[:]


'''
Hice unas copias para probar las 3 funciones, porque sino me 
estaria ordenando la que ya esta ordenada por que la lista al
tener los mimos valores va y busca en la posicion de memoria
existente. Por lo tanto al crear las copias con esas dos maneras,
libreria copy y slice. con esto me crea dos nuevos 
espacios en memoria para las dos nuevas listas 2 y 3
'''

# bubble sort con indice en decremento
def ordenar_numeros_bubble_sort(lista : list):
    len_de_lista = len(lista) -1
    for indice in range(len_de_lista):
        if(lista[indice] > lista[indice + 1]):
            aux = lista[indice]
            lista[indice] = lista[indice + 1]
            lista[indice + 1] = aux
        len_de_lista -= 1
    print(lista)

# ordenar_numeros_bubble_sort(lista_de_numeros)
# print("id en memoria:{0}".format(id(lista_de_numeros)))



#con flag
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

# ordenar_numeros_bubble_sort_v2(lista_de_numeros_2)
# print("id en memoria:{0}".format(id(lista_de_numeros_2)))

#mas obtimizada combinando las dos de abajo.
def ordenar_numeros_bubble_sort_v3(lista: list):
    len_de_lista = len(lista) -1
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        for indice in range(len_de_lista):
            if(lista[indice] > lista[indice +1]):
                aux_backup_valor = lista[indice]
                lista[indice] = lista[indice +1]
                lista[indice +1] = aux_backup_valor
                flag_swap = True
        len_de_lista -= 1
        print(lista)      
                
ordenar_numeros_bubble_sort_v3(lista_de_numeros_3)
# print("id en memoria:{0}".format(id(lista_de_numeros_3)))