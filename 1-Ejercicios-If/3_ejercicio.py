'''
3- Escribir un programa que le pida al usuario que ingrese un 
número entero, y luego imprima "El número ingresado es par" si 
el número es divisible por 2, o "El número ingresado es impar" 
si el número no es divisible por 2.
'''
numero_ingresado_str = input("Ingrese un numero: ")
numero_ingresado_int = int(numero_ingresado_str)

if(numero_ingresado_int % 2 == 0):
    print("El numero ingresado es par")
else:
    print("El numero ingresado es Impar")
