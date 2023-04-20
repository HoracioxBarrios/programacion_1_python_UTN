'''
13- Crea una lista de números y encuentra el promedio de 
todos los números en la lista.

'''

lista_numeros = [1, 5, 10, 11, 20]
acum_suma = 0
contador = 0

for numero in lista_numeros:
    acum_suma += numero
    contador += 1

promedio = acum_suma / contador
print("El promedio de los numeros es: {0}".format(promedio))