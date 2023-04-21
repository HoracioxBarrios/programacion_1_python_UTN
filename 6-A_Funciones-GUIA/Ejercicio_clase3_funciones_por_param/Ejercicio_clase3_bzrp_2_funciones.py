from data import lista_bzrp
# from data import lista_pepe  # psando por parametro lista_de_temas podria despues pasar una lista distinta para cada caso
# from data import rulo        #podria tener varias listas(estas dos son ejemplos)
'''
[
    
    {
        'title': 'QUEVEDO || BZRP Music Sessions #52',
        'views': 227192970,
        'length': 204,
        'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
        'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
        'date': '2022-07-06 00:00:00'
    }
]
---------------------------- lista original, la mia esta cambiada
1 - Tema mas visto
2 - Tema menos visto
3 - Tema mas largo
4 - Tema mas corto
5 - Duracion promedio de temas
6 - Promedio de vistas 
7 - Salir
'''

def print_tema(tema): #Recibe un diccionario que reprecenta un tema, generado en el for de abajo
    '''
    Mustra un tema por terminal
    recibe el diccionario del tema a mostrar
    retorna - no aplica
    '''
    print("\n Titulo: {0} - Views: {1} - Length: {2}".format(
        tema['title'],
        tema['views'],
        tema['length']))
#-----------------------------------------------------------------
def mostrar_lista_de_temas(lista_de_temas):  #Funcion que recorre la lista, espera una LISTA DE TEMAS
    '''
    Mustra una lista de temas por terminal
    recibe la lista de temas
    retorna - no aplica
    '''
    for tema in lista_de_temas:
        print_tema(tema)

def mostrar_cantidad_de_videos_de_la_lista():
    pass



def calcular_tema_mas_menos_por_Clave(lista_de_temas,clave , maximo = True): 
    '''
    Calcula el tema mas / menos dependiendo de la clave(key)
    recibe: arg(1)una lista de temas, arg(2)espera una key: 'views','length'  arg(3)si busca max o min. 
    por defecto maximo = True.
    
    retorna - por defecto el tema max / min
    '''
    indice_max_min = 0
    for indice_actual in range(1, len(lista_de_temas)):
        if(maximo):
            if lista_de_temas[indice_actual][clave] > lista_de_temas[indice_max_min][clave]:
                indice_max_min = indice_actual
        else:
            if lista_de_temas[indice_actual][clave] < lista_de_temas[indice_max_min][clave]:
                indice_max_min = indice_actual
                
    return lista_de_temas[indice_max_min]


def calcular_tema_menos_visto():
    pass

def calcular_tema_mas_largo():
    pass

def calcular_tema_mas_corto():
    pass

def calcular_duracion_promedio():
    pass


def calcular_vistas_promedio():
    pass





while (True):
    respuesta_str = input(
        "Opciones: \n 1- Tema mas visto\n 2- Tema menos Visto\n 3- Tema mas Largo\n 4- Tema mas corto \n 5- Promedio de Duracion Temas\n 6- Promedio de Vistas\n 7- Mostrar Lista\n 8- Mostar Cantidad de videos\n 9- Salir \n\n")
    # Falta validar
    respuesta_int = int(respuesta_str)

    match(respuesta_int):
        case 1:
            # Tema mas visto
            tema_mas_visto = calcular_tema_mas_menos_por_Clave(lista_bzrp,'views') #como la funcion retorna el tema mas visto. lo atajamos en esa variable y luego la mostramos - parametro maximo = true por defecto
            print_tema(tema_mas_visto)
        case 2:
            # Tema menos visto
            tema_menos_visto = calcular_tema_mas_menos_por_Clave(lista_bzrp,'views', maximo = False)
            print_tema(tema_menos_visto)
        case 3:
            # Tema mas largo
            tema_mas_largo = calcular_tema_mas_menos_por_Clave(lista_bzrp,'length') 
            print_tema(tema_mas_largo)
        case 4:
            # Tema mas corto
            tema_mas_corto= calcular_tema_mas_menos_por_Clave(lista_bzrp,'length', maximo= False) 
            print_tema(tema_mas_corto)
        case 5:
            # Duracion Promedio de temas
            calcular_duracion_promedio()
        case 6:
            # Promedio de vistas
            calcular_vistas_promedio()
        case 7:
            # Mostrar Lista ------Lo primero que hay que hacer es recorrerla
            mostrar_lista_de_temas(lista_bzrp) #''' Ahora espera la lista'''
        case 8:
            mostrar_cantidad_de_videos_de_la_lista()
        case 9:
            # Salir
            break  # Rompe la estructura iterativa mas cercana
    input("Pulse enter para continuar")  # detalle para que en la consola pause
