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