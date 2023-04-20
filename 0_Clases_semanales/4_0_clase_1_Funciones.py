# FUNCIONES

'''Una Funcion es un fragmento de codigo que se puede usar, y reutilizar 
las veces que sea necesaria.

Una funcion debe hacer una sola tarea. ej: def sumar():    esto debe 
sumar y retornar resultado. y si queremos mostrarlo debemos pasarle resultado 
a la funcion print() . ej print(resultado)
'''
#Partes de una funcion:
#keyword  / nombre de la funcion /arg 1 ejemplo 100  / arg 2
def calcular_precio_con_iva(valor_sin_iva, iva = 21):
    '''suma el iva al precio. por defecto toma el iva 21%''' #documentacion
    resultado = valor_sin_iva * (1 + (iva /100)) # 200 * (1 + 0.21) = 200 * 1.21 = 242 
    return resultado

print(calcular_precio_con_iva(100)) #121
print(calcular_precio_con_iva(100 , 10.5)) # 110.5



''' El uso de def nos permite crear una funcion.
    Se usa return para que la funcion devuelv uno o mas valores'''

def funcion_suma(a , b):
    return a + b

numero_1 = 20
numero_2 = 10

suma = funcion_suma(numero_1 , numero_2)

print("La suma es: {0}".format(suma))

#es importante DOCUMENTAR las funciones.

def funcion_sumar(variable_a, variable_b):
    '''
    Indicar que hace.
    Que prametros acepta
    Que retorna
    '''
    return variable_a + variable_b

''' el nombre de Una funcion se debe escribir con snake_case todo en minuscula.
debe ser descriptiva(que hace)'''

'''Para usar la funcion debo mirar la documentacion, para comprenderla debe
bastar con mirar el nombre'''

#En resumen vimos.
#palabras claves def y return
#documentar la funcion que creamos: Que hace, Que recibe, Que devuelve
#El nombre debe ser descriptivo y ser escrito con snake_case



