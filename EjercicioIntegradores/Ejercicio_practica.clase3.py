import data_stark

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

# b -Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
lista_de_heroes = data_stark.lista_heroes


def mostrar_heroes():
    for heroe in lista_de_heroes:
        print(heroe["nombre"])

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

#Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)

def mostrar_heroe_mas_alto():

    for indice in range(len(lista_de_heroes)):
        altura_str = lista_de_heroes[indice]["altura"] # en el dicc esta type <str>
        altura_float = float(altura_str)
        if(indice == 0 or altura_float > altura_max):
            altura_max = altura_float
            indice_max = indice
        

    print("El mas alto es{0} con la altura: {1}".format(
        lista_de_heroes[indice_max]["nombre"],altura_max ))


mostrar_heroe_mas_alto()
