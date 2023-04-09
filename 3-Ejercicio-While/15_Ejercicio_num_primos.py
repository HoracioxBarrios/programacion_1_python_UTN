'''
15- Dado un número entero n, imprimir todos los números primos menores o
iguales a n

'''
n = int(input("Ingrese un número entero: "))

# Creamos una lista de números del 2 al n
numeros = list(range(2, n+1))

# Creamos una lista vacía para almacenar los números primos
primos = []

# Mientras haya números en la lista de números
while len(numeros) > 0:
    # Tomamos el primer número de la lista y lo agregamos a la lista de primos
    primo = numeros.pop(0)
    primos.append(primo)

    # Eliminamos los múltiplos del número primo encontrado
    numeros = [num for num in numeros if num % primo != 0]

# Imprimimos la lista de primos
print("Los números primos menores o iguales a", n, "son:", primos)


'''
En matemáticas, un número primo es un número natural mayor que 1 que 
tiene únicamente dos divisores positivos distintos: él mismo y el 1.
Por el contrario, los números compuestos son los números naturales 
que tienen algún divisor natural aparte de sí mismos y del 1, y,
por lo tanto, pueden factorizarse.
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
67, 71, 73, 79, 83, 89, 97, 101, etc...
'''
