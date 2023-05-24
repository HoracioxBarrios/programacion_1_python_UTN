import json

def leer_archivo_json(nombre_path : str)-> list[dict]:
    with open(nombre_path, "r") as archivo:
        equipo = json.load(archivo)
    
        return equipo["jugadores"]
    


lista_jugadores = leer_archivo_json("parcial\dt.json")

'''
1) Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
 Nombre Jugador- Posición. Ejemplo:
 Michael Jordan- Escolta
'''
def print_lista_jugadores(lista_de_jugadores: list[dict], ver_indice = False):
    '''
    Muestra los nombres y posicion de cada jugador.
    Recibe: una lista de jugadores list[dict].y opcional podemos 
    elegir ver el indice donde esta cada jugador (ver_indice = True).

    Devuelve: -1 en caso de error
    '''
    if(lista_de_jugadores):
        if(ver_indice):
            for indice in range(len(lista_jugadores)):
                dato_jugador = "Ubicacion {0}: {1}- {2}".format(
                    indice, lista_de_jugadores[indice]["nombre"], lista_de_jugadores[indice]["nombre"])
                print(dato_jugador)
        else:
            for indice in range(len(lista_jugadores)):
                dato_jugador = "{0} - {1}".format(
                    lista_de_jugadores[indice]["nombre"],lista_de_jugadores[indice]["posicion"])
                print(dato_jugador)
    else:
        print("La lista está vacia")
        return -1

#case 1
# print_lista_jugadores(lista_jugadores, ver_indice=False)

'''
2) Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas
 completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por
 partido, rebotes totales, promedio de rebotes por partido, asistencias totales,
 promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de
 tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
'''
def pedir_numero_a_user():
    '''
    le pide al usuario un numero
    Recibe: no aplcia.
    Devuelve: no aplica.
    '''
    numero_ing_str = input("Ingrese numero: ")
    #validar
    numero_ing_int = int(numero_ing_str)
    return numero_ing_int

def print_datos_jugador(jugador : dict)-> str:
    datos_jugador = "Nombre: {0}, Posicion: {1}\n, Estadisticas:{2}\n".format(
        jugador["nombre"], jugador["posicion"], jugador["estadisticas"])
    print(datos_jugador)

'''
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
'''
def seleccionar_jugador_segun_indice(lista_jugadores : list[dict]):
    if(lista_jugadores):
        print_lista_jugadores(lista_jugadores, ver_indice =True)
        num_ingresado = pedir_numero_a_user()
        for indice in range(len(lista_jugadores)):
            if(indice == num_ingresado):
                datos_del_jugador = lista_jugadores[indice]
        print_datos_jugador(datos_del_jugador)
        return datos_del_jugador
    else:
        print("La lista está vacia")


seleccionar_jugador_segun_indice(lista_jugadores)

