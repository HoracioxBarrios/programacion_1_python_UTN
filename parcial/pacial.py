import json
import os
import re

def clear_console() -> None:
    """
    Espera que el usuario ingrese enter 
    para reimprimir en consola las opciones.
    """
    _ = input('Presione una tecla para continuar...')
    os.system('cls')

def leer_archivo_json(nombre_path : str)-> list[dict]:
    '''
    Lee un archvo json.
    Recibe la ruta con el nombre de archivo .json.
    Devuelve una lista de jugadores.
    '''
    with open(nombre_path, "r", encoding='utf-8') as archivo:
        equipo = json.load(archivo)
    
        return equipo["jugadores"]

#1
def mostrar_nombres_posicion_o_ubicacion(
    lista_de_jugadores: list[dict] , ver_indice_del_jugador = False)-> None | int:
    '''
    Muestra los nombres y posicion dentro de la cnacha de cada jugador, 
    opcionalmente tambien su indice.
    Recibe:(arg 1) una lista de jugadores y (arg 2) opcional puede 
    elegir ver el indice donde esta cada jugador (ver indice = True).

    Devuelve: None o -1 en caso de lista vacia
    '''
    if(lista_de_jugadores):
        if(ver_indice_del_jugador):
            for indice in range(len(lista_de_jugadores)):
                dato_jugador = "Ubicacion {0}: {1}- {2}".format(
                    indice, lista_de_jugadores[indice]["nombre"], 
                    lista_de_jugadores[indice]["posicion"])
                print(dato_jugador)
        else:
            for indice in range(len(lista_de_jugadores)):
                dato_jugador = "{0}- {1}".format(
                    lista_de_jugadores[indice]["nombre"],
                    lista_de_jugadores[indice]["posicion"])
                print(dato_jugador)
    else:
        print("La lista está vacia")
        return -1
    
#2
def pedir_ingreso_de_numero_al_usuario(
    patron_re: str, mensaje_a_mostrar= "Ingrese un valor numérico: ") -> int | float:
    '''
    Pide al usuario que ingrese un numero por consola.
    Recibe: (arg1) un patrón Regex para validar el numero 
    y (arg2) un mensaje string para mostrar al usuario.
    Ejemplo: "Ingrese un valor numérico: " por defecto.
    
    Devuelve: el número ingresado, convertido a int o float.
    '''
    while True:
        mensaje = "{0}".format(mensaje_a_mostrar)
        numero_ingresado_str = input(mensaje)
        num_ingresado = re.findall(patron_re, numero_ingresado_str)
        if num_ingresado:
            resultado_num_str = "".join(num_ingresado)
            if resultado_num_str.count(".") == 1:
                resultado_num = float(resultado_num_str)
            elif resultado_num_str.count(".") == 0:
                resultado_num = int(resultado_num_str)
            return resultado_num
        else:
            print("Incorrecto: ingrese un número válido")


def comprobar_indice_valido(
    lista_jugadores : list[dict], indice_elegido: int)-> bool:
    '''
    Comprueba si el indice pasado por parametro es valido.
    Recibe: (arg1) lista_jugadores y (arg2) el numero (int ) que 
    representa al indice a evaluar en la lista. 
    un indice representa un jugador (diccionario). 
    Deveulve: boolean
    '''
    if(lista_jugadores):
        len_lista = len(lista_jugadores)
        if(indice_elegido >= 0 and indice_elegido < len_lista):
            return True
        else:
            return False
    else:
        print("La lista esta vacia")
        return False
    
def seleccionar_jugador_segun_indice(lista_jugadores : list[dict])-> int | None:
    '''
    De los jugadores existentes permite al usuario elegir uno  segun su indice.
    Recibe una lista de Jugadores.
    Devuelve: el indice del jugador elegido, o -1 en caso de ser lista vacia.
    '''
    if(lista_jugadores):
        while(True):
            mostrar_nombres_posicion_o_ubicacion(
                lista_jugadores, ver_indice_del_jugador =True)
            mensaje = ">>>>> Ingrese numero de (indice) del jugador para ver sus estadisticas: "
            indice_elegido = pedir_ingreso_de_numero_al_usuario(r"^[0-9]+$", mensaje)
            existe_indice = comprobar_indice_valido(lista_jugadores,
                                                    indice_elegido)
            if(existe_indice):
                return indice_elegido
            else:
                print(" Indice invalido, intente nuevamente...\n ")
                os.system('cls')           
    else:
        print("La lista está vacia")
        return -1

def preparar_mensaje_estadisticas_para_guardar(
    lista_jugadores: list[dict], indice_elegido: int)-> str | int:
    '''
    Arma o prepara el mensaje de estadisticas del jugador para 
    guardar a csv.
    Recibe: (arg 1) una lista de jugadores.
    (arg 2) el indice elegido por el usuario.(Int).
    Devuelve una cadena formateada para csv. 
    o si lista esta vacia -1.
    '''
    if(lista_jugadores):
        lista_titulo = ["Nombre", "Posicion"]
        lista_valores = []
        for indice in range(len(lista_jugadores)):
            if indice == indice_elegido:
                lista_valores.append(str(lista_jugadores[indice]["nombre"]))
                lista_valores.append(str(lista_jugadores[indice]["posicion"]))
                
        diccionario_estadist = lista_jugadores[indice]["estadisticas"]
        for clave, valor in diccionario_estadist.items():
            clave = str(clave).capitalize().replace("_", " ")
            lista_titulo.append(clave)
            lista_valores.append(str(valor))
        
        cadena_titulos = ",".join(lista_titulo)
        cadena_valores = ",".join(lista_valores)
        return "{0}\n{1}".format(cadena_titulos,cadena_valores)
    else:
        print("La lista está vacía")
        return -1


def preparar_mensaje_estadisticas_para_mostrar(
    lista_jugadores : list[dict], indice_elegido : int)-> str | int:
    '''
    Prerara el mensaje de estadisticas del jugador para mostrar 
    al usuario.
    Recibe: (arg 1) una lista de jugadores.(arg 2) el 
    indice elegido por el usuario.(Int).
    Devuelve una cadena formateada para mostrar al usuario. 
    o -1 si lista esta vacia.
    '''
    if(lista_jugadores):
        for indice in range(len(lista_jugadores)):
                if(indice == indice_elegido):
                    dato_nombre_y_posicion = "Nombre: {0}\nPosicion: {1}".format(
                        lista_jugadores[indice]["nombre"],
                        lista_jugadores[indice]["posicion"])
                    lista_estadisticas = []
                    diccionario_estadisticas = lista_jugadores[indice]["estadisticas"]
                    for clave, valor in diccionario_estadisticas.items():
                        clave = str(clave).capitalize().replace("_"," ")
                        dato_estadistica = "{0}: {1}".format(clave, valor)
                        lista_estadisticas.append(dato_estadistica)
        estadisticas = "\n".join(lista_estadisticas)
        nombre_estadisticas = "{0}\n{1}".format(
                dato_nombre_y_posicion, estadisticas)
        return nombre_estadisticas
    else:
        print("Lista vacia")
        return -1
    


def mostrar_o_guardar_texto_estadistica(
        lista_jugadores : list[dict], indice_elegido : int, para_guardar = False)-> str:
    '''
    prepara el texto si el ususario desea mostrarlo o guardardarlo
    Recibe: (arg 1) la lista de jugadores y (arg 2) el indice (int) 
    que eligio el usuario.
    Devuelve: la cadena de texto.
    '''
    if(para_guardar):
        mensaje = preparar_mensaje_estadisticas_para_guardar(
            lista_jugadores, indice_elegido)
        return mensaje
    else:
        mensaje = preparar_mensaje_estadisticas_para_mostrar(
            lista_jugadores, indice_elegido)
        return mensaje
#3
def guardar_a_csv(path_nombre : str, dato_a_guardar : str)-> None:
    '''
    Guarda datos str a archivo .csv
    Recibe (arg 1)el nombre con la ruta donde se va a guardar el archivo.
    arg(2) el dato a guardar (str).
    Retorna - (None).
    '''
    with open(path_nombre, "w") as archivo:
        archivo.write(dato_a_guardar)
        mostrar_mensaje_se_guardo_como(path_nombre)
        
        

def mostrar_mensaje_se_guardo_como(path_nombre : str)-> None:
    ''' 
    Toma del nombre_path el nombre y lo formatea para armar
    el mensaje 'se guardo el archivo ...' y lo muestra.
    Recibe (arg 1) el nombre_path (str).
    Devuelve: None
    '''
    nombre_en_str = sacar_nombre_de_cadena_con_regex(
        r"[a-zA-Z_]+\.[csv]{3}", path_nombre)
    nombre_str = "".join(nombre_en_str)
    print("Se guardó archivo como : {0}".format(nombre_str))

def si_no_del_usuario(mensaje_a_mostrar : str)-> bool:
    '''
    Pregunta al usuario si/no validando la respuesta.
    Recibe el mensaje a preguntar.
    Devuelve: boolean
    '''
    while(True):
        eleccion_user = input(mensaje_a_mostrar)
        eleccion_user = eleccion_user.lower()
        respuesta_lista = re.findall(r"^[si]{2}$|^[no]{2}$",eleccion_user)
        respuesta_str = "".join(respuesta_lista)
        if(respuesta_str == "si"):
            return True
        elif(respuesta_str == "no"):
            return False
        else:
           print(" Elija una Opcion valida...")
          
def desea_guardar_como_archivo_csv(path_nombre : str, dato_a_guardar : str)-> None:
    '''
    Pregunta al usuario si quiere guardar el archivo a csv.
    Recibe (arg 1) el nombre con la ruta donde se va a gudardar(str).
    (arg 2) el dato a guardar(str).
    Devuelve: None.
    '''
    mensaje = ">>>>> Desea Guardarlo como archivo? si/no "
    respuesta = si_no_del_usuario(mensaje)
    if(respuesta):
        guardar_a_csv(path_nombre, dato_a_guardar)
    else:
        print(" Eligió no guardar")
        
    
def mostrar_estadisticas_del_jugador_elegido( lista_jugadores : list[dict])-> int:
    '''
    Permite al usuario elecionar un indice, muestra las estadisticas del 
    jugador elegido.
    Recibe: La lista de Jugadores.
    Devuelve el indice (ubicacion del jugador elegido).
    '''
    indice_elegido = seleccionar_jugador_segun_indice(lista_jugadores)
    nombre_mas_estadisticas_para_mostrar = mostrar_o_guardar_texto_estadistica(
        lista_jugadores, indice_elegido, para_guardar= False)
    print("{0}".format(nombre_mas_estadisticas_para_mostrar))
    return indice_elegido


def sacar_nombre_de_cadena_con_regex(exprecion_re_nombre :str, cadena : str)-> str:
    ''' 
    De una cadena toma el nombre del jugador segun expresion regular.
    Recibe una expresion regular para tomar el nombre,
    (arg 2)la cadena str.
    Devuelve el nombre del jugador.
    '''
    nombre_lista = re.findall(exprecion_re_nombre, cadena)
    nombre_str = "".join(nombre_lista)
    return nombre_str


def guardar_estadisticas_del_jugador_elegido(
    lista_jugadores : list[dict], indice_elegido : int)-> None:
    '''
    Permite guardar a archivo csv las estadisticas del jugador
    antes elegido.
    Recibe: (arg 1) la lista de jugadores, y (arg 2) el indice
    ulbicacion del jugador.
    Devuelve - None
    '''
    nombre_mas_estadisticas_para_mostrar = mostrar_o_guardar_texto_estadistica(
        lista_jugadores, indice_elegido, para_guardar= False)
    nombre_del_jugador_con_espacios =sacar_nombre_de_cadena_con_regex(
        r"Nombre: (.*)", nombre_mas_estadisticas_para_mostrar)
    nombre_del_jugador_guion_con_bajo = nombre_del_jugador_con_espacios.replace(" ", "_")
    path_nombre_formateado = \
        "parcial\estadisticas_por_jugador\estadisticas_del_jugador_{0}.csv".format(
        nombre_del_jugador_guion_con_bajo)
    nombre_mas_estadisticas_para_guardar = mostrar_o_guardar_texto_estadistica(
        lista_jugadores, indice_elegido, para_guardar= True)
    desea_guardar_como_archivo_csv(
        path_nombre_formateado,nombre_mas_estadisticas_para_guardar)


#4
def mostrar_nombres_jugadores_ordenados(lista_jugadores : list[dict])-> None:
    '''
    Muestra los nombres de los jugadores ordenados.
    Recibe la lista de jugadores.
    Devuelve - None
    '''
    lista_nombres_ordenados = ordenar_lista_dicc_bubble_sort(lista_jugadores, clave="nombre")
    for jugador in lista_nombres_ordenados:
        print("{0}".format(jugador["nombre"]))


def pedir_nombre_y_apellido_jugador()-> str:
    '''
    Pide el nombre y apellido del jugador.
    Recibe - no aplica
    Devuelve - el nombre con apellido validado
    '''
    nombre_apellido = input(
        ">>>>>> Ingrese nombre y apellido del jugador a Buscar ")
    nombre_apellido_cap = str(nombre_apellido).capitalize()
    nombre_validado = sacar_nombre_de_cadena_con_regex(
        r"^[A-Za-z]+\s{1}[A-Za-z]+$", nombre_apellido_cap)
    return nombre_validado.lower().strip()

def buscar_jugador_y_ver_sus_logros(lista_jugadores: list[dict])-> None:
    '''
    Permite ingresar nombre y apellido del jugador para ver sus
    logros obtenidos.
    Recibe la lista de jugadores.
    Devuelve - None ---
    '''
    mostrar_nombres_jugadores_ordenados(lista_jugadores)
    nombre_ingresado_lower = pedir_nombre_y_apellido_jugador()
    encontrado = False
    for jugador in lista_jugadores:
        if jugador["nombre"].lower().strip() == nombre_ingresado_lower:
            encontrado = True
            print("---- jugador encontrado ----")
            cadena_logros = "Nombre del Jugador: {0}\n{1}".format(
                jugador["nombre"], "\n".join(jugador["logros"]))
            print(cadena_logros)
    if encontrado == False:
        print(" No existe el nombre en la lista")

#5
def calcular_promedio_de_puntos_equipo(lista_jugadores : list[dict])-> float:
    '''
    Calcula el promedio de puntos por partido de todo el equipo 
    Dream team.
    Recibe la lista de jugadores. List
    Devuelve el promedio (Float)
    '''
    cantidad_de_jugadores = len(lista_jugadores)
    acum_promedio_jugador_puntos_por_partido = 0
    for jugador in lista_jugadores:
        dicc_estadisticas_jugador = jugador["estadisticas"]
        for clave, valor in dicc_estadisticas_jugador.items():
            if(clave == "promedio_puntos_por_partido"):   
                acum_promedio_jugador_puntos_por_partido += valor
    promedio_equipo = acum_promedio_jugador_puntos_por_partido / cantidad_de_jugadores
    
    return promedio_equipo


def ordenar_lista_dicc_bubble_sort(
    lista_original : list[dict], clave = "nombre", orden = "asc")-> list | int:
    '''
    Ordena los elementos de una lista de jugadores segun clave.
    Recibe: (arg 1) una lista de jugadores, (arg2) una clave ej:("nombre"),
    (arg 3) el orden( "asc" o "desc").
    Devuelve: una lista de nombres ordenada alfabeticamente. list[dict]
    o -1 si la lista esta vacia.
    '''
    if(lista_original):
        lista = lista_original[:]
        len_lista = len(lista) - 1
        flag_swap = True
        while flag_swap:
            flag_swap = False
            for indice in range(len_lista):
                if lista[indice][clave] > lista[indice + 1][clave] and orden == "asc":
                    lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
                    flag_swap = True
                if lista[indice][clave] < lista[indice + 1][clave] and orden == "desc":
                    lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
                    flag_swap = True
        len_lista -= 1
        return lista
    else:
        print("La lista está vacia")
        return -1

def calcular_y_mostrar_el_promedio_de_puntos_del_dream_team(
    lista_jugadores: list[dict], clave="promedio_puntos_por_partido")-> None | int:
    '''
    Calcula y muestra el promedio de puntos del dream team, luego el promedio
    individual de cada uno.
    Recibe la lista de jugadores.
    No devuelve ningún valor.
    '''
    if(lista_jugadores):
        mensaje_promedio_de_equipo = calcular_promedio_de_puntos_equipo(lista_jugadores)
        print(
            "El promedio de puntos por partido de TODO EL EQUIPO es: >>>>> {0}".format(
                round(mensaje_promedio_de_equipo, 2)))

        lista_ordenada_alfabeticamente = ordenar_lista_dicc_bubble_sort(
            lista_jugadores, clave="nombre", orden="asc")
        for jugador in lista_ordenada_alfabeticamente:
            print("Nombre: {0} - Promedio de puntos por partido: {1}".format(
                jugador["nombre"], jugador["estadisticas"][clave]))
    else:
        print("La lista está vacia")
        return -1
    
# 6
def buscar_jugador_para_ver_logro(
    lista_jugadores: list[dict], clave_nombre="nombre", clave_logros="logros",
    valor_logro="Miembro del Salon de la Fama del Baloncesto", 
    mensaje_a_mostrar_en_print="Pertenece")-> None:
    '''
    Permite al usuario ingresar el nombre de un jugador para ve un logro.
    ejemplo : si pertenece al salon de la fama.
    Recibe (arg ) la lista de jugadores, (arg 2) la clave_logros 
    ejemplo ="logros", (arg 3) valor_logro ejemplo = "Miembro del Salon de 
    la Fama del Baloncesto",
    (arg 4)mensaje_a_mostrar_en_print ejemplo ="Pertenece".
    Deveulve : None
    '''
    mostrar_nombres_jugadores_ordenados(lista_jugadores)
    nombre_ingresado_lower = pedir_nombre_y_apellido_jugador()
    encontrado = False
    flag_ok_condicion = False
    for jugador in lista_jugadores:
        if jugador[clave_nombre].lower().strip() == nombre_ingresado_lower:
            encontrado = True
            print("---- jugador encontrado ----")
            for logro in jugador[clave_logros]:
                if logro == valor_logro:
                    flag_ok_condicion = True
                elif logro != valor_logro:
                    flag_ok_condicion = False 
            break     
    if encontrado:
        if flag_ok_condicion:
            print("{0}: {1}".format(mensaje_a_mostrar_en_print, valor_logro))
        else:
            print("No {0} como: {1}".format(mensaje_a_mostrar_en_print, valor_logro))

#7
def calcular_max_min_estadisticas(
    lista_jugadores: list[dict], clave_estadistica = "estadisticas",
    clave_interior_estadistica = "rebotes_totales", maximo = True)-> int:
    '''
    Calcula el maximo o minimo de las estadisticas segun clave.
    Recibe: (arg 1) La lista de jugadores, (arg 2) la clave "estadisticas,
    (arg 3) la clave interior del diccionario estadisticas ej: "rebotes_totales",
    (arg 4) si maximo o minimo (maximo = True) por defecto.
    '''
    if(lista_jugadores):
        flag_primera_iteracion = True
        for indice in range(len(lista_jugadores)):
            diccionario_estadisticas = lista_jugadores[indice][clave_estadistica]
            valor_estadistica = diccionario_estadisticas[clave_interior_estadistica]
            
            if(flag_primera_iteracion or 
            (valor_estadistica > max_min_estadistica and maximo == True) or 
            (valor_estadistica < max_min_estadistica and maximo == False)): 
                max_min_estadistica = valor_estadistica
                max_min_indice = indice
                flag_primera_iteracion = False    
        return max_min_indice
    else:
        print("La lista está vacia")
        return -1

def armar_diccionario_jugador_max_min_estadisticas(
    lista_jugadores : list[dict], max_min_indice : int,clave_estadistica = "estadisticas",
    clave_interior_estadistica = "rebotes_totales")-> dict | int:
    '''
    Arma un diccionario con el nombre y la estadistica maxima o minima 
    obtenida. ejemplo: Nombre : Michael Jordan, Rebotes totales : 3520.
    Recibe (arg 1 ) la lista de jugadores, (arg 2) el indice maximo o
    minimo obtenido anteriormente. 
    (arg 3) la clave "estadisticas", (arg 4) la clave de la estadistica
    especifica del diccionario (Ejemplo : "rebotes_totales").
    '''
    if max_min_indice is None:
        print("Error al conseguir el jugador con la maxima o minima estadistica")
        return -1
    else:
        jugador_max_min_obtenido = lista_jugadores[max_min_indice]
        
        nuevo_dicc_nombre_estadistica_max_min = {}
        nuevo_dicc_nombre_estadistica_max_min["nombre"] = jugador_max_min_obtenido["nombre"]
        nuevo_dicc_nombre_estadistica_max_min[clave_interior_estadistica] = \
            jugador_max_min_obtenido[clave_estadistica][clave_interior_estadistica]
    
        return nuevo_dicc_nombre_estadistica_max_min


def preparar_datos_nombre_estadistica_de_diccionario_a_texto(
    diccionario_nombre_estadistica : dict)-> str:
    '''
    De un diccionario estadisticas prepara una cadena str.
    Recibe: el diccionario con los datos por ejemplo:  
    Nombre : Michael Jordan, Rebotes totales : 3520
    
    Devuelve una cadena formateada para imprimir por consola.
    con formato:
    Nombre: karl malone
    Rebotes totales: 14968
    '''
    if(diccionario_nombre_estadistica):
        pares_clave_valor = []
        for clave, valor in diccionario_nombre_estadistica.items():
            texto_par = "{0}: {1}".format(clave, valor)
            pares_clave_valor.append(texto_par.capitalize().replace("_", " "))

        cadena = "\n".join(pares_clave_valor)
        return cadena
    else:
        print("Esta vacio")
        return -1

def calcular_y_mostrar_jugador_mayor_estadistica(
    lista_jugadores : list[dict], clave_estadistica = "estadisticas", 
    clave_interior_estadistica = "rebotes_totales")-> None:
    '''
    Calcula y muestra el nombre con su maxima estadistica, segun clave.
    se muestra con formato:
    Nombre: karl malone
    Rebotes totales: 14968
    Recibe (arg 1)la lsita de jugadores, (arg 2) la clave estadisticas,
    (arg 3) la clave de la estadistica ejemplo ("rebotes_totales").
    Devuelve: None
    '''
    max_min_indice = calcular_max_min_estadisticas(
    lista_jugadores, clave_estadistica,clave_interior_estadistica, maximo= True)
    
    jugador_estadistica_dicc = armar_diccionario_jugador_max_min_estadisticas(
    lista_jugadores, max_min_indice ,clave_estadistica,
    clave_interior_estadistica)
    
    cadena = preparar_datos_nombre_estadistica_de_diccionario_a_texto(
        jugador_estadistica_dicc)
    print("{0}".format(cadena))

#8 - 9 - 10
def jugadores_mayores_al_ingresado(lista_jugadores: list[dict], clave_estadistica, 
    clave_interior_estadistica)-> list[dict]:
    '''
    Permite ingresar un valor y busca los que superan ese valor.
    Recibe: (arg 1) la lista de jugadores, 
    (arg 2) clave dicc estadisticas ejemplo "estadisticas".
    (arg 3) la clave dentro del dicc estadisticas (ej: "promedio_puntos_por_partido"))
    Devuelve una nueva lista con los jugadores que cumplen el requisito. 
    '''
    nueva_lista_Jugadores = []
    mensaje_a_mostrar = "Ingrese un valor numérico: "
    numero_ingresado = pedir_ingreso_de_numero_al_usuario(r"^[0-9]+|\.[0-9]+$",
                                                          mensaje_a_mostrar)
    encontrado = False
    for jugador in lista_jugadores:
        if jugador[clave_estadistica][clave_interior_estadistica] > numero_ingresado:
            nueva_lista_Jugadores.append(jugador)
            encontrado = True
    if encontrado == False:
        print("Nadie cumple con la condicion")
    else:
        return nueva_lista_Jugadores
    
def mostrar_estadisticas_jugadores(
    lista_jugadores : list[dict],clave_estadistica = "estadisticas", 
    clave_interior_estadistica = "promedio_puntos_por_partido")-> None:
    '''
    Muestra las estadisticas de los jugadores.
    Recibe (arg 1) la lista de jugadores. y (arg 2) la clave del dicc 
    estadistica ) "estadisticas", (arg 3) la clave del dicc de la 
    estadistica por ejemplo "promedio_puntos_por_partido".
    Retorna - None
    '''
    clave_interior_estadistica_guion = \
        clave_interior_estadistica.replace("_"," ").capitalize()
    for jugador in lista_jugadores:
        nombre = jugador["nombre"]
        valor_estadistica = jugador[clave_estadistica][clave_interior_estadistica]
        print("{0}: {1}: {2}".format(
            nombre, clave_interior_estadistica_guion, valor_estadistica))
        
        
def mostrar_jugadores_mayores_al_ingresado(
    lista_jugadores : list[dict], clave_estadistica = "estadisticas", 
    clave_interior_estadistica = "promedio_puntos_por_partido")-> None | int:
    '''
    Permite ingresar un valor, busca y muestra por consola los que 
    superan ese valor.
    Recibe: (arg 1) una lista de jugadores,(arg 2) clave de estadistica
    "estadisticas" , (arg 3) clave del dicc de la estadistica. 
    ejemplo: "promedio_puntos_por_partido".
    Devuelve None o -1 si No se obtuvo la lista_obtenuida.
    '''
    lista_jugadores_obtenida = jugadores_mayores_al_ingresado(
        lista_jugadores, clave_estadistica, clave_interior_estadistica)
    if(lista_jugadores_obtenida):
        mostrar_estadisticas_jugadores(
            lista_jugadores_obtenida,clave_estadistica, 
            clave_interior_estadistica)
    else:
        return -1
    
#11 -12 - 13 -14 -15 -16

def quitar_el_menos_habil_segun_clave_estadistica(
    lista_jugadores : list[dict], clave_estadisticas = "estadisticas",
    clave_interior_estadistica = "promedio_puntos_por_partido")-> list[dict]:
    '''
    De la lista quita el menos habil segun estadistica.
    Recibe: (arg 1) la lista de jugadores, (arg 2) la clave "estadistica",
    (arg 3) la clave de la estadistica a evaluar. ejemplo :
    "promedio_puntos_por_partido".
    Devuelve una nueva lista de jugadores sin el menos habil.
    o -1 si la lista esta vacia.
    '''
    if(lista_jugadores):
        indice_jugador_menos_habil = calcular_max_min_estadisticas(
            lista_jugadores, clave_estadisticas, clave_interior_estadistica, 
            maximo= False)
        nueva_lista_jugadores = []
        for indice in range(len(lista_jugadores)):
            if(indice != indice_jugador_menos_habil):
                nueva_lista_jugadores.append(lista_jugadores[indice])
        return nueva_lista_jugadores
    else:
        print("La lista está vacia")
        return -1


def calcular_y_mostrar_el_promedio_de_puntos_del_dream_team_sin_el_menos_habil(
    lista_jugadores : list[dict], clave_estadisticas = "estadisticas", 
    clave_interior_estadistica = "promedio_puntos_por_partido")-> None | int:
    '''
    Calcula y muestra el promedio de puntos del dream team sin incluir al 
    menos habil segun estadistica.
    Recibe (arg 1) la lista de jugadores, (arg 2): clave :"estadisticas", 
    (arg 3) la clave de la estadistica a evaluar. ej: "promedio_puntos_por_partido".
    Devuelve - None o -1
    '''
    if(lista_jugadores):
        nueva_lista_sin_el_menos_habil = quitar_el_menos_habil_segun_clave_estadistica(
            lista_jugadores, clave_estadisticas, clave_interior_estadistica)
        calcular_y_mostrar_el_promedio_de_puntos_del_dream_team(
            nueva_lista_sin_el_menos_habil)
    else:
        return -1

#17

def calcular_jugador_con_mas_logros(
    lista_jugadores : list[dict], maximo = True)-> None | int:
    '''
    Calcula el jugador con mas o menos logros y lo muestra.
    Recibe (arg 1) la lista de jugadores, (arg 2) maximo o minimo
    por defecto maximo = True
    Devuelve: None o  -1 en caso de error.
    '''
    if(lista_jugadores):
        flag_max_min = True
        for indice in range(len(lista_jugadores)):
            lista_logros =  lista_jugadores[indice]["logros"]
            cantidad_logros = len(lista_logros)
            
            if(flag_max_min or (cantidad_logros > max_min_logros and maximo == True) 
               or (cantidad_logros < max_min_logros and maximo == False)):
                max_min_logros = cantidad_logros
                max_min_indice = indice
                flag_max_min = False
        if(maximo):
            print("{0} es el jugador con mas logros con: {1}".format(
                lista_jugadores[max_min_indice]["nombre"], max_min_logros))
        else:
            print("{0} es el jugador con menos logros con: {1}".format(
            lista_jugadores[max_min_indice]["nombre"], max_min_logros))
    else:
        print("La lista esta vacia")
        return -1
# 18 - 19
#20
def mostrar_estadistica_ordenado_por_posicion(
    lista_jugadores : list, clave_estadistica = "estadisticas", 
    clave_interior_estadistica = "porcentaje_tiros_de_campo",
    mensaje = "Posicion en la cancha")-> None | int:
    '''
    Permite ingresar un valor y ver los que jugadores que lo superan ordenado
    por posicion en la cancha..
    Recibe: (arg 1) la lista de jugadores, (arg 2) la clave del dicc estadistica = 
    "estadisticas", 
    (arg 3) la clave de la estadistica a evaluar = "porcentaje_tiros_de_campo".
    mensaje a mostrar en el print (mensaje = "Posicion en la cancha").
    Devuelve: None o -1 
    '''
    if(lista_jugadores):
        lista_ordenada_jugadores = ordenar_lista_dicc_bubble_sort(lista_jugadores, 
                                                       clave="posicion", orden="asc")
        lista_de_jugadores_que_superan = jugadores_mayores_al_ingresado(
            lista_ordenada_jugadores,clave_estadistica,
            clave_interior_estadistica= "porcentaje_tiros_de_campo")
        
        if(lista_de_jugadores_que_superan):
            for jugador in lista_de_jugadores_que_superan:
                print("{0}: Nombre: {1} : {2} : {3} {4}".format(
                    mensaje, jugador["posicion"], jugador["nombre"],
                    clave_interior_estadistica, 
                    jugador["estadisticas"]["porcentaje_tiros_de_campo"]))
    else:
        print("La lista está vacia")
        return -1
#23

def filtrar_estadistica(lista_jugadores : list[dict],clave_a_evaluar= "puntos_totales" ):
    '''
    Filtra una lista de dict y arma una nueva lista dict con los datos:
    [{'nombre': 'Magic Johnson', 'puntos_totales': 17707},...]
    Recibe una lista de jugadores list [dict] y una clave ejemplo:
    "puntos_totales"
    Devuelve una lista de dict con los datos listos para ordenar
    segun necesidad.
    '''
    lista_nombres_estadisticas_a_ordenar = []
    
    for jugador in lista_jugadores:
        nuevo_dicc = {}
        nombre = jugador["nombre"]
        dicc_estadistica = jugador["estadisticas"]
        nuevo_dicc["nombre"] = nombre
        for clave, valor in dicc_estadistica.items():
            if clave == clave_a_evaluar:
                nuevo_dicc[clave] = valor
                lista_nombres_estadisticas_a_ordenar.append(nuevo_dicc)
    return lista_nombres_estadisticas_a_ordenar            
   


def ordena_por_estadisticas(
        lista_jugadores : list[dict], clave_a_evaluar, orden):
    '''
    Ordena las estadisticas de una lista de diccionarios, segun clave.
    Recibe una lista de jugadores original.
    Devuelve una lista de dicc con las estadisticas ordenada.
    "asc"  o "desc".
    '''
    lista_a_ordenar_nombre_estadistic = filtrar_estadistica(
        lista_jugadores, clave_a_evaluar)
    lista_ordenada = ordenar_lista_dicc_bubble_sort(
        lista_a_ordenar_nombre_estadistic,clave_a_evaluar, orden)

    return lista_ordenada


def armar_lista_detalle_estadisticas_ranking(
        lista_original : list[dict])-> list[dict]:
    '''
    De una lista de jugadores por estadisticas y las lista en una nueva.
    Recibe una lista de jugadores original.
    Devuelve una lista de dicc con los jugadores ordenados por ranking.
    '''
    list_detalles = []
    lista_claves = [
        "puntos_totales", "rebotes_totales", "asistencias_totales", "robos_totales"]
    for jugador in lista_original:
        nuevo_diccionario = {}
        nombre = jugador["nombre"]
        for clave in lista_claves:
            lista_ordenada = ordena_por_estadisticas(
                lista_original, clave, orden="desc")
            ranking_obtenuido = traer_valor_ranking(lista_ordenada, nombre)
            nuevo_diccionario["nombre"] = nombre
            nuevo_diccionario[clave] = ranking_obtenuido
        list_detalles.append(nuevo_diccionario)
    return list_detalles


def traer_valor_ranking(lista_ordenada : list[dict], nombre :str)-> int:
    '''
    de una lista ordenada verifica que el nombre sea igual
    al ingresado por parametro si es asi trae el valor
    que representa el puesto de ese jugador en el ranking
    de por ejemplo: "robos totales"
    Recibe una lista ordenada desde estadistica mas alta
    a mas baja (orden descendente)
    Devuelve el indice que simboliza el numero que le corresponde
    al jugador en el ranking.
    '''
    for indice in range(len(lista_ordenada)):
        if(lista_ordenada[indice]["nombre"] == nombre):
            return indice +1


def preparar_mensaje_para_guardar(
    lista_jugadores: list[dict])-> str | int:
    '''
    Prepara el mensaje de estadisticas de los jugadores para 
    guardar a csv.
    Recibe: (arg 1) una lista de jugadores.
    (arg 2) el indice elegido por el usuario.(Int).
    Devuelve una cadena formateada para csv. 
    o si lista esta vacia -1.
    '''
    flag_primer_jugador = True
    if(lista_jugadores):
        header_list = []
        values_list = []
        for jugador in lista_jugadores:
            for clave, valor in jugador.items():
                clave_refactorizada = str (clave).replace("_"," ").capitalize()
                if(flag_primer_jugador):
                    values_list.append(str(valor))
                else:
                    if(clave == "nombre"):
                        valor_con_espacio = "\n{0}".format(valor)
                        values_list.append(str(valor_con_espacio))
                    else:
                        values_list.append(str(valor))
                if(clave_refactorizada not in header_list):
                    header_list.append(clave_refactorizada)
                flag_primer_jugador = False

            cadena_valores = ",".join(values_list)
            cadena_valores = cadena_valores.strip()
    cadena_valores +="\n{0}".format(cadena_valores)
    cadena_titulos = ",".join(header_list)
    
    resultado = "{0}\n{1}".format(cadena_titulos, cadena_valores)
    path = "parcial\detalles\detalles_ranking_de_estadisticas.csv"
    desea_guardar_como_archivo_csv(path, resultado)

    
def ordenar_y_guardar_ranking_de_jugadores(lista_jugadores : list[dict])-> None:
    '''
    Ordena y guarda a csv los datos de los jugadores rankeados.
    Recibe la lista de jugadores.
    Devuelve - None
    '''
    lista_detalles_estadisticas_ranking = armar_lista_detalle_estadisticas_ranking(
        lista_jugadores)
   
    preparar_mensaje_para_guardar(lista_detalles_estadisticas_ranking)


#--------------------------------------------------  

#--Menú y ejecucion de la app
def opciones_del_menu()-> str:
    '''
    Opciones del menu.
    Recibe: No aplica.
    Devuelve: una cadena str .
    '''
    opciones = "Bienvenido:\n" \
           "1- Ver Jugadores y Posición de todos los jugadores del Dream Team.\n" \
           "2- Seleccionar un jugador para ver sus estadísticas (Opcional: guardar-en la opcion 3).\n" \
           "3- Guardar estadísticas del jugador seleccionado anteriormente.\n" \
           "4- Buscar un jugador por su nombre para ver sus logros.\n" \
           "5- Ver el promedio de puntos por partido de todo el equipo del Dream team.\n"\
           "6- Ver si el jugador ingresado pertenece al salon de la fama.\n" \
           "7- Ver el jugador con la mayor cantidad de rebotes totales.\n" \
           "8- Ver el jugador con el mayor porcentaje de tiros de campo.\n" \
           "9- Ver el jugador con el mayor cantidad de asistencias totales.\n"\
           "10- Ver los jugadores que tienen el promedio de más puntos por partido que el valor ingresado.\n"\
           "11- Ver los jugadores que tienen el promedio de mas rebotes por partido que el valor ingresado.\n"\
           "12- Ver los jugadores que tienen el promedio asistencias por partido mayor que el valor ingresado.\n"\
           "13- Ver el jugador con la mayor cantidad de robos totales.\n"\
           "14- Ver el jugador con la mayor cantidad de bloqueos totales.\n"\
           "15- Ver los jugadores que tienen el porcentaje de tiros libres superior al valor ingresado.\n"\
           "16- Ver el promedio de puntos por partido del equipo excluyendo al jugador con la menor puntos.\n"\
           "17- Ver el jugador con la mayor cantidad de logros obtenidos.\n"\
           "18- Ver los jugadores que hayan tenido un porcentaje de tiros triples superior al valor ingresado.\n"\
           "19- Ver el jugador con la mayor cantidad de temporadas jugadas.\n"\
           "20- Ver los jugadores ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros \nde campo superior al valor ingresado.\n"\
           "21- Opcion no disponible\n"\
           "22- Opcion no disponible\n"\
           "23- Guardar ranking de les estadisticas de los jugadores (Opcional: guardar)"\
           "24- Salir"
           
           
    ''       
    return opciones

def menu_principal()-> int:
    '''
    Imprime el menu y toma una opcion del usuario
    recibe -no aplica
    devuelve la opcion elegida, en caso de False devuelve -1
    '''
    opciones_para_el_usuario = opciones_del_menu()
    print(opciones_para_el_usuario)
    mensaje_a_mostrar = "Por favor ingrese una opcion: "
    numero_ingresado = pedir_ingreso_de_numero_al_usuario(r"^[0-9]+$", mensaje_a_mostrar)
    return numero_ingresado
   
   
def aplicacion(lista_Jugadores : list[dict])-> None:
    '''
    Opciones para el usuario
    Recibe la lista de Jugadores
    Devuelve: no aplica.
    '''
    flag_guardar_estadisticas = False
    while(True):
        opciones = menu_principal()
        match(opciones):
            case 1:
                mostrar_nombres_posicion_o_ubicacion(lista_Jugadores)
            case 2:
                indice_elegido = mostrar_estadisticas_del_jugador_elegido(
                    lista_Jugadores)
                flag_guardar_estadisticas = True
            case 3:
                if(flag_guardar_estadisticas):
                    guardar_estadisticas_del_jugador_elegido(
                        lista_Jugadores, indice_elegido)
                else:
                    print("Pase por el punto 2 primero")
            case 4:
                buscar_jugador_y_ver_sus_logros(
                    lista_Jugadores)
            case 5:
                calcular_y_mostrar_el_promedio_de_puntos_del_dream_team(
                    lista_Jugadores)
            case 6:
                buscar_jugador_para_ver_logro(lista_Jugadores)
            case 7:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, 
                    clave_interior_estadistica = "rebotes_totales")
            case 8:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, 
                    clave_interior_estadistica = "porcentaje_tiros_de_campo")
            case 9:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, 
                    clave_interior_estadistica = "asistencias_totales")
            case 10:
                mostrar_jugadores_mayores_al_ingresado(
                    lista_Jugadores, 
                    clave_interior_estadistica = "promedio_puntos_por_partido")
            case 11:
                mostrar_jugadores_mayores_al_ingresado(
                    lista_Jugadores, 
                    clave_interior_estadistica = "promedio_rebotes_por_partido")
            case 12:
                mostrar_jugadores_mayores_al_ingresado(
                    lista_Jugadores, 
                    clave_interior_estadistica = "promedio_asistencias_por_partido")
            case 13:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, 
                    clave_interior_estadistica = "robos_totales")
            case 14:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, 
                    clave_interior_estadistica = "bloqueos_totales")
            case 15:
                mostrar_jugadores_mayores_al_ingresado(
                    lista_Jugadores, 
                    clave_interior_estadistica = "porcentaje_tiros_libres")
            case 16:
                    calcular_y_mostrar_el_promedio_de_puntos_del_dream_team_sin_el_menos_habil(
                        lista_Jugadores, 
                        clave_interior_estadistica = "promedio_puntos_por_partido")
            case 17:
                calcular_jugador_con_mas_logros(lista_Jugadores, maximo = True)
            case 18:
                mostrar_jugadores_mayores_al_ingresado(
                    lista_Jugadores, 
                    clave_interior_estadistica = "porcentaje_tiros_triples")
            case 19:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, clave_interior_estadistica = "temporadas")
            case 20:
                mostrar_estadistica_ordenado_por_posicion(lista_Jugadores)
            case 21:
                print("No está dispinible esta opcion")
            case 22:
                print("No está dispinible esta opcion")
            case 23:
                ordenar_y_guardar_ranking_de_jugadores(lista_Jugadores)
            case 24:
                break
            case _:
                print("Opcion incorrecta, por favor intente nuevamente.")
        clear_console()
 
        

def main()-> None:
    '''
    Ejecuta la aplicacion
    Recibe: -
    Devuelve: -No aplica
    '''
    lista_jugadores = leer_archivo_json("parcial\dt.json")
    aplicacion(lista_jugadores)
    

main()#Inicio del programa