import re

def pedir_ingreso_de__numero()-> int:
    '''
    Pide el usuario un numero.
    Recibe: no aplica
    Devuelve: el numero ingresado, casteado a int
    '''
    numero_ingresado_str = input("Por favor ingrese el numero ")
    num_imgresado = re.findall(r"^[0-9]*$", numero_ingresado_str)
    if(num_imgresado):
        resultado_num_str = "".join(num_imgresado)
        resultado_num_int = int(resultado_num_str)
        return resultado_num_int
    else:
        print("Incorrecto, por favor ingrese un numero valido")   


pedir_ingreso_de__numero()