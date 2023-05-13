def ordenar(lista):
    flag_swap = True
    while flag_swap:
        flag_swap = False
        for i in range(len(lista) - 1):
            print(lista)
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                flag_swap = True

def ordenar_lista_diccionarios(lista, clave):
    flag_swap = True
    while flag_swap:
        flag_swap = False
        for i in range(len(lista) - 1):
            if lista[i][clave] > lista[i + 1][clave]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                flag_swap = True

def ordenar_lista_diccionarios_2(lista, clave, clave2):
    flag_swap = True
    while flag_swap:
        flag_swap = False
        for i in range(len(lista) - 1):
            if lista[i][clave] > lista[i + 1][clave]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                flag_swap = True
            elif lista[i][clave] == lista[i + 1][clave]:
                if lista[i][clave2] > lista[i + 1][clave2]:
                    aux = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = aux
                    flag_swap = True


#https://www.onlinegdb.com/Um71v5_F1