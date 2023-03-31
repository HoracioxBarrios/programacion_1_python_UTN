'''
10- Escribir un programa que le pida al usuario que ingrese un número 
entero, y luego imprima "El número es positivo y par" si el número es 
positivo y divisible por 2, o "El número no cumple ninguna condición" 
si el número no cumple ninguna de las dos condiciones anteriores.
'''

numero_ingresado_str = input("Ingrese un numero")
numero_ingresado_int = int(numero_ingresado_str)



if( numero_ingresado_int > 0 and numero_ingresado_int % 2 == 0):
    print("El numero es positivo y par")
else:
    print("El numero no cumple ninguna condicion")

