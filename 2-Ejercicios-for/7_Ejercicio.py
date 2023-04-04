'''7-7. Dado un número entero n, imprimir la secuencia de números impares
menores o iguales a n.'''

numero_str = input("INgrese numero")# ingreso de dato str
numero_int = int(numero_str)# cast a int

for numero in range(numero_int +1):# range crea un itrerable con la longitud de 7 espacios
    if numero % 2 != 0:
        print(numero)