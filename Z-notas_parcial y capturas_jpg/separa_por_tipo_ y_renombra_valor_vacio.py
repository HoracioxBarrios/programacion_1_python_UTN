def contar_por_tipo(lista: list, clave_tipo: str) -> dict:
    '''
    separa por tipo y los contabiliza
    recibe una list de dict
    retorna - una lista de dict con los tipos y cantidades correspondientes
    '''
    nuevo_dicc_contador = {}
    for diccionario in lista:
        nueva_clave = diccionario.get(clave_tipo)#
        if nueva_clave is not None:# evalua si es none, reasigna
            nueva_clave = nueva_clave
        else:
            nueva_clave = "Notiene"
        if nueva_clave == '': # evalua si es "", reasigna "no tiene"
            nueva_clave = 'Notiene'

        if nueva_clave in nuevo_dicc_contador: # verifica si existe en nuevo dicc
            nuevo_dicc_contador[nueva_clave] += 1
        else:
            nuevo_dicc_contador[nueva_clave] = 1
    return nuevo_dicc_contador


''' utiliza el método .get() del diccionario para obtener el valor asociado 
a la clave "clave_tipo". Si la clave no existe en el diccionario, 
se devuelve None (nulo). Esto significa que no se generará una excepción 
si la clave no existe en el diccionario'''
#nueva_clave = diccionario.get(clave_tipo)


'''
La segunda línea de código, "nueva_clave = diccionario[clave_tipo]", utiliza 
el operador de indexación ([]) del diccionario para obtener el valor 
asociado a la clave "clave_tipo". Si la clave no existe en el diccionario, 
se generará una excepción KeyError.

'''
#nueva_clave = diccionario[clave_tipo]

