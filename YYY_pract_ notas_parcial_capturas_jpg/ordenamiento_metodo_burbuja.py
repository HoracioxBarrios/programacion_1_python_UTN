'''Método Burbuja - Algoritmos de Ordenamiento con Python'''


lista_scores = ["70", "90", "0", "80", "60", "85"]

def burbble_sort(lista : list)-> list:
    
    length_menos_uno = len(lista) - 1 # se necesita evaluar hasta el anteultimo 
    
    for i in range(0, length_menos_uno):#bucle para las pasadas
        for j in range(0,length_menos_uno):# comparaciones e intercambios
            if(lista[j] > lista[ j + 1] ):#comprueba si el valor en esa posicion es mayor, que el de la proxima posicion
                auxiliar = lista[j] #guarda el "primer valor" y es temporal para cada iteracion
                lista[j] = lista[j + 1] # el valor del elem de la posicion 2 se asigna al de la posicion anterior(se corre para atras)
                lista[j + 1] = auxiliar # el primer valor se acomoda en la posicion 2 y asi se va corriendo para adelante si es mayor al anterior
    return lista

print("antes de ordenar")
print(lista_scores)

print("despues de ordenar")
print(burbble_sort(lista_scores))    


#https://www.youtube.com/watch?v=nqoMzb65Ez8

#https://onlinegdb.com/3eKSiqqg8