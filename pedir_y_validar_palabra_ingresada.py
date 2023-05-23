import re


def pedir_ingreso_de_palabra() -> str:
    '''
    Pide al usuario un número.
    Devuelve: el número ingresado como cadena de texto
    '''
    palabra_ingresada = input("Por favor ingrese 'asc' o 'desc': ")
    palabra_ingresada = palabra_ingresada.lower()
    resultado = re.search(r"^(asc|desc)$", palabra_ingresada)
    while(resultado is None):
        palabra_ingresada = input("Incorrecto: ingrese 'asc' o 'desc': ")
        palabra_ingresada = palabra_ingresada.lower()
        resultado = re.search(r"^(asc|desc)$", palabra_ingresada)
    print("usted ingresó: {0}".format(palabra_ingresada))
    return palabra_ingresada


pedir_ingreso_de_palabra()
