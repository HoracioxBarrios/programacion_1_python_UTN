import re
'''
1.Crear una función llamada es_mayuscula que reciba un string y 
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

# numero_int = 15 #si le mando un numero vuela todo!
numero_float = "1.2"
numero_str = "15"

def es_entero(numero : str)-> bool:
    resultado = re.search(r"[0-9]+[0-9]+", numero)
    if(resultado):
        return True
    else:
        return False

# print(es_entero(numero_str))

'''
4.Crear una función llamada es_solo_texto que reciba un string y 
devuelvaTrue en caso de que trate solo de caracteres alfabéticos 
y el espacio y False enel casocontrario

'''
texto_prueba = "Pelota"

def es_solo_texto(cadena : str)-> bool:





'''
5.Crear una función llamada es_decimal que reciba dos strings: el primero
representa la expresión a evaluar y el segundo el separador decimal (puede
ser punto . o coma ,). Debe devolver True en caso que se trate de un número
decimalyFalseenelcasocontrario.
'''
numero_str = "152222"
def es_numero_float(numero: str):
    count_puntos = re.findall(r'[\.]', numero)
    # print(count_puntos)
    if(len(count_puntos) > 1):
        return False
    else:
        es_entero = re.findall(r'([0-9]+[\.]{1}[0-9]+)', numero)
        if(len(es_entero) > 0):
            return True
        return False



print(es_numero_float(numero_str))