lista_personajes =\
[
  {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
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
    "altura": "122.77",
    "peso": "25.73",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Brown",
    "fuerza": "35",
    "inteligencia": "average"
  },
  {
    "nombre": "Wolverine",
    "identidad": "Logan",
    "empresa": "Marvel Comics",
    "altura": "160.69999999999999",
    "peso": "135.21000000000001",
    "genero": "F",
    "color_ojos": "Blue",
    "color_pelo": "Black",
    "fuerza": 35,
    "inteligencia": "good"
  }]

def stark_normalizar_datos(heroes: list[dict]) -> list[dict]:
    '''
    normaliza los datos
    recibe una list[dict] personajes
    devuelve una nueva lista de dicc con datos normalizados    
    '''
    result_nueva_lista = []
    if heroes:
        for heroe in heroes:
            keys = list(heroe.keys())
            for key in keys:
                if type(heroe[key]) is str:
                    valor_reemplazado: str = heroe[key].replace('.', '')
                    if valor_reemplazado.isnumeric() and type(heroe[key]) is str:
                        if '.' in heroe[key] and heroe[key].count('.') == 1:
                            heroe[key] = float(heroe[key])
                        else:
                            heroe[key] = int(heroe[key])
                        print(
                            "El dato {0}fue modificado en el heroe {1}".format(key, heroe["nombre"]))
            result_nueva_lista.append(heroe)
        return result_nueva_lista
    else:
        return "La lista esta Vacia"
    
    

# print(stark_normalizar_datos(lista_personajes))


clave_buscada = "altura"

def sumar_dato_heroe(lista_heroes : list[dict], clave_buscada : str):
    if(lista_heroes):
        lista_heroes_normalizada = stark_normalizar_datos(lista_heroes)
        acumulador_de_dato = 0
        for dicc_heroe in lista_heroes_normalizada:
            if dicc_heroe == {} and type(dicc_heroe) is dict:
                acumulador_de_dato += dicc_heroe[clave_buscada]
        return "la suma de todas las {0} es: {1}".format(
            clave_buscada, acumulador_de_dato)
                
    else:
        return "La lista esta vacia"

print(sumar_dato_heroe(lista_personajes, clave_buscada))