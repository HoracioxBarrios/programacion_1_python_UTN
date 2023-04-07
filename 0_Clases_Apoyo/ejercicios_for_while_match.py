'''list en python es lo que en otro lenguaje un array (arr)'''
# lista_de_numeros = [0, 1, 2, 3]
# print(lista_de_numeros)

'''La función range() en Python 3 genera una secuencia de números 
enteros en un rango determinado.(devuelve un objeto iterable). 
La sintaxis básica de la función range() es la siguiente: 
range(start, stop, step)   inicio, fin, incremento( predeterminado = 1)'''

# lista_de_numeros = range(4)
# print(lista_de_numeros)

'''el equivalente a lo de arriba en python hay que tranformarlo a lista con list()
La función list() en Python se utiliza para crear una lista a partir de 
un objeto iterable.
'''

# lista_de_numeros = list(range(4))
# print(lista_de_numeros)


''' for con lista '''
# lista_de_numeros = [0, 1, 2, 3]
# for numeros in lista_de_numeros:
#     print(numeros)
    

# for numero in list(range(4)):
#     print(numero)

'''for comactado en python funcion - vldo por davila'''
# for numero in range(4):
#     print(numero)

'''se puede setear el inicio, hasta donde, y de cuanto en cuanto incrementar'''
# for numero in list(range(1 , 11,1)): # incrementa del 1 al 10 (contador += 1 entre comillas)
#     print(numero)

for numero in list(range(10,0,-1)): #decrementa del 10 al 1 (contador -= 1 entre comillas)
    print(numero)