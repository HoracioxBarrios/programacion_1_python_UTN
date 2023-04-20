'''
16- Dada una lista de números, imprimir todos los números que 
son múltiplos de 3.
'''

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
contador = 0

while(contador <= len(lista_de_numeros)):
    if (contador % 3 == 0 and contador > 0):# multiplo de 3 y mayor a 0
        print(contador)
    contador += 1 