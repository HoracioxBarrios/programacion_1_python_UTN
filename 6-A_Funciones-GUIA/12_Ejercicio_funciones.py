'''
12- Crea una función que reciba dos listas de nombres, y 
devuelva una lista con los nombres que aparecen en ambas listas
'''
lista_nombres_uno = ["Lilia", "Rodolfo", "Kloe", "Eric", "Ambar", "Lilita"]
lista_nombres_dos = ["Rodolfo", "Bender", "Wally", "Kiko", "Lilia", "Ambar"]

def buscar_nombres_repetidos(lista_a, lista_b):
    '''
    Genera una lista nueva a partir de los elementos repetidos de dos listas
    Recibe dos listas
    devuelve una lista nueva
    '''
    lista_repetidos = []
    for nombre_a in lista_a:
        for nombre_b in lista_b:
            if (nombre_a == nombre_b):
                lista_repetidos.append(nombre_a)
    return lista_repetidos



repetidos = buscar_nombres_repetidos(lista_nombres_uno, lista_nombres_dos)

print(repetidos)
