'''
8- Crea una lista con los nombres de tus 5 libros favoritos y luego 
imprime solo los primeros 3 libros de la lista
'''
lista_de_libros = ["harry potter", "El area 7", "El templo", 
                "el señor de los anillos", "Antartida estacion polar"]

for indice in range(len(lista_de_libros)):
    if( indice < 3):
        print(lista_de_libros[indice])
    else:
        break
    #indice += 1    funciona igual sin este incremento










'''esta mal parece'''
# lista_de_libros = ["harry potter", "El area 7", "El templo", 
#                 "el señor de los anillos", "Antartida estacion polar"]

# for indice in range(3):
#     print(lista_de_libros[indice])