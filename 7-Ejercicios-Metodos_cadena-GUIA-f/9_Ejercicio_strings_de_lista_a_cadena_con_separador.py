'''
9. Escribir una función que tome una lista de nombres y los una en una sola
cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"]
-> "Juan\nMaría\nPedro"
'''

lista_de_nombres = ["Juan", "María", "Pedro"]
separador = "\n"

def de_lista_a_cadena_con_separador(lista : list, separador : str)-> str:
    '''
    crea una cadena desde una lista de nombres con un separador entre ellos
    recibe una lista de nombres, y un separador ("ejemplo "\n" , "-" , " ")
    devuelve una cadena
    '''
    cadena = separador.join(lista)
    return cadena

print(de_lista_a_cadena_con_separador(lista_de_nombres, separador))