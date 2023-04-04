'''
10-Dada una lista de números , imprimir la cantidad de números pares en la lista.

'''
i = 0
contador_par = 0
lista_de_numeros = [10, 1, 2, 3, 4, 5, 6, 9]


while(i < len(lista_de_numeros)):
    if lista_de_numeros[i] % 2 == 0:
        contador_par += 1 
    i = i + 1

print("cantidad de pares: {0}".format(contador_par))