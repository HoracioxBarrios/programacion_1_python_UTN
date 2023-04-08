''' CUADRADOS PERFECTOS
8- Escribir un programa que le pida al usuario que ingrese 
un número entero positivo, y luego imprima "El número es un 
cuadrado perfecto" si el número es un cuadrado perfecto, o "El 
número no es un cuadrado perfecto" si el número no es un cuadrado perfecto .
'''

numero = int(input("Ingresa un número: "))
i = 1

while i <= numero:
    suma_divisores = 0
    j = 1

    while j < i:
        if i % j == 0:
            suma_divisores += j
        j += 1

    if suma_divisores == i:
        print(i)

    i += 1
    
    '''Explicación del código:

Primero, le pedimos al usuario que ingrese un número y lo almacenamos
en la variable numero.
Luego, inicializamos la variable i en 1 para comenzar a recorrer los números 
desde el 1 hasta el número ingresado.
Dentro del primer bucle while, inicializamos la variable suma_divisores en 
0 para acumular la suma de los divisores propios de i.
Después, iniciamos otro bucle while anidado para recorrer los números desde 1 
hasta i-1 y verificar si son divisores propios de i. Si lo son, los sumamos 
a la variable suma_divisores.
Por último, si la suma de los divisores propios de i es igual a i, entonces 
i es un número perfecto y lo imprimimos por pantalla.
Incrementamos i en 1 para continuar con el siguiente número.
Espero que te sea útil. ¡Saludos!'''
