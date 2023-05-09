import re

'''
2.Crear una función llamada es_minuscula que reciba un string y 
devuelva True en caso de que todas las letras sean mayúsculas o 
False en el caso contrario
'''

texto_ejemplo = "pepe"

def es_minuscula(texto : str)-> bool:
    '''
    verifica si una palabra esta compuesta por solo letras mayusculas
    recibe una palabra
    devuelve True en caso de ser todo mayusculas
    '''
    if(re.findall(r"^[a-z]+$", texto)): # cometi el error de no ponerle "+" para que no sea solo una letra, sino 1 o mas
        return True
    else:
        return False


print(es_minuscula(texto_ejemplo))



''' uso match para ver si conincide lo uso en un if si hay 
un objeto match seria True, si no devuevulve None'''


















'''1ra practica'''

# # palabra = "PEPE" #False
# # palabra = "Pepe" #False
# palabra = "pepe" #True
# # palabra = "PepE" #False

# def es_mayuscula(cadena :str)-> bool:
#     '''
#     comprueba si una o mas letras son minusculas
#     recibe una cadena str
#     devuelve true en caso de ser todas Minusculas
#     '''
#     es_mayuscula = re.findall(r"^[a-z]+$", cadena)
#     if(len(es_mayuscula) > 0):
#         return True
#     else:
#         return False
   

# print(es_mayuscula(palabra))

# '''
# r"^[a-z]+$"
# Nota: r = regular expression, ^ es empieza con , [] es un conjunto , 
# a-z el rango de caracteres , el + es 1 o mas ocurrencias y es equivalente a {1 ,} que va de uno al "infinito"
# $ significa en este caso termina con minuscula.

# re.findall() retorna una lista
# '''
