import json
from data_prueba import lista_bzrp # me traigo la lista 


def generar_json(nombre_archivo : str, lista : list):
    '''
    Genera un archivo json a partir de una lista de diccionario.str
    Recibe:(arg 1) el path/nombre_archivo.json. (Donde se va a guardar)
    (arg2) recibe una lista de diccionarios.
    Retorna el archivo .json   
    '''
    nuevo_diccionario = {}
    nuevo_diccionario["lista_bzrp"] = lista
    with open(nombre_archivo, "w") as archivo:
        json.dump(nuevo_diccionario, archivo, indent= 4)
 
ruta_y_nombre = "9-Ejercicios-Trabajar_con_archivos_json_y_csv -GUIA-f\mi_bzrp_prueba.json"      
generar_json(ruta_y_nombre, lista_bzrp)