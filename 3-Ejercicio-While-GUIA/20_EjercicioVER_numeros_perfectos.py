'''
20-Dado un número entero n, imprimir todos los números perfectos menores
  iguales a n. Los números perfectos son aquellos números enteros positivos 
que son iguales a la suma de sus divisores propios (excluyendo al propio número).
En otras palabras, si sumamos todos los divisores propios de un número (excluyendo 
el número en sí mismo) y el resultado es igual al número, entonces ese número 
se considera un número perfecto.

Por ejemplo, el primer número perfecto es 6, ya que sus divisores propios son 1,
2 y 3, y 1 + 2 + 3 = 6. Otros ejemplos de números perfectos son 28, 496 y 8128.
Actualmente se conocen más de 50 números perfectos, y se cree que existen 
infinitos números perfectos, aunque no se ha podido demostrar matemáticamente 
esta afirmación.

'''

n = int(input("Ingrese un número entero: "))

print("La secuencia de números perfectos menores o iguales a", n, "es:")
i = 1
while i <= n:
    j = 1
    suma_divisores_propios = 0
    while j < i:
        if i % j == 0:
            suma_divisores_propios += j
        j += 1
    if suma_divisores_propios == i:
        print(i)
    i += 1

'''imprimir todos los números perfectos menores iguales a n
Este código en Python 3 encuentra y muestra todos los números perfectos menores
o iguales a un número entero ingresado por el usuario.

Primero, el código solicita al usuario que ingrese un número entero y lo 
almacena en la variable n mediante la función int(input("Ingrese un número 
entero: ")).

A continuación, el código imprime un mensaje que indica que va a mostrar 
la secuencia de números perfectos menores o iguales a n.

Luego, el código inicializa una variable i en 1 y entra en un bucle while 
que se ejecutará mientras i sea menor o igual a n. En cada iteración del 
bucle while, el código evalúa si i es un número perfecto.

Para determinar si i es un número perfecto, el código inicializa una variable 
j en 1 y entra en otro bucle while que se ejecutará mientras j sea menor que i.
En cada iteración del bucle while interno, el código evalúa si j es un divisor 
propio de i. Si j es un divisor propio de i, entonces se agrega j a la variable 
suma_divisores_propios. Una vez que se hayan considerado todos los divisores 
propios de i, el código verifica si la suma de los divisores propios de i es 
igual a i. Si la suma de los divisores propios de i es igual a i, entonces i 
es un número perfecto y el código lo imprime utilizando la función print(i).

Finalmente, el código incrementa el valor de i en 1 y regresa al inicio del 
bucle while para evaluar el siguiente número. El bucle while continúa hasta 
que i es mayor que n, momento en el que el código termina.

'''