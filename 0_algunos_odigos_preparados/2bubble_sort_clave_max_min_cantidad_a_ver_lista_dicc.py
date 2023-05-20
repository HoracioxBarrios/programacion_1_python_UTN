
lista_heroes_prueba =\
[   {
      "nombre": "MystiqueChuo",
      "identidad": "Raven Darkholme",
      "empresa": "Marvel Comics",
      "altura": 120.65000000000001,
      "peso": 15.960000000000001,
      "genero": "F",
      "color_ojos": "Yellow (without irises)",
      "color_pelo": "red / orange",
      "fuerza": "15",
      "inteligencia": "good"
    },
    {
      "nombre": "Mystique",
      "identidad": "Raven Darkholme",
      "empresa": "Marvel Comics",
      "altura": 178.65000000000001,
      "peso": 54.960000000000001,
      "genero": "F",
      "color_ojos": "Yellow (without irises)",
      "color_pelo": "red / orange",
      "fuerza": "15",
      "inteligencia": "good"
    },
    {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": 79.349999999999994,
    "peso": 180.449999999999999,
    "genero": "F",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  }]
  #Lista de ejemplo


def cantidad_a_listar_por_user(lista_heroes_ordenada : list[dict], cant_a_listar = 0):
    '''
    Lista (una lista de heroes ordenada) en base a una cantidad.
    Recibe: (arg 1) una lista de heroes, 
    (arg 2) recibe la cantidad a listar. (defaul es 0 para que no listar)-
    para el caso que el usuario quiera la lista ordenada completa. 
    La uso en combienacion con la funcion ordenar_numeros_bubble_sort_v5()
    
    Devuelve por la cantidad a listar por el usuario.
    '''
    if(lista_heroes_ordenada and cant_a_listar > 0 
       and cant_a_listar <= len(lista_heroes_ordenada)):
        nueva_lista_cant_elegida = []
        len_a_ver = cant_a_listar 
        for indice in range(len_a_ver):
            nueva_lista_cant_elegida.append(lista_heroes_ordenada[indice])
        return nueva_lista_cant_elegida
    else:
        return -1


def ordenar_numeros_bubble_sort_v5(
    lista_heroes: list[dict], clave : str, ordenamiento = "asc",cant_a_listar = 0)-> list[dict]:
    '''
    Ordena una lista de Heroes segun clave y ordenamiento escogido.
    
    Recibe: (arg 1) una lista de heroes list[dict],
    (arg 2) una clave a evaluar ("peso", "altura", "fuerza")
    (arg 3) forma de ordenamiento (por defaul: "asc"  de minimo a maximo)
    como segunda opcion puede ser tambien: "des" de maximo a minimo
    (arg 4) cuantos quiere ver ordenados. 0 es la lista completa o la cant.
    que se le pase por parametro.
    
    Devuelve: la lista ordenada, o si esta vacia se informa.
    '''
    if(lista_heroes):
        # lista_heroes = lista_heroes_origen[:]
        len_de_lista = len(lista_heroes) -1
        flag_swap = True
        while(flag_swap):
            flag_swap = False
            for indice in range(len_de_lista):
                if(lista_heroes[indice][clave] > lista_heroes[indice +1][clave] and 
                   ordenamiento == "asc"):
                    aux_backup_valor = lista_heroes[indice]
                    lista_heroes[indice] = lista_heroes[indice +1]
                    lista_heroes[indice +1] = aux_backup_valor
                    flag_swap = True
                elif(lista_heroes[indice][clave] < lista_heroes[indice +1][clave] and 
                   ordenamiento == "des"):
                    aux_backup_valor = lista_heroes[indice]
                    lista_heroes[indice] = lista_heroes[indice +1]
                    lista_heroes[indice +1] = aux_backup_valor
                    flag_swap = True
            len_de_lista -= 1
        
        if cant_a_listar == 0:
            return lista_heroes
        else:
            return cantidad_a_listar_por_user(lista_heroes, cant_a_listar)
    else:
        return "La lista esta vacia"    


def print_heroe(lista_heroes : list[dict]):
    for heroe in lista_heroes:
        mensaje = "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}\n".format(heroe["nombre"], \
        heroe["identidad"], heroe["empresa"],heroe["altura"], heroe["peso"], heroe["genero"], \
        heroe["color_ojos"],heroe["color_pelo"], heroe["fuerza"], heroe["inteligencia"])

        print(mensaje)

   
lista_ordenada = ordenar_numeros_bubble_sort_v5(
    lista_heroes_prueba, clave= "altura", ordenamiento= "des",cant_a_listar= 3)

print_heroe(lista_ordenada)

