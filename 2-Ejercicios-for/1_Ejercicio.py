''' NUMERO MAS GRANDE
1-Dada una lista de números,imprimir el número más grande de la lista.
'''

lista_de_numeros = [10, 20, 30, 40, 50]
numero_mas_grande = lista_de_numeros[0] # en la primera iteracion tiene el valor del indice 0

for numero in lista_de_numeros:
    if(numero > numero_mas_grande):
        numero_mas_grande = numero

print("El numero mas grande de la lista es {0}".format(numero_mas_grande))


#ver

# no es correcto, no se estaria haciendo lo que vimos en maximos y minimos(aca inicializamos el numero max en 0)
# lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# numero_mayor = 0
# for numero in lista_de_numeros:
#     if (numero > numero_mayor): 
#         numero_mayor = numero

# print("El numero mas grande es: {0}".format(numero_mayor))    











'''charGPT
da un ejemplo con listas 
lista = [10, 5, 20, 15, 30]
mayor = lista[0] 

for num in lista:
if num > mayor:
mayor = num

print("El número más grande de la lista es:", mayor)

'''





# number_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter_list: list[int] = []
# cont: int = 0 
# for num in number_list:
#     if(number_list[cont] % 2 == 0):
#         filter_list.append(num)
#     cont += 1

# print(filter_list)
