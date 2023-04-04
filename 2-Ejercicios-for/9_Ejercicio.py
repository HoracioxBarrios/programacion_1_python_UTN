'''9-Dada una lista de números,imprimir la cantidad de números negativos en la
lista.'''

list_de_numeros = [0, 1, 2, 3, 4, 5, -2, -5]

for numero in list_de_numeros: # no uso range porque ya tengo la lista quees iterable 
    if numero < 0:
        print(numero)
        
        
        
        
#ver