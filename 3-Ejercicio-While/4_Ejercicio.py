'''
4-Dada una lista de números,  imprimir la suma de todos los elementos de la lista.

'''

lista_de_numeros = [1, 2, 3, 4, 5,]
contador = 0
acumulador_suma = 0

while(contador < len(lista_de_numeros)):
    acumulador_suma = acumulador_suma +lista_de_numeros[contador]
    contador += 1

print(acumulador_suma)






# #lista_de_numeros:list[int] = [1, 2, 3, 4, 5]

# lista_de_numeros:list[int] = [1, 2, 3, 4, 5]

# acumulador_suma = 0
# i = 0

# while(i < len(lista_de_numeros)):# mientras el valor de i seaa menor que la longitud de la lista
#     acumulador_suma = acumulador_suma + lista_de_numeros[i]
#     i += 1

# print(acumulador_suma)

# #ver






'''
chatGPT4:
¡Claro que sí! Aquí te dejo un ejemplo de cómo puedes hacerlo en Python 3
utilizando solamente un bucle while:

python
Copy code


lista = [1, 2, 3, 4, 5]
suma = 0
i = 0

while i < len(lista):
    suma += lista[i]
    i += 1

print("La suma de todos los elementos de la lista es:", suma)
'''
