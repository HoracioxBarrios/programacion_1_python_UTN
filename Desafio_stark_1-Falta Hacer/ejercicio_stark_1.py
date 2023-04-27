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
lista_heroes =\
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
},
{
"nombre": "Pepe",
"identidad": "Howard (Last name unrevealed)",
"empresa": "Marvel Comics",
"altura": "795.349999999999994",
"peso": "18.449999999999999",
"genero": "M",
"color_ojos": "Brown",
"color_pelo": "Yellow",
"fuerza": "2",
"inteligencia": "average"
},
{
"nombre": "Dalia",
"identidad": "Rocket Raccoon",
"empresa": "Marvel Comics",
"altura": "122.77",
"peso": "25.73",
"genero": "F",
"color_ojos": "Azul",
"color_pelo": "Brown",
"fuerza": "5",
"inteligencia": ""
},
{
"nombre": "Pricila",
"identidad": "Rocket Raccoon",
"empresa": "Marvel Comics",
"altura": "155.77",
"peso": "25.73",
"genero": "F",
"color_ojos": "Green",
"color_pelo": "Brown",
"fuerza": "5",
"inteligencia": ""
}
]

# Funciones que muestran
def print_lista_dicc_completo(lista : list[dict])-> None:
    '''
    Recorre una lista de diccionario , muestra los elementos clave y valor
    y los imprime por .
    Recibe una lista con diccionrios dentro
    Devuelve - no aplica
    -
    '''
    contador = 1
    for diccionario in lista:
        print("---------------------------Dato:({0}) ".format(contador))
        for clave, valor  in diccionario.items():
            if(len(diccionario)):
                print(clave, valor)
        contador += 1


def print_dicc(diccionario):
    '''
    muestra un diccionario
    Recibe un diccionario
    devuelve, no aplica
    '''
    print("------------ Resultado ------------")
    for clave, valor in diccionario.items():
        print("------------")
        print("{0} : {1} ".format(clave, valor))
    
#Funcion que recorre una Lista[Dict] y crea un nueva lista dicc a medida
# La usé para listar generos
def listar_por_clave_valor(
    lista : list[dict], clave_requerida : str, valor_requerido : str)-> list[dict]:
    '''
    De una lista[dict] crea una nueva  lista de dicc a medida.
    
    Recibe un arg(1)lista de dicc, arg(2) una clave, y arg(3)un valor
    ej: clave_requerida ="genero", valor_requerido = "F".
    
    Devuelve - una nueva lista[dict]
    '''
    nueva_lista_dicc = []
    for dicc in lista:
        if(dicc[clave_requerida] == valor_requerido and 
            dicc[clave_requerida] not in nueva_lista_dicc):
            nueva_lista_dicc.append(dicc)
    return nueva_lista_dicc
                
#El Max y el Min de la Lista de Dicc
def max_min_de_lista_dicc(
    lista: list[dict], clave_requerida :str, maximo = True)-> dict:
    '''
    De una lista[dicc] convierte de str a float para dar 
    el maximo o el minimo segun necesidad.
    Recibe arg(1)una lista[dict], arg(2) clave ej:clave_requerida="altura",
    arg(3) maximo o minimo. 
    devuelve el maximo o el minimo.
    '''
    for indice in range(len(lista)):
        lista[indice][clave_requerida] = float(lista[indice][clave_requerida])
        if(indice == 0 or lista[indice][clave_requerida] > maximo_valor and maximo == True):
            maximo_valor = lista[indice][clave_requerida]
            maximo_indice = lista[indice]
        if(indice == 0 or lista[indice][clave_requerida] < minimo_valor and maximo == False):
            minimo_valor = lista[indice][clave_requerida]
            minimo_indice = lista[indice]
    if(maximo == True):
        return maximo_indice
    if(maximo == False):
        return minimo_indice
        
# promediar por clave
def promediar_por_clave(lista : list[dict], clave_requerida : str)-> int:
    '''
    muestra el promedio
    recibe una list[dict] y una clave ej: "altura"
    devuelve el promedio
    '''
    cantidad = len(lista)
    acumulador = 0
    for diccionario in lista:
        valor_a_acumular = float(diccionario[clave_requerida])
        acumulador += valor_a_acumular
    promedio = acumulador / cantidad
    return(promedio)



#agrupa contando por tipo
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
    1

            
''' no cuenta los de inteligencia cundo tiene valot = "     '''        
            
            
            
            
            
            
    
while(True):
    respuesta_str = input("Elija una opcion:\n 1-Ver Lista Completa\n 2-Ver los personajes Masculinos \n 3-Ver los personajes Femeninos \n 4-Ver el mas alto Masculino \n 5-Ver el mas Alto Femenino \n 6-Ver el mas bajo Masculino \n 7-Ver el mas bajo Femenino \n 8-Ver la altura promedio Masculinos \n 9-Ver la altura promedio Femeninos \n 10-personajes por tipo de color de ojos \n 11-personajes por tipo de color de Pelo \n 12-Ver personajes por tipo de inteligencia \n 13-listar por color de ojos\n 14-listar por color de Pelo\n 15- listar por inteligencia\n 16- Salir\n")
    respuesta_int = int(respuesta_str)
    
    match(respuesta_int):
        case 1:
           print_lista_dicc_completo(lista_heroes)
        case 2:
            print_lista_dicc_completo(listar_por_clave_valor(
                lista_heroes, clave_requerida ="genero", valor_requerido = "M"))
        case 3:
            print_lista_dicc_completo(listar_por_clave_valor(
                lista_heroes, clave_requerida ="genero", valor_requerido = "F"))
        case 4:
            lista_dicc_resultado = listar_por_clave_valor(
                lista_heroes, clave_requerida ="genero", valor_requerido = "M")
        
            print_dicc(max_min_de_lista_dicc(
                lista_dicc_resultado, clave_requerida="altura", maximo = True))
        case 5:
            lista_dicc_resultado = listar_por_clave_valor(
                lista_heroes, clave_requerida ="genero", valor_requerido = "F")
            
            print_dicc(max_min_de_lista_dicc(
                lista_dicc_resultado, clave_requerida="altura", maximo = True))
        case 6:
            lista_dicc_resultado = listar_por_clave_valor(lista_heroes,
                clave_requerida ="genero", valor_requerido = "M")
            
            print_dicc(max_min_de_lista_dicc(lista_dicc_resultado,
                clave_requerida="altura", maximo = False))
        case 7:
            lista_dicc_resultado = listar_por_clave_valor(
                lista_heroes, clave_requerida ="genero", valor_requerido = "F")
            
            print_dicc(max_min_de_lista_dicc(
                lista_dicc_resultado, clave_requerida="altura", maximo = False))
        case 8:
            lista_dicc_resultado = listar_por_clave_valor(
                lista_heroes, clave_requerida ="genero", valor_requerido = "M")
            
            promedio_masculino =  promediar_por_clave(lista_dicc_resultado, clave_requerida="altura")
            print("El promedio de Masculino es:{0}".format(promedio_masculino))
        case 9:
            lista_dicc_resultado = listar_por_clave_valor(
                lista_heroes, clave_requerida ="genero", valor_requerido = "F")
            
            promedio_femenino = promediar_por_clave(lista_dicc_resultado, clave_requerida="altura")
            print("El promedio de Femenino es: {0}".format(promedio_femenino))
        case 10:
           print(contar_por_tipo(lista_heroes, clave_tipo="color_ojos"))
        case 11:
           print(contar_por_tipo(lista_heroes, clave_tipo ="color_pelo"))
        case 12:
           print(contar_por_tipo(lista_heroes, clave_tipo ="inteligencia"))
        case 13:
           pass
        case 14:
          pass 
        case 15:
            pass
        case 16:
           break

    input("Pulse Enter para continuar\n ")
