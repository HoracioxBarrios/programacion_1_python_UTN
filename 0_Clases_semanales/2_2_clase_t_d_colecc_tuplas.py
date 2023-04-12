## TIPO DE DATOS, (COLECCIONES)

#Tuplas

''' Tuplas: son similares a las LISTAS pero son Inmutables,no 
se pueden modificar una vez declarada. 

1-hay servicios que devuelven Tuplas, tener en cuenta esto.

2-una tupla es como una foto de una lista
'''
lista = tuple([1, "Hola", 1.5])

#Ver tipo de datos
print(type(lista)) # <class 'tuple'>

#ver el elemento del indice 1
print(lista[1]) # Hola

#re asignar un valor - No se puede!
lista[1] = "Chau" #TypeError: 'tuple' object does not support item assignment

#Declaracion de un Tupla

soy_una_tupla = tuple()  # y puede ir dentro un list