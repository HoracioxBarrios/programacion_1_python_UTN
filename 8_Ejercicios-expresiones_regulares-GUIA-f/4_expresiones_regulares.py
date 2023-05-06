import re


'''
4.Crear una función llamada es_solo_texto que reciba un string y 
devuelva True en caso de que trate solo de caracteres alfabéticos 
y el espacio y False en el caso contrario

'''
texto_prueba = "prueba "


def es_solo_texto(cadena: str) -> bool:
    resultado = re.match(r'^[a-zA-Z\s]+$', cadena)
    if(resultado):
        return True
    else:
        return False

print(es_solo_texto(texto_prueba))




'''
r'^[a-zA-Z\s]+$'
Nota:
^ es empoeza con , [] conjunto , en los rangos de a-zA.Z y el \s es espacios en blanco
+ es 1 o mas ocurrencias , y $ termina con ... en este caso con cualquiera de 
los caracteres del conjunto.
'''