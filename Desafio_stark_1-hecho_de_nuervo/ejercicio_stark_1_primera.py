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
16 - Salir
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
        print("------------------------------")
        print_heroes(personaje)
        print("------------------------------")


def print_clave_valor(diccionario):
    for clave, valor in diccionario.items():
        print("{0} {1}".format(clave,valor))


def print_personaje_genero(lista: list ,genero: str):
    '''
    de una lista muestra los nombre segun su genero
    recibe una lista. y un genero clave M o F 
    devuelve, no aplica
    '''
    for personaje in lista:
        if(personaje["genero"] == genero):
            print(personaje["nombre"])

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



def promedio_por_genero(lista : list ,clave_altura : str,clave_genero  : str, genero : str):
    '''
    da el promedio segun la necesidad.
    arg(1) recibe una lista de diccionarios, clave "altura", clave "genero" = F / M
    devuelve - no aplcia
    
    '''
    acumulador = 0
    nueva_lista = []
    for diccionario in lista:
        if(diccionario[clave_genero] == genero):
            acumulador += float(diccionario[clave_altura])
            nueva_lista.append(diccionario)
    cantidad_de_diccionarios_en_lista = len(nueva_lista)
    promedio = acumulador / cantidad_de_diccionarios_en_lista
    print("El promedio es {0}".format(promedio))
    return

def contar_por_tipo(lista : list, clave_tipo)-> dict:
    '''
    separa por tipo y los contabiliza
    recibe una list de dict
    retorna - una lista de dict con los tipos y cantidades correspondientes
    '''
    nuevo_dicc_contador = {}
    for diccionario in lista:
        nueva_clave = diccionario[clave_tipo]
        if (diccionario[clave_tipo] not in nuevo_dicc_contador):
            if(not diccionario[clave_tipo]):# si no tiene
                nueva_clave = "No tiene"
            nuevo_dicc_contador[nueva_clave] = 1
        else:
            nuevo_dicc_contador[nueva_clave] += 1
    return nuevo_dicc_contador
    



def devolver_variantes(lista, clave_tipo):
    aux = None
    nueva_lista = []
    flag = True
    for elem in lista:
        for clave , valor in elem.items():
            if(flag or aux):
                if(valor != aux  and clave == clave_tipo):
                    aux = valor
                    nueva_lista.append(aux)
                    flag = False
    return nueva_lista


def listar(lista, clave_tipo):
    nueva_lista = devolver_variantes(lista, clave_tipo)

    for variante in nueva_lista:
        for personaje in lista_personajes:
            if(personaje[clave_tipo] == variante):
                print_heroes(personaje)
                          

while(True):
    respuesta_str = input("Elija una opcion:\n 1-Ver Lista Completa\n 2-Ver los personajes Masculinos \n 3-Ver los personajes Femeninos \n 4-Ver el mas alto Masculino \n 5-Ver el mas Alto Femenino \n 6-Ver el mas bajo Masculino \n 7-Ver el mas bajo Femenino \n 8-Ver la altura promedio Masculinos \n 9-Ver la altura promedio Femeninos \n 10-personajes por tipo de color de ojos \n 11-personajes por tipo de color de Pelo \n 12-Ver personajes por tipo de inteligencia \n 13-listar por color de ojos\n 14-listar por color de Pelo\n 15- listar por inteligencia\n 16- Salir\n")
    respuesta_int = int(respuesta_str)
    
    match(respuesta_int):
        case 1:
            mostrar_lista_completa(lista_personajes)
        case 2:
            print_personaje_genero(lista_personajes,genero = "M")
        case 3:
            print_personaje_genero(lista_personajes,genero = "F")
        case 4:
            heroe_segun_altura_genero_v2(
                lista_personajes, genero="M", min_max="Alto")
        case 5:
            heroe_segun_altura_genero_v2(
                lista_personajes, genero = "F", min_max="Alto")
        case 6:
            heroe_segun_altura_genero_v2(
                lista_personajes, genero = "M", min_max = "Bajo")
        case 7:
            heroe_segun_altura_genero_v2(
                lista_personajes, genero = "F", min_max = "Bajo")
        case 8:
            promedio_por_genero(lista_personajes,
                clave_altura = "altura",clave_genero="genero", genero="M")
        case 9:
            promedio_por_genero(
                lista_personajes,
                clave_altura = "altura",clave_genero="genero", genero="F")
        case 10:
            resultado_color_pelo = contar_por_tipo(
                lista_personajes, clave_tipo = "color_ojos")
            print_clave_valor(resultado_color_pelo)
        case 11:
            resultado_ojos = contar_por_tipo(lista_personajes, clave_tipo = "color_pelo")
            print_clave_valor(resultado_ojos)
        case 12:
            tipos_inteligencia = contar_por_tipo(lista_personajes, clave_tipo = "inteligencia")
            print_clave_valor(tipos_inteligencia)
        case 13:
            listar(lista_personajes, clave_tipo = "color_ojos")
        case 14:
           listar(lista_personajes, clave_tipo = "color_pelo")
        case 15:
            listar(lista_personajes, clave_tipo = "inteligencia")
        case 16:
           break

    input("Pulse Enter para continuar\n ")
