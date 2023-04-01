'''NUMERO MAYOR QUE OTRO
4- Escribir un programa que le pida al usuario que ingrese 
dos números enteros, y luego imprima "El primer número es mayor"
si el primer número es mayor que el segundo, "El segundo número es mayor"
si el segundo número es mayor que el primero, o "Los dos números son iguales" 
si los dos números son iguales.
'''

primer_numero_ingresado_str = input("Ingrese un numero")
primer_numero_ingresado_int = int(primer_numero_ingresado_str)

segundo_numero_ingresado_str = input("Ingrese otro numero")
segundo_numero_ingresado_int = int(segundo_numero_ingresado_str)

if(primer_numero_ingresado_int > segundo_numero_ingresado_int):
    print("El primer número es mayor")
elif(primer_numero_ingresado_int < segundo_numero_ingresado_int):
    print("El segundo número es mayor")
else:
    print("Los dos números son iguales")















# primer_numero_str = input("Ingrese un numero: ")
# primer_numero_int = int(primer_numero_str)

# segundo_numero_str = input("Ingrese un segundo numero")
# segundo_numero_int = int(segundo_numero_str)

# if(primer_numero_int > segundo_numero_int):
#     print("El primer numero es mayor")
# elif( primer_numero_int < segundo_numero_int):
#     print("El segundo numero es mayor")
# else:
#     print("Son iguales")
