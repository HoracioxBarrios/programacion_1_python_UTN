'''NUMEROS PRIMOS
7- Escribir un programa que le pida al usuario que ingrese 
un número entero positivo, y luego imprima "El número es primo" 
si el número es primo, o "El número no es primo" si el número no es primo .
'''



numero_ingresado_str = input("Ingrese un numero")
numero_ingresado_int = int(numero_ingresado_str)

if (numero_ingresado_int % 2 != 0) or numero_ingresado_int == 2:
    print("Es primo")
else:
    print("No es primo")






















# numero_ingresado_str = input("Ingrese un numero")
# numero_ingresado_int = int(numero_ingresado_str)

# contador_divisores = 0
# numero_a_iterar = 1

# while(contador_divisores <= 2 and numero_a_iterar <= numero_ingresado_int):
#     if(numero_ingresado_int % numero_a_iterar == 0):
#         contador_divisores += 1
#     numero_a_iterar += 1

# if(contador_divisores == 2):
#     print("Es numero primo")
# else:
#     print("No es numero primo")
    

'''
Numeros Primos:
En matemáticas, un número primo es un número natural mayor que 1 que
tiene únicamente dos divisores positivos distintos: él mismo y el 1.
Por el contrario, los números compuestos son los números naturales que 
tienen algún divisor natural aparte de sí mismos y del 1, y, por lo tanto, 
pueden factorizarse.

Ej:, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
79, 83, 89, 97, 101, a infinito...
'''