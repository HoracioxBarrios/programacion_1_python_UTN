'''
8. Escribir una función que reciba dos string (nombre y apellido) y 
devuelva un diccionario con el nombre y apellido, eliminando los 
espacios del comienzo y el final y colocando la primer letra en 
mayúscula

'''

nombre = "pedro            "
apellido ="   apostol "

def nombre_y_apellido_corregidos_to_diccionary(nombre : str, apellido : str)-> dict:
    '''
    crea un diccionario con el nombre y apellido sin espacios y capitalize
    Recibe un nombre y un apellido.
    devuelve un diccionario con clave Nombre y el nombre y clave Apellido 
    con el correspondiente
    '''
    
    nombre_sin_espacios = nombre.strip()
    apellido_sin_espacios = apellido.strip()
    nombre_capitalized = nombre_sin_espacios.capitalize()
    apellido_capitalized = apellido_sin_espacios.capitalize()
    diccionario_persona = {}
    diccionario_persona["Nombre"] = nombre_capitalized
    diccionario_persona["Apellido"] = apellido_capitalized
    
    return diccionario_persona

print(nombre_y_apellido_corregidos_to_diccionary(nombre, apellido))

    