'''
18.Crea un diccionario que represente los juegos de una consola, donde las
claves son los nombres de los juegos y los valores son las puntuaciones
correspondientes. 
Solicita al usuario el nombre de un juego y luego su
puntuación, si el juego no existe agregarlo y si existe actualizar su 
puntuación

'''


dicc_juegos = {
    "Street Fighter" : 15000,
    "Super Mario 2" : 20000,
    "Metro 2033" : 18000,
    "League Of Legends" : 30000}

# Mostrar los juegos disponibles
print("Juegos disponibles:")
for juego in dicc_juegos:
    print("- {0}".format(juego))
    
nombre_juego = input("Ingrese un nombre de un Juego ").capitalize()
puntuacion_str = input("Ingrese puntuacion ")
puntuacion_int = int(puntuacion_str)


flag_actualizo = False
flag_agrego = False

#si uso esto dentro del for no anda, ya que a se encontraria recorriendo las claves y por ende da error, hay que usar un metodo. ver abajo otro ejemplo
if(nombre_juego not in dicc_juegos): # si no está en el diccionario
    dicc_juegos[nombre_juego] = puntuacion_int
    flag_agrego = True
else:
    dicc_juegos[nombre_juego] = puntuacion_int
    flag_actualizo = True

      
if(flag_agrego):
    print("No existia y se agregó", dicc_juegos)
if(flag_actualizo):
    print("existe y se actualizó", dicc_juegos)



'''
entonces no es posible verificar si esta en el diccionario 
y si no esta agregarlo? dentro de un bucle for? 

ChatGPT
Sí es posible verificar si un elemento no está en el diccionario y 
agregarlo dentro de un bucle for, pero en el código original que 
proporcionaste, el bucle for estaba iterando sobre las claves del 
diccionario dicc_juegos, por lo que la verificación 
if(juego not in dicc_juegos) nunca se cumpliría, ya que el bucle ya 
está recorriendo las claves existentes en el diccionario.

Si deseas agregar un elemento que no está en el diccionario, podrías 
usar el método setdefault() del diccionario, que te permitirá agregar 
el elemento si no existe y actualizarlo si ya existe, de manera más 
eficiente que usando una estructura if dentro del bucle for. Aquí te 
dejo un ejemplo de cómo podrías modificar el código para usar el método 

setdefault():

python
Copy code

dicc_juegos = {
    "Street Fighter" : 15000,
    "Super Mario 2" : 20000,
    "Metro 2033" : 18000,
    "League Of Legends" : 30000}

# Mostrar los juegos disponibles
print("Juegos disponibles:")
for juego in dicc_juegos:
    print("- {0}".format(juego))
    
nombre_juego = input("Ingrese un nombre de un Juego ").capitalize()
puntuacion_str = input("Ingrese puntuacion ")
puntuacion_int = int(puntuacion_str)

puntuacion_anterior = dicc_juegos.setdefault(nombre_juego, puntuacion_int) 

if puntuacion_anterior == puntuacion_int:
    print("No existía y se agregó", dicc_juegos)
else:
    print("Ya existía y se actualizó", dicc_juegos)
    
    
En este ejemplo, el método setdefault() se usa para agregar el 
elemento si no existe o actualizarlo si ya existe. El método 
devuelve el valor anterior asociado a la clave o el valor nuevo si se 
ha agregado una nueva clave. Luego, se verifica si el valor anterior es 
igual al valor nuevo, lo que indica si se agregó un nuevo elemento o se 
actualizó un elemento existente.





Regenerate response
Send a message.

Free Research Preview. ChatGPT may produce inaccurate information ab
'''






'''Nota: El código tiene un error en el bucle for de verificación de juegos.
La condición if(juego not in dicc_juegos) nunca se cumpliría, ya que el 
bucle for ya está recorriendo los elementos de dicc_juegos'''

# dicc_juegos = {
#     "Street Fighter" : 15000,
#     "Super Mario 2" : 20000,
#     "Metro 2033" : 18000,
#     "League Of Legends" : 30000}

# # Mostrar las películas disponibles
# print("Juegos disponibles:")
# for juego in dicc_juegos:
#     print("- {0}".format(juego))
    
# nombre_juego = input("Ingrese un nombre de un Juego ").capitalize()
# puntuacion_str = input("Ingrese puntuacion ")
# puntuacion_int = int(puntuacion_str)


# flag_actualizo = False
# flag_agrego = False

# for juego in dicc_juegos:
#     if(juego not in dicc_juegos): # si no está en el diccionario
#         dicc_juegos[nombre_juego] = puntuacion_int
#         flag_agrego = True
#     else:
#         dicc_juegos[nombre_juego] = puntuacion_int
#         flag_actualizo = True
        
        
# if(flag_agrego):
#     print("No existia y se agregó", dicc_juegos)
# if(flag_actualizo):
#     print("existe y se actualizó", dicc_juegos)
