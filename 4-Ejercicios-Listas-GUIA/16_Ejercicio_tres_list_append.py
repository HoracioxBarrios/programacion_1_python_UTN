'''
16-Crea dos listas con la misma cantidad de elementos y luego 
crea una tercera lista que contenga los elementos 
de ambas listas intercalados. Por ejemplo,
si las dos listas son [1, 2, 3] y ["a", "b", "c"], 
la tercera lista deberíaser[1,"a",2,
"b",3,"c"].
'''

lista_uno = [1, 2, 3]
lista_dos = ["a", "b", "c"]

lista_tres = []

for indice in range(len(lista_uno)):
    lista_tres.append(lista_uno[indice])
    lista_tres.append(lista_dos[indice])

print(lista_tres)