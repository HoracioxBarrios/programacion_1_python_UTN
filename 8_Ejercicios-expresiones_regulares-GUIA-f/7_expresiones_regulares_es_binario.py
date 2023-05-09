import re

'''
7. Crear una función llamada es_binario que devuelva True en caso de un
número binario válido (solo ceros y unos) o False en el caso contrario
    '''
    
numero = "101a"

def es_binario(numero : str)-> bool:
    '''
    verifica que sea numeros binarios
    recibe un numero str
    devuelve un bollean
    '''
    patron = r'^[01]+$'
    if re.findall(patron, numero):
        return True
    else:
        return False
    
print(es_binario(numero))

''' si uso re.match tambien anda'''
