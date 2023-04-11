'''
13- Escribir un programa que le pida al usuario que ingrese un 
número entero, y luego imprima "El número es divisible por 3 y por 5" 
si el número es divisible por 3 y por 5, o "El número no es divisible 
por 3 y por 5" si el número no es divisible por 3 y por 5 .

'''

numero_ingresado_str = input("Ingrese un numero: ")
numero_ingresado_int = int(numero_ingresado_str)

if(numero_ingresado_int % 3 == 0 and numero_ingresado_int % 5 == 0):
    print("el numero es divisible por 3 y por 5")
else:
    print("el numero no es divisible por 3 y por 5")