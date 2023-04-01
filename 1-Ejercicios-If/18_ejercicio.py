'''
18- Escribir un programa que le pida al usuario que ingrese un 
número entero, y luego imprima "El número es par y es múltiplo 
de 3" si el número es par y es múltiplo de 3, o "El número no cumple 
ninguna de las dos condiciones" si el número no cumple ninguna de las dos condiciones.
'''

numero_ingresado_str = input("Ingrese un numero")
numero_ingresado_int = int(numero_ingresado_str)

if( numero_ingresado_int % 2 == 0 and numero_ingresado_int % 3 == 0):
    print("El número es par y es múltiplo de 3")
else:
    print("El número no cumple ninguna de las dos condiciones")



'''
Para saber si un número es múltiplo de 3 y es par:
puedes utilizar la operación módulo (%) para determinar si el número es 
divisible por 3, (osea si un numero n % 3 == 0 es multiplo de 3 )
y luego comprobar si el número es par utilizando 
el operador de resto (%) nuevamente si el resultado de ambas es 0 entonces 
ese numero es tambien par.
(osea n % 2 == 0)
'''