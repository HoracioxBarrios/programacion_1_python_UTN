'''6- Dada una lista de palabras,imprimir la cantidad total de vocales en la lista.'''


lista_de_palabras = ["PERRO", "HOlA", "MOUSE", "computadora"]
contador_vocales = 0
for palabra in lista_de_palabras:  # recorremos la lista
    for letra in palabra:# recorremos cada string de la palabra
        if (letra == "A" or letra == "E" or letra == "I" or letra == "O" or 
            letra == "U" or letra == "a" or letra == "e" or letra == "i" or 
            letra == "o" or letra == "u"):
            contador_vocales += 1

print(contador_vocales)



# lista_de_palabras = ["hola", "mundo", "python", "programacion"]

# cantidad_de_vocales = 0

# for palabra in lista_de_palabras:
#     for letra in palabra:
#         if letra in "aeiouAEIOU":
#             cantidad_de_vocales += 1

# print("La cantidad total de vocales en la lista es:", cantidad_de_vocales)
