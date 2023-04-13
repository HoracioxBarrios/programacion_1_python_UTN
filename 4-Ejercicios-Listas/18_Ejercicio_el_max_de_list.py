'''
18_Solicitar al usuario números enteros hasta que ingrese el 0. 
Almacenar los números en una lista y luego imprimir el mayor 
(sin utilizar la funciónmax() )

'''
lista_de_numeros = []
flag_max = True

while(True):
    numero_str = input("Ingrese numero")
    numero_int = int(numero_str)
    if(numero_int == 0):
        break
    lista_de_numeros.append(numero_int)

for numero in lista_de_numeros:
    if(flag_max):
        numero_max = numero
        flag_max = False
    else:
        if(numero > numero_max):
            numero_max =numero

print("El numero max es:{0}".format(numero_max))