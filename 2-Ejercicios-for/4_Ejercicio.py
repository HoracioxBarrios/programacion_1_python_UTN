'''
4-Dado un número entero n,imprimir la suma de los números impares menores
o iguales a n.'''

acum_suma_inpares = 0
numero_str = input("Ingrese un numero: ")
numero_int = int(numero_str)

for numero in range(numero_int + 1):# +1 incluye el numero ingresado
    if(numero % 2 != 0):
        acum_suma_inpares = acum_suma_inpares + numero

print(acum_suma_inpares)