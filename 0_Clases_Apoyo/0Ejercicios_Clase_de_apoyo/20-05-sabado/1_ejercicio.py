


'''
1.Obtener una lista con los nombres de todas las series de anime.
'''

series = [
    {"nombre": "Dragon Ball Z", "año": 1989},
    {"nombre": "Sailor Moon", "año": 1992},
    {"nombre": "Pokemon", "año": 1997},
    {"nombre": "Digimon Adventure", "año": 1999},
    {"nombre": "Yu Yu Hakusho", "año": 1992},
    {"nombre": "Neon Genesis Evangelion", "año": 1995},
    {"nombre": "One Piece", "año": 1999},
    {"nombre": "Rurouni Kenshin", "año": 1996}
    ]



nueva_lista_nombres = list(map(lambda serie: serie["nombre"], series))
print(nueva_lista_nombres)

#es necesario castear a list()
