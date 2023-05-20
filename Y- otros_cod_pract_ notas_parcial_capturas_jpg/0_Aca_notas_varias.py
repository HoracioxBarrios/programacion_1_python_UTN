'''metodo len():
La función len() devuelve la longitud de un objeto, es decir,
el número de elementos que contiene. El tipo de objeto puede 
ser una cadena de caracteres, una lista, una tupla, un diccionario, 
un conjunto, entre otros.
'''
# palabra = "pepe"

# resultado = len(palabra)
# print(resultado)# muestra 4



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

# numeros = 15

# for numero in range(15 +1): #for numero in range(1, 15 +1, 1):   = inicio, fin, incremento
#     print(numero)



#indices
'''enumerate()
La función que devuelve los índices de una lista en Python 3 es la función 
enumerate(), comenzando desde 0 a n

'''



############ LISTAS

# lista_de_nombres = ["pepe", "eddi", "kiki", "rulo"]

# for nombre in lista_de_nombres:
#     print(nombre) # imprime pepe eddi kiki rulo
    
# lista_de_nombres_dos = ["adri", "kami", "luli", "tati"]

# for nombre in range(10):
#     print(nombre) #imprime 0 1 2 3 4 5 6 7 8 9  me da un numero que va de 
                    # 0 hasta el que le pase -1 (son 10, que se puede usar como indice)
                    # asi esta definido a mano 10 elementos

# for indice in len(nombre):
#     print(nombre) #da error porque no es iterable len()

# for indice in range(len(lista_de_nombres_dos)):# range() arma un numero iterable dependiendo del largo de la lista con len()
#     print(indice)# imprime el indice
#     print(lista_de_nombres_dos[indice]) #imprime el elemento en ese indice


''' no funco, hay que reverrlo'''

# lista_edad = [18, 20, 30, 41, 25]

# for edad in lista_edad:
#             print("valor edad_indice {0}".format(edad))
#             edad_max = edad
#             edad_min = edad
#             print(edad_max)
#             print(edad_min)
#             if (edad > edad_max):
#                 edad_max = edad
#             if (edad < edad_min):
#                 edad_min = edad

# print("la edad minima es: {0} y la edad maxima es: {1}".format(
#             edad_min, edad_max))



lista_nombres = ["Lili", "Erica", "Federico", "Ricardo", "Pricila"]

lista_edad = [18, 20, 30, 41, 25]

#una solucion simple 
        # flag_edad = True
        # for edad in lista_edad:
        #     if(flag_edad): #Maximos y minimos
        #         edad_min = edad
        #         edad_max = edad
        #         flag_edad = False
        #     else:
        #         if(edad < edad_min):
        #             edad_min = edad
        #         if(edad > edad_max):
        #             edad_max = edad
        # print("la edad minima es: {0} y la edad maxima es: {1}".format(
        #     edad_min, edad_max))
