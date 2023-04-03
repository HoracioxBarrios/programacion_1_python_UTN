'''
7- Dada una lista de números, imprimir todos los números que son mayores que
el promedio de la lista.
'''
#Uso funcion sum() suma los elementos de un obj iterable,
''' 
len() que es una función integrada que se utiliza para obtener 
la longitud de un objeto iterable, como una cadena, una lista, 
una tupla, un diccionario, un conjunto, etc. Devuelve el número 
de elementos en el objeto iterable. '''

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
promedio = sum(lista_de_numeros) / len(lista_de_numeros)

print("El promedio es {0}".format(promedio))

i = 0
suma = 0
while( i < len(lista_de_numeros)):
    if(lista_de_numeros[i] > promedio):
        print(lista_de_numeros[i])
    i += 1















'''
chat gpt4

En este ejemplo, se define una lista de números lista.Luego se 
calcula el promedio de la lista dividiendo la suma de los números 
en la lista por la cantidad de números en la lista. Después se 
imprime el valor del promedio. Luego se itera sobre la lista usando
un bucle for.Dentro del bucle, se verifica si el número actual es 
mayor que el promedio de la lista. Si es así, se imprime el número. 
Esto imprimirá todos los números de la lista que son mayores que el promedio de la lista.

También puedes hacerlo con un bucle 
while
de la siguiente manera:

lista = [2, 4, 6, 8, 10]

promedio = sum(lista) / len(lista)

print("El promedio de la lista es:", promedio)

i = 0
while i < len(lista):
    if lista[i] > promedio:
        print(lista[i])
    i += 1
'''