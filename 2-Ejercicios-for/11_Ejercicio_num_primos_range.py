'''
11_Dado un número entero n, imprimir la SECUENCIA de números primos menores
o iguales a n.'''

numero_ingresado_str = input("Ingrese un numero")
numero_ingresado_int = int(numero_ingresado_str)

for numero in range(numero_ingresado_int + 1):
    if ((numero % 2 != 0 and numero > 1) or numero == 2):
        print("Numero Primo: {0}".format(numero))
        

#Numeros primos Ok    
'''¿Cuáles son los números primos de 1 al 100?
Resultado de imagen para numeros primos
Así que ya tenemos la lista de números primos entre 1 y 100: 2, 3, 5,
7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
79, 83, 89 y 97'''