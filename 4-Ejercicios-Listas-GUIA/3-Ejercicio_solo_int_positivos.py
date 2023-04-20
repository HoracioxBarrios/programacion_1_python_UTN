'''
3- Crea una lista vacía y pide al usuario que ingrese 
números enteros hasta que ingrese un número negativo. 
Luego, muestra la suma de todos los números ingresados.
'''

lista_de_numeros = []
Flag_while = True
acum_suma_numeros = 0

while(Flag_while):
    numero_str = input("Ingrese numero")
    numero_int = int(numero_str)
    if(numero_int > 0):
        lista_de_numeros.append(numero_int)#agrego a la lista
        acum_suma_numeros = acum_suma_numeros + numero_int
    else:
        Flag_while = False

print("La suma de todos los numeros es: {0}".format(
    acum_suma_numeros))    















# lista_de_numeros = []
# acum = 0

# while(True):    
#     numero_ingresado_str = input("Ingrese un numero")
#     numero_ingresado_int = int(numero_ingresado_str)
#     if numero_ingresado_int > 0:
#         lista_de_numeros.append(numero_ingresado_int)
#         acum = acum + numero_ingresado_int
#     else:
#         break


# print("La suma acumulada es {0}".format(acum))







# lista_de_numeros = []
Flag = True

# while(Flag):    
#     numero_ingresado_str = input("Ingrese un numero")
#     numero_ingresado_int = int(numero_ingresado_str)
#     if numero_ingresado_int > 0:
#         lista_de_numeros.append(numero_ingresado_int)
#     else:
#         Flag = False


# suma_numeros_posit = sum(lista_de_numeros)
# print(suma_numeros_posit)
