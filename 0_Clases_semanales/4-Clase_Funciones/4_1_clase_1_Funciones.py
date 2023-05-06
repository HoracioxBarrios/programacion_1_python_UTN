#Funciones

'''Argumentos:
'''
'''Por posicion'''
#Por posicion: son las mas basicas, e intuitiva de pasar parametros
# def resta(variable_a, variable_b):
#     return variable_a - variable_b

# print(resta(20, 5)) #15


'''Por nombre de arg'''
#Por nombre:Otra forma de llamar a una funcion es usando el nombre del
#, argumento con igual = y su valor

def resta(variable_a, variable_b):
    return variable_a - variable_b

print(resta(variable_b= 10, variable_a= 50))# 40

'''Argumento opcional.
permite tener una funcion con algun parametro opcional, que pueda sar usado o
no dependiendo de la circustancias. los arg opcionales simpre van despues de los argumentos
obligatorios'''

def resta(variable_a, variable_b = 5):
    return variable_a - variable_b

print(resta(variable_a= 15))# 10
#-------------------------------
def resta(variable_a, variable_b = 5):
    return variable_a - variable_b

variable_aux = 50
print(resta(variable_aux))# 45
#-------------------------------
# def resta(variable_a, variable_b = 5):
#     return variable_a - variable_b

# print(resta(,15))#  Asi da error

'''Parametros con Tipo: 
Podemos decirle a la funcion quiero recibir un determinado
tipo de dato'''

def resta(variable_a: int, variable_b: int):
    ''' 
    realiza una resta
    recibe dos numeros enteros
    retorna el resultado
    '''
    return variable_a - variable_b

print(resta(10, 5)) # 5

'''tambien se puede indicar de que tipo va a ser el dato que va a devolver
con -> '''
def resta(variable_a: int, variable_b: int) -> int: # ponemos flecha y el tipo de dato que retorna, cerramos con : al final
    ''' 
    realiza una resta
    recibe dos numeros enteros
    retorna el resultado
    '''
    return variable_a - variable_b

print(resta(10, 5)) # 5
