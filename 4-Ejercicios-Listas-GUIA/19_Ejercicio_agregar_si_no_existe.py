'''
19.Crea una lista vacía y pide al usuario que ingrese una palabra. 
Luego, agrega la palabra a la lista si no se encuentra 
ya en la lista. Repite este proceso hasta
que la lista tenga al menos 5 palabras.
'''

nueva_lista = []

for i in range(5):
   palabra_ingresada = input("Ingrese palabra ")
   if(palabra_ingresada not in nueva_lista):
       nueva_lista.append(palabra_ingresada)
   else:
       palabra_ingresada = input(
           "Ya se encuentra Ingrese otra palabra ")
print("La slita con los datos {0}".format(nueva_lista))










'''Otra forma'''
# palabras = []

# while len(palabras) < 5:
#     nueva_palabra = input("Ingresa una palabra: ")
#     if nueva_palabra not in palabras:
#         palabras.append(nueva_palabra)

# print("La lista final de palabras es:", palabras)
