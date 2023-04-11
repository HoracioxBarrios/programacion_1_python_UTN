'''
9- Crea una lista de números enteros y pide al usuario 
que ingrese otro número entero. Luego, busca el número 
ingresado en la lista y muestra la posición en la que se 
encuentra. Si el número no se encuentra en la lista, muestra 
un mensaje indicando que no se encontró

'''

lista_numeros = [1, 2, 3,4, 5] # Creamos la lista de números enteros

numero_ingresado_str = input("Ingresa un numero")# Pedimos al usuario que ingrese un número entero
numero_ingresado_int = int(numero_ingresado_str)
flag_encontrado = False

# # Buscamos el número en la lista
for indice in range(len(lista_numeros)): # range( len() )
    if(numero_ingresado_int == lista_numeros[indice]):# si el ingresado es igual al elemento en la posicion indice en ese momento. si hay muestra
        
        print("El numero esta en la posicion {0}".format(indice))#El indice dice la posicion
        flag_encontrado = True



if(flag_encontrado == False):
    print("El numero no esta en la lista")






'''dato
La función range(len(lista_numeros)) en Python 3 crea un objeto de 
rango que representa una secuencia de números enteros desde 0 
hasta la longitud de la lista_numeros menos 1. Este objeto de
rango se puede utilizar para iterar sobre los índices de la 
lista_numeros en un bucle for. Por ejemplo:

Copy code:
lista_numeros = [1, 2, 3, 4, 5]
for i in range(len(lista_numeros)):
    print(lista_numeros[i])             #muestra todos los elementos
'''















# # Creamos la lista de números enteros
# numeros = [1, 5, 8, 10, 15, 20]

# # Pedimos al usuario que ingrese un número entero
# numero_buscar = int(input("Ingrese un número entero: "))

# # Buscamos el número en la lista
# encontrado = False
# for i in range(len(numeros)):
#     if numeros[i] == numero_buscar:
#         # Si el número está en la lista, mostramos su posición
#         print("El número", numero_buscar, "se encuentra en la posición", i)
#         encontrado = True
#         break

# if not encontrado:
#     # Si el número no está en la lista, mostramos un mensaje de error
#     print("El número", numero_buscar, "no se encuentra en la lista.")