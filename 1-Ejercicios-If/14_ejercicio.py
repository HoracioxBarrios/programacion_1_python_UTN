'''
14- Escribir un programa que le pida al usuario que ingrese un número 
entero, y luego imprima "El número es múltiplo de 4 y de 6" si el número 
es múltiplo de 4 y de 6, o "El número no es múltiplo de 4 y de 6" si el número 
no es múltiplo de 4 y de 6.
'''

numero_ingresado_str = input("Ingrese un numero")
numero_ingresado_int = int(numero_ingresado_str)

if(numero_ingresado_int % 4 == 0 and numero_ingresado_int % 6 == 0):
    print("El número es múltiplo de 4 y de 6")
else:
    print("El número no es múltiplo de 4 y de 6")