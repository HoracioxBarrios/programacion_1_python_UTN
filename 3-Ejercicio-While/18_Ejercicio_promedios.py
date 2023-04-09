'''
18-Dada una lista de números, imprimir la suma de los números en la lista que son mayores que el promedio de la lista.
'''
# Definimos la lista de números
numeros = [2, 5, 8, 10, 12]

# Calculamos el promedio de la lista
promedio = sum(numeros) / len(numeros)

# Inicializamos la variable de suma en cero
suma = 0

# Inicializamos el índice del bucle en cero
i = 0

# Iteramos mientras el índice sea menor que la longitud de la lista
while i < len(numeros):
    # Si el número actual es mayor que el promedio, lo sumamos a la variable de suma
    if numeros[i] > promedio:
        suma += numeros[i]
    # Incrementamos el índice del bucle
    i += 1

# Imprimimos la suma de los números mayores que el promedio
print("La suma de los números mayores que el promedio es:", suma)



'''En este ejemplo, la lista de números es [2, 5, 8, 10, 12]. 
El promedio de la lista es (2+5+8+10+12)/5 = 7.4. Luego, iteramos
sobre cada número en la lista y sumamos solo aquellos que son 
mayores que el promedio. En este caso, los números mayores que 
el promedio son 8, 10 y 12, por lo que la suma final es 8+10+12 
= 30. Finalmente, imprimimos la suma de los números mayores 
que el promedio.'''