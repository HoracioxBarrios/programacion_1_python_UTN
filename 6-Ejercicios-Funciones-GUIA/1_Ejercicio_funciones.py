'''
1-Crear una función que convierta grados Celsius a grados 
Fahrenheit. Recibe un parámetro (grados Celsius) y devuelve 
el resultado en grados Fahrenheit.

'''
grado_celsuis_ingresado = 10


def convert_celsius_to_farenheit(grados_celsius):
    ''' 
    convierte grados celsius a frenheut
    recibe como arg: grados celsius
    devuelve farenheit
    '''
    farenheit = grados_celsius * 1.8 + 32
    return farenheit


farengeit = convert_celsius_to_farenheit(grado_celsuis_ingresado) #llamada a la funcion

print(farengeit)












'''forma mas simple'''
# def convert_celsius_to_farenheit(grados_celsius):
#     farenheit = grados_celsius * 1.8 + 32
#     return farenheit

# farengeit = convert_celsius_to_farenheit(10) #como retorna, lo atajo en esta variable

# print(farengeit)





'''¿Cuál es la fórmula para convertir de Celsius a Fahrenheit?
Para convertir de ºC a ºF use la fórmula: ºF = ºC x 1.8 + 32. Para 
convertir de ºF a ºC use la fórmula: ºC = (ºF-32) ÷ 1.8.'''