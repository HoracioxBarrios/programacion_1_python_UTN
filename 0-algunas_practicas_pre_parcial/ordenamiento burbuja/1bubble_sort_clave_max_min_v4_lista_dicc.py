
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
  
def ordenar_numeros_bubble_sort_v4(
    lista_heroes : list[dict], clave : str, ordenamiento = "min_a_max")-> list[dict]:
    '''
    Ordena una lista de Heroes segun clave y ordenamiento escogido.
    Recibe: (arg 1) Recibe una lista de heroes list[dict],
    (arg 2) una clave a evaluar ("peso", "altura", "fuerza")
    (arg 3) forma de ordenamiento (por defaul: "min_a_max")puede tambien: "max_a_min"
    
    Devuelve: la lista ordenada, o si esta vacia se informa.
    '''
    if(lista_heroes):
        len_de_lista = len(lista_heroes) -1
        flag_swap = True
        while(flag_swap):
            flag_swap = False
            for indice in range(len_de_lista):
                if(lista_heroes[indice][clave] > lista_heroes[indice +1][clave] and 
                   ordenamiento == "min_a_max"):
                    aux_backup_valor = lista_heroes[indice]
                    lista_heroes[indice] = lista_heroes[indice +1]
                    lista_heroes[indice +1] = aux_backup_valor
                    flag_swap = True
                elif(lista_heroes[indice][clave] < lista_heroes[indice +1][clave] and 
                   ordenamiento == "max_a_min"):
                    aux_backup_valor = lista_heroes[indice]
                    lista_heroes[indice] = lista_heroes[indice +1]
                    lista_heroes[indice +1] = aux_backup_valor
                    flag_swap = True
            len_de_lista -= 1
        return lista_heroes           
    else:
        return "La lista esta vacia"    
    
    
    
    
lista_ordenada = ordenar_numeros_bubble_sort_v4(
    lista_heroes_prueba, clave= "peso", ordenamiento= "max_a_min")

print(lista_heroes_prueba)