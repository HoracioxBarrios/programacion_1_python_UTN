'''9-Dada una lista de números,imprimir la cantidad de números 
negativos en la lista.'''

list_de_numeros = [0, 1, 2, 3, 4, 5, -2, -5]
contador_negativos = 0
for numero in list_de_numeros: # no uso range porque ya tengo la lista quees iterable 
    if numero < 0:
        contador_negativos += 1

if(contador_negativos > 0):
    print("cant. de numeros negativos es {0}".format(contador_negativos))
else:
    print("no hay negativos")