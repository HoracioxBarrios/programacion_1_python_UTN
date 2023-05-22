from functools import *

series = [


    {"nombre": "Dragon Ball Z", "año": 1989},


    {"nombre": "Sailor Moon", "año": 1992},


    {"nombre": "Pokemon", "año": 1997},


    {"nombre": "Digimon Adventure",
"año": 1999},


    {"nombre": "Yu Yu Hakusho", "año": 1992},


    {"nombre": "Neon Genesis Evangelion", "año": 1995},


    {"nombre": "One Piece", "año": 1999},


    {"nombre": "Rurouni Kenshin", "año": 1996}
]
# map reduce filter

def my_map(funcion, lista):
    lista_nueva = []

    for elemento in lista:
        elemento_mapeado = funcion(elemento)
        lista_nueva.append(elemento_mapeado)

    return lista_nueva



# lista_nombre = my_map(lambda serie : serie["nombre"], series)
# print(lista_nombre)

def my_reduce(funcion, lista):
    flag_primer_elemento = True
    for elemento in lista:
        if flag_primer_elemento:
            valor = elemento
            flag_primer_elemento = False
        else:
            valor = funcion(valor, elemento)
    return valor

a = [2,2,3]
print(my_reduce(lambda x,y : x + y, a))

def my_filter(funcion, lista):
    lista_filtrada = []
    for elemento in lista:
        if funcion(elemento):
            lista_filtrada.append(elemento)

    return lista_filtrada

print(my_filter(lambda numero: numero >2, a))

