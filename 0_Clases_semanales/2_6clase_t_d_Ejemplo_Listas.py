'''EJEMPLOS DE LISTAS'''
# #Las listas tienen indices que empiezan en 0

listas_de_valores = [1, 33, 12, -12]
print(listas_de_valores)
listas_de_valores[1] = 22 # ------re-asignar valor a la posicion 1
print(listas_de_valores)
# listas_de_valores.append(99) #---Agregar un nuevo elemento a la lista
print(listas_de_valores)

''' hay dos formas de recorrer una lista en python'''

'''1- POR VALOR'''
#---- recorrer la Lista por elementos
for valor in listas_de_valores:
    print(valor)

'''2- POR INDICE'''

#---- recorrer la lista generando un indice. -----usando range()que devuelve un iterable desde 0 por default hasta el numero quele pasemos. 
cantidad_de_elmentos = len(listas_de_valores)     # len() devuelve la cantidad de elementos de la lista, se se lo podemos pasar a range()
for indice in range(cantidad_de_elmentos):
    print(listas_de_valores[indice])

#--- recorrer generando indice - simplificado # MEJOR
for indice in range(len(listas_de_valores)):
    print(listas_de_valores[indice])

''''''

















listas_de_valores = [1, 33, 12, -12]
listas_de_valores.append(99) #---Agregar un nuevo elemento a la lista  #99

'''Lo que devuelve len()'''
cantidad_de_elmentos = len(listas_de_valores)
print(cantidad_de_elmentos) # 5

'''lo que devuelve range'''
indices = range(len(listas_de_valores))
print(indices) #range(0,5)

resultado_range = range(10)
print(resultado_range) #range(0, 10)

''' emulando un indice'''
indice_simulado = 2
print(listas_de_valores[indice_simulado]) # 12
