''' CUADRADOS PERFECTOS
8- Escribir un programa que le pida al usuario que ingrese 
un número entero positivo, y luego imprima "El número es un 
cuadrado perfecto" si el número es un cuadrado perfecto, o "El 
número no es un cuadrado perfecto" si el número no es un cuadrado perfecto .
'''
# corroborar ,no lo entiendo
num = int(input("Ingrese un número entero positivo: "))
i = 1
while i*i <= num:
    if i*i == num:
        print("El número es un cuadrado perfecto")
        break
    i += 1
else:
    print("El número no es un cuadrado perfecto")


'''
Este programa le pide al usuario que ingrese un número entero 
positivo y luego utiliza un bucle while para verificar si el 
número es un cuadrado perfecto. Si el número es un cuadrado 
perfecto, el programa imprime "El número es un cuadrado perfecto".
De lo contrario, el programa imprime "El número no es un cuadrado perfecto".

¡Claro! Aquí te dejo un listado de los primeros 20 cuadrados perfectos:

1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 
324, 361, 400

Un cuadrado perfecto es un número entero que puede ser expresado como el 
producto de dos números iguales. Por ejemplo, 4 es un cuadrado perfecto porque 2 x 2 = 4.
'''