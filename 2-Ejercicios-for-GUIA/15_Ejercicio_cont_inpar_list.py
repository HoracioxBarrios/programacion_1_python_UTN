'''
15- Dada una lista de números, imprimir la cantidad de números 
impares en la
lista.
'''
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
contador_inpar = 0
for numero in lista_de_numeros:
    if numero % 2 != 0:
        contador_inpar = contador_inpar + 1
print("la cant. de inpares es: {0}".format(contador_inpar))
