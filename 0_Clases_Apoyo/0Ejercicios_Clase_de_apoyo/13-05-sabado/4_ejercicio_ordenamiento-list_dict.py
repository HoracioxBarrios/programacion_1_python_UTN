'''
4. Crea una función que ordene una lista de diccionarios con información 
sobre libros (título, autor, año de publicación) por año de publicación 
de menor a mayor.
'''
libros = [
    {
        "título": "Harry Potter y la piedra filosofal",
        "autor": "J.K. Rowling",
        "año": 1997
    },
    {
        "título": "Crepúsculo",
        "autor": "Stephenie Meyer",
        "año": 2005
    },
    {
        "título": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año": 1605
    },
    {
        "título": "Los juegos del hambre",
        "autor": "Suzanne Collins",
        "año": 2008
    },
    {
        "título": "El código Da Vinci",
        "autor": "Dan Brown",
        "año": 2003
}]

def ordenar_libros_por_clave(
    lista_de_libros : list[dict], clave_buscada : str)-> list[dict]:
    len_de_lista = len(lista_de_libros)-1
    flag_swap = True
    
    while(flag_swap):
        flag_swap = False
        for indice in range(len_de_lista):
            if(lista_de_libros[indice][clave_buscada] > 
               lista_de_libros[indice +1 ][clave_buscada]):
                aux_valor = lista_de_libros[indice]
                lista_de_libros[indice] = lista_de_libros[indice +1]
                lista_de_libros[indice +1] = aux_valor
                flag_swap = True
        len_de_lista -= 1
    return lista_de_libros




# lista_de_libros_ordenada = ordenar_libros_por_clave(libros, clave_buscada= "título")
# print(lista_de_libros_ordenada)


# lista_de_libros_ordenada = ordenar_libros_por_clave(libros, clave_buscada= "autor")
# print(lista_de_libros_ordenada)


lista_de_libros_ordenada = ordenar_libros_por_clave(libros, clave_buscada= "año")
print(lista_de_libros_ordenada)