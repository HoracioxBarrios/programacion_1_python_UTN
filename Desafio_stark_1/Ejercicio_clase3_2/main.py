from data_stark import lista_personajes

# Descomentar para probar que todo va bien
# print(lista_personajes)


# b- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def mostrar_heroes():
    for heroe in lista_personajes:
        print(heroe["nombre"])

# c-Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def mostrar_heroes_y_altura():
    for heroe in lista_personajes:
        print("Nombre: {0} su altura: {1} ".format(heroe["nombre"], heroe["altura"]))

# d-Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def mostrar_heroe_mes_alto():
    for indice in range(len(lista_personajes)):
        altura_str = lista_personajes[indice]["altura"] #cast str a float
        altura_float = float(altura_str)
        if(indice == 0 or altura_max < altura_float):# cometi un error de comparar con :lista_personajes[indice]["altura"] ya que es string el valor. por eso castee a float
            altura_max = altura_float
            indice_mas_alto = indice
    print("El heroe mas alto es: {0}su altura es {1}".format(
        lista_personajes[indice_mas_alto]["nombre"],lista_personajes[indice_mas_alto]["altura"]))

# e-Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def mostrar_heroe_mas_bajo():
    for indice in range(len(lista_personajes)):
        altura_str = lista_personajes[indice]["altura"]
        altura_float = float(altura_str)
        if(indice == 0 or altura_float < altura_min):
            altura_min = altura_float
            indice_de_mas_bajo = indice
    print("El heroe mas bajo es: {0}su altura es {1}".format(
        lista_personajes[indice_de_mas_bajo]["nombre"],lista_personajes[indice_de_mas_bajo]["altura"]))

# f-Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
def mostrar_altura_promedio():
    acum_de_altura = 0
    for indice in range(len(lista_personajes)):
        altura_str = lista_personajes[indice]["altura"]
        altura_float = float(altura_str)
        acum_de_altura += altura_float

    altura_promedio = acum_de_altura / len(lista_personajes)
    print("La altura promedio es: {0}".format(altura_promedio))



# h-Calcular e informar cual es el superhéroe más y menos pesado.
def mostrar_heroe_mas_pesado():
    for indice in range(len(lista_personajes)):
        peso_str = lista_personajes[indice]["peso"]
        peso_float = float(peso_str)
        if(indice == 0 or peso_float > peso_max):
            peso_max = peso_float
            indice_de_peso_max = indice
    print("El heroe con mas pesado es: {0} y su peso: {1}".format(
        lista_personajes[indice_de_peso_max]["nombre"], 
        lista_personajes[indice_de_peso_max]["peso"]))

def mostrar_heroe_menos_peso():
    for indice in range(len(lista_personajes)):
        peso_str = lista_personajes[indice]["peso"]
        peso_float = float(peso_str)
        if(indice == 0 or peso_float < peso_min):
            peso_min = peso_float
            indice_peso_min = indice
    print("El heroe con menos peso es: {0} con un peso: {1}".format(
        lista_personajes[indice_peso_min]["nombre"],
        lista_personajes[indice_peso_min]["peso"]
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
            
