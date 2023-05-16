lista_heroes_prueba =\
[
  {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": 79.349999999999994,
    "peso": 18.449999999999999,
    "genero": "F",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  },
  {
    "nombre": "Rocket Raccoon",
    "identidad": "Rocket Raccoon",
    "empresa": "Marvel Comics",
    "altura": 122.77,
    "peso": 25.73,
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Brown",
    "fuerza": "5",
    "inteligencia": "average"
  },
  {
    "nombre": "Wolverine",
    "identidad": "Logan",
    "empresa": "Marvel Comics",
    "altura": 160.69999999999999,
    "peso": 135.21000000000001,
    "genero": "F",
    "color_ojos": "Blue",
    "color_pelo": "Black",
    "fuerza": "35",
    "inteligencia": "good"
  }]

clave_ingresada = "altura"

def ordenar_por_key(lista_heroes: list[dict], clave_buscada: str, menor_a_mayor=True) -> list[dict]:
    '''
    Ordena una lista de heroes segun clave y sentido de ordenamiento
    Recibe: (arg 1) la lista de heroes, (arg 2) la clave (ejemplo: 'altura'),
    (arg 3)el sentido de ordenamiento, por defecto (menor_a_mayor = True) 
    si se cambia a false cambia el sentido al de  mayor a menor.
    Devuelve la lista ordenada.
    '''
    len_de_lista = len(lista_heroes) - 1
    flag_swap = True
    while flag_swap:
        flag_swap = False
        for indice in range(len_de_lista):
            if(lista_heroes[indice][clave_buscada] > 
               lista_heroes[indice + 1][clave_buscada] and menor_a_mayor):
                aux_valor = lista_heroes[indice]
                lista_heroes[indice] = lista_heroes[indice + 1]
                lista_heroes[indice + 1] = aux_valor
                flag_swap = True
                
            if(lista_heroes[indice][clave_buscada] < 
               lista_heroes[indice + 1][clave_buscada] and not menor_a_mayor):
                aux_valor = lista_heroes[indice]
                lista_heroes[indice] = lista_heroes[indice + 1]
                lista_heroes[indice + 1] = aux_valor
                flag_swap = True
        len_de_lista -= 1
    return lista_heroes


print(ordenar_por_key(lista_heroes_prueba, clave_ingresada, menor_a_mayor=False))

    







def ordenar_por_altura(lista_heroes: list[dict]) -> list[dict]:
    '''
    Ordena de MENOR A MAYOR segun el peso del heroe
    Recibe una lista de diccionario heroes
    devuelve la lista ordenada
    '''
    len_de_lista = len(lista_heroes) - 1
    flag_swap = True
    while flag_swap:
        flag_swap = False
        for indice in range(len_de_lista):
            if lista_heroes[indice]["nombre"] > lista_heroes[indice + 1]["nombre"]:
                aux_backup_valor = lista_heroes[indice]
                lista_heroes[indice] = lista_heroes[indice + 1]
                lista_heroes[indice + 1] = aux_backup_valor
                flag_swap = True
        len_de_lista -= 1
    return lista_heroes
    
# print(ordenar_por_altura(lista_heroes_prueba))



# def ordenar_por_altura(lista_heroes: list[dict]) -> list[dict]:
#     '''
#     Ordena de MAYOR A MENOR segun el peso del heroe
#     Recibe una lista de diccionario heroes
#     devuelve la lista ordenada
#     '''
#     len_de_lista = len(lista_heroes) - 1
#     flag_swap = True
#     while flag_swap:
#         flag_swap = False
#         for indice in range(len_de_lista):
#             if lista_heroes[indice]["altura"] < lista_heroes[indice + 1]["altura"]:
#                 aux_backup_valor = lista_heroes[indice]
#                 lista_heroes[indice] = lista_heroes[indice + 1]
#                 lista_heroes[indice + 1] = aux_backup_valor
#                 flag_swap = True
#         len_de_lista -= 1
#     return lista_heroes
    
# print(ordenar_por_altura(lista_heroes_prueba))