'''
9-Dada una lista de palabras, imprimir todas las palabras que 
tengan una longitud mayor a 5 caracteres.
'''

lista_de_palabras = ["MATE", "PAVA", "AZUCAR","MEDIALUNAS","BISCOCHITOS"]
indice = 0
# print(lista_de_palabras[3])
# print(len(lista_de_palabras))

while(indice < len(lista_de_palabras)):# condicion de iteracion
    if(len(lista_de_palabras[indice]) > 5):# si el elemento en la posisicion indice tiene len() > 5
        print(lista_de_palabras[indice]) #mostar el elemento en la posisicon indice
    indice += 1






# palabras = ["Python", "programación", "informática", "programa", "lenguaje"]
# i = 0 # inicializamos el contador del bucle
# while i < len(palabras):
#     if len(palabras[i]) > 5:
#         print(palabras[i])
#     i += 1 # aumentamos el contador en cada iteración


