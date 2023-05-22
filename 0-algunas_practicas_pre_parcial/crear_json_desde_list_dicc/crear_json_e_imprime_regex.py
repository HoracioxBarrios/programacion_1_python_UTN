import json
import re
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

def crear_archivo_json(lista_heroes : list[dict], nombre_path : str):
    nuevo_diccionario = {}
    nuevo_diccionario["heroes"] = lista_heroes
    with open(nombre_path, "w") as archivo:
        json.dump(nuevo_diccionario, archivo, indent= 4)
        nombre = 
        nombre = re.findall(r"[a-z_A-Z]+\.json$", nombre_path)
        nombre = "".join(nombre)
        print("Se creó el archivo {0}".format(nombre))

crear_archivo_json(lista_personajes, "0-algunas_practicas_pre_parcial\crear_json_desde_list_dicc\mi_primer_archivo.json")