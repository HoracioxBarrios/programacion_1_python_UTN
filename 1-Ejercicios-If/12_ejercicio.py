'''
12- Escribir un programa que le pida al usuario que ingrese 
dos números enteros, y luego imprima "El primer número es positivo" 
si el primer número es mayor que cero, "El segundo número es positivo" 
si el segundo número es mayor que cero, o "Ambos números son negativos" 
si los dos números son negativos.
'''

primer_numero_str = input("ingrese un numero")
primer_numero_int = int(primer_numero_str)

segundo_numero_str = input("ingrese otro numero")
segundo_numero_int = int(segundo_numero_str)


if(primer_numero_int > 0):
    print("El primer numero es positivo")
elif(segundo_numero_int > 0):
    print("El segundo numero es positivo")
else:
    print("Ambos son negativos")



