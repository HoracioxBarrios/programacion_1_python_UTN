



def stark_normalizar_datos(lista_heroes: list[dict]) -> list[dict] | str:
    '''
    Verifica y normaliza los valores si son numericos.
    Recibe: una list[dict] personajes
    Devuelve: una nueva lista de heroes con datos normalizados    
    '''
    nueva_lista_normalizada = []
    if(lista_heroes):
        for heroe in lista_heroes:
            keys = list(heroe.keys())
            for key in keys:
                if(type(heroe[key]) is str):
                    valor_reemplazado : str = heroe[key].replace('.', '')
                    if(valor_reemplazado.isnumeric() and type(heroe[key]) is str):
                        if('.' in heroe[key] and heroe[key].count('.') == 1):
                            heroe[key] = float(heroe[key])
                        else:
                            heroe[key] = int(heroe[key])
                        print("El dato {0}fue modificado en el heroe {1}".format(
                            key, heroe["nombre"]))
            nueva_lista_normalizada.append(heroe)
        return nueva_lista_normalizada
    else:
        return "La lista esta Vacia"