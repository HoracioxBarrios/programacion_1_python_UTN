'''
9- Crear una función que cuente la cantidad de veces que 
aparece un elemento en una lista. Recibe una lista y un 
elemento como parámetros y devuelve la cantidad de veces 
que aparece en la lista.
'''
lista_de_numeros = [1, 2, 3, 4, 4, 4, 5, 55, 60]
numero_a_comprobar = 5

def contar_repetidos(lista, elemento_a_comprobar):
    '''
    cuenta la cantidad de veces que aparece un elemento en una lista.
    recibe una lista y un elemento a comprobar
    retorna la cantidad de veces que se repite un elemento
    '''
    contador_repetidos = 0
    for elemento in lista:
        if(elemento == elemento_a_comprobar):
            contador_repetidos += 1
    return contador_repetidos



repetidos = contar_repetidos(lista_de_numeros, numero_a_comprobar)

print("El numero {0} se repite: {1}".format(numero_a_comprobar, repetidos))