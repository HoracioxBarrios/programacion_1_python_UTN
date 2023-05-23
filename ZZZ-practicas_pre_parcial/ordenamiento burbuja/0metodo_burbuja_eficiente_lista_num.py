lista = [5, 1, 6, 12, 1, 0, 2]

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
                
ordenar_numeros_bubble_sort_v3(lista)
print("id en memoria:{0}".format(id(lista)))