'''
17.Crea un diccionario que represente las películas de un cine, 
donde las claves son los nombres de las películas y los valores 
son los horarios correspondientes. Modifica el horario de la 
película "Avengers:Endgame"a las
19:30.

'''

dicc_peliculas = {
    "harry potter" : "19:30",
    "Terminator" : "22:00",
    "Narnia" : "17:00",
    "Avengers:Endgame" : "15:00"
}

# Mostrar las películas disponibles
print("Películas disponibles:")
for pelicula in dicc_peliculas:
    print("- {0}".format(pelicula))

# Pedir al usuario que ingrese la película y el nuevo horario
pelicula_buscada = input("Ingrese el nombre de la película que desea cambiar el horario: ")
if pelicula_buscada not in dicc_peliculas:
    print("Lo siento, esa película no está disponible.")
else:
    nuevo_valor_horario = input("Ingrese el nuevo horario en formato HH:MM: ")
    # Validar que el nuevo horario sea un valor de tiempo válido
    partes_horario = nuevo_valor_horario.split(":")
    # print("aca se crea una lista con estos valores para validar",partes_horario)
    if len(partes_horario) != 2 or not partes_horario[0].isdigit() or not partes_horario[1].isdigit():
        print("Lo siento, el formato del horario es inválido.")
    else:
        hora = int(partes_horario[0])
        minuto = int(partes_horario[1])
        if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
            print("Lo siento, el formato del horario es inválido.")
        else:
            # Actualizar el diccionario y mostrar un mensaje de confirmación
            dicc_peliculas[pelicula_buscada] = nuevo_valor_horario
            print("El nuevo horario de", pelicula_buscada, "es", nuevo_valor_horario)
            print(dicc_peliculas)
























'''no me sirve usa try y except ValueError'''
# dicc_peliculas = {
#     "harry potter" : "19:30",
#     "Terminator" : "22:00",
#     "Narnia" : "17:00",
#     "Avengers:Endgame" : "15:00"
# }

# # Mostrar las películas disponibles
# print("Películas disponibles:")
# for pelicula in dicc_peliculas:
#     print("- " + pelicula)

# # Pedir al usuario que ingrese la película y el nuevo horario
# pelicula_buscada = input("Ingrese el nombre de la película que desea cambiar el horario: ")
# if pelicula_buscada not in dicc_peliculas:
#     print("Lo siento, esa película no está disponible.")
# else:
#     nuevo_valor_horario = input("Ingrese el nuevo horario en formato HH:MM: ")
#     # Validar que el nuevo horario sea un valor de tiempo válido
#     try:
#         hora, minuto = map(int, nuevo_valor_horario.split(":"))
#         if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
#             raise ValueError("Formato de hora inválido")
#     except ValueError:
#         print("Lo siento, el formato del horario es inválido.")
#     else:
#         # Actualizar el diccionario y mostrar un mensaje de confirmación
#         dicc_peliculas[pelicula_buscada] = nuevo_valor_horario
#         print("El nuevo horario de", pelicula_buscada, "es", nuevo_valor_horario)
#         print(dicc_peliculas)




















'''incorrecto'''


# dicc_peliculas = {
#     "harry potter" : "19:30",
#     "Terminator" : "22:00",
#     "Narnia" : "17:00",
#     "Avengers:Endgame" : "15:00"
# }

# pelicula_buscada = input("Qué película busca para cambiar horario: ")
# nuevo_valor_horario = input("Ingrese nuevo horario: ")
# if pelicula_buscada in dicc_peliculas:
#     dicc_peliculas[pelicula_buscada] = (nuevo_valor_horario)

# print(dicc_peliculas)
