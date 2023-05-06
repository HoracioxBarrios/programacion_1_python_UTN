'''
Ejercicios Listas
1-
Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
listas primero, y despues usando listas y comparar la composición del código.

2-
La real academia española nos pide desarrollar un pequeño programa que contenta el
diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
algoritmo que nos permita el ingreso de una palabra en español y su traducción al
ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
inglés. Recordar validar los datos de forma correcta.

3-
Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición
de memoria es la que mas ocurrencias tiene dentro de esa lista.

4-
Debemos desarrollar un algoritmo que permita computar los votos del Senado de
Berlinberlín. Se deberá ingresar el nombre de cada senador y si está Presente o no en
la sesión. Si el senador está presente, se deberá pedir el valor del voto El voto de los
senadores berliberlineses puede ser Afirmativo, Negativo o Abstención (validar). El
valor por defecto para los senadores ausentes será Abstención. Se deberá Informar:
o Cantidad total de senadores.
o Cantidad de senadores presentes.
o Cantidad y porcentaje de votos afirmativos.
o Cantidad y porcentaje de votos negativos.
o Cantidad y porcentaje de abstenciones.
o Generar una lista de senadores por cada tipo de voto y mostrarlas por
pantalla.

5-
Para una veterinaria se pide clasificar el ingreso de pacientes hasta que el usuario
quiera (se limita a 1 perrito por ingreso), se les pide:
nombre, precio de la consulta (validar entre 500$ y 2500$) raza: (validar entre caniche,
ovejero, siberiano), edad (validar 1 a 15) y peso (entre 25 y 40 kilos) determinar:
1. Generar un listado con todos los datos de los pacientes ordenados por edad.
2. Generar un listado de los perros que pesen más de 30 kilos y ordenarla por
nombre.
3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de
impuesto por ingresos brutos e informarlo.
4. Informar el nombre y el peso del perro con más peso.


6-
Se nos pide realizar un programa que le pida al usuario una N cantidad de veces y
calcular la máxima diferencia en la secuencia de números ingresada.
7-
Un grupo de cinco amigos se juntan para jugar una partida de CS:GO, deciden que
van a jugar 10 partidas y necesitan realizar datos estadísticos sobre las partidas
jugadas. Para eso necesitan ingresar los siguientes datos en el siguiente orden
especifico: nombre, edad, bajas confirmadas (el murió), muertes confirmadas (el mate
a otro jugador). Con esos datos se necesita saber:
• Nombre del jugador más joven.
• Jugador que más bajas tuvo.
• Jugador con menos muertes
• El promedio de bajas del equipo
• La cantidad de jugadores que tienen entre 20 y 30 años cuyas bajas estan
entre 10 y 20
• El nombre y edad del jugador que más muertes tuvo (MVP)
Nota: los datos tienen que ingresar en 1 solo string separado por espacios, y ser
almacenados en una lista, investigar que función les permite lograrlo y como hacer una
lista de listas.

8-
Escribir un programa que le pida al usuario ingresar una lista de nombres de personas
(previamente validada) y luego le pidan 1 solo nombre en específico. Se debe buscar
el nombre especifico en la lista de nombres y si esta presente el programa deberá
imprimir la posición del nombre en la lista, la posición de memoria donde se encuentra
ese nombre y la cantidad de caracteres que tiene el nombre, si no se encuentra, se
deberá informar por pantalla.

9-
Realizar un programa que pida una cadena de texto al usuario y le pida una cadena de
texto y determine que la cadena ingresada es un palíndromo o no. De serlo deberá
imprimir la palabra por consola.
10-
Se necesita un programa que solicite al usuario que ingrese una lista de números
enteros de tamaño N. El programa deberá remover el valor máximo y mínimo de la
lista y luego calcular y mostrar el promedio de los valores restantes y determinar si el
promedio es mayor o menor que la diferencia entre el máximo y el mínimo valor
previamente removido.
'''
''''''
#-------------------------------------------------
'''
1- Una concesionaria de autos nos pide desarrollar un sistema para controlar
el stock de autos que tienen disponible a la venta. Para esto se necesita
saber de cada auto: la marca, el año del modelo y el precio (validar los 
tipos de datos ingresados) y mostrarlos por pantalla en forma secuencial y 
ordenada. Realizar el ejercicio sin usar listas primero, y despues usando 
listas y comparar la composición del código.'''


option = True
while(option):
    marca = input("ingrese la marca del auto ")
    while(marca.isnumeric()):
        marca = input("Incorrecto!ingrese la marca del auto ")
        
    print(marca)
    
    precio_str = input("ingrese el año modelo del auto ")# erroral usar una variable con Ñ
    precio_int = int(precio_str)
    while(precio_int < 1886 or precio_int > 2023):
            precio_str = input("Incorrecto! ingrese el año modelo del auto ")
            precio_int = int(precio_str)
    print(precio_int)
    
    precio_str = input("ingrese el año modelo del auto ")# erroral usar una variable con Ñ
    precio_int = int(precio_str)
    while(precio_int < 0 ):
            precio_str = input("Incorrecto! ingrese el año modelo del auto ")
            precio_int = int(precio_str)
    print(precio_int)
    
    option = input("Desea ingresar otro? ")