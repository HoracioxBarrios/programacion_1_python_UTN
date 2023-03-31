
# comentario simple de una linea #
""" comentario de varias lineaas """

#declaracion de una variable
mi_variable = "Pepe"

#numeros
variable_numero_float = 15.2

#casteo, convertir de un tipo de datos a otro
variable_numero_int = int(variable_numero_float)
#mostrmos por pantalla
print(variable_numero_int)

#para ingresar un dato, usamos input
'''
nombre_ingresado = input("Por favor ingrese su nombre")

print(nombre_ingresado)
'''


# if
'''
numero_uno = 1
numero_dos = 2

if(numero_uno < numero_dos):
    print("Es menor")

'''

# if - else
'''
primer_numero = input("Ingrese un numero: ")
segundo_numero = input("Ingrese un segundo : ")

if(primer_numero > segundo_numero):
    print("El primer numero es mayor: " + primer_numero)
else:
    print("El primer numero es mayor: " + segundo_numero)
'''

# if - else if

primer_numero = input("Ingrese un numero: ")
primer_numero = int(primer_numero)
segundo_numero = input("Ingrese otro numero")
segundo_numero = int(segundo_numero)

if(primer_numero > segundo_numero):
    print("el primero es mayor")
elif(primer_numero < segundo_numero):
    print("El segundo es mayor")
else:
    print("Son iguales")
