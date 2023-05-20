import json
import os
import re

#hay que shalow copiar las listas dentro de las funciones de ordenamiento, esas copias la retirnamos
#usar regex en lugar de isnumeric()
def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

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


#1. 
'''
1. Listar los primeros N héroes. El valor de N será ingresado por el usuario
(Validar que no supere max. de lista)
'''
def ordenar_numeros_bubble_sort_v5(
    lista_heroes : list[dict], clave : str, ordenamiento = "min_a_max",cant_a_ver = 0)-> list[dict]:
    '''
    Ordena una lista de Heroes segun clave y ordenamiento escogido.
    Recibe: (arg 1) Recibe una lista de heroes list[dict],
    (arg 2) una clave a evaluar ("peso", "altura", "fuerza")
    (arg 3) forma de ordenamiento (por defaul: "min_a_max")puede tambien: "max_a_min"
    
    Devuelve: la lista ordenada, o si esta vacia se informa.
    '''
    if(lista_heroes):
        len_de_lista = len(lista_heroes) -1
        flag_swap = True
        while(flag_swap):
            flag_swap = False
            for indice in range(len_de_lista):
                if(lista_heroes[indice][clave] > lista_heroes[indice +1][clave] and 
                   ordenamiento == "min_a_max"):
                    aux_backup_valor = lista_heroes[indice]
                    lista_heroes[indice] = lista_heroes[indice +1]
                    lista_heroes[indice +1] = aux_backup_valor
                    flag_swap = True
                elif(lista_heroes[indice][clave] < lista_heroes[indice +1][clave] and 
                   ordenamiento == "max_a_min"):
                    aux_backup_valor = lista_heroes[indice]
                    lista_heroes[indice] = lista_heroes[indice +1]
                    lista_heroes[indice +1] = aux_backup_valor
                    flag_swap = True
            len_de_lista -= 1
        
        if(cant_a_ver > 0):
            return
        elif(cant_a_ver == 0):
            len_a_ver =  cant_a_ver
            for indice in range(len_a_ver):
                print(indice)
        else:
            return "elija una cantidad a ver mayor a 0"           
    else:
        return "La lista esta vacia"         


def print_dato(palabra : str):
    '''
    imprime un dato
    recibe una cadena str
    devuelve - no aplica
    '''
    print("{0}".format(palabra))  
    
    
    #-------- menú
def imprimir_menu():
    '''
    imprime un menu de opciones
    recibe- no aplica
    devuelve - no aplica
    '''
    lista = ["Elija una Opcion:",
            "1- Ordenar por altura de menor a mayor",
            "2- Ordenar por altura de mayor a menor",
            "3- Ordenar por peso de menor a mayor",
            "4- Ordenar por peso de mayor a menor",
            "5- Ordenar alfabeticamente",
            "6- Ordenar por nombre mas largo ",
            "7- Salir"]
    
    for item in lista:
        print_dato(item)    
        
                        
def menu_principal_desafio_6(): 
    '''
    imprime el menu y toma una opcion del usuario
    recibe -no aplica
    devuelve la opcion elegida, en caso de False devuelve -1
    '''
    imprimir_menu()
    respuesta = input('Ingrese una opción: ')
    if re.match('^[1-8]{1}$', respuesta):
        return respuesta
    else:
        return -1   
    
    
def  stark_marvel_app_6(lista_heroes : list[dict]):
    '''
    ejecuta las opciones del menú
    recibe la lista de heroes
    revuelve - no aplica
    '''
    while(True):
        respuesta = menu_principal_desafio_6()
        match(respuesta):
            case "1":
                print(lista_heroes)
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                break     
            case _:
                print("Opcion incorrecta")
        clear_console()

    
        
        
def main():
    '''
    ejecuta el comienzo de la aplicacion
    recibe no aplica
    devuelve -* no aplica
    '''
    ruta_del_archivo_json = "D_SIMULACRO_PARCIAL_clase10\data_stark.json"
    lista_personajes_all_str = leer_archivo(ruta_del_archivo_json)
    lista_heroes_normalizada = stark_normalizar_datos(lista_personajes_all_str)
    stark_marvel_app_6(lista_heroes_normalizada)
     
# main()#Ejecucion del programa