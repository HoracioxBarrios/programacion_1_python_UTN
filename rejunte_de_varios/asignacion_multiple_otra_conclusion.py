#es lo mismo?}

'''
Sí, ambas formas de intercambiar valores en un bubble sort son equivalentes
y producirán el mismo resultado. Tanto la asignación individual de valores 
como la asignación múltiple utilizando la sintaxis de tupla producirán el 
intercambio de los valores correctamente.
'''

lista_heroes[indice] = lista_heroes[indice + 1]
lista_heroes[indice + 1] = lista_heroes[indice]


'''
En el código que mostraste, no es necesario crear una variable temporal adicional 
para intercambiar los valores utilizando las asignaciones individuales. 
'''




lista_heroes[indice], lista_heroes[indice + 1] = lista_heroes[indice + 1], lista_heroes[indice]
'''aca :
Se utiliza la sintaxis de tupla para intercambiar los valores. Los valores 
lista_heroes[indice + 1] y lista_heroes[indice] se empaquetan en una tupla 
(lista_heroes[indice + 1], lista_heroes[indice]), y luego se desempaquetan 
en las posiciones correspondientes lista_heroes[indice] y lista_heroes[indice + 1].
Esto tiene el efecto de intercambiar los valores entre las dos posiciones.
'''
