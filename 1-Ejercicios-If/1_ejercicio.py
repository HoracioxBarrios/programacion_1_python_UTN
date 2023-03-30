'''
1- Escribir un programa que le pida al usuario que ingrese un número 
entero positivo, y luego imprima "El número ingresado es positivo" 
si el número es mayor que cero, o "El número ingresado es cero o negativo" 
si el número es menor o igual a cero.
'''

numero_str = input("Ingrese un numero")
numero_Int = int(numero_str)

if(numero_Int > 0):
    print("El numero es positivo")
else:
    print("El numero es cero o negativo")