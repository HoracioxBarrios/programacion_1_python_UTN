'''
6- Crear una función que calcule el área de un triángulo. 
Recibe dos parámetros (base y altura) y devuelve el área.
'''

base_ingresada_str = input("Ingrese Base del triangulo ")
base_ingresada_int = int(base_ingresada_str)

altura_ingresada_str = input("Ingrese altura del triangulo ")
altura_ingresada_int = int(altura_ingresada_str)
#-------
def calcular_area_de_triangulo(base, altura):
    '''
    calcula el area de un triangulo
    Recibe dos parámetros (base y altura)
    devuelve el área
    '''
    area_triangulo = (base * altura) / 2
    
    return area_triangulo

#---- Fin funcion
area_del_triangulo = calcular_area_de_triangulo(
    base_ingresada_int, altura_ingresada_int)

print("El area del triangulo es: {0}".format(area_del_triangulo))
