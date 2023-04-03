'''
3-Dado un número entero n, imprimir la secuencia de números pares menores o iguales a n.
'''

numero_ingresado_str = input("Ingrese un numero")
numero_ingresado_int = int(numero_ingresado_str)

for numero in range(numero_ingresado_int +1):
    if numero % 2 == 0:
        print(numero)



        

'''aumentando'''
# numero_ingresado_str = input("Ingrese un numero")#ingreso "10"
# numero_ingresado_int = int(numero_ingresado_str) # casteo str a int = 10

# for numero in range(0, numero_ingresado_int + 1, 1): #en range (comienza en 0, termina en 10 sin incluirlo, decrememeta de a 1)
#     if(numero % 2 == 0):# si es par que me lo muestre
#         print(numero)


'''decrementando'''
# numero_ingresado_str = input("Ingrese un numero")#ingreso "10"
# numero_ingresado_int = int(numero_ingresado_str) # casteo str a int = 10

# for numero in range(numero_ingresado_int, 0, -1): #en range (comienza en 10, termina en 0 sin incluirlo, decrememeta de a 1)
#     if(numero % 2 == 0):# si es par que me lo muestre
#         print(numero)



