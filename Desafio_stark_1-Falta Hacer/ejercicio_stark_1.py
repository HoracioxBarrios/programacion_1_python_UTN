from data_stark import lista_personajes
'''
Formato de los datos recibidos
lista_heroes =
[
{
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
},
{
"nombre": "Rocket Raccoon",
"identidad": "Rocket Raccoon",
"empresa": "Marvel Comics",
"altura": "122.77",
"peso": "25.73",
"genero": "M",
"color_ojos": "Brown",
"color_pelo": "Brown",
"fuerza": "5",
"inteligencia": "average"
}
]

Desafío #01:
0 -Agregar al código elaborado para cumplir el desafío #01 los siguientes 
puntos, utilizando un menú que permita acceder a cada uno de los puntos 
por separado.
1- imprimir lista completa
2 -Recorrer la lista imprimiendo por consola el nombre de cada superhéroe 
de género M
3-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
de género F

4- Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
5- Recorrer la lista y determinar cuál es el superhéroe más alto de género F 

6 -Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
7- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 

8- Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
9- Recorrer la lista y determinar la altura promedio de los  superhéroes de género F

Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
10- Determinar cuántos superhéroes tienen cada tipo de color de ojos.
11- Determinar cuántos superhéroes tienen cada tipo de color de pelo.
12-Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
13- Listar todos los superhéroes agrupados por color de ojos.
14 -Listar todos los superhéroes agrupados por color de pelo.
15 -Listar todos los superhéroes agrupados por tipo de inteligencia

'''

def print_heroes(personaje):
    ''' 
    imprime una lista de dicc personaje
    recibe un lista de dicc
    devuelve - no aplica
    '''
    print(
    "nombre: {0} - identidad: {1} - empresa: {2} - altura:{3} - peso:{4} - genero:{5} - color_ojos:{6} - color_pelo:{7} - fuerza:{8} - inteligencia:{9}\n".format(
    personaje["nombre"], personaje["identidad"], personaje["empresa"], personaje["altura"],
    personaje["peso"], personaje["genero"], personaje["color_ojos"],
    personaje["color_pelo"], personaje["fuerza"], personaje["inteligencia"]
    ))

def mostrar_lista_completa(lista: list):
    '''
    recorre una lista y muestra 
    recibe una lista de dicc
    retorna - no aplica'''
    for personaje in lista:
        print_heroes(personaje)


def mostrar_personaje(lista: list ,genero: str):
    for personaje in lista:
        if(personaje["genero"] == genero):
            print(personaje["nombre"])

#4- Recorrer la lista y determinar cuál es el superhéroe más alto de género M 

# def max_min_de_la_lista(lista, clave):
#     max_min_indice = 0
#     for indice in range(1, len(lista)):
#         if (lista[indice][clave] > lista[max_min_indice][clave]):
#             max_min_indice = indice
#     return max_min_indice

def heroe_segun_altura_genero_v2(lista_heroes: list, genero: str, min_max: str) -> None:
    heroe_aux = {}
    for heroe in lista_heroes:
        if not heroe_aux and (heroe['genero'] == genero):# en la primera iteracion, guarda el primero
            heroe_aux = heroe
        if (heroe_aux and heroe['genero'] == genero):
            if ((min_max == 'Bajo' and float(heroe['altura']) < float(heroe_aux['altura'])) or 
                (min_max == 'Alto' and float(heroe['altura']) > float(heroe_aux['altura']))):
                    heroe_aux = heroe

    print(f"Nombre: {heroe_aux['nombre']} - Altura: {heroe_aux['altura']} mts.")



while(True):
    respuesta_str = input("Elija una opcion:\n 1-Ver Lista Completa\n 2-Ver los personajes Masculinos \n 3-Ver los personajes Femeninos \n 4-Ver el mas alto Masculino \n 5-Ver el mas Alto Femenino \n 6-Ver el mas bajo Masculino \n 7-Ver el mas bajo Femenino \n 8-Ver la altura promedio Masculinos \n 9-Ver la altura promedio Femeninos \n 10-personajes por tipo de color de ojos \n 11-personajes por tipo de color de Pelo \n 12-Ver personajes por tipo de inteligencia \n 13-Salir\n\n")
    respuesta_int = int(respuesta_str)
    
    match(respuesta_int):
        case 1:
            mostrar_lista_completa(lista_personajes)
        case 2:
            mostrar_personaje(lista_personajes,genero = "M")
        case 3:
            mostrar_personaje(lista_personajes,genero = "F")
        case 4:
            heroe_segun_altura_genero_v2(lista_personajes, genero="M", min_max="Alto")
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            break

    input("Pulse Enter para continuar\n\n ")
