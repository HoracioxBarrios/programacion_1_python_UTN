import re

'''
5.Crear una función llamada es_decimal que reciba dos strings: el primero
representa la expresión a evaluar y el segundo el separador decimal (puede
ser punto . o coma ,). Debe devolver True en caso que se trate de un número
decimal y False en el caso contrario.
'''



numero_str = "152,222"

import re

def es_numero_float(numero: str):
    '''
    verifica si un numero en string es float
    recibe un string
    devuelve true en caso de ser flotante
    '''
    regex = r'[+-]?[0-9]+[\.|\,]{1}[0-9]+'
    resultado = re.findall(regex, numero)
    if(resultado):
        return True
    else: # si es None
        return False

print(es_numero_float(numero_str))

















# numero_str = "152.222"
# separador = "."
# import re

# def es_numero_float(numero: str, separador: str):
#     '''
    
#     '''
#     regex = r'[+-]?[0-9]+['+ separador +']{1}[0-9]+'
#     resultado = re.match(regex, numero)
#     if(resultado):
#         return True
#     else: # si es None
#         return False

# print(es_numero_float(numero_str, separador))















# aca no puse separador y esta incorrecta, por esto tambien
# def es_numero_float(numero: str):
#     lista_con_puntos = re.findall(r'[\.]', numero)
#     # print(count_puntos)
#     if(len(lista_con_puntos) > 1):
#         return False
#     else:
#         lista_resultado = re.findall(r'([0-9]+[\.]{1}[0-9]+)', numero)
#         if(len(lista_resultado) > 0 or numero.isdigit()):
#             return True
#         return False



# print(es_numero_float(numero_str))