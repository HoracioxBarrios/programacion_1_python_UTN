'''
7- Escribir un programa que le pida al usuario que ingrese 
un número entero positivo, y luego imprima "El número es primo" 
si el número es primo, o "El número no es primo" si el número no es primo.
'''

numero_ingresado_str = input("Ingrese un numero")
numero_ingresado_int = int(numero_ingresado_str)
if(not (numero_ingresado_int % 2 == 0) or numero_ingresado_int == 2):
    print("el numero primo")
else:
    print("El numero no es primo")
