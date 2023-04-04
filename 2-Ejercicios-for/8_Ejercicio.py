'''8- Dado un número entero n,imprimir la suma de los números pares menores o
iguales a n.
'''
acum_par = 0

numero_str = input("ingrese numero")
numero_int = int(numero_str)

for numero in range(numero_int +1):
    if numero % 2 == 0:
        acum_par = acum_par + numero

print("La xuma de los pares es: {0}".format(acum_par))



#ver