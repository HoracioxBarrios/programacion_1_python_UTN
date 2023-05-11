import os
import re
import json

# por el profe facu
def clear_console() -> None:
    """
    Espera a que el usuario presione enter
    para borrar la consola y volver a mostrar lo apropiado.
    """
    _ = input('Press a key to continue...')
    os.system('cls')
    
#pertenece al strark 2
def print_dato(palabra : str):
    '''
    imprime un dato
    recibe una cadena str
    devuelve - no aplica
    '''
    print("{0}".format(palabra))
    
#1.1--------------------------------- print Menu
def imprimir_menu_desafio_5():
    '''
    imprime un menu de opciones
    recibe- no aplica
    devuelve - no aplica
    '''
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
        
# 1.2---------------------# toma de la eleccion del usuario para el menu
def stark_menu_principal_desafio_5(): 
    '''
    imprime el menu y toma una opcion del usuario
    recibe -no aplica
    devuelve la opcion elegida, en caso de False devuelve -1
    '''
    imprimir_menu_desafio_5()
    respuesta = input('Ingrese una opción: ').upper()
    if re.match('^[A-OZ]{1}$', respuesta):
        return respuesta
    else:
        return -1

#1.3 ------------------------------- 
def  stark_marvel_app_5(lista_de_personajes):
    while(True):
        imprimir_menu_desafio_5()
        respuesta = stark_menu_principal_desafio_5()
        match(respuesta):
            case "A":
                print("usted ingreso la A")
            case "B":
                print(lista_de_personajes)
            case "C":
                pass
            case "D":
                pass
            case "E":
                pass
            case "F":
                pass
            case "G":
                pass
            case "H":
                pass
            case "I":
                pass
            case "J":
                pass
            case "K":
                pass
            case "L":
                pass
            case "M":
                pass
            case "N":
                pass
            case "O":
                pass
            case "Z":
                break
            case other:
                print("Opcion incorrecta")
        clear_console()


# 1.4 -------------------------------------- Generar Lista a partir de json
def leer_archivo_json(path_completo: str) -> list[dict]:
    '''
    De un archivo json, crea una lista de diccionarios heroes
    Recibe la ruta del archivo
    devuelve una lista de diccionarios
    '''
    with open(path_completo, 'r') as archivo: # r = solo lectura
        archivo_json = json.load(archivo)
        archivo_lista_dict = archivo_json['heroes'] #accedemos a la clave y traemos lo que esta dentro
        return archivo_lista_dict
    
# leer_archivo_json("Desafio_Stark_03-Archivos\data_stark.json") # se usa en main.py
lista_de_heroes_en_crudo_str = leer_archivo_json("Desafio_Stark_03-Archivos\data_stark.json")


#------------------------------------------------------------------------------------
# Voy a usar Normalizar datos para poder calcular maximos, minimos

def stark_normalizar_datos(heroes: list[dict]) -> list[dict]:
    '''
    normaliza los datos
    recibe una list[dict] personajes
    devuelve una nueva lista de dicc con datos normalizados    
    '''
    result_nueva_lista = []
    if heroes:
        for heroe in heroes:
            keys = list(heroe.keys())
            for key in keys:
                if type(heroe[key]) is str:
                    valor_reemplazado: str = heroe[key].replace('.', '')
                    if valor_reemplazado.isnumeric() and type(heroe[key]) is str:
                        if '.' in heroe[key] and heroe[key].count('.') == 1:
                            heroe[key] = float(heroe[key])
                        else:
                            heroe[key] = int(heroe[key])
                        print(
                            "El dato {0} fue modificado en el heroe {1}".format(key, heroe["nombre"]))
            result_nueva_lista.append(heroe)
        return result_nueva_lista
    else:
        return "La lista esta Vacia"
    
lista_de_heroes = stark_normalizar_datos(lista_de_heroes_en_crudo_str)
#1.5------------------------------------------
'''
Crear la función 'guardar_archivo' la cual recibirá por parámetro un
string que indicará el nombre con el cual se guardará el archivo junto
con su extensión (ejemplo: 'archivo.csv') y como segundo parámetro
tendrá un string el cual será el contenido a guardar en dicho archivo.
Debe abrirse el archivo en modo escritura+, ya que en caso de no
existir, lo creara y en caso de existir, lo va a sobreescribir La función
debera retornar True si no hubo errores, caso contrario False, además
en caso de éxito, deberá imprimir un mensaje respetando el formato:
.Se creó el archivo: nombre_archivo.csv
En caso de retornar False, el mensaje deberá decir: ‘Error al crear el
archivo: nombre_archivo’
'''
def guardar_archivo(nombre_archivo_csv: str, lista: list[dict]) -> bool:
    ''' 
    genera un archivo csv de heroes a partir de una lista de diccionarios
    Recibe: (arg 1)Recibe un str con la ruta con el nombre y extencion de archivo 
    ejemplo: csv, (arg 2) Recibe una lista de dict
    Devuelve: un archivo csv, y un valor True si se genero corrctamente,
    caso contrario False
    '''
    try:
        with open(nombre_archivo_csv, "w+") as archivo:
            for heroe in lista:
                linea = "{0}, {1}, {2}, {3}, {4}, {5},{6}, {7}, {8}, {9}"
                linea = linea.format(
                    heroe["nombre"],
                    heroe["identidad"],
                    heroe["empresa"],
                    heroe["altura"],
                    heroe["peso"],
                    heroe["genero"],
                    heroe["color_ojos"],
                    heroe["color_pelo"],
                    heroe["fuerza"],
                    heroe["inteligencia"]
                )
                archivo.write(linea + "\n")  # Escribir la línea en el archivo con un salto de línea
        print("Se creó el archivo: {0}".format(nombre_archivo_csv))
        return True
    except Exception as e:
        print("Error al crear el archivo: {0}".format(nombre_archivo_csv))
        print(str(e))
        return False

    
# lista_de_heroes = leer_archivo_json("Desafio_Stark_03-Archivos\data_stark.json")
# ruta_csv = "Desafio_Stark_03-Archivos\data_stark.csv"
# print(guardar_archivo(ruta_csv, lista_de_heroes))

#1.6 --------------------------------------------------------------------
'''
Crear la función 'capitalizar_palabras' la cual recibirá por parámetro un
string que puede contener una o muchas palabras. La función deberá
retornar dicho string en el cual todas y cada una de las palabras que
contenga, deberán estar capitalizadas (Primera letra en mayúscula).
'''
frase = "dicho string en el cual todas y cada una de las palabras"

def capitalizar_palabras(cadena: str) -> str:
    '''
    capitaliza palabras
    Recibe una cadena str.
    devuelve dicho string en el cual todas y cada una de las palabras 
    que contenga, deberán estar capitalizadas.
    '''
    lista_palabras = cadena.split()
    lista_palabras_capitalizadas = []
    for palabra in lista_palabras:
        palabra_capitalizada = palabra.capitalize()
        lista_palabras_capitalizadas.append(palabra_capitalizada)
    return ' '.join(lista_palabras_capitalizadas)


# print(capitalizar_palabras(frase))

#1.7--------------------------------------------------------------------
'''
Crear la función 'obtener_nombre_capitalizado' la cual recibirá por
parámetro un diccionario el cual representará a un héroe y devolverá
un string el cual contenga su nombre formateado de la siguiente
manera:
Nombre: Venom
Reutilizar 'capitalizar_palabras'
'''
#Ejemplo de heroe
heroe_dicc = {
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
    }

def obtener_nombre_capitalizado(diccionario_heroe : dict)-> str:
    '''
    obtiene el nombre del heroe, capitalizado.
    recibe un diccionario.
    devuelve un str.
    '''
    nombre_origen = "Nombre: {0}".format(diccionario_heroe["nombre"])
    nombre_capitalized = capitalizar_palabras(nombre_origen)
    return nombre_capitalized


# nombre = obtener_nombre_capitalizado(heroe_dicc)
# print(nombre)

#1.8-----------------------------------------------------------
'''
Crear la función 'obtener_nombre_y_dato' la cual recibirá por
parámetro un diccionario el cual representará a un héroe y una key
(string) la cual representará la key del héroe a imprimir. La función
devolverá un string el cual contenga el nombre y dato (key) del héroe a
imprimir.
El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.
El string resultante debe estar formateado al estilo: (suponiendo que la
key es fuerza)
Nombre: Venom | Fuerza: 500
Reutilizar 'obtener_nombre_capitalizado'
'''
#del stark 2- pero lo mejoré, ya no recorre con un for, sino que verifica si esta en el dict
def obtener_nombre_y_dato_v2(diccionario_heroe: dict, clave_buscada: str) -> str:
    '''
    Obtiene el nombre del héroe y un dato específico.
    Recibe un diccionario y una clave (por ejemplo: "altura", "fuerza", "peso").
    Devuelve una cadena formateada.
    '''
    if clave_buscada in diccionario_heroe:
        nombre_capitalizado = obtener_nombre_capitalizado(diccionario_heroe)
        return "{0} | {1}: {2}".format(nombre_capitalizado,clave_buscada,
            diccionario_heroe[clave_buscada]
        )
    else:
        return "Dato no encontrado para el héroe."

# nombre__dato_buscado = obtener_nombre_y_dato_v2(heroe_dicc, clave_buscada="fuerza")
# print(nombre__dato_buscado)

#segunda parte 
#2.1 -----------------------------------------------------
'''
Crear la función 'es_genero' la cual recibirá por parámetro un
diccionario que representará un héroe y un string el cual será usado
para evaluar si el héroe coincide con el género buscado (El string
puede ser M, F o NB). retornará True en caso de que cumpla, False
caso contrario.
'''
def es_genero(diccionario_heroe : dict, valor_genero : str)-> bool:
    '''
    verifica si el heroe es del genero buscado.
    recibe un diccionario heroe.
    devuelve un boolean
    '''
    return diccionario_heroe["genero"] == valor_genero
 
# print(es_genero(heroe_dicc, valor_genero="M"))

#2.2 ----------------------------------------------------
'''
2.2. Crear la función 'stark_guardar_heroe_genero' la cual recibira por
parámetro la lista de héroes y un string el cual representará el género
a evaluar (puede ser M o F). Deberá imprimir solamente los héroes o
heroínas que coincidan con el género pasado por parámetro y
además, deberá guardar dichos nombres en un archivo con extensión
csv (cada nombre deberá ir separado por una coma)
Reutilizar las funciones 'es_genero', 'obtener_nombre_capitalizado',
'imprimir_dato' y 'guardar_archivo'.
En el caso de 'guardar_archivo', cuando se llame a esta función el
nombre de archivo a guardar deberá respetar el formato:
heroes_M.csv, heroes_F.csv o heroes_NB según corresponda.
La función retornará True si pudo guardar el archivo, False caso
contrario
'''
def stark_guardar_heroe_genero(lista_de_heroes: list[dict], genero_buscado: str):
    '''
    crea un csv con los heroes que cumplen con el genero elegido
    recibe una lista de heroes
    revuelve un archivo csv
    '''
    genero_csv = ""
    if genero_buscado == "M":
        genero_csv = "M"
    elif genero_buscado == "F":
        genero_csv = "F"
        
    lista_heroes_genero = []
    for heroe in lista_de_heroes:
        es_el_mismo_genero = es_genero(heroe, genero_buscado)
        if es_el_mismo_genero:
            nombre_capitalized = obtener_nombre_capitalizado(heroe)
            heroe["nombre"] = nombre_capitalized
            lista_heroes_genero.append(heroe)
    name_path_archivo_genero = "Desafio_Stark_03-Archivos\heroes_{0}.csv".format(genero_csv)
    se_guardo = guardar_archivo(name_path_archivo_genero, lista_heroes_genero)
    return se_guardo
                 

# resultado_genero_csv = stark_guardar_heroe_genero(lista_de_heroes, genero_buscado="F")

#3 parte 
#3.1---------------------------------------------------------
'''
3.1 Basandote en la función 'calcular_min', crear la función
'calcular_min_genero' la cual recibirá como parámetro extra un string
que representa el género de la heroína/héroe a buscar. modificar un
poco la lógica para que dentro no se traiga por defecto al primer héroe
de la lista sino que mediante un flag, se traiga el primer héroe que
COINCIDA con el género pasado por parámetro. A partir de allí, podrá
empezar a comparar entre héroes o heroínas que coincidan con el
género pasado por parámetro. La función retornará el héroe o heroína
que cumpla la condición de tener el mínimo (peso, altura u otro dato)
'''           
def calcular_min_genero(
    lista_heroes: list[dict], clave_buscada: str, genero_buscado: str) -> dict:
    '''
    Calcula el mínimo de una lista de héroes según clave y género.
    Recibe (arg1)una lista de diccionarios. 
    (arg2)recibe una clave de búsqueda, por ejemplo clave_buscada = "altura". en str
    (arg3)recibe un genero en str por ejemplo : genero_buscado "F".
    Retorna el héroe o heroína que cumpla la condición de tener el mínimo de 
    la clave_buscada y genero.
    '''
    mim_indice = None
    
    for indice in range(len(lista_heroes)):
        if lista_heroes[indice]['genero'] == genero_buscado:
            if (mim_indice is None or 
                lista_heroes[indice][clave_buscada] < 
                lista_heroes[mim_indice][clave_buscada]):
                mim_indice = indice
                
    if mim_indice is not None:
        return lista_heroes[mim_indice]
    
    return None

# minima_altura_fem = calcular_min_genero(lista_de_heroes, clave_buscada="altura", genero_buscado="F")
# print(minima_altura_fem)

#3.2-----------------------------------------------------
'''
3.2 Basandote en la función 'calcular_max', crear la función
'calcular_max_genero' la cual recibirá como parámetro extra un string
que representará el género de la heroína/héroe a buscar. modificar un
poco la lógica para que dentro no se traiga por defecto al primer héroe
de la lista sino que mediante un flag, se traiga el primer héroe que
COINCIDA con el género pasado por parámetro. A partir de allí, podrá
empezar a comparar entre héroes o heroínas que coincidan con el
género pasado por parámetro. La función retornará el héroe o heroína
que cumpla la condición de tener el máximo (peso, altura u otro dato)
'''

def calcular_max_genero(
    lista_heroes: list[dict], clave_buscada: str, genero_buscado: str) -> dict:
    '''
    Calcula el maximo de una lista de héroes según clave y género.
    Recibe (arg1)una lista de diccionarios. 
    (arg2)recibe una clave de búsqueda, por ejemplo clave_buscada = "altura". en str
    (arg3)recibe un genero en str por ejemplo : genero_buscado "F".
    Retorna el héroe o heroína que cumpla la condición de tener el mínimo de 
    la clave_buscada y genero.
    '''
    
    max_indice = None
    
    for indice in range(len(lista_heroes)):
        if lista_heroes[indice]['genero'] == genero_buscado:
            if (max_indice is None or 
                lista_heroes[indice][clave_buscada] > 
                lista_heroes[max_indice][clave_buscada]):
                max_indice = indice
                
    if max_indice is not None:
        return lista_heroes[max_indice]
    
    return None

# maxima_altura_fem = calcular_max_genero(lista_de_heroes, clave_buscada="altura", genero_buscado="F")
# print(maxima_altura_fem)

#3.3 ---------------------------------------------------------------
'''
3.3 Basandote en la funcion 'calcular_max_min_dato', crear una funcion
con la misma lógica la cual reciba un parámetro string que
representará el género del héroe/heroína a buscar y renombrarla a
'calcular_max_min_dato_genero'. La estructura será similar a la ya
antes creada, salvo que dentro de ella deberá llamar a
'calcular_max_genero' y 'calcular_min_genero', pasandoles el nuevo
parámetro. Esta función retornará el héroe o heroína que cumpla con
las condiciones pasados por parámetro. Por ejemplo, si se le pasa 'F' y
'minimo', retornará la heroína que tenga el mínimo (altura, peso u otro
dato)

'''


def calcular_max_min_dato_genero(
    lista_heroes :list[dict], tipo_de_calculo : str, clave_buscada :str , genero_buscado :str)-> dict:
    '''
    Busca el heroe segun tipo de calculo , clave, y genero. 
    Recibe (arg1) lista de diccionario heroe, (arg2) tipo de calculo "maximo" o "minimo",
    (arg3) recibe la clave ejemplo "altura" en str, (arg 4) genero "F" o "M".
    
    Devuelve el heroe buscado en formato dict, o error.
    '''
    if(tipo_de_calculo == "maximo"):
        return calcular_max_genero(lista_heroes, clave_buscada, genero_buscado)
    elif(tipo_de_calculo == "minimo"):
        return calcular_min_genero(lista_heroes, clave_buscada, genero_buscado)
    else:
        return "Error :Ingrese clave 'maximo' o 'minimo'"

# resultado_max_o_min_por_clave = calcular_max_min_dato_genero(
#     lista_de_heroes, tipo_de_calculo="minimo",
#     clave_buscada="altura",genero_buscado="F")

# print(resultado_max_o_min_por_clave)

#3.4 -------------------------------------------------------
'''
3.4 Basandote en la función 'stark_calcular_imprimir_heroe' crear la
función ‘stark_calcular_imprimir_guardar_heroe_genero’ que además
reciba un string el cual representará el género a evaluar. El formato de
mensaje a imprimir deberá ser estilo:
Mayor Altura: Nombre: Gamora | Altura: 183.65
Además la función deberá guardar en un archivo csv el resultado
obtenido.
Reutilizar: 'calcular_max_min_dato_genero', 'obtener_nombre_y_dato',
'imprimir_dato' y 'guardar_archivo'.
En el caso de 'guardar_archivo' el nombre del archivo debe respetar el
formato:
heroes_calculo_key_genero.csv

Donde:
● cálculo: representará el string máximo o mínimo
● key: representará cual es la key la cual se tiene que hacer el
cálculo
● genero: representará el género a calcular.

Ejemplo: para calcular el héroe más alto femenino, el archivo se
deberá llamar:
heroes_maximo_altura_F.csv
Esta función retornará True si pudo guardar el archivo, False caso
contrario

'''

tipo_de_calculo = "maximo"
clave_a_calcular = "altura"

def stark_calcular_imprimir_guardar_heroe_genero(
    lista_heroes :list[dict], tipo_de_calculo : str, clave_buscada : str,genero_buscado : str):
    '''
    Imprime el nombre y el valor calculado del héroe que cumpla dichas condiciones. 

    Recibe (arg1)una lista de dicc heroes list[dict], 
    (arg2) un tipo de calculo("maximo" o "minimo"),
    (arg3) una clave (ejemplo "altura", "fuerza", "peso").
    (arg4) genero buscado en str "F" o "M"
    Genera un archivo csv con el heroe que cumple las condiciones
    Devuelve -1 en caso de error.
    '''
    if(lista_heroes):
        genero_csv = ""
        if genero_buscado == "M":
            genero_csv = "M"
        elif genero_buscado == "F":
            genero_csv = "F"
        nueva_lista_genero_max_min = []
        heroe_dicc_max_o_min_genero= calcular_max_min_dato_genero(
            lista_heroes, tipo_de_calculo,clave_buscada,genero_buscado)

        nombre_y_dato_capitalized = obtener_nombre_y_dato_v2(
            heroe_dicc_max_o_min_genero, clave_buscada)
        nueva_lista_genero_max_min.append(heroe_dicc_max_o_min_genero)
        
        if(tipo_de_calculo == "maximo"):
            print_dato("Mayor {0} : Nombre {1}".format(clave_buscada, 
                                                       nombre_y_dato_capitalized))
        else:
            print_dato("Menor {0} : Nombre {1}".format(clave_buscada, 
                                                       nombre_y_dato_capitalized))
        name_path_archivo_genero = "Desafio_Stark_03-Archivos\heroes_{0}_{1}_{2}.csv".format(
        tipo_de_calculo,clave_buscada, genero_csv)
    
        se_guardo = guardar_archivo(
            name_path_archivo_genero, nueva_lista_genero_max_min)
    else:
        return -1
    
# stark_calcular_imprimir_guardar_heroe_genero(lista_de_heroes, 
#                                              tipo_de_calculo="maximo", 
#                                              clave_buscada="altura",
#                                              genero_buscado="F")

