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
4-Crear un nuevo diccionario con los nombres y años de estreno de los animes 
de la lista:
'''

'''1-Generar una sublista de los animes estrenados antes de 1995:'''
#1
animes_antes_95 = []

for anime in animes_90s:
    if(anime["año"] < 1995):
        animes_antes_95.append(anime)

print(animes_antes_95)


'''2-Generar una sublista de los animes con más de 1 temporada:'''
#2
animes_mas_de_una_temp = []
for anime in animes_90s:
    if(anime["temporadas"] > 1):
        animes_mas_de_una_temp.append(anime)
print(animes_mas_de_una_temp)


'''3-Buscar en la lista el anime con nombre "Pokemon" e imprimir su año de estreno:'''
#3
for anime in animes_90s:
    if(anime["nombre"] == "Pokemon"):
        print("El anime: {0} se estrenó en el año: {1}".format(
            anime["nombre"], anime["año"]))



'''4-Crear un nuevo diccionario con los nombres y años de estreno de los animes 
de la lista:'''
#4
nueva_lista =[]
for anime in animes_90s: #recorro la lista y guardo en cada iteracion un elemento en la variable anime
    nuevo_dicc = {}
    if anime["nombre"] not in nuevo_dicc: #con el elemento si la key y su valor no estan en el nuevo diccionario. AGREGAMELO a nuevo diccionario
        nuevo_dicc["nombre"] = anime["nombre"]# agrega el nombre
        nuevo_dicc["año"] = anime["año"]# agrega el año
        nueva_lista.append(nuevo_dicc) #ese nuevo dicc agregalo a la nueva lista

print(nueva_lista)

''' ACA HAY QUE TENER EN CUENTA QUE NECESITAMOS  CREAR NUEVOS DICCIONARIOS VARIAS VECES para ir metiendo cada anime diferente en dicc diferentes.
Y SOLO NECESIRAMOS UNA NUEV LISTA. POR ESO LA LISTA SE DECLARA AFUERA DEL FOR.
si la Lista nueva se declara dentro del for se crearia una lista y dentro un dicc siempre EN CADA ITERACCION.
vasta con poner la declaracion de la nuevalista dentro del for para ver el problema'''


# nuevos_animes = []
# for anime in animes_90s:
#     nuevo_dicc = {}
#     if anime["nombre"] not in [a.get("nombre") for a in nuevos_animes]:
#         nuevo_dicc["nombre"] = anime["nombre"]
#         nuevo_dicc["año"] = anime["año"]
#         nuevos_animes.append(nuevo_dicc)
# print(nuevos_animes)