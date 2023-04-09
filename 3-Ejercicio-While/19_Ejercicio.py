'''
19- Dada una lista de números, imprimir todos los números que 
son mayores que el número anterior en la lista
'''
lista = [1, 3, 2, 5, 4, 7, 6, 9, 8]
#print(lista[-1]) #imprime el ultimo elemento
indice = 1
while indice < len(lista):# mientras contador sea menor al largo de la lista itera
    if lista[indice] > lista[indice-1]: # si el elemento en la posicion en ese momento "indice" es mayor El ULTMO ELEMENTO
        print(lista[indice])# imprime los anteriores al ultimo de la lista
    indice += 1