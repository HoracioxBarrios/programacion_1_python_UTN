''' CUADRADOS PERFECTOS
8- Escribir un programa que le pida al usuario que ingrese 
un número entero positivo, y luego imprima "El número es un 
cuadrado perfecto" si el número es un cuadrado perfecto, o "El 
número no es un cuadrado perfecto" si el número no es un cuadrado perfecto .
'''
import math
numero_ingresado_str = input("Ingrese un numero")
numero_ingresado_int = int(numero_ingresado_str)

raiz = math.sqrt(numero_ingresado_int) # para usar el modulo math ,hay que importarlo
# math.sqrt() devuelve la raiz cuadrada del numero pasado como argumento
if(raiz.is_integer()):# raiz.is_integer() comprueba si es entero
    print("El numero es un cuadrado perfecto")
else:
    print("El numero no es un cuadrado perfecto")




    '''
    CUADRADO PERFECTO:
    Un cuadrado perfecto es el resultado de multiplicar un 
    por sí mismo. También podemos decir que los cuadrados 
    perfectos son los números que poseen raíces cuadradas 
    exactas. 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, ...

    Ejermplo : raiz cuadrada de 16 es = 4 porque 4 elevado a 2 ( o lo que 
    es lo mismo: multiplicado por si mismo da 16
    como 4 (que la raiz de 16) es un entero, nos dice que 16 es un cuadrado perfecto) 
    '''