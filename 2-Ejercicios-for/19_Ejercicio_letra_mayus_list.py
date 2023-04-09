'''
19- 19.Dada una lista de palabras, imprimir las palabras que tienen
una letra mayúscula.
'''

palabras = ["Hola", "Mundo", "hola", "123A", "ABC", "adiós"]

for palabra in palabras:
    tiene_mayuscula = False
    for letra in palabra:# recorre letra x letra de cada palabra en cad iteracion
        if letra.isupper():# si hay una mayus ,cmbia la flag y corta la iteracion.
            tiene_mayuscula = True
            break
    if (tiene_mayuscula == True):# si es mayus muestra la palabra y sigue iteando hasta completar los items de la lista
        print(palabra)


# palabras = ["Hola", "Mundo", "hola", "123A", "ABC", "adiós"]

# for palabra in palabras:
#     if any(letra.isupper() for letra in palabra):
#         print(palabra)

