
lista_bzrp = [{'title': 'QUEVEDO || BZRP Music Sessions #52', 'views': 227192970, 'length': 204, 'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg', 'url': 'https://youtube.com/watch?v=A_g3lMcWVy0', 'date': '2022-07-06 00:00:00'}, 
              {'title': 'VILLANO ANTILLANO || BZRP Music Sessions #51', 'views': 112947399, 'length': 188, 'img_url': 'https://i.ytimg.com/vi/wvz97-lNPH8/sddefault.jpg', 'url': 'https://youtube.com/watch?v=wvz97-lNPH8', 'date': '2022-06-08 00:00:00'}, 
              {'title': 'PAULO LONDRA || BZRP Music Sessions #23', 'views': 101654971, 'length': 258, 'img_url': 'https://i.ytimg.com/vi/WkgHkrM9fo0/sddefault.jpg', 'url': 'https://youtube.com/watch?v=WkgHkrM9fo0', 'date': '2022-04-25 00:00:00'}]

def calcular_tema_mas_largo(lista_bzrp):
    #maximo_largo
    for indice in range(len(lista_bzrp)):
        if(
        indice == 0 or lista_bzrp[maximo_indice]["length"] < lista_bzrp[indice]["length"]):
            maximo_indice = indice
    print("El tema de mayor duracion es: {0} con: {1}\n".format(
        lista_bzrp[maximo_indice]["title"], lista_bzrp[maximo_indice]["length"]))
    

# calcular_tema_mas_largo(lista_bzrp)



lista_de_heroes =\
[{
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  },
  {
    "nombre": "Rocket Raccoon",
    "identidad": "Rocket Raccoon",
    "empresa": "Marvel Comics",
    "altura": "122.77",
    "peso": "25.73",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Brown",
    "fuerza": "5",
    "inteligencia": "average"
  },
  {
    "nombre": "Wolverine",
    "identidad": "Logan",
    "empresa": "Marvel Comics",
    "altura": "160.69999999999999",
    "peso": "135.21000000000001",
    "genero": "M",
    "color_ojos": "Blue",
    "color_pelo": "Black",
    "fuerza": "35",
    "inteligencia": "good"
  },
  {
    "nombre": "Black Widow",
    "identidad": "Natasha Romanoff",
    "empresa": "Marvel Comics",
    "altura": "170.78999999999999",
    "peso": "59.340000000000003",
    "genero": "F",
    "color_ojos": "Green",
    "color_pelo": "Auburn",
    "fuerza": "15",
    "inteligencia": "good"
  },
  {
    "nombre": "Mystique",
    "identidad": "Raven Darkholme",
    "empresa": "Marvel Comics",
    "altura": "178.65000000000001",
    "peso": "54.960000000000001",
    "genero": "F",
    "color_ojos": "Yellow (without irises)",
    "color_pelo": "Red / Orange",
    "fuerza": "15",
    "inteligencia": "good"
  },
  {
    "nombre": "Spider-Man",
    "identidad": "Peter Parker",
    "empresa": "Marvel Comics",
    "altura": "178.28",
    "peso": "74.25",
    "genero": "M",
    "color_ojos": "Hazel",
    "color_pelo": "Brown",
    "fuerza": "55",
    "inteligencia": "high"
  },
  {
    "nombre": "Storm",
    "identidad": "Ororo Munroe",
    "empresa": "Marvel Comics",
    "altura": "180.72",
    "peso": "57.5",
    "genero": "F",
    "color_ojos": "Blue",
    "color_pelo": "White",
    "fuerza": "10",
    "inteligencia": "good"
  },
  {
    "nombre": "Gamora",
    "identidad": "Gamora Zen Whoberi Ben Titan",
    "empresa": "Marvel Comics",
    "altura": "183.65000000000001",
    "peso": "77.769999999999996",
    "genero": "F",
    "color_ojos": "Yellow",
    "color_pelo": "Black",
    "fuerza": "85",
    "inteligencia": "good"
  },
  {
    "nombre": "Thing",
    "identidad": "Ben Grimm",
    "empresa": "Marvel Comics",
    "altura": "183.55000000000001",
    "peso": "225.41999999999999",
    "genero": "M",
    "color_ojos": "Blue",
    "color_pelo": "No Hair",
    "fuerza": "85",
    "inteligencia": "good"
  }]



def heroe_segun_altura_genero_v2(lista_heroes: list, genero: str, min_max: str) -> None:
    heroe_aux = {}
    for heroe in lista_heroes:
        if not heroe_aux and (heroe['genero'] == genero):# en la primera iteracion, guarda el primero
            heroe_aux = heroe
        if (heroe_aux and heroe['genero'] == genero):
            if ((min_max == 'Bajo' and float(heroe['altura']) < float(heroe_aux['altura'])) or 
                (min_max == 'Alto' and float(heroe['altura']) > float(heroe_aux['altura']))):
                    heroe_aux = heroe

    print(f"Nombre: {heroe_aux['nombre']} - Altura: {heroe_aux['altura']} mts.")

heroe_segun_altura_genero_v2(lista_de_heroes, genero="M", min_max="Alto")   