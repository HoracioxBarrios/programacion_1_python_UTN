import re

'''
6. Crear una función llamada es_alfanumerico que devuelva True en caso de
tratarse de solo letras y números y False en el caso contrario (es decir que
contenga caracteres especiales)
'''
alfanumerico = "pepe123"

def es_alfanumerico(cadena :str)-> bool:
    '''
    verifica si es alfanumerico
    recibe una cadena str
    devuelve un boolean
    '''
    if re.findall(r"^[a-zA-Z0-9]+$",cadena):
        return True
    else:
        return False
print(es_alfanumerico(alfanumerico))
    

''' si uso re.match tambien anda'''



# def es_alfanumerico(cadena :str)-> bool:
#     regex = re.match(r"^[a-zA-Z0-9]+$", cadena)
#     if regex:
#         return True
#     else:
#         return False

# print(es_alfanumerico("pepe123")) # True
# print(es_alfanumerico("pepe 123")) # False
# print(es_alfanumerico("pepe!123")) # False




'''Nota: \w no me sirve por el guion bajo

En regex (expresiones regulares) en Python, \w es una secuencia 
de escape que representa cualquier carácter alfanumérico y el 
guión bajo (). Esto incluye letras mayúsculas y minúsculas 
(de la A a la Z y de la a a la z), números (del 0 al 9) y 
el guión bajo ().
'''