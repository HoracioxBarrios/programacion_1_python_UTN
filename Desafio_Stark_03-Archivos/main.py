import re
import json

#1.1
def print_dato(palabra : str):
    '''
    imprime un dato
    recibe una cadena str
    devuelve - no aplica
    '''
    print("{0}".format(palabra))

def imprimir_menu_desafio_5():
    lista = ["A- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M",
             "B- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F",
             "C- Recorrer la lista y determinar cuál es el superhéroe más alto de género M ",
             "D- Recorrer la lista y determinar cuál es el superhéroe más alto de género F ",
             "E- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M ",
             "F- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F ",
             "G- Recorrer la lista y determinar la altura promedio de los  superhéroes de género M",
             "H- Recorrer la lista y determinar la altura promedio de los  superhéroes de género F",
             "I- Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)",
             "J- Determinar cuántos superhéroes tienen cada tipo de color de ojos.",
             "K- Determinar cuántos superhéroes tienen cada tipo de color de pelo.",
             "L- Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). ",
             "M- Listar todos los superhéroes agrupados por color de ojos.",
             "N- Listar todos los superhéroes agrupados por color de pelo.",
             "O- Listar todos los superhéroes agrupados por tipo de inteligencia",
             "Z- Salir"]
    
    for item in lista:
        print_dato(item)
        
imprimir_menu_desafio_5()



# 1.2
def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    respuesta = input('Ingrese una opción: ').upper()
    if re.match('^[A-OZ]{1}$', respuesta):
        return respuesta
    return -1

# 1.4
def leer_archivo(path_completo: str) -> list[dict]:
    # with open(path_completo, 'r') as archivo:
    #     archivo_json = json.load(archivo)
    #     archivo_dict = dict(archivo_json)
    #     archivo_lista_dict = archivo_dict['heroes']
    #     return archivo_lista_dict
    with open(path_completo, 'r') as archivo:
        return list[dict](json.load(archivo)['heroes'])