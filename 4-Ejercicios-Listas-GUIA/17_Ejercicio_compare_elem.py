'''
17- Crea dos listas de números y encuentra los elementos que se encuentran en
ambas listas.
'''


lista_uno = [66, 10, 21, 33, 7]
lista_dos = [5, 33, 7, 6, 66]

lista_tres = []

for elemento_uno in lista_uno: # for anidados , cada uno recorre una lista, pasando por sus elementos
    for elemento_dos in lista_dos:
        if(elemento_uno == elemento_dos):# comparacion de elmentos, si es true es porque hay repetidos
            lista_tres.append(elemento_uno)# agrega a la lista 3
            

print("Los repetidos son {0}".format(lista_tres))# Muestro la lista 3

for elemento in lista_tres:
    print(elemento) #muestro cda repetido














# No anda porque busca y compara el mismo indice de dos listas.
'''El problema es que estás comparando los elementos de 
las dos listas en la misma posición utilizando el índice del bucle for.

Si un elemento se encuentra en una posición diferente en cada lista,
no se considerará como repetido y no se agregará a la lista_tres.'''

# lista_uno = [10, 21, 33, 7]
# lista_dos = [5, 33, 7, 6]

# lista_tres = []

# for indice in range(len(lista_uno)):
#     if(lista_uno[indice] == lista_dos[indice]):
#         lista_tres.append(lista_dos[indice])

# print("Los repetidos son: {0}".format(lista_tres))