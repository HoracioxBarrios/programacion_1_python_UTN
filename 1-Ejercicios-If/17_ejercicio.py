'''
17- Escribir un programa que le pida al usuario que ingrese 
un número entero, y luego imprima "El número es negativo" si 
el número es menor que cero, "El número es cero" si el número es 
igual a cero, o "El número es positivo" si el número es mayor que cero .
'''

numero_ingresado_str = input("INgrese un numero")
numero_ingresado_int = int(numero_ingresado_str)

if(numero_ingresado_int < 0):
    print("El numero es negativo")
elif(numero_ingresado_int > 0):
    print("El numero es Positivo")
else:
    print("El numero es Cero")