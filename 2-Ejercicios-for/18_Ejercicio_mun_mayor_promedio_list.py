'''
18-Dada una lista de números, imprimir la suma de los números en
la lista que son mayores que el promedio de la lista.
'''
lista_de_numeros = [10, 20, 30, 55, 57, 66, 100]

acum = 0
contador = 0
for numero in lista_de_numeros:
    acum = acum + numero
    contador += 1

promedio = acum / contador


print("el promedio es: {:.2f} Los num mayores al prom. son ".format(
    promedio)) #----------- 2 digitos -------------

# teniendo el promedio comparamos los que son mayores a el, recorriendo la lista nuevamente
for numero in lista_de_numeros:
    if(numero > promedio):
        print(numero)
