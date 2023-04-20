'''12-Dada una lista de números, imprimir la cantidad de 
números pares en la lista.'''

lista_de_numeros = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for numero in lista_de_numeros:
    if(numero % 2 == 0):# es par
        print(numero)