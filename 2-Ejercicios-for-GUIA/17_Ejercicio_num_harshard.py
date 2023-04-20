'''
17- .Dado un número entero n, imprimir la secuencia de números de Harshad
menores o iguales a n
'''
n = int(input("Ingrese un número entero: "))

for i in range(1, n+1):
    digits_sum = 0
    num = i
    while num > 0:
        digits_sum += num % 10
        num //= 10
    if i % digits_sum == 0:
        print(i)
        
'''chat gpt:

En este código, utilizamos un bucle while para obtener los dígitos
del número actual i. Primero, inicializamos una variable digits_sum
en cero. Luego, creamos una variable num que contiene el valor de i.
Dentro del bucle while, utilizamos la operación módulo (%) para 
obtener el último dígito de num, lo sumamos a digits_sum y luego 
dividimos num entre 10 utilizando la operación de división entera (//) 
para eliminar el último dígito. Repetimos este proceso hasta que num 
sea igual a cero, lo que significa que hemos obtenido todos los 
dígitos del número. Finalmente, comprobamos si el número actual i 
es divisible por digits_sum utilizando la operación módulo (%), 
y si es así, lo imprimimos utilizando la función print().'''