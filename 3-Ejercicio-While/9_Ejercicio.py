'''9-Dado un número entero n,  imprimir todos los números impares menores o
iguales a n.'''



numero_str = input("Ingrese un numero")
numero_int = int(numero_str)
contador = 0
while(contador <= numero_int):
    if contador % 2 != 0:
        print(contador)
    contador += 1
    
    
    

# n = int(input("Ingrese un número entero: "))
# i = 1
# while i <= n:
#     if i % 2 != 0:
#         print(i)
#     i += 1