'''
6. Crea una función que ordene una lista de tuplas (nombre, edad, 
altura) primero por edad de menor a mayor y luego por altura 
de menor a mayor.
'''
lista_tuplas = [("Juan", 25, 170),
                ("María", 30, 165),
                ("Pedro", 40, 180),
                ("Ana", 35, 160),
                ("Luis", 28, 175)]

# con lista no hay drama

def ordenar_lista_de_tupas(
    lista_tupla : list[tuple], dato_a_ordenar = "altura", orientacion ="min_a_max")-> list[tuple]:
    '''
    Ordena una lista de tuplas segun dato a ordenar
    Recibe:(arg 1) una lista de tuplas, (arg2 ) el dato a ordenar("altura" o "edad"),
    (arg3) la orientacion (por defecto de "min_a_max") o cambiar a "max_a_min".
    Devuelve: una lista, de tuplas ordenada.
    
    '''
    if(lista_tupla):
        
        len_lista = len(lista_tupla) -1
        flag_swap = True
    
        while(flag_swap):
            flag_swap = False
            for indice in range(len_lista):
                if(dato_a_ordenar == "edad"):
                    valor_actual = lista_tupla[indice +1][1]
                    valor_siguiente = lista_tupla[indice][1]
                elif(dato_a_ordenar == "altura"):
                    valor_actual = lista_tupla[indice +1][2]# cambia el indice de la tupla
                    valor_siguiente = lista_tupla[indice][2]
                
                if(orientacion == "min_a_max" and valor_actual < valor_siguiente):
                    lista_tuplas[indice], lista_tuplas[indice + 1] = lista_tuplas[indice + 1], lista_tuplas[indice]# cambio las posiciones entre las tuplas
                    flag_swap = True
                elif(orientacion == "max_a_min" and valor_actual > valor_siguiente):
                    lista_tuplas[indice], lista_tuplas[indice + 1] = lista_tuplas[indice + 1], lista_tuplas[indice]# cambio las posiciones entre las tuplas
                    flag_swap = True
            len_lista -= 1
        return lista_tupla
                
    else:
        return "La lista esta vacia"
    
lista_tupla_ordenada = ordenar_lista_de_tupas(lista_tuplas)
print(lista_tupla_ordenada)

'''
la idea es cambiar de lugar entre las tuplas, para evaluar nos guardamos los valores 
en las variables
'''