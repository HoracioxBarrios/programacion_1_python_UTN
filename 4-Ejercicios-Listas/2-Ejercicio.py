'''
2- Crea una lista con 5 números enteros. Luego solicita un 
nuevo número y reemplaza el tercer elemento de la lista por 
el número ingresado. Finalmente imprime todos los números

'''

lista_de_numeros = [1, 2, 3, 4, 5]
nuevo_numero_str = input("Ingrese un numero")
nuevo_numero_int = int(nuevo_numero_str)

lista_de_numeros[2] = nuevo_numero_int

for numero in lista_de_numeros:
    print(numero)
