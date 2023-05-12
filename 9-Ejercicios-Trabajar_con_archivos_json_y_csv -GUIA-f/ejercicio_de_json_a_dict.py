
import json # con esta libreria podemos generar la lista de diccionarios
def parse_json(nombre_path_artchivo :str)-> list[dict]:
    '''
    genera una lista de diccionarios a partir de un json
    recibe 1 argumento: la ruta con el nombre y su extencion .json.
    devuelve una nueva list[dict]
    '''
    lista_heroes = []
    with open(nombre_path_artchivo, "r") as archivo:
        nuevo_dicc = json.load(archivo)
        lista_heroes = nuevo_dicc["heroes"]
    return lista_heroes

lista_resultante = parse_json("9-Ejercicios-Trabajar_con_archivos_json_y_csv -GUIA-f\heroes_prueba.json")
print(lista_resultante)












#video CLASE_09 - PL01_PYTHON link: https://www.youtube.com/watch?v=65FcdtyIK4M   minutos: 1:38:38 / 2:26:00



'''para imprimir el json'''
# def parse_json(nombre_path_artchivo :str):
#     lista_heroes = []
#     with open(nombre_path_artchivo, "r") as archivo:
#         for heroe in archivo:
#             print(heroe, end="") #asi no imprime los saltos de linea