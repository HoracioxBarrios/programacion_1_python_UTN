'''
2-
Dado un número entero n, imprimir todos los números desde 1 hasta n en orden ascendente.

'''

contador = 1

numero_ingresado_str = input("Ingrese un numero: ")
numero_ingresado_int = int(numero_ingresado_str)

while(contador <= numero_ingresado_int):
    print(contador)
    contador = contador + 1   #contador += 1