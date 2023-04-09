'''metodo len():
La función len() devuelve la longitud de un objeto, es decir,
el número de elementos que contiene. El tipo de objeto puede 
ser una cadena de caracteres, una lista, una tupla, un diccionario, 
un conjunto, entre otros.
'''
palabra = "pepe"

resultado = len(palabra)
print(resultado)# muestra 4



'''el metodo range():
El método range() devuelve un objeto de tipo rango que representa 
una secuencia de números enteros. La secuencia comienza en 0 por 
defecto y se incrementa en 1 por cada elemento. El método range() 
acepta uno, dos o tres argumentos, que indican el inicio, el final y 
el paso de la secuencia. El objeto de rango se puede convertir en una 
lista o en una tupla utilizando las funciones list() o tuple()..
'''
# palabra = "pepe"

# resultado = range(palabra)
# print(resultado)
#directamente muestra error porque range acepta numeros. 
# desde el numero que le pasamos como argumento, te arma un iterable desde 
# 0 defualf hasta n que le hallamos pasado - 1 si querems incluirlo debemos 
#sumar +1

numeros = 15

for numero in range(15 +1): #for numero in range(1, 15 +1, 1):   = inicio, fin, incremento
    print(numero)



#indices
'''enumerate()
La función que devuelve los índices de una lista en Python 3 es la función 
enumerate(), comenzando desde 0 a n

'''