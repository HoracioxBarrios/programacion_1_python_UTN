'''
8- Crear una función que verifique si un número es par o impar.
Recibe un número como parámetro y devuelve True si es par o 
False si es impar.
'''

numero_str = input("Ingrese un numero") 
numero_int = int(numero_str)

def es_par(numero):
    '''
    verifica si un numero es par
    recibe un numero
    devuelve True en caso de ser par, False en caso de inpar
    '''
    if(numero % 2 == 0):
        return True
    else:
        return False


print(es_par(numero_int))