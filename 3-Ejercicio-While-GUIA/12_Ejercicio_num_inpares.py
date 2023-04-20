'''
12-Dado un número entero n, imprimir la suma de todos los 
números impares menores o iguales a n.
'''

numero_str = input("Ingrese numero")
numero_int = int(numero_str)

acum_de_inpares = 0
contador = 0

while(contador <= numero_int):
    if(contador % 2 != 0):
        acum_de_inpares = acum_de_inpares + contador
    contador += 1

print("La suma de los impares es: {0}".format(acum_de_inpares))