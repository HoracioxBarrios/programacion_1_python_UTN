import json
import re
import os


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
    
    
def print_lista_dicc_completo(lista : list[dict], mensaje = "Heroe")-> None:
    '''
    Recorre una lista de diccionario , muestra los elementos clave y valor
    y los imprime con un mensaje.
    Recibe una lista con diccionarios
    Devuelve - no aplica
    -
    '''
    contador = 1
    for diccionario in lista:
        print("---------------------------{0}:({1}) ".format(mensaje , contador))
        for clave, valor  in diccionario.items():
            if(len(diccionario)):
                print(clave, valor)
        contador += 1

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


#1  
def ordenar_por_altura(lista_heroes: list[dict]) -> list[dict]:
    '''
    Ordena de MENOR A MAYOR segun el peso del heroe
    Recibe una lista de diccionario heroes
    devuelve la lista ordenada
    '''
    len_de_lista = len(lista_heroes) -1
    flag_swap = True
    while flag_swap:
        flag_swap = False
        for indice in range(len_de_lista):
            if lista_heroes[indice]["altura"] > lista_heroes[indice + 1]["altura"]:
                aux_backup_valor = lista_heroes[indice]
                lista_heroes[indice] = lista_heroes[indice + 1]
                lista_heroes[indice + 1] = aux_backup_valor
                flag_swap = True
        len_de_lista -= 1
    return lista_heroes
    

#2
def ordenar_por_peso(lista_heroes: list[dict]) -> list[dict]:
    '''
    Ordena de MAYOR A MENOR segun el peso del heroe
    Recibe una lista de diccionario heroes
    devuelve la lista ordenada
    '''
    len_de_lista = len(lista_heroes) -1
    flag_swap = True
    while flag_swap:
        flag_swap = False
        for indice in range(len_de_lista):
            if lista_heroes[indice]["peso"] < lista_heroes[indice + 1]["peso"]:
                aux_backup_valor = lista_heroes[indice]
                lista_heroes[indice] = lista_heroes[indice + 1]
                lista_heroes[indice + 1] = aux_backup_valor
                flag_swap = True
        len_de_lista -= 1
    return lista_heroes
    

 
 #3
def ordenar_por_nombre(lista_heroes: list[dict]) -> list[dict]:
    '''
    Ordena alfabeticamente el nombre 
    Recibe una lista de diccionario heroes
    devuelve la lista ordenada
    '''
    len_de_lista = len(lista_heroes) -1
    flag_swap = True
    while flag_swap:
        flag_swap = False
        for indice in range(len_de_lista):
            if lista_heroes[indice]["nombre"] > lista_heroes[indice + 1]["nombre"]:
                aux_backup_valor = lista_heroes[indice]
                lista_heroes[indice] = lista_heroes[indice + 1]
                lista_heroes[indice + 1] = aux_backup_valor
                flag_swap = True
        len_de_lista -= 1
    return lista_heroes
 

#4
def ordenar_por_largo_nombre(lista_heroes: list[dict]) -> list[dict]:
    '''
    Ordena menor a mayor segun el largo del nombre 
    Recibe una lista de diccionario heroes
    devuelve la lista ordenada
    '''
    len_de_lista = len(lista_heroes) -1
    flag_swap = True
    while flag_swap:
        flag_swap = False
        for indice in range(len_de_lista):
            if len(lista_heroes[indice]["nombre"]) > len(lista_heroes[indice + 1]["nombre"]):
                aux_backup_valor = lista_heroes[indice]
                lista_heroes[indice] = lista_heroes[indice + 1]
                lista_heroes[indice + 1] = aux_backup_valor
                flag_swap = True
        len_de_lista -= 1
    return lista_heroes


#5
def ordenar_por_key(lista_heroes: list[dict], clave_buscada: str, menor_a_mayor=True) -> list[dict]:
    '''
    Ordena una lista de heroes segun clave y sentido de ordenamiento
    Recibe: (arg 1) la lista de heroes, (arg 2) la clave (ejemplo: 'altura'),
    (arg 3)el sentido de ordenamiento, por defecto (menor_a_mayor = True) 
    si se cambia a false cambia el sentido al de  mayor a menor.
    Devuelve la lista ordenada.
    '''
    len_de_lista = len(lista_heroes) - 1
    flag_swap = True
    while flag_swap:
        flag_swap = False
        for indice in range(len_de_lista):
            if(lista_heroes[indice][clave_buscada] > 
               lista_heroes[indice + 1][clave_buscada] and menor_a_mayor):
                aux_valor = lista_heroes[indice]
                lista_heroes[indice] = lista_heroes[indice + 1]
                lista_heroes[indice + 1] = aux_valor
                flag_swap = True
                
            if(lista_heroes[indice][clave_buscada] < 
               lista_heroes[indice + 1][clave_buscada] and not menor_a_mayor):
                aux_valor = lista_heroes[indice]
                lista_heroes[indice] = lista_heroes[indice + 1]
                lista_heroes[indice + 1] = aux_valor
                flag_swap = True
        len_de_lista -= 1
    return lista_heroes

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
                print_lista_dicc_completo(ordenar_por_altura(lista_heroes))
            case "2":
                print_lista_dicc_completo(ordenar_por_key(lista_heroes, clave_buscada="altura", menor_a_mayor = False))
            case "3":
                print_lista_dicc_completo(ordenar_por_key(lista_heroes, clave_buscada="peso"))
            case "4":
                print_lista_dicc_completo(ordenar_por_peso(lista_heroes))
            case "5":
                print_lista_dicc_completo(ordenar_por_nombre(lista_heroes))
            case "6":
                print_lista_dicc_completo(ordenar_por_largo_nombre(lista_heroes))
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
    ruta_del_archivo_json = "Desafio_Stark_6\data_stark.json"
    lista_personajes_all_str = leer_archivo(ruta_del_archivo_json)
    lista_heroes_normalizada = stark_normalizar_datos(lista_personajes_all_str)
    stark_marvel_app_6(lista_heroes_normalizada)
     
main()#Ejecucion del programa