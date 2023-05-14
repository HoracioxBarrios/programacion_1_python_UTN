import re
import json

from Desafio_Stark_5_primer_intento_muy_malo.abandonada_biblioteca_stark_desafio_5 import clear_console



# heroe_dicc = {
#       "nombre": "mystique",
#       "identidad": "Raven Darkholme",
#       "empresa": "Marvel Comics",
#       "altura": "178.65000000000001",
#       "peso": "54.960000000000001",
#       "genero": "F",
#       "color_ojos": "Yellow (without irises)",
#       "color_pelo": "red / orange",
#       "fuerza": "15",
#       "inteligencia": "good"
#     }

lista_heroes_prueba =\
[   {
      "nombre": "MystiqueChuo",
      "identidad": "Raven Darkholme",
      "empresa": "Marvel Comics",
      "altura": 178.65000000000001,
      "peso": "54.960000000000001",
      "genero": "F",
      "color_ojos": "Yellow (without irises)",
      "color_pelo": "red / orange",
      "fuerza": "15",
      "inteligencia": "good"
    },
    {
      "nombre": "Mystique",
      "identidad": "Raven Darkholme",
      "empresa": "Marvel Comics",
      "altura": 178.65000000000001,
      "peso": "54.960000000000001",
      "genero": "F",
      "color_ojos": "Yellow (without irises)",
      "color_pelo": "red / orange",
      "fuerza": "15",
      "inteligencia": "good"
    },
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
    "color_ojos": "",
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

#1. Primera Parte ------------------------------
'''
1.1. Crear la función "imprimir_menu_desafio_5" que imprima el menú de
opciones por pantalla (las opciones son las que se van a utilizar para
acceder a la funcionalidad de los puntos A hasta el O y Z para salir).
Reutilizar la función 'imprimir_dato' realizada en una práctica anterior.
'''
#pertenece al strark 02
def print_dato(palabra : str):
    '''
    imprime un dato
    recibe una cadena str
    devuelve - no aplica
    '''
    print("{0}".format(palabra))
    
    
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

'''
1.4. Crear la función 'leer_archivo' la cual recibirá por parámetro un string
que indicará el nombre y extensión del archivo a leer (Ejemplo:
archivo.json). Dicho archivo se abrirá en modo lectura únicamente y
retornará la lista de héroes como una lista de diccionarios.

'''
def leer_archivo(nombre_archivo :str)-> list[dict]:
    '''
    Genera una lista de diccionarios a partir de un json
    Recibe: el path/nombre_archivo.json. (Desde donde toma los datos)
    Devuelve una nueva list[dict]
    '''
    lista_heroes = []
    with open(nombre_archivo, "r") as archivo:
        nuevo_dicc = json.load(archivo)
        lista_heroes = nuevo_dicc["heroes"]
    return lista_heroes
    
# mi_lista_heroes = leer_archivo("Desafio_Stark_5-Archivos\data_stark.json")
# print(mi_lista_heroes)

'''
1.5. Crear la función 'guardar_archivo' la cual recibirá por parámetro un
string que indicará el nombre con el cual se guardará el archivo junto
con su extensión (ejemplo: 'archivo.csv') y como segundo parámetro
tendrá un string el cual será el contenido a guardar en dicho archivo.

Debe abrirse el archivo en modo escritura+, ya que en caso de no
existir, lo creara y en caso de existir, lo va a sobreescribir.

La función debera retornar True si no hubo errores, caso contrario False, además
en caso de éxito, deberá imprimir un mensaje respetando el formato:
.Se creó el archivo: nombre_archivo.csv
En caso de retornar False, el mensaje deberá decir: ‘Error al crear el
archivo: nombre_archivo’
Donde nombre_archivo será el nombre que recibirá el archivo a ser
creado, conjuntamente con su extensión.

'''
def guardar_archivo(nombre_archivo : str, contenido_a_guardar : str):
    '''
    Genera un archivo con la extension requerida .
    Recibe: (arg 1)El path/nombre_archivo.extencion (ejemplo: csv) el path:
    (Donde se va a guardar).
    (arg 2) El contenido a guardar (una cadena str).
    Devuelve: un boolean para caso de exito True, sino False.
    '''
    retorno = False
    try:
        with open(nombre_archivo, "w+") as archivo:
            archivo.write(contenido_a_guardar)
            retorno = True
            print("Se creó el archivo {0}".format(nombre_archivo))
    except:
        retorno = False
        print("Error al crear el archivo {0}".format(nombre_archivo))
        
    return retorno

'''
1.6. Crear la función 'capitalizar_palabras' la cual recibirá por parámetro un
string que puede contener una o muchas palabras. La función deberá
retornar dicho string en el cual todas y cada una de las palabras que
contenga, deberán estar capitalizadas (Primera letra en mayúscula).

'''
# frase = "dicho string en el cual todas y cada una de las palabras"

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

'''
1.7. Crear la función 'obtener_nombre_capitalizado' la cual recibirá por
parámetro un diccionario el cual representará a un héroe y devolverá
un string el cual contenga su nombre formateado de la siguiente
manera:
Nombre: Venom
Reutilizar 'capitalizar_palabras'
'''
def obtener_nombre_capitalizado(diccionario_heroe : dict)-> str:
    '''
    Capitaliza el nombre de un heroe
    recibe un diccionario. {dict}
    devuelve un str.
    '''
    nombre_origen = "Nombre: {0}".format(diccionario_heroe["nombre"])
    nombre_capitalized = capitalizar_palabras(nombre_origen)
    return nombre_capitalized


# nombre = obtener_nombre_capitalizado(heroe_dicc)
# print(nombre)

'''
1.8. Crear la función 'obtener_nombre_y_dato' la cual recibirá por
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
def obtener_nombre_y_dato(diccionario_heroe: dict, clave_buscada: str) -> str:
    '''
    Obtiene el nombre del héroe y un dato específico.
    Recibe: arg(1) un diccionario y arg(2) una clave (por ejemplo: 
    "altura", "fuerza", "peso").
    Devuelve una cadena formateada.
    '''
    if clave_buscada in diccionario_heroe:
        nombre_capitalizado = obtener_nombre_capitalizado(diccionario_heroe)
        return "{0} | {1}: {2}".format(nombre_capitalizado,clave_buscada,
            diccionario_heroe[clave_buscada]
        )
    else:
        return "Dato no encontrado para el héroe."

# nombre__dato_buscado = obtener_nombre_y_dato(heroe_dicc, clave_buscada="fuerza")
# print(nombre__dato_buscado)

#2. Segunda Parte------------------------------
'''
2.1. Crear la función 'es_genero' la cual recibirá por parámetro un
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
 
# print(es_genero(heroe_dicc, valor_genero="F"))

'''
2.2. Crear la función 'stark_guardar_heroe_genero' la cual recibira por
parámetro la lista de héroes y un string el cual representará el género
a evaluar (puede ser M o F). 
Deberá imprimir solamente los héroes o
heroínas que coincidan con el género pasado por parámetro y
además, deberá guardar dichos nombres en un archivo con extensión
csv (cada nombre deberá ir separado por una coma)
Reutilizar las funciones 'es_genero', 'obtener_nombre_capitalizado',
'imprimir_dato' y 'guardar_archivo'.
En el caso de 'guardar_archivo', cuando se llame a esta función el
nombre de archivo a guardar deberá respetar el formato:
heroes_M.csv, heroes_F.csv o heroes_NB según corresponda.
La función retornará True si pudo guardar el archivo, False caso
contrario.
'''
def stark_guardar_heroe_genero(lista_de_heroes: list[dict], genero_buscado: str)-> bool:
    '''
    crea un csv con los heroes que cumplen con el genero elegido
    recibe una lista de heroes y el genero buscado ("F", "M", "NB")
    revuelve un boolean
    '''
    nueva_lista = []
    for heroe in lista_de_heroes:
        es_igual_al_genero_buscado = es_genero(heroe, genero_buscado)
        if(es_igual_al_genero_buscado):
            nombre_heroe_capitalized = obtener_nombre_capitalizado(heroe)
            print_dato(nombre_heroe_capitalized)
            nueva_lista.append(nombre_heroe_capitalized)
            
    cadena = ",".join(nueva_lista)
    name_path_archivo_genero = "Desafio_Stark_5-Archivos\heroes_{0}.csv".format(genero_buscado)
    resultado_boleano = guardar_archivo(name_path_archivo_genero, cadena)
    return resultado_boleano
            
    
                 
# stark_guardar_heroe_genero(lista_heroes_prueba, genero_buscado="F")

#3. Tercera Parte------------------------------
'''
3.1. Basandote en la función 'calcular_min', crear la función
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
        if(lista_heroes[indice]['genero'] == genero_buscado):
            if (mim_indice is None or 
                lista_heroes[indice][clave_buscada] < 
                lista_heroes[mim_indice][clave_buscada]):
                mim_indice = indice
                
    if mim_indice is not None:
        return lista_heroes[mim_indice]
    
    return None

# minima_altura_fem = calcular_min_genero(lista_heroes_prueba, clave_buscada="altura", genero_buscado="F")
# print(minima_altura_fem)

'''
3.2. Basandote en la función 'calcular_max', crear la función
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

# maxima_altura_fem = calcular_max_genero(lista_heroes_prueba, clave_buscada="altura", genero_buscado="F")
# print(maxima_altura_fem)

'''
3.3. Basandote en la funcion 'calcular_max_min_dato', crear una funcion
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
    Recibe: (arg1) lista de diccionario heroe,
    (arg2) tipo de calculo "maximo" o "minimo",
    (arg3) recibe la clave ejemplo "altura" en str, 
    (arg 4) genero "F" o "M".
    
    Devuelve el heroe buscado en formato dict, o error.
    '''
    if(tipo_de_calculo == "maximo"):
        return calcular_max_genero(lista_heroes, clave_buscada, genero_buscado)
    elif(tipo_de_calculo == "minimo"):
        return calcular_min_genero(lista_heroes, clave_buscada, genero_buscado)
    else:
        return "Error :Ingrese clave 'maximo' o 'minimo'"

# resultado = calcular_max_min_dato_genero(
#     lista_heroes_prueba, tipo_de_calculo="minimo",
#     clave_buscada="altura",genero_buscado="F")
# print(resultado)

'''
3.4. Basandote en la función 'stark_calcular_imprimir_heroe' crear la
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
def stark_calcular_imprimir_guardar_heroe_genero(
    lista_heroes :list[dict], tipo_de_calculo : str, clave_buscada : str,genero_buscado : str)-> bool:
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
        
        heroe_dicc_max_o_min_genero= calcular_max_min_dato_genero(
            lista_heroes, tipo_de_calculo,clave_buscada,genero_buscado)

        nombre_y_dato_capitalized = obtener_nombre_y_dato(
            heroe_dicc_max_o_min_genero, clave_buscada)
        
        if(tipo_de_calculo == "maximo"):#Mayor Altura: Nombre: Gamora | Altura: 183.65
            heroe_mensaje = "Mayor {0}: {1}".format(clave_buscada, 
                                                       nombre_y_dato_capitalized)
            print_dato(heroe_mensaje)
        else:
           heroe_mensaje =  "Menor {0}: {1}".format(clave_buscada, 
                                                       nombre_y_dato_capitalized)
           print_dato(heroe_mensaje)
                                                                    #heroes_maximo_altura_F.csv
        name_path_archivo_genero = "Desafio_Stark_5-Archivos\heroes_{0}_{1}_{2}.csv".format(
        tipo_de_calculo,clave_buscada, genero_buscado)
    
        resultado_booleano = guardar_archivo(
            name_path_archivo_genero, heroe_mensaje)
        return resultado_booleano
    
# stark_calcular_imprimir_guardar_heroe_genero(lista_heroes_prueba, 
#                                              tipo_de_calculo="maximo", 
#                                              clave_buscada="altura",
#                                              genero_buscado="F")


#4. Cuarta Parte------------------------------
'''
4.1. Basandote en la función 'sumar_dato_heroe', crear la función llamada
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
        if(bool(type(dicc_heroe)) and dicc_heroe 
           and "genero" in dicc_heroe 
           and dicc_heroe["genero"] == genero_buscado 
           and clave_a_calcular in dicc_heroe):
            acumulador_de_dato += dicc_heroe[clave_a_calcular]
            
    if(acumulador_de_dato > 0):
        return acumulador_de_dato
    else:
        return -1

# print(sumar_dato_heroe_genero(
#     lista_heroes_prueba, clave_a_calcular="altura", genero_buscado="F"))

'''
4.2. Crear la función 'cantidad_heroes_genero' la cual recibirá por
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

# resultado = cantidad_heroes_genero(lista_heroes_prueba, genero_buscado="F")
# print(resultado)



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
'''
4.3. Basandote en la función 'calcular_promedio', crear la función
'calcular_promedio_genero' la cual tendrá como parámetro extra un
string que representará el género a buscar. la lógica es similar a la
función anteriormente mencionada en el enunciado. Reutilizar las
funciones: 'sumar_dato_heroe_genero', 'cantidad_heroes_genero' y
'dividir'.
retornará el promedio obtenido, según la key y género pasado por
parámetro
'''
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

'''
4.4. Basandote en la función ‘stark_calcular_imprimir_promedio_altura',
desarrollar la función 'stark_calcular_imprimir_guardar_
promedio_altura_genero' la cual tendrá como parámetro extra un string
que representará el género de los héroes a buscar.
La función antes de hacer nada, deberá validar que la lista no esté
vacía. En caso de no estar vacía: calculará el promedio y lo imprimirá
formateado al estilo:
Altura promedio género F: 178.45
En caso de estar vacía, imprimirá como mensaje:
Error: Lista de héroes vacía.
Luego de imprimir la función deberá guardar en un archivo los mismos
datos. El nombre del archivo debe tener el siguiente formato:------------------
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
    lista_heroes : list[dict], genero_buscado : str)-> bool:
    '''
    imprime el promedio de la altura segun genero y la guarda a formato csv.
    Recibe (arg 1) la lista de heroes, y (arg 2) genero buscado ("F", "M")
    Devuelve True en caso de generar el archivo correctamente.
    '''
    if(lista_heroes):
        clave_a_calcular = "altura"
        resultado_promedio = calcular_promedio_genero(lista_heroes, clave_a_calcular, genero_buscado)
        dato_promedio_genero = "Altura promedio genero {0}: {1}".format(genero_buscado, round(resultado_promedio, 2))
        print_dato(dato_promedio_genero) 

        name_path_archivo_genero = "Desafio_Stark_5-Archivos\heroes_promedio_{0}_{1}.csv".format(
            clave_a_calcular, genero_buscado)
    
        resultado_booleano = guardar_archivo(
            name_path_archivo_genero, dato_promedio_genero)
        return resultado_booleano
    else:
        print("Error: Lista de héroes vacía.")

# stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes_prueba, genero_buscado="F")

#5. Quinta Parte------------------------------
'''
5.1. Crear la función 'calcular_cantidad_tipo' la cual recibirá por parámetro
la lista de héroes y un string que representará el tipo de dato/key a
buscar (color_ojos, color_pelo, etc)
Antes de hacer nada, deberá validar que la lista no esté vacía. En caso
de estarlo devolver un diccionario con la siguiente estructura:
{
"Error": “La lista se encuentra vacía”
}
La función deberá retornar un diccionario con los distintos valores del
tipo de dato pasada por parámetro y la cantidad de cada uno (crear un
diccionario clave valor).
Por ejemplo, si el tipo de dato fuese color_ojos, devolverá un
diccionario de la siguiente manera:
{
"Celeste": 4,
"Verde": 8,
"Marron": 6
}
Reutilizar la función 'capitalizar_palabras' para capitalizar los valores
de las keys
'''
def calcular_cantidad_tipo(lista_heroes : list[dict], clave_buscada : str)-> dict:
    '''
    calcula la cantidad por tipo de valor ,segun clave.
    Recibe: (arg1) una lista de heroes
    (arg2) una key del heroe (ejemplo clave_buscada = "color_pelo")
    Devuelve : un dccionario
    '''
    if(lista_heroes):
        nuevo_diccionario = {}
        for heroe in lista_heroes:
            valor_tipo_original = heroe[clave_buscada]
            valor_tipo_capitalized = capitalizar_palabras(valor_tipo_original)
            if(valor_tipo_capitalized == ""):
                valor_tipo_capitalized = "No tiene"
            
            if(valor_tipo_capitalized in nuevo_diccionario):
                nuevo_diccionario[valor_tipo_capitalized] += 1
            else:
                nuevo_diccionario[valor_tipo_capitalized] = 1
        return nuevo_diccionario
    else:
        return {'"Error": “La lista se encuentra vacía”'}

# print(calcular_cantidad_tipo(lista_heroes_prueba, clave_buscada="color_pelo"))

'''
5.2. Crear la función 'guardar_cantidad_heroes_tipo' la cual recibirá como
parámetro un diccionario que representará las distintas variedades del
tipo de dato (distintos colores de ojos, pelo, etc) como clave con sus
respectivas cantidades como valor. Como segundo parámetro recibirá
el dato (color_pelo, color_ojos, etc) el cual tendrás que usarlo
únicamente en el mensaje final formateado. Esta función deberá iterar
cada key del diccionario y variabilizar dicha key con su valor para
luego formatearlos en un mensaje el cual deberá guardar en archivo.
Por ejemplo:
"Caracteristica: color_ojos Blue - Cantidad de heroes: 9"
Reutilizar la función 'guardar_archivo'. El nombre del archivo final
deberá respetar el formato:
heroes_cantidad_tipoDato.csv
Donde:
● tipoDato: representará el nombre de la key la cual se está
evaluando la cantidad de héroes.
Ejemplo:
heroes_cantidad_color_pelo.csv
heroes_cantidad_color_ojos.csv
La función retornará True si salió todo bien, False caso contrario.

'''
decc = {
"Celeste": 4,
"Verde": 8,
"Marron": 6
}
def guardar_cantidad_heroes_tipo(diccionario_heroe : dict, clave_buscada : str)-> bool:
    '''
    guarda la cantidad de heroes por tipo segun clave
    Recibe : (arg 1) un lista de heroes, (arg 2) una clave (ejemplo : "color_pelo")
    Devuelve True en caso de guardar el archivo correctamente.
    '''
    nueva_lista_cantidad_tipos = []
    for clave, Valor in diccionario_heroe.items():
        dato = "Caracteristica: {0} {1} - Cantidad de heroes: {2}".format(
         clave_buscada, clave, Valor)
        nueva_lista_cantidad_tipos.append(dato)
       
    name_path_archivo_genero ="Desafio_Stark_5-Archivos\heroes_cantidad_{0}.csv".format(
        clave_buscada)
    datos_a_guardar = '\n'.join(nueva_lista_cantidad_tipos)
    
    resultado_booleano = guardar_archivo(
            name_path_archivo_genero, datos_a_guardar)
    return resultado_booleano
        
    

# guardar_cantidad_heroes_tipo(decc, clave_buscada="color_pelo")

'''
5.3. Crear la función 'stark_calcular_cantidad_por_tipo' la cual recibirá por
parámetro la lista de héroes y un string que representará el tipo de
dato/key a buscar (color_ojos, color_pelo, etc). Dentro deberás
reutilizar 'calcular_cantidad_tipo' y 'guardar_cantidad_heroes_tipo' con
la lógica que cada una de esas funciones manejan.
Esta función retornará True si pudo guardar el archivo, False caso
contrario.

'''
def stark_calcular_cantidad_por_tipo(lista_heroes :list[dict], clave_buscada : str):
    '''
    calcula ña cantidad por tipo
    Recibe : (arg 1)Una Lista de heroes, (arg 2) una clave (ejemplo "color_ojos")
    Devuelve : 
    '''
    diccionario_resultados = calcular_cantidad_tipo(lista_heroes, clave_buscada)
    resultado_booleano = guardar_cantidad_heroes_tipo(diccionario_resultados, clave_buscada)
    return resultado_booleano
    
# stark_calcular_cantidad_por_tipo(lista_heroes_prueba,clave_buscada= "color_ojos")

#6. Sexta Parte------------------------------
'''
6.1. Crear la función 'obtener_lista_de_tipos' la cual recibirá por parámetro
la lista de héroes y un string que representará el tipo de dato/key a
buscar (color_ojos, color_pelo, etc).
Esta función deberá iterar la lista de héroes guardando en una lista las
variedades del tipo de dato pasado por parámetro (sus valores).
En caso de encontrar una key sin valor (o string vacío), deberás
hardcodear con el valor 'N/A' y luego agregarlo a la lista donde irás
guardando todos los valores encontrados, si el valor del héroe no tiene
errores, guardarlo tal cual viene.
Finalmente deberás eliminar los duplicados de esa lista y retornarla
como un set.
Reutilizar 'capitalizar_palabras' para guardar cada uno de los datos
con la primera letra mayúscula.
'''
def obtener_lista_de_tipos(lista_heroes : list[dict], clave_buscada : str)-> set:
    '''
    |De una lista de heroes obtiene el tipo de valor sin duplicados.
    |Recibe una lista de heroes. (arg 2) la clave buscada (ej: "color_ojos).
    |devuelve un set
    '''
    nueva_lista_variedades = []
    for heroe in lista_heroes:
        if(heroe[clave_buscada] == ""):
            heroe[clave_buscada] = "N/A"
        valor_capitalized = capitalizar_palabras(heroe[clave_buscada])
        if(valor_capitalized not in nueva_lista_variedades):
            nueva_lista_variedades.append(valor_capitalized)
    return set(nueva_lista_variedades)

# tipos = obtener_lista_de_tipos(lista_heroes_prueba, clave_buscada="color_ojos")
# print(tipos)

'''
6.2. Crear la función 'normalizar_dato' la cual recibirá por parámetro un
dato de héroe (el valor de una de sus keys, por ejemplo si la key fuese
color_ojos y su valor fuese Verde, recibira este ultimo) y tambien una
variable como string la cual representará el valor por defecto a colocar
en caso de que el valor está vacío. Deberá validar que el dato no esté
vacío, en caso de estarlo lo reemplazará con el valor default pasado
por parámetro y lo retornará, caso contrario lo retornará sin
modificaciones
'''

def normalizar_dato(valor : str, valor_reemplazante= "N/A"):
    '''
    Normaliza un valor string.
    Recibe: (arg 1) valor (ejemplo: verde), (arg2) Opcional:valor 
    reemplazante en caaso de que el valor sea "", 
    por defaul reemplaza por "N/A".
    Retorna el valor modificado si fue necesario.
    '''
    if(valor == ""):
        valor = valor_reemplazante
    return valor

'''
6.3. Crear la función 'normalizar_heroe' la cual recibirá dos parámetros. el
primero será un diccionario que representará un solo héroe, el
segundo parámetro será el nombre de la key de dicho diccionario la
cual debe ser normalizada.
La función deberá capitalizar las palabras que tenga dicha key como
valor, luego deberá normalizar el dato (ya que si viene vacío, habrá
que setearlo con N/A).
Finalmente deberá capitalizar todas las palabras del nombre del héroe
y deberá retornar al Hero con cada palabra de su nombre
capitalizados, cada palabra del valor de la key capitalizadas y
normalizadas (con N/A en caso de que estuviesen vacías por defecto).
Reutilizar: 'capitalizar_palabras' y 'normalizar_dato'
'''
def normalizar_heroe(heroe : dict, clave_a_normalizar : str)-> dict:
    '''
    Normaliza el nombre y el valor de la clave buscada ademas las capitaliza.
    Recibe:(arg 1) un diccionario - heroe y arg 2) la clave a normalizar
    ejemplo "color_pelo". ----Normaliza datos str dentro del dicc----
    Devuelve el heroe - normalizado.
    '''
    valor_capitalized = capitalizar_palabras(heroe[clave_a_normalizar])
    heroe[clave_a_normalizar] = valor_capitalized
    
    valor_normalizado = normalizar_dato(heroe[clave_a_normalizar])
    heroe[clave_a_normalizar] = valor_normalizado
    
    nombre_capitalized = capitalizar_palabras(heroe["nombre"])
    heroe["nombre"] = nombre_capitalized
        
    return heroe    
        
    
# heroe_normalizado = normalizar_heroe(
#     heroe_dicc, clave_a_normalizar="color_pelo")
# print(heroe_dicc)

'''
6.4. Crear la funcion 'obtener_heroes_por_tipo' el cual recibira por
parámetro:
A. La lista de héroes
B. Un set de tipos/variedades (colores de ojos, de pelo, etc)
C. El tipo de dato a evaluar (la key en cuestion, color_ojos,
color_pelo, etc)
PRESTAR ATENCIÓN:
A. Deberá iterar el set de tipos/variedades y por cada tipo tendrá evaluar
si ese tipo existe como key en un diccionario el cual deberás armar.
(contendrá cada variedad como key y una lista de nombres de héroes
como valor de cada una de ellas).
B. En caso de no existir dicha key en el diccionario, agregarla con una
lista vacía como valor.
C. Dentro de la iteración de variedades, iterar la lista de héroes (for
anidado) 'normalizando' el posible valor que tenga la key evaluada, ya
que podría venir vacía (qué función usarias aca? guiño guiño)
D. Una vez normalizado el dato, evaluar si dicho dato coincide con el tipo
pasado por parámetro.
E. En caso de que coincida, agregarlo a la lista (inicialmente vacía) de la
variedad iterada en el primer bucle.
Esta función retornará un diccionario con cada variedad como key y
una lista de nombres como valor.
Por ejemplo:
{
"Celestes": ["Capitan America", "Tony Stark"],
"Verdes": ["Hulk", "Viuda Negra"]
....
}
'''
set_heroes_tipo_nombre = obtener_lista_de_tipos(lista_heroes_prueba, clave_buscada="color_pelo")


#{'Red / Orange', 'Brown', 'Black', 'Yellow'}


def obtener_heroes_por_tipo(
    lista_heroes :list[dict], set_de_variedades : str, clave_buscada : str)->dict:
    '''
    obtierne heroes por tipo.
    Recibe: (arg1)lista de heroes, (arg 2) Un set de tipos/variedades (colores de ojos, de pelo, etc)
    (arg 3) una clave a evaluar.El tipo de dato a evaluar (la key en cuestion, color_ojos,
    color_pelo, etc).
    
    Retorna un diccionario. ejemplo:
    {"Green" : ["hulk", "blanka", "ET"],
    {....}
    {....} 
    '''
    nuevo_diccionario_variedades = {}
    for tipo_variedad in set_de_variedades:
        if(tipo_variedad not in nuevo_diccionario_variedades):
            nueva_lista = []
            nuevo_diccionario_variedades[tipo_variedad] = nueva_lista
            for heroe in lista_heroes:
               valor_normalizado = normalizar_dato(heroe[clave_buscada])
               heroe[clave_buscada] = valor_normalizado
               heroe[clave_buscada] = capitalizar_palabras(heroe[clave_buscada]) #capit. la clave antes de evaluar
               if(heroe[clave_buscada] == tipo_variedad):
                   nueva_lista.append(heroe["nombre"])
    return nuevo_diccionario_variedades
              
            
    


dicc_heroe_por_tipo =  obtener_heroes_por_tipo(lista_heroes_prueba, set_heroes_tipo_nombre, clave_buscada="color_pelo")
# print(dicc_heroe_por_tipo)

'''
6.5. Crear la funcion 'guardar_heroes_por_tipo' la cual recibira por
parámetro un diccionario que representará los distintos tipos como
clave y una lista de nombres como valor (Lo retorna la función anterior)
y además como segundo parámetro tendrá un string el cual
representará el tipo de dato a evaluar (color_pelo, color_ojos, etc).
Deberá recorrer cada key y cada valor (lista) que esta contenga para
finalmente crear un string el cual será un mensaje que deberás
imprimir formateado.
Por ejemplo:
"color_ojos Green: Black Widow | Hulk"
Reutilizar la función 'guardar_archivo'. El archivo final deberá respetar
el formato:
heroes_segun_TipoDato.csv
Donde:
● TipoDato: es la key la cual indicará qué cosas se deben guardar
en el archivo.
Ejemplo:
heroes_segun_color_pelo.csv (Agrupados por color de pelo)
heroes_segun_color_ojos.csv (Agrupados por color de ojos)
Esta función retorna True si salió todo bien, False caso contrario.

'''
def guardar_heroes_por_tipo(diccionario_tipos_y_nombres : dict[str, list],clave_buscada : str):
    nueva_lista_tipos_y_nombres = []
    for clave, valor in diccionario_tipos_y_nombres.items():
        dato_str = "color de Pelo {0}: {1}".format(clave," | ".join(valor))
        nueva_lista_tipos_y_nombres.append(dato_str)
        
    name_path_archivo_genero ="Desafio_Stark_5-Archivos\heroes_segun_{0}.csv".format(
        clave_buscada)
    datos_a_guardar = '\n'.join(nueva_lista_tipos_y_nombres)
    
    resultado_booleano = guardar_archivo(
            name_path_archivo_genero, datos_a_guardar)
    
    return resultado_booleano

# guardar_heroes_por_tipo(dicc_heroe_por_tipo, clave_buscada="color_pelo")



'''
6.6. Crear la función 'stark_listar_heroes_por_dato' la cual recibirá por
parámetro la lista de héroes y un string que representará el tipo de
dato a evaluar (color_pelo, color_ojos, etc). Dentro deberás reutilizar
las funciones:
A. 'obtener_lista_de_tipos'
B. 'obtener_heroes_por_tipo'
C. 'guardar_heroes_por_tipo'
Pasando por parámetro lo que corresponda según la lógica de las
funciones usadas.
Esta función retornará True si pudo guardar el archivo, False caso
contrario.
'''

def stark_listar_heroes_por_dato(lista_heroes : list[dict], clave_buscada : str):
    set_heroes_tipo_nombre = obtener_lista_de_tipos(lista_heroes, clave_buscada)
    dicc_heroe_por_tipo_nombre =  obtener_heroes_por_tipo(lista_heroes, set_heroes_tipo_nombre, clave_buscada)
    resultado_booleano = guardar_heroes_por_tipo(dicc_heroe_por_tipo_nombre, clave_buscada)
    
    return resultado_booleano

print(stark_listar_heroes_por_dato(lista_heroes_prueba, clave_buscada="color_ojos"))

