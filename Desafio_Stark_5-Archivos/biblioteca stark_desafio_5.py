import re
import json

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

#1. Primera Parte------------------------------
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
    Genera un archivo con la extension requerida 
    Recibe: el path/nombre_archivo.extencion (ejemplo: csv) el path:
    (Donde se va a guardar)
    Devuelve: un boolean para caso de exito True, sino False
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
def stark_guardar_heroe_genero(lista_de_heroes: list[dict], genero_buscado: str):
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

