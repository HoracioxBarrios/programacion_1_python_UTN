from set_de_datos_list_dict import lista_personajes

#datos altura en float (ver set de datos)

def sumar_dato_heroe_genero(
    lista_heroes: list[dict], clave_a_calcular: str, genero_buscado: str) -> int:
    """
    Acumula la suma de una clave en un diccionario para héroes de un género 
    específico.
    (arg1)lista_heroes: Lista de diccionarios de héroes.
    (arg2) clave_a_calcular: Clave a sumar en cada héroe.
    (arg3)genero_buscado: Género de los héroes a filtrar 'F' o 'M'.
    Devuelve La suma de los valores de la clave en los héroes que cumplen las 
    condiciones, -1 en caso contrario
    """
    acumulador_de_dato = 0
    
    for dicc_heroe in lista_heroes:
        if(bool(type(dicc_heroe)) and dicc_heroe 
           and "genero" in dicc_heroe 
           and dicc_heroe["genero"] == genero_buscado 
           and clave_a_calcular in dicc_heroe):
            acumulador_de_dato += dicc_heroe[clave_a_calcular]
            
    if(acumulador_de_dato > 0):
        return acumulador_de_dato
    else:
        return -1
    
    
def cantidad_heroes_genero(lista_heroes : list[dict], genero_buscado : str)-> int:
    '''
    Da la cantidad de heroes del genero elegido.
    Recibe una lista de diccionario heroe
    devuelve la cantidad
    '''
    contador_de_heroes_genero = 0
    for heroe in lista_heroes:
        if(heroe["genero"] == genero_buscado):
            contador_de_heroes_genero += 1
            
    if(contador_de_heroes_genero > 0):
        return contador_de_heroes_genero
    else:
        return contador_de_heroes_genero


def dividir(dividendo, divisor )-> float:
    '''
    realiza la division entre dos numeros
    recibe un dividendo Int o Float, y un divisor int o float
    devuelve el resultado (float) o en caso de error 0
    '''
    if divisor != 0 and isinstance(dividendo, (int, float)) and isinstance(
        divisor, (int, float)):
        return dividendo / divisor
    else:
        return 0


def calcular_promedio_genero(
    lista_heroes : list[dict], clave_a_calcular : str, genero_buscado : str)-> float:
    '''
    calcula el promedio total segun necesidad en base a una lista de heroes
    recibe una lista de dicc heroes y una clave a calcular (ej: clave = "altura")
    devuelve el promedio
    '''
    resultado_acumulado = sumar_dato_heroe_genero(
        lista_heroes, clave_a_calcular,genero_buscado)
    cantidad_de_heroes = cantidad_heroes_genero(lista_heroes, genero_buscado)
    promedio = dividir(resultado_acumulado, cantidad_de_heroes)
    return promedio



''' Para no ejecutar muchas lienas en las opciones, crearemos una funcion que haga eso:

resultado_promedio = calcular_promedio_genero(
    lista_personajes, "altura", genero_buscado="M")
    print(resultado_promedio)
'''


def calcular_y_mostrar_promedio_por_clave(
    lista_personajes : list[dict], clave_a_calcular : str, genero_buscado : str)-> None:
    '''
    se encarga de calcular y mostrar 
    recibe:(arg1)..., (arg2),... (arg3)...
    Devuelve - no aplica
    '''
    resultado_promedio = calcular_promedio_genero(
    lista_personajes, clave_a_calcular, genero_buscado)
    print(resultado_promedio)
    
    



''' en las opciones de la aplicacion'''

#case 1:
calcular_y_mostrar_promedio_por_clave(
    lista_personajes, "altura", genero_buscado="F")
    
