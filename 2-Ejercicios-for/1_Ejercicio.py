'''
1-Dada una lista de números, imprimir el número más grande de la lista.
'''

number_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter_list: list[int] = []
cont: int = 0 
for num in number_list:
    if(number_list[cont] % 2 == 0):
        filter_list.append(num)
    cont += 1

print(filter_list)
