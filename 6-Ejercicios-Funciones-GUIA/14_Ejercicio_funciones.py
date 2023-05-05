'''
14- Crear una función que recibe una lista de números y 
devuelve un diccionario con el valor mínimo, el valor máximo 
y el promedio de los números en la lista.
'''
# Tengo una duda de que tan bien este esto, por favor si hay alguna devolucion le agradeceria
lista_de_numeros = [5, 10, 20, 45, 3, 90]

def numero_min_max_promedio(lista):
    '''
    crea un diccionario en base a una lista de numeros
    recibe una lista de numeros
    retorna un diccionario con el numero maximo, numero minimo, y el promedio
    '''
    nuevo_dicc = {}
    acum_numeros = 0
    for indice in range(len(lista)):
        if(indice == 0):
            numero_maximo = lista[indice]
            numero_minimo = lista[indice]
            nuevo_dicc["Maximo"] = numero_maximo
            nuevo_dicc["Minimo"] = numero_minimo
        if(lista[indice] > numero_maximo):
            numero_maximo = lista[indice]
            nuevo_dicc["Maximo"] = numero_maximo
        if(lista[indice] < numero_minimo):
            numero_minimo = lista[indice]
            nuevo_dicc["Minimo"] = numero_minimo
        acum_numeros += lista[indice]
    promedio = acum_numeros / len(lista)
    nuevo_dicc["Promedio"] = promedio
    return nuevo_dicc

dicc = numero_min_max_promedio(lista_de_numeros)
print(dicc)







'''otra forma'''
# def numero_min_max_promedio(lista):
#     nuevo_dicc = {}
#     numero_maximo = lista[0]
#     numero_minimo = lista[0]
#     suma = 0
#     for indice in range(len(lista)):
#         if(lista[indice] > numero_maximo):
#             numero_maximo = lista[indice]
#         if(lista[indice] < numero_minimo):
#             numero_minimo = lista[indice]
#         suma += lista[indice]
#     nuevo_dicc["Maximo"] = numero_maximo
#     nuevo_dicc["Minimo"] = numero_minimo
#     nuevo_dicc["Promedio"] = suma / len(lista)
#     return nuevo_dicc

# lista_de_numeros = [5, 10, 20]
# dicc = numero_min_max_promedio(lista_de_numeros)
# print(dicc)
