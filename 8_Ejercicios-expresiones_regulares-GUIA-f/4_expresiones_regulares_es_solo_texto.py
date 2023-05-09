import re


'''
4.Crear una función llamada es_solo_texto que reciba un string y 
devuelva True en caso de que trate solo de caracteres alfabéticos 
y el espacio y False en el caso contrario

'''
texto_prueba = "prueba "


def es_solo_texto(cadena: str) -> bool:
    '''
    verifica si es solo texto
    recibe una cadena
    devuelve true en caso de ser solo texto
    '''
    resultado = re.findall(r'^[a-zA-Z ]+$', cadena)
    if(resultado):
        return True
    else:
        return False

print(es_solo_texto(texto_prueba))




'''
r'^[a-zA-Z\s]+$'
Nota:
^ es empieza con , [] conjunto , en los rangos de a-zA.Z y el " " es espacios en blanco
+ es 1 o mas ocurrencias , y $ termina con ... en este caso con cualquiera de 
los caracteres del conjunto.
'''

'''
no uso \s porque en regex, el metacaracter \s representa un 
espacio en blanco, incluyendo espacios, tabulaciones y saltos de línea.
'''