'''
13-Dada una lista de números, imprimir la cantidad de números negativos en la
lista
'''
lista_de_numeros = [1, 2, -2, -5, 5, -10]
indice = 0
contador_de_negativos = 0

while(indice < len(lista_de_numeros)):
    if(lista_de_numeros[indice] < 0 ):
        contador_de_negativos += 1
    indice += 1


print("La cantidad de negaticos es: {0}".format(
    contador_de_negativos))

