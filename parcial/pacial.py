import json
import os
import re

'''
"jugadores": [
{
      "nombre": "Michael Jordan",
      "posicion": "Escolta",
      "estadisticas": {
        "temporadas": 15,
        "puntos_totales": 32292,
        "promedio_puntos_por_partido": 30.1,
        "rebotes_totales": 6672,
        "promedio_rebotes_por_partido": 6.2,
        "asistencias_totales": 5633,
        "promedio_asistencias_por_partido": 5.3,
        "robos_totales": 2514,
        "bloqueos_totales": 893,
        "porcentaje_tiros_de_campo": 49.7,
        "porcentaje_tiros_libres": 83.5,
        "porcentaje_tiros_triples": 32.7
      },
      "logros": [
        "6 veces campeón de la NBA",
        "6 veces MVP de la NBA",
        "14 veces All-Star",
        "10 veces líder en anotaciones de la NBA",
        "5 veces MVP de las Finales de la NBA",
        "Defensor del Año en la NBA en 1988",
        "Miembro del Salon de la Fama del Baloncesto"
      ]
    },
]
'''
    

def leer_archivo_json(nombre_path : str)-> list:
    '''
    Lee un archvo json.
    Recibe la ruta con el nombre de archivo .json.
    Devuelve una lista de jugadores
    '''
    with open(nombre_path, "r") as archivo:
        equipo = json.load(archivo)
    
        return equipo["jugadores"]

'''
1) Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
 Nombre Jugador- Posición. Ejemplo:
 Michael Jordan- Escolta
'''
def mostrar_nombres_posicion_o_tambien_ubicacion(
    lista_de_jugadores: list , ver_indice_ubi = False):
    '''
    Muestra los nombres, posicion de cada jugador y opcionalmente su indice.
    Recibe: una lista de jugadores y opcional elegir ver el indice 
    donde esta cada jugador (ver_indice = True).

    Devuelve: -1 en caso de error
    '''
    if(lista_de_jugadores):
        if(ver_indice_ubi):
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

#case 1


'''
2) Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas
 completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por
 partido, rebotes totales, promedio de rebotes por partido, asistencias totales,
 promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de
 tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
'''
def pedir_ingreso_de_numero(patron_re : str)-> int:
    '''
    Pide el usuario un numero.
    Recibe: un patron Regex para validar.
    Devuelve: el numero ingresado, casteado a int
    '''
    while(True):
        numero_ingresado_str = input("Por favor ingrese numero de la opcion: ")
        num_imgresado = re.findall(patron_re, numero_ingresado_str)
        if(num_imgresado):
            resultado_num_str = "".join(num_imgresado)
            resultado_num_int = int(resultado_num_str)
            return resultado_num_int
        else:
            print("Incorrecto, Por favor ingrese numero de la opcion:")


def seleccionar_jugador_segun_indice(lista_jugadores : list[dict]):
    '''
    Permite selecionar un jugador por su indice en la lista.
    Recibe una lista de Jugadores.
    Devuelve - no aplica.
    '''
    if(lista_jugadores):
        mostrar_nombres_posicion_o_tambien_ubicacion(
            lista_jugadores, ver_indice_ubi =True)
        patron_de_validacion = r"^[0-9]+$"
        indice_elegido = pedir_ingreso_de_numero(patron_de_validacion)
        
        for indice in range(len(lista_jugadores)):
            if(indice == indice_elegido):
                dato_nombre_y_posicion = "Nombre {0}- Posicion:{1}".format(
                    lista_jugadores[indice]["nombre"],
                    lista_jugadores[indice]["posicion"])
                
                lista_estadisticas = []
                diccionario_estadisticas = lista_jugadores[indice]["estadisticas"]
                for clave, valor in diccionario_estadisticas.items():
                    dato_estadistica = "{0}: {1}".format(clave, valor)
                    lista_estadisticas.append(dato_estadistica)
                    
        estadisticas = "\n".join(lista_estadisticas)
        nombre_estadisticas = "{0}\n{1}".format(
            dato_nombre_y_posicion, estadisticas)
        print(nombre_estadisticas)           
                    
    else:
        print("La lista está vacia")


#--Menú y ejecucion de la app
def clear_console() -> None:
    """
    Espera que el usuario ingrese enter 
    para reimprimir en consola las opciones.
    """
    _ = input('Presione una tecla para continuar...')
    os.system('cls')

def opciones_del_menu():
    '''
    Opciones del menu.
    Recibe: No aplica.
    Devuelve: No aplica
    '''
    opciones = "Bienvenido. Ingrese una opcion: \n1- Ver Jugadores y Posicion de todos los jugadores del Dream Team\n2- Seleccionar un jugador y ver sus estadisticas\n"
    return opciones

def print_dato(dato : str):
    '''
    imprime una cadena de texto.
    Recibe una cadena.
    Devuelve: No aplica.
    '''
    print("{0}".format(dato))
    

def menu_principal():
    '''
    imprime el menu y toma una opcion del usuario
    recibe -no aplica
    devuelve la opcion elegida, en caso de False devuelve -1
    '''
    opciones_para_el_usuario = opciones_del_menu()
    print_dato(opciones_para_el_usuario)
    patron_de_validacion = r"^[0-9]+$"
    numero_ingresado = pedir_ingreso_de_numero(patron_de_validacion)
    return numero_ingresado
   
   
def aplicacion(lista_Jugadores : list[dict]):
    '''
    opciones para el usuario
    Recibe la lista de Jugadores
    Devuelve: no aplica.
    '''
    while(True):
        opciones = menu_principal()
        match(opciones):
            case 1:
                mostrar_nombres_posicion_o_tambien_ubicacion(lista_Jugadores)
            case 2:
                seleccionar_jugador_segun_indice(lista_Jugadores)
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                break
            case _:
                print("Opcion incorrecta")
        clear_console()
 
        

def main():
    '''
    Ejecuta la aplicacion
    Recibe: -
    Devuelve: -
    '''
    lista_jugadores = leer_archivo_json("parcial\dt.json")
    aplicacion(lista_jugadores)
    

main()#Inicio del programa