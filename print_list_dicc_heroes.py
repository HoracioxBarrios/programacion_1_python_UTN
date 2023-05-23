lista_personajes =\
[
  {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": 79.349999999999994,
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
    "altura": 122.77,
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
    "altura": 160.69999999999999,
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
    "altura": 170.78999999999999,
    "peso": "59.340000000000003",
    "genero": "F",
    "color_ojos": "Green",
    "color_pelo": "Auburn",
    "fuerza": "15",
    "inteligencia": "good"
  }]



def print_dicc_heroes(lista_heroes : list[dict]):
    '''
    imprime los heroes.
    recibe una lista de heroes.
    devuelve .no aplica
    '''
    for heroe in lista_heroes:
        mensaje = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}\n"
        mensaje = mensaje.format(heroe["nombre"],
                               heroe["identidad"],
                               heroe["empresa"],
                               heroe["altura"],
                               heroe["peso"],
                               heroe["genero"],
                               heroe["color_ojos"],
                               heroe["color_pelo"],
                               heroe["fuerza"],
                               heroe["inteligencia"])
        print(mensaje)
        
print_dicc_heroes(lista_personajes)      
        
