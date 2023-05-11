import json
# fue requerida en el ejercicio stark 05 (stark 3 para nosostros en realidad)

def leer_archivo_json(path_completo: str) -> list[dict]:
    '''
    De un archivo json, crea una lista de diccionarios
    Recibe la ruta del archivo
    devuelve una lista de diccionarios
    '''
    with open(path_completo, 'r') as archivo: # r = solo lectura
        archivo_json = json.load(archivo) # trae el json  lo guarda en archivo_json
        archivo_lista_dict = archivo_json['heroes'] #accedemos a la clave y traemos lo que esta dentro que es la lista de diccionarios
        return archivo_lista_dict
    


lista_de_heroes = leer_archivo_json("9-Ejercicios-Trabajar_con_archivos_json_y_csv -GUIA-f\data_stark.json")
print(lista_de_heroes)


''' Otras versiones'''

# def leer_archivo_json(path_completo: str) -> list[dict]:
#     '''
#     De un archivo json, crea una lista de diccionarios
#     Recibe la ruta del archivo
#     devuelve una lista de diccionarios
#     '''
#     with open(path_completo, 'r') as archivo: # r = solo lectura
#         archivo_json = json.load(archivo)
#         archivo_dict = dict(archivo_json)
#         archivo_lista_dict = archivo_dict['heroes']
#         return archivo_lista_dict
'''

Esta función llamada "leer_archivo_son" toma la ruta completa de un 
archivo JSON como argumento y devuelve una lista de diccionarios. 
El objetivo de esta función es leer el contenido de un archivo JSON 
y convertirlo en una lista de diccionarios.

Aquí está cómo funciona el código paso a paso:

La función recibe la ruta completa del archivo JSON como argumento: 
path_completo.
Se abre el archivo usando la función open en modo de solo lectura 
('r').
El contenido del archivo se carga utilizando la función
json.load(archivo). Esto devuelve una representación de Python 
del archivo JSON, que es generalmente una combinación de listas 
y diccionarios.
El contenido cargado se convierte en un diccionario utilizando 
dict(archivo_json).
Se accede a la lista de diccionarios dentro del diccionario 
utilizando la clave 'heroes' (suponiendo que esa es la estructura 
del archivo JSON).
La lista de diccionarios se devuelve como resultado de la función.
En resumen, esta función lee un archivo JSON, extrae la lista de 
diccionarios contenidos en él y la devuelve como resultado.
'''

#Version mas larga , pero paso a paso
# def leer_archivo_json(path_completo : str)-> list[dict]:
#     '''
#     De un archivo json, crea una lista de diccionarios
#     Recibe la ruta del archivo
#     devuelve una lista de diccionarios
#     '''
#     with open(path_completo, "r") as archivo:
#         archivo_json = json.load(archivo) # cargamos y guardamos el json
#         nuevo_archivo_diccionario = {}
#         nuevo_archivo_diccionario = archivo_json
#         nuevo_archivo_lista = []
#         nuevo_archivo_lista = nuevo_archivo_diccionario["heroes"]
#         return nuevo_archivo_lista

# # ejemplo del profe
# def leer_archivo(path_completo: str) -> list[dict]:
#     with open(path_completo, 'r') as archivo: # r = solo lectura
#         archivo_json = json.load(archivo)
#         archivo_dict = dict(archivo_json)
#         archivo_lista_dict = archivo_dict['heroes']
#         return archivo_lista_dict

#     # with open(path_completo, 'r') as archivo:
#     #     return list[dict](json.load(archivo)['heroes'])


# fin 1.4 ---------------------------------------------------------------  