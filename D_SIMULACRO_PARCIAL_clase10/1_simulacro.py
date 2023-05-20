import json
import os
import re


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

def normalizar_datos_numericos(lista_heroes: list[dict]) -> list[dict] | str:
    '''
    Verifica y normaliza los valores numericos.
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
                    if(valor_reemplazado.isnumeric() and 
                       type(heroe[key]) is str):
                        if('.' in heroe[key] and heroe[key].count('.') == 1):
                            heroe[key] = float(heroe[key])
                        else:
                            heroe[key] = int(heroe[key])
                        print(
                            "El dato {0}fue modificado en el heroe {1}".format(
                            key, heroe["nombre"]))
            nueva_lista_normalizada.append(heroe)
        return nueva_lista_normalizada
    else:
        return "La lista esta Vacia"

def reemplazar_valores_str_vacios(
    lista_heroe : list[dict], valor_que_reemplaza = "N/A")-> list[dict]:
    '''
    verifica si hay valores str vacio y lo reemplaza por otro caracter.
    Recibe una lista de heroes y un valor reemplzante str ("N/A) o el 
    que quiera.
    Devuelve la lista de heroes, con los str vacio reemplazados.
    '''
    for heroe in lista_heroe:
        for clave in heroe.keys():
            if(heroe[clave] == ""):
                heroe[clave] = valor_que_reemplaza
    return lista_heroe
#------------------------------------------------------       

def print_dato(palabra : str):
    '''
    imprime un dato
    recibe una cadena str
    devuelve - no aplica
    '''
    print("{0}".format(palabra))  

   
def imprimir_menu():
    '''
    imprime un menu de opciones
    recibe- no aplica
    devuelve - no aplica
    '''
    lista = ["Elija una Opcion:",
            "1- Elejir cantidad a Listar",
            "2- Ordenar por altura de mayor a menor",
            "3- Ordenar por peso de menor a mayor",
            "4- Ordenar por peso de mayor a menor",
            "5- Ordenar alfabeticamente",
            "6- Ordenar por nombre mas largo ",
            "7- Salir"]
    
    for item in lista:
        print_dato(item)  

# def print_heroes(lista_heroes : list[dict]):
#     for heroe in lista_heroes:
#         mensaje = "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}\n".format(heroe["nombre"], \
#         heroe["identidad"], heroe["empresa"],heroe["altura"], heroe["peso"], heroe["genero"], \
#         heroe["color_ojos"],heroe["color_pelo"], heroe["fuerza"], heroe["inteligencia"])

#         print(mensaje)       
#------------------------------------------------------  
def cantidad_a_listar_por_user(lista_heroes_ordenada : list[dict], cant_a_listar = 0):
    '''
    Lista (una lista de heroes ordenada) en base a una cantidad.
    Recibe: (arg 1) una lista de heroes, 
    (arg 2) recibe la cantidad a listar. (defaul es 0 para que no listar)-
    para el caso que el usuario quiera la lista ordenada completa. 
    La uso en combienacion con la funcion ordenar_numeros_bubble_sort_v5()
    
    Devuelve por la cantidad a listar por el usuario.
    '''
    if(lista_heroes_ordenada and cant_a_listar > 0 
       and cant_a_listar <= len(lista_heroes_ordenada)):
        nueva_lista_cant_elegida = []
        len_a_ver = cant_a_listar 
        for indice in range(len_a_ver):
            nueva_lista_cant_elegida.append(lista_heroes_ordenada[indice])
        return nueva_lista_cant_elegida
    else:
        return -1


def ordenar_bubble_sort_v5(
    lista_heroes: list[dict], clave : str, ordenamiento ,cant_a_listar = 0)-> list[dict]:
    '''
    Ordena una lista de Heroes segun clave y ordenamiento escogido.
    
    Recibe: (arg 1) una lista de heroes list[dict],
    (arg 2) una clave a evaluar ("peso", "altura", "fuerza")
    (arg 3) forma de ordenamiento (por defaul: "asc"  de minimo a maximo)
    como segunda opcion puede ser tambien: "des" de maximo a minimo
    (arg 4) cuantos quiere ver ordenados. 0 es la lista completa o la cant.
    que se le pase por parametro.
    
    Devuelve: la lista ordenada, o si esta vacia se informa.
    '''
    if(lista_heroes):
        # lista_heroes = lista_heroes_origen[:]
        len_de_lista = len(lista_heroes) -1
        flag_swap = True
        while(flag_swap):
            flag_swap = False
            for indice in range(len_de_lista):
                if(lista_heroes[indice][clave] > lista_heroes[indice +1][clave] and 
                   ordenamiento == "asc"):
                    aux_backup_valor = lista_heroes[indice]
                    lista_heroes[indice] = lista_heroes[indice +1]
                    lista_heroes[indice +1] = aux_backup_valor
                    flag_swap = True
                elif(lista_heroes[indice][clave] < lista_heroes[indice +1][clave] and 
                   ordenamiento == "des"):
                    aux_backup_valor = lista_heroes[indice]
                    lista_heroes[indice] = lista_heroes[indice +1]
                    lista_heroes[indice +1] = aux_backup_valor
                    flag_swap = True
            len_de_lista -= 1
        
        if cant_a_listar == 0:
            return lista_heroes 
        else:
            return cantidad_a_listar_por_user(lista_heroes, cant_a_listar)
    else:
        return "La lista esta vacia"    

def print_heroes(lista_heroes : list[dict]):
    for heroe in lista_heroes:
        mensaje = "Nombre: {0}, Identidad: {1}, Empresa: {2}, Altura: {3}, Peso: {4} Genero {5}, Color Ojos: {6}, Color Pelo: {7}, Fuerza: {8}, Inteligencia: {9}\n".format(heroe["nombre"], \
        heroe["identidad"], heroe["empresa"],heroe["altura"], heroe["peso"], heroe["genero"],
        heroe["color_ojos"],heroe["color_pelo"], heroe["fuerza"], heroe["inteligencia"])

        print(mensaje)


#---------- -------------------- ----------

def validar_respuesta(patron_re : str, texto : str )-> str | int:
    '''
    valida si un texto conincide con el patron
    Recibe: un texto a evaluar y un patron regex
    devuelve un int
    '''
    if(texto):
        if(re.match(patron_re, texto)):
            return texto
        return -1
    else:
        return -1



def solicitar_numero_imput(patron_re : str)-> int:
    '''
    solicita un numero por input y valida  
    recibe un patron regex para validar lo que ingresa el user
    deuvleve: la cantidad elegida por el usuario si esta ok.
    '''
    numero = input("Ingrese un número entero mayor a 0: ")
    esta_ok = validar_respuesta(patron_re, numero)
    while (not esta_ok):
        print("El número debe ser mayor a 0. Inténtelo nuevamente.")
        numero = input("Ingrese un número entero mayor a 0: ")
        
    return int(numero)
     
def solicitar_respuesta_str_input(patron_re : str)-> str:
    '''
    solicita una respuesta al usuario por input y valida
    recibe: un patro regex para validar lo que ingresa el user.
    deuvleve: la respuesta si esta ok.
    '''
    respuesta = input("Ingrese el orden ' asc ' o ' desc '")
    esta_ok = validar_respuesta(patron_re, respuesta)
    while(not esta_ok):
        print("incorrecto. Inténtelo nuevamente.")
        respuesta = input("Ingrese el orden ' asc ' o ' desc '")
    return respuesta
    
        

def comprobar_si_supera_el_maxiomo_de_elementos(
    lista_heroes : list[dict], numero : int)-> int | str:
    '''
    comprueba que un numero no supere a la cantidad maxima de heroes en lista.
    Recibe: una lista de heroes, y un numero str.
    Devuelve: un numero int,o avisa si esta vacia la lista u si supera el 
    macimo elemestos.
    '''
    if(lista_heroes):
        cantidad_en_lista = len(lista_heroes)
        if(numero <= cantidad_en_lista):
            return numero
        else:
            return "La cantidad supera a los heroes en lista"
    else:
        return "La lista está vacia"    


      
def menu_principal(): 
    '''
    imprime el menu y toma una opcion del usuario
    recibe -no aplica
    devuelve la opcion elegida, en caso de False devuelve -1
    '''
    
    imprimir_menu()
    opcion_del_menu = input('Ingrese una opción: ')
    if re.match('^[1-8]{1}$', opcion_del_menu):
        return int(opcion_del_menu)
    else:
        return -1  
    
    
def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')
    
def  app_simulacro(lista_heroes : list[dict]):
    '''
    ejecuta las opciones del menú
    recibe la lista de heroes
    revuelve - no aplica
    '''
    while(True):
        respuesta = menu_principal()
        match(respuesta):
            case 1:
                numero_ingresado = solicitar_numero_imput(r'^[1-9][0-9]*$')
                numero_ingresadp_comprobado = comprobar_si_supera_el_maxiomo_de_elementos(
                    lista_heroes, numero_ingresado)
                lista_a_cantidad_mostrar = ordenar_bubble_sort_v5(
                    lista_heroes, clave="altura", ordenamiento="asc", 
                    cant_a_listar= numero_ingresadp_comprobado)
                
                print_heroes(lista_a_cantidad_mostrar)
                
            case 2:
                respuesta = solicitar_respuesta_str_input(r"^a[s]c$|^d[e][s]c$")
                lista_a_mostrar_segun_orden = ordenar_bubble_sort_v5(
                    lista_heroes,clave="altura",ordenamiento = respuesta)
                print_heroes(lista_a_mostrar_segun_orden)
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                break     
            case _:
                print("Opcion incorrecta")
        clear_console()

   

def main():
    '''
    ejecuta el comienzo de la aplicacion.
    recibe no aplica
    devuelve -* no aplica
    '''
    lista_personajes_all_str = leer_archivo(
        "D_SIMULACRO_PARCIAL_clase10\data_stark.json")
    
    lista_heroes_normalizada_num = normalizar_datos_numericos(
        lista_personajes_all_str)
    
    lista_heroes_normalizada = reemplazar_valores_str_vacios(lista_heroes_normalizada_num)
    
    app_simulacro(lista_heroes_normalizada) 
 
 
    
main()#Ejecucion del programa