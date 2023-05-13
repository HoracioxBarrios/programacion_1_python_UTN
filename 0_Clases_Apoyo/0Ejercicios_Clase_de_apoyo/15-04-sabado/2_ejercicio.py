'''
2. Crea una función que ordene una lista de cadenas 
alfabéticamente de A a Z.
'''


lista_de_letras = ['B', 'G', 'V', 'S', 'N', 'E', 'X', 'M', 
                   'P', 'F', 'L', 'R', 'Q', 'A', 'T', 'C', 
                   'Z', 'Y', 'K', 'I', 'U', 'D', 'W', 'H', 
                   'O', 'J']

def ordenar_letras_bubble_sort(lista : list):
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        for indice in range(len(lista)-1):
            if(lista[indice] > lista[indice +1]):
                aux = lista[indice]
                lista[indice] = lista[indice +1]
                lista[indice +1] = aux
                flag_swap = True
    return lista

print(ordenar_letras_bubble_sort(lista_de_letras))














#lista ordenada
'''
lista_de_letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                   'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
                   'Y', 'Z']
'''