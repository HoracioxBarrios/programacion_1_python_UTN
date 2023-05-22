import re

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
    opciones = "1-Listar segun cantidad ingresada\n \
                1- Ordenar de menor a mayor\n \
                2- Ordenar de mayor a menor\n \
                3- Ordenar por altura\n \
                4- Ordenar por peso\ \
                5- Salir"
    return opciones


def menu_principal():
    '''
    imprime el menu y toma una opcion del usuario
    recibe -no aplica
    devuelve la opcion elegida, en caso de False devuelve -1
    '''
    opciones_del_menu = opciones_menu()
    print_dato(opciones_menu)
    respuesta = input('Ingrese una opción: ').upper()
    if re.match('^[A-OZ]{1}$', respuesta):
        return respuesta
    else:
        return -1  






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

# numero = "100"

# resultado = re.findall(r"^[0-9]*$", numero)
# if(resultado):
#     res_str = "".join(resultado)
#     res_int = int(res_str)
#     print(res_int)
#     print(type(res_int))

#-------------------------- regex caracteres alfabeticos, son equivalentes :
#--a
# cadena = "a".upper()

# resultado = re.match(r"^[A-OZ]{1}$", cadena)
# res = resultado.group()
# print(res)

#--b
# resultado = re.findall(r"^[A-OZ]{1}$", cadena)
# res = "".join(resultado)
# print(res)

