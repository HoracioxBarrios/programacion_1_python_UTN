'''
1-Dado un número entero n, imprimir todos los números desde n hasta 1 en
orden descendente.
'''
''' nota: desde el numero que ingresa el usuario hasta 1'''

numero_ingresado_str = input("INgrese un numero")  #"10"
#validar
numero_ingresado_int = int(numero_ingresado_str) # cast a int  10
contador = numero_ingresado_int #contador pasa a valer 10 en esta linea

#              10     >=      1
while(contador >= 1):
    print(contador)
    contador = contador - 1  
    #contador pasa a valer 9 y se evalua nuevamente la condicion
    












# numero_ingresado_str = input("INgrese un numero")
# numero_ingresado_int = int(numero_ingresado_str)

# contador = numero_ingresado_int  # ver si esta ok

# while(contador >= 1):
#     print(contador)
#     contador -= 1










'''
Ej: chat gtp4
n = int(input("Ingrese un número entero: "))

i = n
while i >= 1:
    print(i)
    i -= 1
'''