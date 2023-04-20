'''
20- Escribir un programa que le pida al usuario que ingrese dos números
enteros, y luego imprima "Los dos números son iguales" si los dos números 
son iguales, "El primer número es mayor" si el primer número es mayor que el 
segundo, o "El segundo número es mayor" si el segundo número es 
mayor que el primero .

'''
primer_numero_string = input("Ingrese un numero")
primer_numero_integer = int(primer_numero_string)

segundo_numero_string = input("Ingrese un numero")
segundo_numero_integer = int(segundo_numero_string)


if(primer_numero_integer > segundo_numero_integer):
    print("El primer numero es mayor")
elif(segundo_numero_integer > primer_numero_integer):
    print("El segundo numero es mayor")
else:
    print("Los dos números son iguales")