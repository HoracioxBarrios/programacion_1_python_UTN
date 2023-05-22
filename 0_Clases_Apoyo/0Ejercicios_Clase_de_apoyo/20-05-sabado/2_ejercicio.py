

'''
2. Obtener las series de anime lanzadas
después de 1995.
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




nueva_lista_series_despues_95 = list(filter(
    lambda serie : serie["año"] > 1995,series))

print(nueva_lista_series_despues_95)