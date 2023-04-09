''' NUMERO MAS CHICO
5-Dada una lista de números,imprimir el número más pequeño de la lista.
'''

lista_de_numeros = [5, 10, 20, 30, 40, 50]
numero_mas_chico = lista_de_numeros[0] # en la primera iteracion tiene el valor del indice 0

for numero in lista_de_numeros:
    if(numero < numero_mas_chico):
        numero_mas_chico = numero

print(numero_mas_chico)


#ver



'''hay una funcion que busca el mas chico de la lista'''
# lista_de_numeros = [5, 10, 20, 30, 40, 50]
# numero_mas_chico = min(lista_de_numeros)
# print("El numero mas chico es: {0}".format(numero_mas_chico))


#no es correcto,hacerlo asi.  no se estaria haciendo lo que vimos en maximos y minimos(aca inicializamos el numero max en 0)
# lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# numero_min = 0
# for numero in lista_de_numeros:
#     if (numero < numero_min): 
#         numero_min = numero

# print("El numero mas chico es: {0}".format(numero_min)) 
#estaria imprimiendo siempre el 0 que no pertenece a la lista
# por eso existe la forma de los maximos y minomos que no inicializan un numero para comparar antes,
#sino que se carga el primer valor de la lista y se usa ese para comparar