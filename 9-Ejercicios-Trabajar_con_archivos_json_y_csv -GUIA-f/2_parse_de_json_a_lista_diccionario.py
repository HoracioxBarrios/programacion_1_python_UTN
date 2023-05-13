
import json



def parse_json_a_lista_diccionary(nombre_archivo :str)-> list[dict]:
    '''
    Genera una lista de diccionarios a partir de un json
    Recibe: el path/nombre_archivo.json. (Desde donde toma los datos)
    devuelve una nueva list[dict]
    '''
    lista_heroes = []
    with open(nombre_archivo, "r") as archivo:
        nuevo_dicc = json.load(archivo)
        lista_heroes = nuevo_dicc["heroes"]
    return lista_heroes

lista_resultante = parse_json_a_lista_diccionary("9-Ejercicios-Trabajar_con_archivos_json_y_csv -GUIA-f\heroes_prueba.json")
print(lista_resultante)












#video CLASE_09 - PL01_PYTHON link: https://www.youtube.com/watch?v=65FcdtyIK4M   minutos: 1:38:38 / 2:26:00



'''para imprimir el json'''
# def parse_json(nombre_path_artchivo :str):
#     lista_heroes = []
#     with open(nombre_path_artchivo, "r") as archivo:
#         for heroe in archivo:
#             print(heroe, end="") #asi no imprime los saltos de linea