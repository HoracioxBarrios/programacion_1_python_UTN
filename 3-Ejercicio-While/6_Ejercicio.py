''' 
6- Dado un número entero n,  imprimir la suma de todos los números pares
menores o iguales a n.

'''

numero_ingresado_str = input("ingrese un numero")
numero_ingresado_int = int(numero_ingresado_str)

contador = 0
acum_suma_de_pares = 0

while(contador <= numero_ingresado_int ): # mietras contador sea menor o igual al ingresado
    if(contador % 2 == 0):
        acum_suma_de_pares = acum_suma_de_pares + contador
    contador += 1

print("La suma de todos los números pares menores o iguales a: {0} es {1}".format(numero_ingresado_int 
, acum_suma_de_pares))


















''' chat GPT4
en python 3 usando bucle while  Dado un número entero n, imprimir 
la suma de todos los números pares
menores o iguales a n.
¡Claro! Aquí tienes el código en Python 3 que cumple con lo que pides:

python Copy code
n = int(input("Ingresa un número entero: "))
suma = 0
i = 0

while i <= n:
    if i % 2 == 0:
        suma += i
    i += 1

print("La suma de todos los números pares menores o iguales a", n, "es:", s
'''