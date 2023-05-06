from data import lista_bzrp
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
#------------------ Print Lista
def mostrar_lista_de_videos():
    for video in lista_bzrp:
        print("\nTitulo: {0} - views: {1} - length: {2}".format(
            video["title"], video["views"], video["length"]))

#-------------------- Mas visto
def calcular_tema_vas_visto():
    # maximo_views = None            se vuelven innecesaria
    # maximo_indice = None
    for indice in range(len(lista_bzrp)): #Genero un indice, asi busco el indice del mas visto y con ese dato puedo printear las demas keys con sus valores
        if(indice == 0 or maximo_views < lista_bzrp[indice]["views"] ):
            maximo_views = lista_bzrp[indice]["views"]   # esto se usa para comparar
            maximo_indice = indice                       #Lo que mas interesa es obtener este maximo_indice para poder ingresar a los demas keys/valores
    print("El tema  mas visto es: {0} con {1} de views".format(
        lista_bzrp[maximo_indice]["title"],
        lista_bzrp[maximo_indice]["views"]))

#-------------------- Menos Visto
def calcular_tema_menos_visto():
    for indice in range(len(lista_bzrp)):# genero indice para recorrer
        if(indice == 0 or lista_bzrp[indice]["views"] < minimo_views): # el indice 0 es mi flag
            minimo_views = lista_bzrp[indice]["views"]
            minimo_indice = indice
    print("El tema  menos visto es: {0} con {1} de views".format(
        lista_bzrp[minimo_indice]["title"],
        lista_bzrp[minimo_indice]["views"]))

    '''EL CODIGO DE ARRIBA ,PERO MAS NINJA: '''
    # for indice in range(len(lista_bzrp)):# genero indice para recorrer
    #     if(indice == 0 or lista_bzrp[minimo_indice]["views"] < lista_bzrp[indice]["views"]): # el indice 0 es mi flag
    #         minimo_indice = indice
            
    # print("El tema  menos visto es: {0} con {1} de views".format(
    #     lista_bzrp[minimo_indice]["title"],
    #     lista_bzrp[minimo_indice]["views"]))

#--------------------- Mas Largo
def calcular_tema_mas_largo():
    #maximo_largo
    for indice in range(len(lista_bzrp)):
        if(
        indice == 0 or lista_bzrp[maximo_indice]["length"] < lista_bzrp[indice]["length"]):
            maximo_indice = indice
    print("El tema de mayor duracion es: {0} con: {1}".format(
        lista_bzrp[maximo_indice]["title"], lista_bzrp[maximo_indice]["length"]))

#---------------------- Mas corto
def calcular_tema_mas_corto():
    #minimo_largo
    for indice in range(len(lista_bzrp)):
        if(indice == 0 or lista_bzrp[indice]["length"] < lista_bzrp[minimo_indice]["length"]):
            minimo_indice = indice
    print("El tema de menor duracion es: {0} con: {1}".format(
        lista_bzrp[minimo_indice]["title"], lista_bzrp[minimo_indice]["length"]))

#----------------------- Duracion Promedio
def calcular_duracion_promedio():
    acum_duracion_videos = 0
    
    for video in lista_bzrp:
        acum_duracion_videos += video["length"]
    promedio_duracion = acum_duracion_videos / len(lista_bzrp)
    print("El promedio de duracion de los Videos es: {0}".format(promedio_duracion))

#---------------------- Vistas promedio
def calcular_vistas_promedio():
    acum_views_videos = 0
    
    for video in lista_bzrp:
        acum_views_videos += video["views"]
    print("El promedio de duracion de los Videos es: {0}".format(acum_views_videos / len(lista_bzrp))) # El profe Davila enseño que esto se puede hacer asi.

#------------------Print cant temas
def mostrar_cantidad_de_videos_de_la_lista():
    cantidad_de_videos = len(lista_bzrp)
    print("Hay {0} Videos en la Lista".format(cantidad_de_videos))







while (True):
    respuesta_str = input(
        "Opciones: \n 1- Tema mas visto\n 2- Tema menos Visto\n 3- Tema mas Largo\n 4- Tema mas corto \n 5- Promedio de Duracion Temas\n 6- Promedio de Vistas\n 7- Mostrar Lista\n 8- Mostar Cantidad de videos\n 9- Salir \n\n")
    # Falta validar
    respuesta_int = int(respuesta_str)

    match(respuesta_int):
        case 1:
            # Tema mas visto
            calcular_tema_vas_visto()
        case 2:
            # Tema menos visto
            calcular_tema_menos_visto()
        case 3:
            # Tema mas largo
            calcular_tema_mas_largo()
        case 4:
            # Tema mas corto
            calcular_tema_mas_corto()
        case 5:
            # Duracion Promedio de temas
            calcular_duracion_promedio()
        case 6:
            # Promedio de vistas
            calcular_vistas_promedio()
        case 7:
            # Mostrar Lista ------Lo primero que hay que hacer es recorrerla
            mostrar_lista_de_videos()
        case 8:
            mostrar_cantidad_de_videos_de_la_lista()
        case 9:
            # Salir
            break  # Rompe la estructura iterativa mas cercana
    input("Pulse enter para continuar")  # detalle para que en la consola pause
