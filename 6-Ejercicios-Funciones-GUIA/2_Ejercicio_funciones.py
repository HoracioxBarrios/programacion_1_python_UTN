'''
2- Crear una función que calcule el área de un círculo. 
Recibe un parámetro (radio) y devuelve el área del círculo.
'''
radio_ingresado = 10

def calcular_area_de_circulo(radio):
    '''
    calcula el area de un circulo
    recibe el radio
    retorna el area
    '''
    area = (radio * radio) * 3.141592
    return area
    
area_circulo = calcular_area_de_circulo(radio_ingresado)


print(area_circulo)

















'''un ej: de chat-gtp'''
# import math

# radio = float(input("Ingrese el radio del círculo: "))
# area = math.pi * radio**2

# print("El área del círculo es:", area)