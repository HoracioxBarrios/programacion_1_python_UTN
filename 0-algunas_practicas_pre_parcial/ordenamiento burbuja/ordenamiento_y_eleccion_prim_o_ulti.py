
lista_personajes =\
[
  {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": 79.349999999999994,
    "peso": "18.449999999999999",
    "genero": "M",
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
    "peso": "25.73",
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
    "peso": "135.21000000000001",
    "genero": "M",
    "color_ojos": "Blue",
    "color_pelo": "Black",
    "fuerza": "35",
    "inteligencia": "good"
  },
  {
    "nombre": "Black Widow",
    "identidad": "Natasha Romanoff",
    "empresa": "Marvel Comics",
    "altura": 170.78999999999999,
    "peso": "59.340000000000003",
    "genero": "F",
    "color_ojos": "Green",
    "color_pelo": "Auburn",
    "fuerza": "15",
    "inteligencia": "good"
  }]


def ordenar_heroes_b_sort_clave(
    lista_heroes_original : list[dict], clave : str, ordenamiento = "asc")->list[dict]:
    '''
    Ordena una lista de heroes segun 'clave', y 'ordenamiento'.
    Recibe: (arg 1 )Una Lista de heroes, (arg 2) Una Clave ("altura",
    "fuerza", "peso"), (arg 3 ) Ordenamiento por defecto ascendente ("asc"),
    o se puede cambiar a Descendente ("desc").
    Devuelve la Lista ordenada, o en caso de estar vacia la lista, el mensaje:
    'Lista Vacia'
    '''
    if(lista_heroes_original):
        lista_heroes = lista_heroes_original[:]
        
        len_lista = len(lista_heroes) -1
        flag_swap = True
        while(flag_swap):
            flag_swap = False
            for indice in range(len_lista):
                if(lista_heroes[indice][clave] > lista_heroes[indice + 1][clave] 
                   and ordenamiento == "asc"):
                    lista_heroes[indice] , lista_heroes[indice +1] = \
                        lista_heroes[indice +1] , lista_heroes[indice]
                    flag_swap = True
                if(lista_heroes[indice][clave] < lista_heroes[indice + 1][clave] 
                   and ordenamiento == "desc"):
                    lista_heroes[indice] , lista_heroes[indice +1] = \
                        lista_heroes[indice +1] , lista_heroes[indice]
                    flag_swap = True
            len_lista -= 1
        return  lista_heroes            
    else:
        return "la lista está vacia"
    
lista_ordenada = ordenar_heroes_b_sort_clave(lista_personajes, clave="altura")
# print(lista_ordenada)



def listar_por_cantidad_si_primeros_o_ultimos(
    lista_heroes_ordenada : list[dict], cantidad = 0,posicion= "primeros")-> list[dict]:
    '''
    Se encarga de listar segun cantidad primeros o ultimos.
    Recibe: (arg 1)Una lista de heroes ya ordenada,(arg 2)La 
    cantidad a listar, (el 0 es todos) o elejir otro numero,
    (arg 3) posicion 'primeros' o 'ultimos'.
    '''
    if(lista_heroes_ordenada):
        if(cantidad > 0 and cantidad <= len(lista_heroes_ordenada) 
           and posicion =="primeros"):
            lista_primeros = lista_heroes_ordenada[ : cantidad]
            
            return lista_primeros
        elif(cantidad > 0 and cantidad <= len(lista_heroes_ordenada) 
             and posicion =="ultimos"):
            lista_ultimos = lista_heroes_ordenada[-cantidad:]
            
            return lista_ultimos
        elif(cantidad == 0):
            
            return lista_heroes_ordenada
        else:
            print("Cantidad supera la permitida")
            return -1
    else:
        print("Lista Vacia")
        return -1
    
            
cantidad_heroes_a_mostrar = listar_por_cantidad_si_primeros_o_ultimos(
    lista_ordenada, cantidad= 2, posicion="primeros")

print(cantidad_heroes_a_mostrar)
