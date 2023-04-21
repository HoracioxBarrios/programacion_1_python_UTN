from data_stark import lista_heroes

''' Desafío #00:

a- Analizar detenidamente el set de datos
b- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
c-Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
d-Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
e-Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
f-Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
g-Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
h-Calcular e informar cual es el superhéroe más y menos pesado.
i-Ordenar el código implementando una función para cada uno de los valores informados.
j-Construir un menú que permita elegir qué dato obtener
'''
'''Ejermplo:
lista_heroes = [ {
        "nombre": "Howard the Duck",
        "identidad": "Howard (Last name unrevealed)",
        "empresa": "Marvel Comics",
        "altura": "79.349999999999994",
        "peso": "18.449999999999999",
        "genero": "M",
        "color_ojos": "Brown",
        "color_pelo": "Yellow",
        "fuerza": "2",
        "inteligencia": "average"
    },]'''


# b- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def mostrar_heroes():
    for heroe in lista_heroes:
        print(heroe["nombre"])

# c-Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def mostrar_heroes_y_altura():
    for heroe in lista_heroes:
        print("Nombre: {0} su altura: {1} ".format(heroe["nombre"], heroe["altura"]))

# d-Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def mostrar_heroe_mes_alto():
    for indice in range(len(lista_heroes)):
        altura_str = lista_heroes[indice]["altura"] #cast str a float
        altura_float = float(altura_str)
        if(indice == 0 or altura_max < altura_float):# cometi un error de comparar con :lista_heroes[indice]["altura"] ya que es string el valor. por eso castee a float
            altura_max = altura_float
            indice_mas_alto = indice
    print("El heroe mas alto es: {0}su altura es {1}".format(
        lista_heroes[indice_mas_alto]["nombre"],lista_heroes[indice_mas_alto]["altura"]))

# e-Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def mostrar_heroe_mas_bajo():
    for indice in range(len(lista_heroes)):
        altura_str = lista_heroes[indice]["altura"]
        altura_float = float(altura_str)
        if(indice == 0 or altura_float < altura_min):
            altura_min = altura_float
            indice_de_mas_bajo = indice
    print("El heroe mas bajo es: {0}su altura es {1}".format(
        lista_heroes[indice_de_mas_bajo]["nombre"],lista_heroes[indice_de_mas_bajo]["altura"]))

# f-Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
def mostrar_altura_promedio():
    acum_de_altura = 0
    for indice in range(len(lista_heroes)):
        altura_str = lista_heroes[indice]["altura"]
        altura_float = float(altura_str)
        acum_de_altura += altura_float

    altura_promedio = acum_de_altura / len(lista_heroes)
    print("La altura promedio es: {0}".format(altura_promedio))



# h-Calcular e informar cual es el superhéroe más y menos pesado.
def mostrar_heroe_mas_pesado():
    for indice in range(len(lista_heroes)):
        peso_str = lista_heroes[indice]["peso"]
        peso_float = float(peso_str)
        if(indice == 0 or peso_float > peso_max):
            peso_max = peso_float
            indice_de_peso_max = indice
    print("El heroe con mas pesado es: {0} y su peso: {1}".format(
        lista_heroes[indice_de_peso_max]["nombre"], 
        lista_heroes[indice_de_peso_max]["peso"]))
def mostrar_heroe_menos_peso():
    for indice in range(len(lista_heroes)):
        peso_str = lista_heroes[indice]["peso"]
        peso_float = float(peso_str)
        if(indice == 0 or peso_float < peso_min):
            peso_min = peso_float
            indice_peso_min = indice
    print("El heroe con menos peso es: {0} con un peso: {1}".format(
        lista_heroes[indice_peso_min]["nombre"],
        lista_heroes[indice_peso_min]["peso"]
    ))


while(True):
    respuesta_str = input("Elija una opcion:\n 1-Ver todos los Heroes\n 2-Ver heroes y su altura\n 3-Ver Heroe mas alto\n 4-Ver heroe mas bajo\n 5-Ver altura promedio\n 6-Ver Heroe mas pesado\n 7-Ver heroe menos pesado\n 8-Salir")
    respuesta_int = int(respuesta_str)
    
    match(respuesta_int):
        case 1:
            mostrar_heroes()
        case 2:
            mostrar_heroes_y_altura()
        case 3:
            mostrar_heroe_mes_alto()
        case 4:
            mostrar_heroe_mas_bajo()
        case 5:
            mostrar_altura_promedio()
        case 6:
            mostrar_heroe_mas_pesado()
        case 7:
            mostrar_heroe_menos_peso()
        case 8:
            break
            




























































# b -Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# lista_de_heroes = data_stark.lista_heroes


# def mostrar_heroes():
#     for heroe in lista_de_heroes:
#         print(heroe["nombre"])

# mostrar_heroes()

# c- Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo

# def mostrar_nombre_altura():
#     for heroe in lista_de_heroes:
#         print("Nombre: {0} Altura {1}".format(
#             heroe["nombre"], heroe["altura"]))

# mostrar_nombre_altura()

# d- Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)


# def mostrar_heroe_mas_alto():

#     for indice in range(len(lista_de_heroes)):
#         altura_str = lista_de_heroes[indice]["altura"] # en el dicc esta type <str>
#         altura_float = float(altura_str)
#         if(indice == 0 or altura_float > altura_max):
#             altura_max = altura_float
#             indice_max = indice


#     print("El mas alto es{0} con la altura: {1}".format(
#         lista_de_heroes[indice_max]["nombre"],altura_max ))


# mostrar_heroe_mas_alto()

# Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)

# def mostrar_heroe_mas_alto():

#     for indice in range(len(lista_de_heroes)):
#         altura_str = lista_de_heroes[indice]["altura"] # en el dicc esta type <str>
#         altura_float = float(altura_str)
#         if(indice == 0 or altura_float > altura_max):
#             altura_max = altura_float
#             indice_max = indice


#     print("El mas alto es{0} con la altura: {1}".format(
#         lista_de_heroes[indice_max]["nombre"],altura_max ))


# mostrar_heroe_mas_alto()
