animes_90s = [
    {"nombre": "Dragon Ball Z", "año": 1989, "temporadas": 9, "personaje_principal": "Goku"},
    {"nombre": "Sailor Moon", "año": 1992, "temporadas": 5, "personaje_principal": "Usagi Tsukino"},
    {"nombre": "Pokemon", "año": 1997, "temporadas": 23, "personaje_principal": "Ash Ketchum"},
    {"nombre": "Digimon Adventure", "año": 1999, "temporadas": 1, "personaje_principal": "Tai Kamiya"},
    {"nombre": "Evangelion", "año": 1995, "temporadas": 1, "personaje_principal": "Shinji Ikari"}
]

'''
1-Generar una sublista de los animes estrenados antes de 1995:
2-Generar una sublista de los animes con más de 1 temporada:
3-Buscar en la lista el anime con nombre "Pokemon" e imprimir su año de estreno:
4-Crear un nuevo diccionario con los nombres y años de estreno de los animes de la lista:
'''


nuevo_diccionario={}
print(nuevo_diccionario)
for anime in animes_90s:
    #es la primera vez que creo esta clave
    if "temporadas" not in nuevo_diccionario:
        nueva_lista = []
        nueva_lista.append(anime["nombre"])
        nuevo_diccionario["temporadas"] = anime["temporadas"]
        nuevo_diccionario["nombres"] = nueva_lista
    elif nuevo_diccionario["temporadas"] == anime["temporadas"]:
        nuevo_diccionario["nombres"].append(anime["nombre"])
        
print(nuevo_diccionario)
