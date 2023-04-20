'''
4- Crea una lista vacía y pide al usuario que ingrese una palabra.
Luego, muestra la primera letra de la palabra. Repite este proceso
hasta que el usuario ingrese una palabra que comience con la letra "z".
'''

lista_de_palabras = [] #lista vacia
flag_while = True

while(flag_while):
    palabra_ingresada = input("Ingrese una palabra")
    if(palabra_ingresada[0] != "Z" and palabra_ingresada[0] != "z"):
        lista_de_palabras.append(palabra_ingresada)
        print(palabra_ingresada[0])
    else:
        flag_while = False














# #lista_de_palabras = list()  es equivalente
# lista_de_palabras = []
# i = 0

# while(True):
#     palabra = input("Ingrese una palabra")
#     if(palabra[i] != "z"):
#         lista_de_palabras.append(palabra)
#         print(palabra[0])
#     else:
#         break

    
# print("FIN")

