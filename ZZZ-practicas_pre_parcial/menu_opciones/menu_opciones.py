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


def opciones_menu()-> str:
    '''
    Opciones del menú
    Recibe: No aplica
    Devuelve: las opciones (str)
    '''
    opciones = "1-Listar segun cantidad ingresada\n1- Ordenar de menor a mayor\n2- Ordenar de mayor a menor\n3- Ordenar por altura\n4- Ordenar por peso\n5- Salir"
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
    if re.findall(r'[0-9]{1}', respuesta):
        return respuesta
    else:
        return -1  


def aplicacion():
    while(True):
        opciones = menu_principal()
        match(opciones):
            case "1":
                print("elijio el 1")
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                break
            case _:
                print("Opcion incorrecta")
        clear_console()
        
aplicacion()




def main():
    pass

'''ejemplo'''
def main():
    ruta_del_archivo_json = "Desafio_Stark_5-Archivos\data_stark.json"
    lista_personajes_all_str = leer_archivo(ruta_del_archivo_json)
    lista_heroes_normalizada = stark_normalizar_datos(lista_personajes_all_str)
    stark_marvel_app_5(lista_heroes_normalizada) 
     
main()#Ejecucion del programa



''' algunas validaciones regex'''

#-------------------------- regex caracteres numericos
#--
# numero = "1"

# resultado = re.findall(r"^[1-9]{1}$", numero)
# res = "".join(resultado)
# print(res)


#--
# numero = "1"

# resultado = re.findall(r"^[0-9]{2}$", numero)
# res = "".join(resultado)
# print(res)



#-- int

numero = "100"

resultado = re.findall(r"^[0-9]*$", numero)
if(resultado):
    res_str = "".join(resultado)
    res_int = int(res_str)
    print(res_int)
    print(type(res_int))

#-------------------------- regex caracteres alfabeticos, son equivalentes :
#--a
# cadena = "a".upper()     #.upper() si vas a esperar letra

# resultado = re.match(r"^[A-OZ]{1}$", cadena)
# res = resultado.group()
# print(res)

# --b
resultado = re.findall(r"^[A-OZ]{1}$", cadena)
res = "".join(resultado)
print(res)

