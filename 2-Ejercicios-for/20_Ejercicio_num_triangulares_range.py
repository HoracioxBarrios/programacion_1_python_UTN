'''
20- Dado un número entero n, imprimir la secuencia de números triangulares
menores o iguales a n.
'''
#Los primeros números triangulares son:  1 , 3 , 6 , 10 , 15 , 21, 28 , 36 , 45 , 55 , …




numero_str = input("Ingrese un número entero: ")
numero_int = int(numero_str)

acum_triangular = 1

for numero in range(1, numero_int + 1):
    if (acum_triangular > numero_int):
        break
    print(acum_triangular)
    numero = numero + 1
    acum_triangular = numero * (numero + 1) // 2







#CHAT GPT

# n = int(input("Ingrese un número entero: "))

# triangular = 1

# for i in range(1, n+1):
#     if triangular > n:
#         break
#     print(triangular)
#     i += 1
#     triangular = i*(i+1)//2

'''
Primero, se le pide al usuario que ingrese un número entero n
utilizando la función input().
Luego, se convierte el valor ingresado a un entero utilizando 
la función int() y se almacena en la variable n.

Después, se inicializa la variable triangularen 1, que representa
el primer número triangular.

Luego, se utiliza un bucle 
forpara generar y imprimir los números triangulares menores 
o iguales a n. El bucle se ejecuta para cada valor de ien el 
rango de 1 a n+1
.

Dentro del bucle, se utiliza una declaración if para verificar 
si el número triangular actual (triangular) es mayor que n. 
Si es así, se utiliza la SENTENCIA breakpara salir del bucle.

Si el número triangular actual es menor o igual a n
, se imprime el número triangular actual utilizando la función 
print().Luego, se actualiza la variable i sumándole 1 
y se utiliza la fórmula triangular = i*(i+1)//2 para 
generar el siguiente número triangular.

Finalmente, cuando el número triangular actual es mayor que 
n
, el bucle se detiene y el programa termina.

Espero que esto te haya ayudado a entender cómo imprimir la 
secuencia de números triangulares menores o iguales a n 
utilizando un bucle for
.





'''
