import json

def leer_archivo_json(nombre_path : str)-> list[dict]:
    with open(nombre_path, "r") as archivo:
        lista_heroe = json.load(archivo)
        return lista_heroe["heroes"]

lista_heroes = leer_archivo_json("0-algunas_practicas_pre_parcial\leer_json_a_list_dicc\data_stark.json")
print(lista_heroes)