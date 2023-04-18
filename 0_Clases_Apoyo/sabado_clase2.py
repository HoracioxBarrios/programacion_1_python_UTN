"""LISTAS: le podemos guardar datos de cualquier tipo y es
dinamica: se puede agregar elementos, eliminar, ordenar y recorrer"""
#una forma de crear la lista:
mi_lista = []

#otra forma de crearla:
mi_lista_dos = list()

#verifico que sean del tipo list:
print(type(mi_lista))
print(type(mi_lista_dos))

#mostrar un elemento de una sublista. se debe agregar otro corchete al lado
lista_madre = [1, 2, ["a", "b", "c"], 4, 5]
print(lista_madre[2][1]) #obtengo "b"

#mostrar el ultimo elemento de la lista con -1:
print(lista_madre[-1]) #5

#inicio:final:paso (el valor de paso no se imprimiria o le aumento +1 a la pos que quiero)
print(lista_madre[0:3]) #del 0 al 2

#listas paralelas: se vinculan las listas por el indice, tienen que tener la misma cantidad de elementos
lista_paralela_1 = [1,2,3]
lista_paralela_2 = ["a","b","c"]

#recorrer las listas usando FOR i IN range(cantidad de elementos):
for i in range(len(lista_paralela_1)):
    #deberia mostrar 1 con "a", 2 con "b" y 3 con "c"
    print("nota: {0} - letra: {1}".format(lista_paralela_1[i], lista_paralela_2[i]))
    
"""DICCIONARIOS"""
#crear un diccionario {clave:valor}:
diccionario = {
    "clave1": "valor1",
    "clave2": "valor2"
}

#para agregar un nuevo elemento al dict:
diccionario["clave3"] = "valor3"

#modificar el valor de una clave:
diccionario["clave3"] = "valor modificado"

#mostrar el diccionario con el elemento agregado y modificado:
print(diccionario)

#preguntar si un determinado elemento existe en el dict:
if "clave2" in diccionario: #esta clave ("clave2") existe en(in) DICCIONARIO:
    print(True)
else:
    print(False)
    
    
"""TUPLAS: son inmutables, no se pueden modificar
se declaran con parentesis"""

#creando una tupla con tuple()
tupla = tuple(["dato1", "dato2"])

#creando una tupla con parentesis
tupla_dos = ("dato3", "dato4")

"""SET: coleccion de elementos sin elementos repetidos, si tiene elementos repetidos
los elimina o los omite a la hora de mostrarlo"""
#creardo el set con set()
mi_set = set([1,2,2,3,3,3,3,4,5])

#muestra 1,2,3,4,5 (eliminando los repetidos)
print(mi_set)


"""LISTA DE DICCIONARIOS"""
#lista de diccionarios
animes_90s = [
    {"nombre": "Dragon Ball Z", "año": 1989, "temporadas": 9, "personaje_principal": "Goku"},
    {"nombre": "Sailor Moon", "año": 1992, "temporadas": 5, "personaje_principal": "Usagi Tsukino"},
    {"nombre": "Pokemon", "año": 1997, "temporadas": 23, "personaje_principal": "Ash Ketchum"},
    {"nombre": "Digimon Adventure", "año": 1999, "temporadas": 1, "personaje_principal": "Tai Kamiya"},
    {"nombre": "Evangelion", "año": 1995, "temporadas": 1, "personaje_principal": "Shinji Ikari"}
]

#imprimir cada elemento de la lista (cada diccionario):
for anime in animes_90s: #por cada anime que SE ENCUENTRA EN animes_90s
    print(anime)
    
#imprimir "nombre" de cada elemento de la lista:
for anime in animes_90s:
    print(anime["nombre"])
    
#si quiero obtener el indice/tamaño/cantidad de elemntos de la lista uso el range:
for i in range(len(animes_90s)):
    print(i)
    
#mostrar la serie si tiene mas de una temporada:
temporadas = []
for anime in animes_90s:
    if anime["temporadas"] > 1:
        temporadas.append(anime["nombre"])
print(temporadas)

#para "agrupar" diccionarios se deben crear una sublista:
#ej: quiero "agrupar" los animes que tienen mas de 3 temporadas -> se crea una lista


