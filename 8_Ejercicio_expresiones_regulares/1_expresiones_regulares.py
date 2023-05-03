import re
'''
Crear una función llamada es_mayuscula que reciba un string y 
devuelva True en caso de que todas las letras sean mayúsculas 
o False en el caso contrario
'''
palabra = "pepe"

def es_mayuscula(cadena :str)-> bool:
    '''
    comprueba si una o mas letras son mayusculas
    recibe una cadena str
    devuelve true en caso de ser todo 
    '''
    es_mayuscula = re.findall(r"[a-z]+", cadena)
    if(len(es_mayuscula) > 0):
        return False
    else:
        return True
   

# print(es_mayuscula(palabra))

'''
2.Crear una función llamada es_minuscula que reciba un string y 
devuelva True en caso de que todas las letras sean mayúsculas o 
False en el caso contrario
'''


def es_mayuscula(cadena :str)-> bool:
    '''
    comprueba si una o mas letras son minusculas
    recibe una cadena str
    devuelve true en caso de ser todo minuscula
    '''
    es_mayuscula = re.findall(r"[A-Z]+", cadena)
    if(len(es_mayuscula) > 0):
        return False
    else:
        return True
   

# print(es_mayuscula(palabra))


'''
3.Crear una función llamada es_entero que reciba un string y devuelva 
True en caso de que se trate de un número entero y False en caso 
contrario.
'''

numero_int = 15
numero_float = 1.2
numero_str = "15"

def es_entero(numero)-> bool:
    resultado = re.findall(r"[0-9]{1,}", numero)
    print(resultado)
