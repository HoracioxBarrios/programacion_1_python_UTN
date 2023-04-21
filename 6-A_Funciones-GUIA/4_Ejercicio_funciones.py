'''
4- Crear una función que calcule el promedio de edad de 
un grupo de personas. Recibe una lista de edades y devuelve 
el promedio.
'''

lista_de_edades_de_personas = [21, 30, 50, 40]

def calcular_promedio(lista_de_edades):
    '''
    calcula el promedio de edades
    recibe una lista de edades
    devuelve el promedio de edades
    '''
    cantidad_de_personas = len(lista_de_edades)
    acum_edad = 0
    for edad in lista_de_edades:
        acum_edad += edad
    
    promedio_edad = acum_edad / cantidad_de_personas
    return promedio_edad

promedio_de_edad = calcular_promedio(lista_de_edades_de_personas)
print(promedio_de_edad)















# lista_de_alumnos_utn = [
#     {"nombre" : "pepe", "edad" : 35},
#     {"nombre" : "rulo", "edad" : 30},
#     {"nombre" : "nair", "edad" : 21},
#     {"nombre" : "Lilia", "edad" :25}
# ]

# def calcular_promedio_edades(lista_de_personas):
#     '''
#     Calcula el promedio de edades
#     recibe una lista de personas
#     devuelve el promedio de edades
#     '''
#     cantidad_personas = len(lista_de_personas)
#     acum_edades = 0
#     for persona in lista_de_personas:
#         acum_edades = acum_edades + persona["edad"]
    
#     promedio_edad = acum_edades / cantidad_personas
#     return promedio_edad


# promedio_de_edades = calcular_promedio_edades(lista_de_alumnos_utn)
# print(promedio_de_edades)