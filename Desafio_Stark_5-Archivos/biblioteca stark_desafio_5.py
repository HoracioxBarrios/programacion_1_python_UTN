import re
import json
import os



def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')
    
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
                            "El dato {0}fue modificado en el heroe {1}".format(key, heroe["nombre"]))
            result_nueva_lista.append(heroe)
        return result_nueva_lista
    else:
        return "La lista esta Vacia"

#1. Primera Parte------------------------------



def print_dato(palabra : str):
    '''
    imprime un dato
    recibe una cadena str
    devuelve - no aplica
    '''
    print("{0}".format(palabra))
    
#1.1     
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
        
#1.2
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
#1.4
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
    
#1.5
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
        with open(nombre_archivo, "w+",newline='\n') as archivo:
            archivo.write(contenido_a_guardar)
            retorno = True
            print("Se creó el archivo {0}".format(nombre_archivo))
    except:
        retorno = False
        print("Error al crear el archivo {0}".format(nombre_archivo))
        
    return retorno

#1.6

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


#1.7

def obtener_nombre_capitalizado(diccionario_heroe : dict)-> str:
    '''
    Capitaliza el nombre de un heroe
    recibe un diccionario. {dict}
    devuelve un str.
    '''
    nombre_origen = "Nombre: {0}".format(diccionario_heroe["nombre"])
    nombre_capitalized = capitalizar_palabras(nombre_origen)
    return nombre_capitalized


#1.8
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

'''   '''

#2. Segunda Parte------------------------------

#2.1
def es_genero(diccionario_heroe : dict, valor_genero : str)-> bool:
    '''
    verifica si el heroe es del genero buscado.
    recibe un diccionario heroe.
    devuelve un boolean
    '''
    return diccionario_heroe["genero"] == valor_genero
 

#2.2
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
    name_path_archivo_genero = "Desafio_Stark_5-Archivos\heroes_{0}.csv".format(
        genero_buscado)
    resultado_boleano = guardar_archivo(name_path_archivo_genero, cadena)
    return resultado_boleano
                    


#3. Tercera Parte------------------------------
#3.1
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


#3.2
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


#3.3
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


#3.4
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
    


#4. Cuarta Parte------------------------------

#4.1
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


#4.2
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




def dividir(dividendo, divisor )-> float:
    '''
    realiza la division entre dos numeros
    recibe un dividendo Int o Float, y un divisor int o float
    devuelve el resultado (float) o en caso de error 0
    '''
    if divisor != 0 and isinstance(dividendo, (int, float)) and isinstance(
        divisor, (int, float)):
        return dividendo / divisor
    else:
        return 0
    
#4.3
def calcular_promedio_genero(
    lista_heroes : list[dict], clave_a_calcular : str, genero_buscado : str)-> float:
    '''
    calcula el promedio total segun necesidad en base a una lista de heroes
    recibe una lista de dicc heroes y una clave a calcular (ej: clave = "altura")
    devuelve el promedio
    '''
    resultado_acumulado = sumar_dato_heroe_genero(
        lista_heroes, clave_a_calcular,genero_buscado)
    cantidad_de_heroes = cantidad_heroes_genero(lista_heroes, genero_buscado)
    promedio = dividir(resultado_acumulado, cantidad_de_heroes)
    return promedio


#4.4
def stark_calcular_imprimir_guardar_promedio_altura_genero(
    lista_heroes : list[dict], genero_buscado : str)-> bool:
    '''
    imprime el promedio de la altura segun genero y la guarda a formato csv.
    Recibe (arg 1) la lista de heroes, y (arg 2) genero buscado ("F", "M")
    Devuelve True en caso de generar el archivo correctamente.
    '''
    if(lista_heroes):
        clave_a_calcular = "altura"
        resultado_promedio = calcular_promedio_genero(
            lista_heroes, clave_a_calcular, genero_buscado)
        dato_promedio_genero = "Altura promedio genero {0}: {1}".format(
            genero_buscado, round(resultado_promedio, 2))
        print_dato(dato_promedio_genero) 

        name_path_archivo_genero = "Desafio_Stark_5-Archivos\heroes_promedio_{0}_{1}.csv".format(
            clave_a_calcular, genero_buscado)
    
        resultado_booleano = guardar_archivo(
            name_path_archivo_genero, dato_promedio_genero)
        return resultado_booleano
    else:
        print("Error: Lista de héroes vacía.")



#5. Quinta Parte------------------------------

#5.1
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


#5.2
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
        
    

#5.3
def stark_calcular_cantidad_por_tipo(lista_heroes :list[dict], clave_buscada : str):
    '''
    calcula ña cantidad por tipo
    Recibe : (arg 1)Una Lista de heroes, (arg 2) una clave (ejemplo "color_ojos")
    Devuelve : 
    '''
    diccionario_resultados = calcular_cantidad_tipo(lista_heroes, clave_buscada)
    resultado_booleano = guardar_cantidad_heroes_tipo(
        diccionario_resultados, clave_buscada)
    return resultado_booleano
    


#6. Sexta Parte------------------------------
#6.1
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



#6.2

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

#6.3
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
        

#6.4
# set_heroes_tipo_nombre = obtener_lista_de_tipos(lista_heroes_prueba, clave_buscada="color_pelo")


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
              

#6.5
def guardar_heroes_por_tipo(
    diccionario_tipos_y_nombres : dict[str, list],clave_buscada : str):
    nueva_lista_tipos_y_nombres = []
    for clave, valor in diccionario_tipos_y_nombres.items():
        dato_str = "{0} {1}: {2}".format(clave_buscada, clave," | ".join(valor))
        nueva_lista_tipos_y_nombres.append(dato_str)
        
    name_path_archivo_genero ="Desafio_Stark_5-Archivos\heroes_segun_{0}.csv".format(
        clave_buscada)
    datos_a_guardar = '\n'.join(nueva_lista_tipos_y_nombres)
    
    resultado_booleano = guardar_archivo(
            name_path_archivo_genero, datos_a_guardar)
    
    return resultado_booleano



#6.6

def stark_listar_heroes_por_dato(lista_heroes : list[dict], clave_buscada : str):
    set_heroes_tipo_nombre = obtener_lista_de_tipos(lista_heroes, clave_buscada)
    dicc_heroe_por_tipo_nombre =  obtener_heroes_por_tipo(
        lista_heroes, set_heroes_tipo_nombre, clave_buscada)
    resultado_booleano = guardar_heroes_por_tipo(
        dicc_heroe_por_tipo_nombre, clave_buscada)
    
    return resultado_booleano




 #1.3
def  stark_marvel_app_5(lista_de_personajes: list[dict]):
    while(True):
        respuesta = stark_menu_principal_desafio_5()
        match(respuesta):
            case "A":
                stark_guardar_heroe_genero(lista_de_personajes, genero_buscado = "M")
            case "B":
                stark_guardar_heroe_genero(lista_de_personajes, genero_buscado = "F")
            case "C":
                stark_calcular_imprimir_guardar_heroe_genero(lista_de_personajes, 
                                             tipo_de_calculo ="maximo", 
                                             clave_buscada ="altura",
                                             genero_buscado ="M")
            case "D":
                stark_calcular_imprimir_guardar_heroe_genero(lista_de_personajes, 
                                             tipo_de_calculo ="maximo", 
                                             clave_buscada ="altura",
                                             genero_buscado ="F")
            case "E":
                stark_calcular_imprimir_guardar_heroe_genero(lista_de_personajes, 
                                             tipo_de_calculo ="minimo", 
                                             clave_buscada ="altura",
                                             genero_buscado ="M")
            case "F":
                stark_calcular_imprimir_guardar_heroe_genero(lista_de_personajes, 
                                             tipo_de_calculo="minimo", 
                                             clave_buscada ="altura",
                                             genero_buscado ="F")
            case "G":
                stark_calcular_imprimir_guardar_promedio_altura_genero(
                        lista_de_personajes, genero_buscado ="M")
            case "H":
                stark_calcular_imprimir_guardar_promedio_altura_genero(
                        lista_de_personajes, genero_buscado ="F")
            case "I":
                pass
            case "J":
                stark_calcular_cantidad_por_tipo(lista_de_personajes, clave_buscada = "color_ojos")
            case "K":
                stark_calcular_cantidad_por_tipo(lista_de_personajes, clave_buscada = "color_pelo")
            case "L":
                stark_calcular_cantidad_por_tipo(lista_de_personajes, clave_buscada = "inteligencia")
            case "M":
                stark_listar_heroes_por_dato(lista_de_personajes, clave_buscada = "color_ojos")
            case "N":
                stark_listar_heroes_por_dato(lista_de_personajes, clave_buscada = "color_pelo")
            case "O":
                stark_listar_heroes_por_dato(lista_de_personajes, clave_buscada = "inteligencia")
            case "Z":
                break
            case other:
                print("Opcion incorrecta")
        clear_console()




def main():
    ruta_del_archivo_json = "Desafio_Stark_5-Archivos\data_stark.json"
    lista_personajes_all_str = leer_archivo(ruta_del_archivo_json)
    lista_heroes_normalizada = stark_normalizar_datos(lista_personajes_all_str)
    stark_marvel_app_5(lista_heroes_normalizada) 
     
main()#Ejecucion del programa
