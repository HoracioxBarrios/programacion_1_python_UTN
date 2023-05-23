import os
import re
import json
def leer_archivo_json(nombre_path : str)-> list[dict]:
    with open(nombre_path, "r") as archivo:
        lista_heroe = json.load(archivo)
        return lista_heroe["heroes"]


#normalizamos
def stark_normalizar_datos(lista_heroes: list[dict]) -> list[dict] | str:
    '''
    Verifica y normaliza los valores si son numericos.
    Recibe: una list[dict] personajes
    Devuelve: una nueva lista de heroes con datos normalizados    
    '''
    nueva_lista_normalizada = []
    if(lista_heroes):
        for heroe in lista_heroes:
            keys = list(heroe.keys())
            for key in keys:
                if(type(heroe[key]) is str):
                    valor_reemplazado : str = heroe[key].replace('.', '')
                    if(valor_reemplazado.isnumeric() and type(heroe[key]) is str):
                        if('.' in heroe[key] and heroe[key].count('.') == 1):
                            heroe[key] = float(heroe[key])
                        else:
                            heroe[key] = int(heroe[key])
                        print("El dato {0}fue modificado en el heroe {1}".format(
                            key, heroe["nombre"]))
            nueva_lista_normalizada.append(heroe)
        return nueva_lista_normalizada
    else:
        return "La lista esta Vacia"


def normalizar_valores_str_vacios(
    lista_heroe : list[dict], valor_que_reemplaza = "N/A")-> list[dict]:
    '''
    verifica los str vacios y los renombra segun criterio
    Recibe:(arg 1)Una lista de heroes, (arg2)el valor str reemplazante("N/A").
    Devuelve la lista corregida.
    '''
    for heroe in lista_heroe:
        for clave in heroe.keys():
            if(heroe[clave] == ""):
                heroe[clave] = valor_que_reemplaza
    return lista_heroe





'''
1. Listar los primeros N héroes. El valor de N será ingresado por el usuario
(Validar que no supere max. de lista)

'''


def ordenar_heroes_b_sort_clave(
    lista_heroes_original : list[dict], clave : str, ordenamiento = "asc")->list[dict]:
    '''
    Ordena una lista de heroes segun 'clave', y 'ordenamiento'.
    Recibe: (arg 1 )Una Lista de heroes, (arg 2) Una Clave ("altura",
    "fuerza", "peso"), (arg 3 ) Ordenamiento por defecto ascendente ("asc"),
    o se puede cambiar a Descendente ("desc").
    Devuelve la Lista ordenada, o en caso de estar vacia la lista, el mensaje:
    'Lista Vacia'
    '''
    if(lista_heroes_original):
        lista_heroes = lista_heroes_original[:]
        
        len_lista = len(lista_heroes) -1
        flag_swap = True
        while(flag_swap):
            flag_swap = False
            for indice in range(len_lista):
                if(lista_heroes[indice][clave] > lista_heroes[indice + 1][clave] 
                   and ordenamiento == "asc"):
                    lista_heroes[indice] , lista_heroes[indice +1] = \
                        lista_heroes[indice +1] , lista_heroes[indice]
                    flag_swap = True
                if(lista_heroes[indice][clave] < lista_heroes[indice + 1][clave] 
                   and ordenamiento == "desc"):
                    lista_heroes[indice] , lista_heroes[indice +1] = \
                        lista_heroes[indice +1] , lista_heroes[indice]
                    flag_swap = True
            len_lista -= 1
        return  lista_heroes            
    else:
        return "la lista está vacia"
    
    
def contar_elementos_en_lista(lista_de_heroes : list[dict])-> int:
    '''
    deduce cuantos elementos (heroes) hay en una lista
    recibe la lista de diccionarios heroes.
    devuelve la cantidad
    '''
    if(lista_de_heroes):
        cantidad_heroes = len(lista_de_heroes)
        return cantidad_heroes




def pedir_ingreso_de_numero(patron_re : str)-> int:
    '''
    Pide el usuario un numero.
    Recibe: no aplica
    Devuelve: el numero ingresado, casteado a int
    '''
    numero_ingresado_str = input("Por favor ingrese cantidad a ver: ")
    num_imgresado = re.findall(patron_re, numero_ingresado_str)
    if(num_imgresado):
        resultado_num_str = "".join(num_imgresado)
        resultado_num_int = int(resultado_num_str)
        return resultado_num_int
    else:
        print("Incorrecto, por favor ingrese un numero valido")   





def listar_por_cantidad_si_primeros_o_ultimos(
    lista_heroes_ordenada : list[dict], cantidad = 0,posicion= "primeros")-> list[dict]:
    '''
    Se encarga de listar segun cantidad primeros o ultimos.
    Recibe: (arg 1)Una lista de heroes ya ordenada,(arg 2)La 
    cantidad a listar, (el 0 es todos) o elejir otro numero,
    (arg 3) posicion 'primeros' o 'ultimos'.
    '''
    if(lista_heroes_ordenada):
        if(cantidad <= len(lista_heroes_ordenada) and posicion =="primeros"):
            lista_primeros = lista_heroes_ordenada[ : cantidad]
            return lista_primeros
        
        elif(cantidad <= len(lista_heroes_ordenada) and posicion =="ultimos"):
            lista_ultimos = lista_heroes_ordenada[-cantidad:]
            return lista_ultimos
        
        else:
            return "La cantidad supera el maximo de elementos en lista."
    else:
        return "Lista Vacia"
    
def print_dicc_heroes(lista_heroes : list[dict]):
    '''
    imprime los heroes.
    recibe una lista de heroes.
    devuelve .no aplica
    '''
    for heroe in lista_heroes:
        mensaje = "nombre: {0},identidad: {1},empresa: {2},altura: {3},peso: {4},genero: {5},color_ojos: {6},color_pelo: {7},fuerza: {8},inteligencia: {9}\n"
        mensaje = mensaje.format(heroe["nombre"],
                               heroe["identidad"],
                               heroe["empresa"],
                               heroe["altura"],
                               heroe["peso"],
                               heroe["genero"],
                               heroe["color_ojos"],
                               heroe["color_pelo"],
                               heroe["fuerza"],
                               heroe["inteligencia"])
        print(mensaje)
        
  

#case 1          
def pedir_numero_para_mostrar_ordenados(
    lista_heroes_origen : list[dict], clave : str, ordenamiento = "asc")-> list[dict]:
    '''
    lista y muestra la cantidad de heroes segun necesidad.
    Recibe: (arg 1 )Una Lista de heroes, (arg 2) Una Clave ("altura",
    "fuerza", "peso"), (arg 3 ) Ordenamiento por defecto ascendente ("asc"),
    o se puede cambiar a Descendente ("desc").
    '''
    if(lista_heroes_origen):
        lista_heroes_copia = lista_heroes_origen[:]
        lista_heroes_ordenada = ordenar_heroes_b_sort_clave(
            lista_heroes_copia, clave, ordenamiento)
        
        cantidad_heroes_en_lista = contar_elementos_en_lista(lista_heroes_ordenada)
        print("Hay {0} en la lista".format(cantidad_heroes_en_lista))
        
        numero_int_ingresado = pedir_ingreso_de_numero(r"^[0-9]*$")
        listado_por_cantidad_elegida = listar_por_cantidad_si_primeros_o_ultimos(
        lista_heroes_copia, numero_int_ingresado)
        
        
        print_dicc_heroes(listado_por_cantidad_elegida) 
        return listado_por_cantidad_elegida
    else:
        print("La lista esta vacia")
        return False

#----------- fin 1ra parte case 1
'''
2. Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de
manera ascendente (‘asc’) o descendente (‘desc’)
'''
#case 2



def pedir_ingreso_de_palabra(patron : str, mensaje : str) -> str:
    '''
    Pide al usuario un número.
    recibe - no aplica
    Devuelve: el número ingresado como cadena de texto
    '''
    
    palabra_ingresada = input("Por favor ingrese {0}".format(mensaje))
    palabra_ingresada = palabra_ingresada.lower()
    resultado = re.search(patron, palabra_ingresada)
    while(resultado is None):
        palabra_ingresada = input("Incorrecto: ingrese {0} ".format(mensaje))
        palabra_ingresada = palabra_ingresada.lower()
        resultado = re.search(patron, palabra_ingresada)
    print("usted ingresó: {0}".format(palabra_ingresada))
    return palabra_ingresada


def Ordenar_y_Listar_héroes_por_altura(lista_heroes_origen : list[dict]):
    '''
    ordena y lista heroes por altura segun criterio del usuario.
    recibe una lista de heroes.
    devuelve una lista ordenada.
    '''
    if(lista_heroes_origen):
        lista_heroes = lista_heroes_origen[:]
        ordenar_user = pedir_ingreso_de_palabra(r"^(asc|desc)$",mensaje="el orden: 'asc' o 'desc': ")
        lista_ordenada = ordenar_heroes_b_sort_clave(
        lista_heroes, clave="altura", ordenamiento = ordenar_user)
        print_dicc_heroes(lista_ordenada)
        
        return lista_ordenada
    else:
        print("La lista esta vacia")
        return -1

#----------- fin 2ra parte case 2
'''
Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar
de manera ascendente (‘asc’) o descendente (‘desc’
'''
def Ordenar_y_Listar_héroes_por_fuerza(lista_heroes : list[dict]):
    '''
    ordena y lista heroes por altura segun criterio del usuario.
    recibe una lista de heroes.
    devuelve una lista ordenada.
    '''
    if(lista_heroes):
        ordenar_user = pedir_ingreso_de_palabra(r"^(asc|desc)$", mensaje="el orden: 'asc' o 'desc':" )
        lista_ordenada = ordenar_heroes_b_sort_clave(
        lista_heroes, clave="fuerza", ordenamiento = ordenar_user)
        print_dicc_heroes(lista_ordenada)
        
        return lista_ordenada    
    else:
        print("La lista esta vacia")
        return -1

#----------- fin 3ra parte case 3
'''
4. Calcular promedio de cualquier key numérica, filtrar los que cumplan con la
condición de superar o no al promedio (preguntar al usuario la condición:
‘menor’ o ‘mayor’) se deberá listar en consola aquellos que cumplan con ser
mayores o menores según corresponda
'''
def sumar_dato_heroe(lista_heroes : list[dict], clave_a_calcular : str):
    '''
    de una list[dicc] acumula(suma) segun clave
    recibe una lista de dicc heroes y una clave str (ejermplo "altura)
    retorna la suma de lo buscado - si la lista esta vacia da -1
    '''
    if(lista_heroes):
        acumulador_de_dato = 0
        for dicc_heroe in lista_heroes:
            if (clave_a_calcular in dicc_heroe and 
                bool(dicc_heroe) and type(dicc_heroe) is dict):
                
                acumulador_de_dato += dicc_heroe[clave_a_calcular]
        return acumulador_de_dato
    else:
        return -1
    
    
def calcular_promedio_por_clave_segun_user(lista_heroes: list[dict], clave : str)-> list[dict]:
    '''
    calcula el promedio segun clave, pide al user eleccion si mayores o menores
    añ promedio.
    recibe: lista de heroes, y clave "altura"
    devuelve una nueva lista de heroes.
    '''
    if(lista_heroes):
        lista_heroes_copia = lista_heroes[:]
        
        suma_de_valores_segun_clave = sumar_dato_heroe(lista_heroes_copia, clave)
        cantidad = len(lista_heroes_copia)
        promedio = suma_de_valores_segun_clave / cantidad
        mayor_o_menor = pedir_ingreso_de_palabra(r"^(menor|mayor)$", mensaje="'menor' o 'mayor'")
        nueva_lista_promedio_heroes = []
        for heroe in lista_heroes_copia:
            if(mayor_o_menor == "menor" and heroe[clave] < promedio):
                nueva_lista_promedio_heroes.append(heroe)
            if(mayor_o_menor == "mayor" and heroe[clave] > promedio):
                nueva_lista_promedio_heroes.append(heroe)
        print_dicc_heroes(nueva_lista_promedio_heroes)
        return nueva_lista_promedio_heroes
    else:
        print("La lista esta vacia")
   
#---------------fin case 4
'''
5. Buscar héroes por inteligencia [good, average, high] y listar en consola los
que cumplan dicha búsqueda. (Usando RegEx)
'''
import re

def buscar_y_mostrar_por_inteligencia(lista_heroes):
    '''
    Busca heroes por inteligencia y los lista por consola.
    recibe una lista de heroes.
    devuelve: no aplica
    '''
    nueva_lista_good = []
    nueva_lista_average = []
    nueva_lista_high = []
    opcion_de_inteligencia_por_user = pedir_ingreso_de_palabra(
        r"^(good|average|high)$",mensaje="tipo de inteligencia:'good' o 'average' o 'high'")
    for heroe in lista_heroes:
        if(opcion_de_inteligencia_por_user == "good" and heroe["inteligencia"] == "good"):
            nueva_lista_good.append(heroe)
        elif(opcion_de_inteligencia_por_user == "average" and heroe["inteligencia"] == "average"):
            nueva_lista_average.append(heroe)
        elif(opcion_de_inteligencia_por_user == "high" and heroe["inteligencia"] == "high"):
            nueva_lista_high.append(heroe)
    
    match(opcion_de_inteligencia_por_user):
        case "good":
            print("Heroes con inteligencia 'good':")
            for heroe in nueva_lista_good:
                print(heroe)
            return nueva_lista_good
        case "average":
            print("\nHeroes con inteligencia 'average':")
            for heroe in nueva_lista_average:
                print(heroe)
            return nueva_lista_average
        case "high":
            print("\nHeroes con inteligencia 'high':")
            for heroe in nueva_lista_high:
                print(heroe)
            return nueva_lista_high 

#-------- fin case 5
'''
6. Exportar a CSV la lista de héroes ordenada según opción elegida
anteriormente [1-4]
'''


def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')
    

def print_dato(palabra : str):
    '''
    imprime un dato
    recibe una cadena str
    devuelve - no aplica
    '''
    print("{0}".format(palabra))


def opciones_menu()-> str:
    '''
    Opciones del menú
    Recibe: No aplica
    Devuelve: las opciones (str)
    '''
    opciones = "\n1-Listar los primeros N héroes\n2-Ordenar y Listar héroes por altura\n3-Ordenar y Listar héroes por fuerza\n4-Calcular promedio de cualquier key numérica\n5-Buscar héroes por inteligencia [good, average, high]\n6-Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]\n7-Salir\n"
    return opciones


def menu_principal():
    '''
    imprime el menu y toma una opcion del usuario
    recibe -no aplica
    devuelve la opcion elegida, en caso de False devuelve -1
    '''
    opciones_del_menu = opciones_menu()
    print_dato(opciones_del_menu)
    respuesta = input('Ingrese una opción: ')
    if re.findall(r'[1-7]{1}', respuesta):
        return respuesta
    else:
        return -1 
    
    
def crear_archivo_csv(nombre_path: str, lista_a_guardar: list[dict]):
    with open(nombre_path, "w+") as archivo:
        for heroe in lista_a_guardar:
            mensaje = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}\n"
            mensaje = mensaje.format(heroe["nombre"],
                                     heroe["identidad"],
                                     heroe["empresa"],
                                     heroe["altura"],
                                     heroe["peso"],
                                     heroe["genero"],
                                     heroe["color_ojos"],
                                     heroe["color_pelo"],
                                     heroe["fuerza"],
                                     heroe["inteligencia"])
            archivo.write(mensaje)
    print("Archivo Guardado{0}".format(nombre_path))





      
def aplicacion(lista_personajes):
    '''
    opciones para el susuario
    recibe la lista de personajes
    devuelve: no aplica.
    '''
    flag_uno = False
    flag_dos = False
    flag_tres = False
    flag_cuatro = False
    while(True):
        opciones = menu_principal()
        match(opciones):
            case "1":
                lista_ordenada_cantidad =pedir_numero_para_mostrar_ordenados(
                    lista_personajes, "altura")
                flag_uno = True
            case "2":
                lista_ordenada_altura = Ordenar_y_Listar_héroes_por_altura(
                    lista_personajes)
                flag_dos = True
            case "3":
                lista_ordenada_fuerza = Ordenar_y_Listar_héroes_por_fuerza(
                    lista_personajes)
                flag_tres = True
            case "4":
                lista_promedio_mayor_o_menor = calcular_promedio_por_clave_segun_user(
                    lista_personajes, clave="altura")
                flag_cuatro = True
            case "5":
                buscar_y_mostrar_por_inteligencia(lista_personajes)
            case "6":
                if(flag_uno):
                    ruta_donde_se_va_a_guardar = "D_SIMULACRO_PARCIAL_clase10\lista_ordenada_cantidad.csv"
                    crear_archivo_csv(ruta_donde_se_va_a_guardar, lista_ordenada_cantidad)
                else:
                    print("Primero elegir la opcion 1")
                    
                if(flag_dos):
                    ruta_donde_se_va_a_guardar = "D_SIMULACRO_PARCIAL_clase10\lista_ordenada_altura.csv"
                    crear_archivo_csv(ruta_donde_se_va_a_guardar, lista_ordenada_altura)
                else:
                    print("Primero elegir la opcion 2")
                    
                if(flag_tres):
                    ruta_donde_se_va_a_guardar = "D_SIMULACRO_PARCIAL_clase10\lista_ordenada_fuerza.csv"
                    crear_archivo_csv(ruta_donde_se_va_a_guardar, lista_ordenada_fuerza)
                else:
                    print("Primero elegir la opcion 3")
                    
                if(flag_cuatro):
                  ruta_donde_se_va_a_guardar = "D_SIMULACRO_PARCIAL_clase10\lista_promedio_mayor_o_menor.csv"   
                  crear_archivo_csv(ruta_donde_se_va_a_guardar, lista_promedio_mayor_o_menor)
                else:
                    print("Primero elegir la opcion 4") 
            case _:
                print("Opcion incorrecta")
        clear_console()
        




def main():
    nombre_path_json = "D_SIMULACRO_PARCIAL_clase10\data_stark.json"
    lista_personajes_origen = leer_archivo_json(nombre_path_json)
    lista_vacios_reemplazados = normalizar_valores_str_vacios(lista_personajes_origen)
    lista_heroes_normalizada = stark_normalizar_datos(lista_vacios_reemplazados)
    aplicacion(lista_heroes_normalizada)
     
main()#Ejecucion del programa