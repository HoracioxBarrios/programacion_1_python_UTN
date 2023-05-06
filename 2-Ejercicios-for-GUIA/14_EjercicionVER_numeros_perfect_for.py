'''Dado un número entero n, imprimir la secuencia de números perfectos
menores o iguales a n.'''

n = int(input("Ingrese un número entero: "))

print("La secuencia de números perfectos menores o iguales a", n, "es:")
for i in range(1, n+1):
    suma_divisores_propios = 0
    for j in range(1, i):
        if i % j == 0:
            suma_divisores_propios += j
    if suma_divisores_propios == i:
        print(i)
        
        
'''
Si deseas imprimir la secuencia de números perfectos menores o 
iguales a n sin utilizar funciones ni la instrucción return, 
puedes seguir los siguientes pasos:

Utiliza un bucle for para iterar desde 1 hasta n. Para cada 
número, verifica si es perfecto calculando la suma de sus 
divisores propios (excluyendo al número en sí mismo) utilizando 
otro bucle for y la operación módulo (%).

Si la suma de los divisores propios es igual al número, 
imprime el número.


La secuencia de números perfectos menores o iguales a 100 es:
6
28

'''
