'''Dado un número entero n, imprimir la secuencia de números perfectos
menores o iguales a n.'''

numero_ingresado_str = input("ingrese un numero")
numero_ingresado_int = int(numero_ingresado_str)

for numero_i in range(1, numero_ingresado_int + 1):
    suma_divisores = 0# se cuenta cuantos divisores tiene el numero 
    for numero_j in range(1, numero_i):
        if(numero_i % numero_j == 0):
            suma_divisores = suma_divisores + numero_j
    if suma_divisores == numero_i:
        print(numero_i)
        
        
        
# num = int(input("Ingrese un número: "))

# for i in range(1, num+1):
#     suma_divisores = 0
#     for j in range(1, i):
#         if i % j == 0:
#             suma_divisores += j
#     if suma_divisores == i:
#         print(i)

'''Explicación del código:
Pedimos al usuario que ingrese un número y lo guardamos en la variable num.
Luego, usamos un bucle for para iterar a través de los números del 1 al num 
(incluyendo num) usando range(1, num+1).
Para cada número i en el bucle for, inicializamos la variable suma_divisores
a cero.
Luego, usamos otro bucle for para iterar a través de los números del 1 al i 
(excluyendo i) usando range(1, i).
Dentro del segundo bucle for, verificamos si i es divisible por j 
(es decir, si i % j == 0). Si es así, sumamos j a suma_divisores.
Después de salir del segundo bucle for, verificamos si suma_divisores 
es igual a i. Si es así, entonces i es un número perfecto y lo imprimimos 
en la pantalla.'''