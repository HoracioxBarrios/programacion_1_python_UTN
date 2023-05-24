import re
def pedir_ingreso_de_numero(patron_re : str)-> int:
    '''
    Pide el usuario un numero.
    Recibe: un patron Regex para validar.
    Devuelve: el numero ingresado, casteado a int 
    o -1 en caso de error.
    '''
    flag = True
    while(True):
        numero_ingresado_str = input("Por favor ingrese cantidad a ver: ")
        num_imgresado = re.findall(patron_re, numero_ingresado_str)
        if(num_imgresado):
            resultado_num_str = "".join(num_imgresado)
            resultado_num_int = int(resultado_num_str)
            return resultado_num_int
        else:
            print("Incorrecto, por favor ingrese un numero valido") 
            


patron = r"^[0-9]+$"
numero = pedir_ingreso_de_numero(patron)
print(numero)