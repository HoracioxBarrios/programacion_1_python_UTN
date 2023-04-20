'''
15- Crea una lista de números enteros y luego encuentra la 
suma de los números en índices impares.
'''
lista_de_numeros = [1, 2, 3, 4]

acum_de_elementos_indices_inpares = 0

# como len() no da un iterable, lo debemos comvertir con range()
for indice in range( len(lista_de_numeros)):
    #print(indice)
    if(indice % 2 != 0): # si el indice es inpar se acumulan - EL INDICE 0 NO CUENTA INPAR -segun Ai cuenta como par ya que es divisible por 2 sin dejar residuo. por lo tanto el indice 0 no se suma.
        acum_de_elementos_indices_inpares += lista_de_numeros[indice]


print("la suma los números en índices impare es: {0}".format(
    acum_de_elementos_indices_inpares))



'''
La función len() en Python 3 devuelve la longitud de un objeto iterable, 
es decir, el número de elementos que contiene.
'''
'''
la función range() en Python genera una secuencia de números enteros 
que se pueden utilizar como índices para acceder a los elementos de una 
lista u otro objeto iterable.
'''