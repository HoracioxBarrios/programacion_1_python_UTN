from data_stark import lista_heroes

def stark_normalizar_datos(lista_heroes:list) -> str:
    if not lista_heroes:
        return(print('ERROR!! La lista de heroes esta vacia!'))
    datos_normalizados = False
    if not isinstance(lista_heroes[0]['peso'], (int, float)):
        for heroe in lista_heroes:
            for key,value in heroe.items():
                if '.' in value:
                    value_modificado = float(value)
                    heroe[key] = value_modificado
                    datos_normalizados = True
                elif value.isdigit():
                    value_modificado = int(value)
                    heroe[key] = value_modificado
                    datos_normalizados = True
    if datos_normalizados:
        print('\nDatos normalizados')
    else:
        print('\nNo hizo falta normalizar datos')

stark_normalizar_datos(lista_heroes)


#................................................PUNTO 1.......................................................
def obtener_nombre(diccionario: dict) -> str:
    for key,value in diccionario.items():
        if key == 'nombre':
            nombre_a_mostrar = value
    string_del_nombre = f"\nNombre: {nombre_a_mostrar}"
    return string_del_nombre

def imprimir_dato(dato):
    print(dato)

def stark_imprimir_nombres_heroes(lista_de_heores:list):
    if not lista_de_heores:
        return -1
    for heroe in lista_de_heores:
        nombre = obtener_nombre(heroe)
        imprimir_dato(nombre)
#................................................PUNTO 2.......................................................
def obtener_nombre_y_dato(diccionario:dict,clave:str) -> str:
    for key,value in diccionario.items():
        if key == 'nombre':
            nombre_a_mostrar = value
        if key == clave:
            clave_a_mostrar = key
            valor_a_mostrar = value
    string_combinada = f"\nNombre: {nombre_a_mostrar} | {clave_a_mostrar}: {valor_a_mostrar}"
    return string_combinada

def stark_imprimir_nombres_alturas(lista_de_heroes:list):
    clave = 'altura'
    if not lista_de_heroes:
        return -1
    for heroe in lista_de_heroes:
        string_heroe_altura = obtener_nombre_y_dato(heroe,clave)
        print(string_heroe_altura)
#............................................PUNTO 3, 4, 6, 7..................................................
def calcular_max(lista_de_heroes:list,clave:str) -> str:
    bandera_max = 0
    for heroe in lista_de_heroes:
        if bandera_max == 0 or heroe[clave] > valor_max:
            nombre_valor_max = heroe['nombre']
            valor_max = heroe[clave]
            bandera_max = 1
    return(nombre_valor_max)

def calcular_min(lista_de_heroes:list,clave:str) -> str:
    bandera_min = 0
    for heroe in lista_de_heroes:
        if bandera_min == 0 or heroe[clave] < valor_min:
            nombre_valor_min = heroe['nombre']
            valor_min = heroe[clave]
            bandera_min = 1
    return(nombre_valor_min)

def calcular_max_min_dato(lista_de_heroes:list,calculo:str,clave:str):
    for heroe in lista_de_heroes:
        if calculo == 'maximo':
            return(calcular_max(lista_de_heroes,clave))
        elif calculo == 'minimo':
            return(calcular_min(lista_de_heroes,clave))

def stark_calcular_imprimir_heroe(lista_de_heroes:list,calculo:str,clave:str):
    if not lista_de_heroes:
        return -1
    nombre = calcular_max_min_dato(lista_de_heroes,calculo,clave)
    if calculo == 'maximo':
        max_o_min = 'Mayor'
    elif calculo == 'minimo':
        max_o_min = 'Menor'
    for heroe in lista_de_heroes:
        if nombre == heroe['nombre']:
            match (stark_menu_principal()):
                case 6:
                    llamada = f"\n{max_o_min} {clave}: {nombre} | {clave}: {heroe[clave]} | Identidad: {heroe['identidad']}"
                case _:
                    llamada = f"\n{max_o_min} {clave}: {nombre} | {clave}: {heroe[clave]}"
    imprimir_dato(llamada)
#................................................PUNTO 5.......................................................
def sumar_dato_heroe(lista_de_heroes:list,clave:str) -> float:
    acumulador_valor_clave = 0
    for heroe in lista_de_heroes:
        if isinstance(heroe , dict) and heroe:
            acumulador_valor_clave += heroe[clave]
    return acumulador_valor_clave

def dividir(numero_uno,numero_dos) -> float:
    dividendo = numero_uno
    divisor = numero_dos
    if divisor == 0:
        return 0
    else:
        resultado = dividendo / divisor
    return resultado

def calcular_promedio(lista_de_heroes:list,clave:str) -> float:
    promedio = dividir(sumar_dato_heroe(lista_de_heroes,clave),len(lista_de_heroes))
    return promedio

def stark_calcular_imprimir_promedio_altura(lista_de_heroes:list,clave):
    if not lista_de_heroes:
        return -1
    promedio_altura = calcular_promedio(lista_de_heroes, "altura")
    imprimir_dato(f"\nEl promedio de altura del total de heroes es: {promedio_altura}")
#..............................................................................................................
def retornar_menu():
    menu = '\nMenu de opciones:\n1- Mostrar el nombre de los superheroes.\n2- Mostrar el nombre y la altura de cada superheore.\n3- Mostrar el superheroe mas alto.\n4- Mostrar el superheroe mas bajo.\n5- Mostrar la altura promedio del total de superheroes.\n6- Mostrar la identidad de los superheroes que corresponden al mas alto y al mas bajo.\n7- Mostrar el superheroe mas y el menos pesado.\ningrese la opcion deseada: '
    return menu

def validar_entero(string:str) -> int:
    if string.isdigit():
        return int(string)
    return -1

def stark_menu_principal():
    opcion = validar_entero(input(retornar_menu()))
    if opcion:
        return opcion
    else:
        return -1

def stark_marvel_app(lista_de_heroes):
    match (stark_menu_principal()):
        case 1:
            stark_imprimir_nombres_heroes(lista_heroes)
        case 2:
            stark_imprimir_nombres_alturas(lista_heroes)
        case 3:
            stark_calcular_imprimir_heroe(lista_heroes,'maximo','altura')
        case 4:
            stark_calcular_imprimir_heroe(lista_heroes,'minimo','altura')
        case 5:
            stark_calcular_imprimir_promedio_altura(lista_heroes,'altura')
        case 6:
            stark_calcular_imprimir_heroe(lista_heroes,'maximo','altura')
            stark_calcular_imprimir_heroe(lista_heroes,'minimo','altura')
        case 7:
            stark_calcular_imprimir_heroe(lista_heroes,'maximo','peso')
            stark_calcular_imprimir_heroe(lista_heroes,'minimo','peso')
        case _:
            print('\nOpcion Invalida!!')

while True:            
    stark_marvel_app(lista_heroes)

