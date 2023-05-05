import re

'''
3.Crear una función llamada es_entero que reciba un string y devuelva 
True en caso de que se trate de un número entero (int) y False en caso 
contrario.
'''


numero = "1551025"
# numero = "1.5"     # si en la regex no se incluye el \. al menos una vez no lo toma y esta bien en este caso

def es_entero(numero: str) -> bool:
    resultado = re.match(r'^[+-]?[0-9]+$', numero)
    if resultado:
        return True
    else:
        return False
print(es_entero(numero))


'''
r'^[+-]?[0-9]+$'
Nota
'''