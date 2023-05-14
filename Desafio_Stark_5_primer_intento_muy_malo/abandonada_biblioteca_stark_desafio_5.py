import os
import re
import json
import os


lista_heroes_prueba =\
[
  {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": 79.349999999999994,
    "peso": "18.449999999999999",
    "genero": "F",
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
    "genero": "F",
    "color_ojos": "Blue",
    "color_pelo": "Black",
    "fuerza": "35",
    "inteligencia": "good"
  }]

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
'''
1.1. Crear la función "imprimir_menu_desafio_5" que imprima el menú de
opciones por pantalla (las opciones son las que se van a utilizar para
acceder a la funcionalidad de los puntos A hasta el O y Z para salir).
Reutilizar la función 'imprimir_dato' realizada en una práctica anterior.


'''
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
'''
1.2. Crear la funcion 'stark_menu_principal_desafio_5' la cual se encargará
de imprimir el menú de opciones y le pedirá al usuario que ingrese la
letra de una de las opciones elegidas, deberá validar la letra usando
RegEx y en caso de ser correcta tendrá que retornarla, Caso contrario
retornará -1. El usuario puede ingresar tanto letras minúsculas como
mayúsculas y ambas se deben tomar como válidas
Reutilizar la función 'imprimir_menu_Desafio_5'

'''
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
'''
1.3. Crear la función 'stark_marvel_app_5' la cual recibirá por parámetro la
lista de héroes y se encargará de la ejecución principal de nuestro
programa. (usar if/elif o match según prefiera) Reutilizar las funciones
con prefijo 'stark_' donde crea correspondiente.

'''

def  stark_marvel_app_5(lista_de_personajes: list[dict]):
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


# 1.4 -------------------------------------- 
'''
1.4. Crear la función 'leer_archivo' la cual recibirá por parámetro un string
que indicará el nombre y extensión del archivo a leer (Ejemplo:
archivo.json). Dicho archivo se abrirá en modo lectura únicamente y
retornará la lista de héroes como una lista de diccionarios.

'''
#Genera la Lista a partir de json
def leer_archivo(path_archivo_completo: str) -> list[dict]:
    '''
    De un archivo json, crea una lista de diccionarios heroes
    Recibe la ruta del archivo
    devuelve una lista de diccionarios
    '''
    with open(path_archivo_completo, 'r') as archivo: # r = solo lectura
        archivo_json = json.load(archivo)
        archivo_lista_dict = archivo_json['heroes'] #accedemos a la clave y traemos lo que esta dentro
        return archivo_lista_dict
    
# leer_archivo("Desafio_Stark_03-Archivos\data_stark.json") # se usa en main.py
lista_de_heroes_en_crudo_str = leer_archivo("Desafio_Stark_03-Archivos\data_stark.json")


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
    
lista_heroes = stark_normalizar_datos(lista_de_heroes_en_crudo_str)
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

def guardar_archivo(nombre_del_archivo_path: str, contenido_a_guardar: str):
    '''
    guarda un contenido recibido al formato indicado.
    '''
    flag_exito = False
    try:
        with open(nombre_del_archivo_path, "w+") as archivo:
            archivo.write(contenido_a_guardar)
        flag_exito = True
    except:
        pass
    
    if flag_exito:
        print(f"Se creó el archivo: {nombre_del_archivo_path}")
        return True
    else:
        print(f"Error al crear el archivo: {nombre_del_archivo_path}")
        return False

'''
como funciona el try  el except:
El bloque try se utiliza para encerrar el código que puede generar una 
excepción. Dentro de este bloque, se ejecuta el código que se quiere probar
en busca de errores. Si ocurre una excepción durante la ejecución de este
código, se salta inmediatamente al bloque except correspondiente sin ejecutar 
el resto del código dentro del bloque try.
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
    
        se_guardo_boolean = guardar_archivo(
            name_path_archivo_genero, nueva_lista_genero_max_min)
        return se_guardo_boolean
    
# stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, 
#                                              tipo_de_calculo="maximo", 
#                                              clave_buscada="altura",
#                                              genero_buscado="F")

# 4 parte----------------------------------------------------
'''
4.1 Basandote en la función 'sumar_dato_heroe', crear la función llamada
'sumar_dato_heroe_genero' la cual deberá tener un parámetro extra
del tipo string que representará el género con el que se va a trabajar.
Esta función antes de realizar la suma en su variable sumadora,
deberá validar lo siguiente:

A. El tipo de dato del héroe debe ser diccionario.
B. El héroe actual de la iteración no debe estar vacío (ser
diccionario vacío)
C. El género del héroe debe coincidir con el pasado por
parámetro.

Una vez que cumpla con las condiciones, podrá realizar la suma. La
función deberá retornar la suma del valor de la key de los héroes o
heroínas que cumplan las condiciones o -1 en caso de que no se
cumplan las validaciones
'''


def sumar_dato_heroe_genero(
    lista_heroes: list[dict], clave_a_calcular: str, genero_buscado: str) -> int:
    """
    Acumula la suma de una clave en un diccionario para héroes de un género 
    específico.
    (arg1)lista_heroes: Lista de diccionarios de héroes.
    (arg2) clave_a_calcular: Clave a sumar en cada héroe.
    (arg3)genero_buscado: Género de los héroes a filtrar.
    Devuelve La suma de los valores de la clave en los héroes que cumplen las 
    condiciones, -1 en caso contrario
    """
    acumulador_de_dato = 0
    
    for dicc_heroe in lista_heroes:
        if(bool(type(dicc_heroe)) and dicc_heroe and "genero" in dicc_heroe 
           and dicc_heroe["genero"] == genero_buscado and clave_a_calcular in dicc_heroe):
            acumulador_de_dato += dicc_heroe[clave_a_calcular]
            
    if(acumulador_de_dato > 0):
        return acumulador_de_dato
    else:
        return -1

# print(sumar_dato_heroe_genero(
#     lista_heroes_prueba, clave_a_calcular="altura", genero_buscado="F"))

#4.2-------------------------------------------------------
'''
4.2 Crear la función 'cantidad_heroes_genero' la cual recibirá por
parámetro la lista de héroes y un string que representará el género a
buscar. La función deberá iterar y sumar la cantidad de héroes o
heroínas que cumplan con la condición de género pasada por
parámetro, retornará dicha suma.

'''
def cantidad_heroes_genero(lista_heroes : list[dict], genero_buscado : str)-> int:
    '''
    Da la cantidad de heroes del genero elegido.
    Recibe una lista de diccionario heroe
    devuelve la cantidad
    '''
    contador_de_heroes_genero = 0
    for heroe in lista_heroes:
        if(heroe["genero"] == genero_buscado):
            contador_de_heroes_genero += 1
            
    if(contador_de_heroes_genero > 0):
        return contador_de_heroes_genero
    else:
        return contador_de_heroes_genero

# para 4.3----------------------------------
def dividir(dividendo, divisor )-> float:
    '''
    realiza la division entre dos numeros
    recibe un dividendo Int o Float, y un divisor int o float
    devuelve el resultado (float) o en caso de error 0
    '''
    if divisor != 0 and isinstance(dividendo, (int, float)) and isinstance(divisor, (int, float)):
        return dividendo / divisor
    else:
        return 0
#4.3--------------------------------------------------------
'''
Basandote en la función 'calcular_promedio', crear la función
'calcular_promedio_genero' la cual tendrá como parámetro extra un
string que representará el género a buscar. la lógica es similar a la
función anteriormente mencionada en el enunciado. Reutilizar las
funciones: 'sumar_dato_heroe_genero', 'cantidad_heroes_genero' y
'dividir'.
retornará el promedio obtenido, según la key y género pasado por
parámetro.
'''

#uso la funcion normalizar datos, en la funcion sumar_dato_heroe
def calcular_promedio_genero(
    lista_heroes : list[dict], clave_a_calcular : str, genero_buscado : str)-> float:
    '''
    calcula el promedio total segun necesidad en base a una lista de heroes
    recibe una lista de dicc heroes y una clave a calcular (ej: clave = "altura")
    devuelve el promedio
    '''
    resultado_acumulado = sumar_dato_heroe_genero(lista_heroes, clave_a_calcular,genero_buscado)
    cantidad_de_heroes = cantidad_heroes_genero(lista_heroes, genero_buscado)
    promedio = dividir(resultado_acumulado, cantidad_de_heroes)
    return promedio

# resultado_promedio = calcular_promedio_genero(
#     lista_heroes_prueba, clave_a_calcular="altura", genero_buscado="F")
# print(resultado_promedio)


#4.4----------------------------------------------------------------
'''
Basandote en la función "stark_calcular_imprimir_promedio_altura",
desarrollar la función  'stark_calcular_imprimir_guardar_promedio_altura_genero' 
la cual tendrá como parámetro extra un string
que representará el género de los héroes a buscar.

La función antes de hacer nada, deberá validar que la lista no esté
vacía. En caso de no estar vacía: calculará el promedio y lo imprimirá
formateado al estilo:

Altura promedio género F: 178.45

En caso de estar vacía, imprimirá como mensaje:
Error: Lista de héroes vacía.

Luego de imprimir la función deberá guardar en un archivo los mismos
datos. El nombre del archivo debe tener el siguiente formato:

heroes_promedio_altura_genero.csv

Donde:
A. genero: será el género de los héroes a calcular, siendo M y F
únicas opciones posibles.
Ejemplos:
heroes_promedio_altura_F.csv
heroes_promedio_altura_M.csv

Reutilizar las funciones: 'calcular_promedio_genero', 'imprimir_dato' y
'guardar_archivo'.
Esta función retornará True si pudo la lista tiene algún elemento y pudo
guardar el archivo, False en caso de que esté vacía o no haya podido
guardar el archivo.
'''
def stark_calcular_imprimir_guardar_promedio_altura_genero(
        lista_heroes : list[dict], genero_buscado : str):
    '''
    calcula el promedio total de alturas de los heroes  y lo muestra.
    recibe una lista de heroes
    devuelve el resultado y en caso de error -1
    
    '''
    if(lista_heroes):
        genero_csv = ""
        if genero_buscado == "M":
            genero_csv = "M"
        elif genero_buscado == "F":
            genero_csv = "F"

        
        clave_a_calcular = "altura"
        resultado_promedio = calcular_promedio_genero(lista_heroes, clave_a_calcular, genero_buscado)
        # print(resultado_promedio)
        dato = "{0} promedio del genero {1} es: {2}".format(
            clave_a_calcular, genero_buscado ,resultado_promedio)
        # print(dato)
        nueva_lista = []
        nueva_lista.append(dato)
        print(nueva_lista)                     #heroes_promedio_altura_genero.csv
        name_path_archivo_genero = "Desafio_Stark_03-Archivos\heroes_promedio_{0}_{1}.csv".format(
            clave_a_calcular, genero_csv)
        guardar_archivo(
            name_path_archivo_genero, nueva_lista)
        return True
    else:
        print("Error: Lista de héroes vacía.")
        return False

print_dato(stark_calcular_imprimir_guardar_promedio_altura_genero(
    lista_heroes_prueba, genero_buscado="F")) 


#5.2
# def guardar_cantidad_heroes_tipo(cantidad_tipo, tipo):
#     nombreArchvo = f"heroes_cantidad_{tipo}.csv"
#     mensajito = "{} , {}"
#     with open(nombreArchvo, "w") as f:
#         for key, value in cantidad_tipo.items():
#             if not key:
#                 key="decolorado"
#             mensajeFormateado = mensajito.format(key, value)
#             f.write(mensajeFormateado + "\n")
    
#     return True
