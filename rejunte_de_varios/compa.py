import json
# import csv
import pprint
import re
# def imprimir_dato(dato):
#     if type(dato) == str:
#         print(dato)
# def menu_opciones():
#     menu = "1-LISTAR CANTIDAD DE HEROES REQUERIDO\n\
#             2-ORDENAR Y LISTAR HEROES POR ALTURA\n\
#             3-ORDENAR Y LISTAR HEROES POR FUERZA\n\
#             4-CALCULAR PROMEDIO DE DATOS DE LOS HEROES\n\
#             5-BUSCAR HEROES POR INTELIGENCIA\n\
#             6-EXPORTAR ARCHIVO CSV DE OPCIONES ANTERIORES"
#     return menu
# def pedir_opciones():
#     imprimir_dato(menu_opciones)
#     cadena = input("Ingresa la opcion deseada: ")
#     if re.search(r"^[1-6]{1}$",cadena):
#         opcion_validada = cadena
#         return opcion_validada
#     else:
#         imprimir_dato("ingresa la opcion deseada")
# def control_funciones(lista):
#     while(True):
#         opcion = pedir_opciones()
#         match(opcion):
#             case "1":
#                 while(True):

#                     cantidad = input("Ingresa la cantidad de heroes a listar: ")
#                     if re.match(r"[aA-zZ]+",cantidad) or int(cantidad) > len(lista_personajes):
#                         imprimir_dato("el numero ingresado exede la cantidad de heroes")
#                     else:
#                         cantidad_int = int(cantidad)
#                         break
#                 imprimir_dato(listar_heroes(lista_personajes,cantidad_int))
#                 break
#             case "2":
#                 while(True):
#                     clave_ingresada = input("ingrese el dato a calcular altura|peso|fuerza: ")
#                     # if re.search(r"altura|peso|fuerza",clave_ingresada):
#                     #     validacion_clave = clave_ingresada
#                     # else:
#                     #     imprimir_dato("Error: ingrese como se le indica")
#                     orden_ingresado = input("Ingresa desc|asc dependiendo del orden que requiera: ")
#                     # if re.search(r"desc|asc",orden_ingresado):
#                     #     validacion_orden = orden_ingresado
#                     # else:
#                     #     imprimir_dato("Error: ingrese como se le indica")

#                     # imprimir_dato(ordenar_listar_heroes_altura(lista_personajes,validacion_clave,validacion_orden))
#                     imprimir_dato(ordenar_listar_heroes_altura(lista_personajes,clave_ingresada,orden_ingresado))

#             case "3":
#                 pass
#             case "4":
#                 pass
#             case "5":
#                 pass
#             case "6":
#                 pass
#             case "7":
#                 break
                
def stark_normalizar_datos(lista_heroes:list)->list:
    """
    recibe como parametro una lista
    se castea las claves que tengan string numericos de los diccionarios dentro de la lista
    se imprime por panatalla datos normalizados
    retorna la lista con las claves actualizadas
    """
    if len(lista_heroes) == 0:
        print("Error: lista vacia")
    else:
        flag = False
        for heroes in lista_heroes:
            if type(heroes["altura"]) != float:
                heroes["altura"] = float(heroes["altura"])
                flag = True
            
            if type(heroes["peso"]) != float:
                heroes["peso"] = float(heroes["peso"])
                flag = True

            if type(heroes["fuerza"]) != int:
                heroes["fuerza"] = int(heroes["fuerza"])
                flag = True
        # if flag ==True:
            # imprimir_dato("datos normalizados")
    return lista_heroes


def leer_archivo(ruta_archivo:str):
    with  open(ruta_archivo,"r") as archivo:
        dicionario = json.load(archivo)
        return dicionario["heroes"]
    
ruta =r"C:\Users\Usuario\OneDrive\Escritorio\desafio #6 strak\data_stark.json"
leer_archivo(ruta)
# leer_archivo(r"C:\Users\Usuario\OneDrive\Escritorio\desafio 5 stark\data_stark.json")
lista_personajes = stark_normalizar_datos(leer_archivo(ruta))
# def guardar_archivo(nombre_ruta:str,guardar:dict):
#     flag = False
# #     lista = []
#     with open(nombre_ruta,"w+") as archivo_stark:
#         json.dump(guardar,archivo_stark)
#         flag = True
#         print("Se creo el archivo {0}".format(nombre_ruta))
#     if flag == False:
#         print("Error al crear archivo: {0}".format(nombre_ruta))
#     return flag
# print(guardar_archivo())
#1 Listar los primeros N héroes. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)
def listar_heroes(lista_heroes:list,cantidad)->list:
    lista_heroes_copia = lista_heroes[:]
    lista_nueva = []
    for indice in range(int(cantidad)):
            lista_nueva.append(lista_heroes_copia[indice]["nombre"])

    return lista_nueva
# cantidad = int(input("ingrese un numero: "))
# print(listar_heroes(lista_personajes,cantidad))
def obtener_nombre_dato(heroe,dato):
    return "Nombre: {0}|{1}: {2}".format(heroe["nombre"],dato,heroe[dato])

# print(obtener_nombre_dato(lista_personajes[1],lista_personajes["altura"]))
# Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
def ordenar_listar_heroes_altura(lista_heroes,key,orden):
    lista_heroes_copia = lista_heroes[:]
    lista_nombre_altura = []
    rango = len(lista_heroes_copia) -1
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        for indice in range(rango):
            if orden == "asc" and lista_heroes_copia[indice][key] > lista_heroes_copia[indice+1][key] \
               or orden == "desc" and lista_heroes_copia[indice][key] < lista_heroes_copia[indice+1][key]:
                lista_heroes_copia[indice],lista_heroes_copia[indice+1] = lista_heroes[indice+1],lista_heroes[indice]
                flag_swap = True
    for heroes in lista_heroes_copia:
           lista_nombre_altura.append(obtener_nombre_dato(heroes,key))      
    return lista_nombre_altura
# print(ordenar_listar_heroes_altura(lista_personajes,"altura","asc"))
# Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
def ordenar_listar_heroes_fuerza(lista_heroes,key,orden):
    return ordenar_listar_heroes_altura(lista_heroes,key,orden)
# print(ordenar_listar_heroes_fuerza(lista_personajes,"fuerza","desc"))
# print(ordenar_listar_heroes_fuerza(lista_personajes,"fuerza"))


# Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el 
# promedio (preguntar al usuario la condición: ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que cumplan
# con ser mayores o menores según corresponda.
def calcular_promedio(lista_heroes,key,dato):
    lista_heroes_copia = lista_heroes[:]
    lista_promedio = []
    # lista_mayor_promedio = []
    suma = 0
    for heroes in lista_heroes_copia:
        suma += heroes[key]
    promedio = suma / len(lista_heroes_copia)
    for heroes in lista_heroes_copia:
        if dato == "menor" and heroes[key] < promedio or dato == "mayor" and heroes[key] > promedio:
            lista_promedio.append(obtener_nombre_dato(heroes,key))
    print(promedio)

    return lista_promedio


# print(calcular_promedio(lista_personajes,"fuerza","mayor"))
#  Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda. (Usando RegEx)
def listar_heroes_por_inteligencia(lista_heroes,dato):
    lista_heroes_copia = lista_heroes[:]
    if not lista_heroes_copia:
        return -1
    else:
        lista_inteligencia = []
        for heroe in lista_heroes_copia:
            if heroe["inteligencia"] == dato:
                lista_inteligencia.append(obtener_nombre_dato(heroe,"inteligencia"))
        return lista_inteligencia     
# print(listar_heroes_por_inteligencia(lista_personajes,"good"))

#  Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]
def exportar_archivo_csv(lista_pasada,nombre_archivo):
    
    with open(nombre_archivo,"w") as archivo:
        for heroes in lista_pasada:
            dato = "{0},{1},{2},{3},{4},{5} \n".format(heroes["nombre"],heroes["identidad"],heroes["empresa"],heroes["altura"],heroes["peso"],heroes["genero"])
            archivo.write(dato)
        # return  archivo
# exportar_archivo_csv(lista_personajes,"lista_inteligencia.csv")

def exportar_archivo_csv_dos(lista_pasada,nombre_archivo):
    dato = ""
    with open(nombre_archivo,"w") as archivo:
        for heroes in lista_pasada:
            valores =  heroes.values()
            for valor in valores:
                # print(valor)
                dato += "{0},".format(valor)
            # dato = "-".join(valores)
            print(dato)
            # print(valores)
            archivo.write(dato)
        # return  archivo
exportar_archivo_csv_dos(lista_personajes,"lista_inteligencia.csv")
# def exportar_archivo(lista_pasada):
#     # with open(nombre_archivo,"w") as archivo:
#         lista = []
#         for heroes in lista_pasada:
#                 lista.append(str(heroes))
#                 # archivo.write(dato)
#         print(lista)
#         # return archivo
#             # print(heroes[clave])

# print(exportar_archivo(lista_personajes))

# Aclaraciones:
# Los puntos deben ser accedidos mediante un menú. Para todas las opciones, validar lo ingresado por consola con RegEx
# El set de datos proviene de un json
# Realizar las validaciones que crea pertinentes
# En todos los casos se deberá trabajar con una copia de la lista original
# control_funciones(lista_personajes)
