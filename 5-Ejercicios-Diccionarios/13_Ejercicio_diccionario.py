'''13- Crea un diccionario que contenga el nombre y el nivel de 
dificultad de varios juegos de mesa.Luego,pedirle al usuario un
nivelde dificultad, buscar los que coinciden e imprimir sus nombres'''

diccionario_juegos_mesa = {"Escape Room" : "FACIL","Splendor" : "MEDIO",
                    "Holmes Sherlock" : "MEDIO","Catán el Duelo" : "FACIL",
                    "Stratego" : "DIFICIL", }


dificultad_ingresado = input(
    "Ingrese nivel de dificiltad FACIL, MEDIO, DIFICIL: ")
while(dificultad_ingresado != "FACIL" or dificultad_ingresado != "MEDIO" 
    or dificultad_ingresado != "DIFICIL"):
    dificultad_ingresado = input(
        "Incorrecto! Ingrese dificiltad FACIL, MEDIO, DIFICIL: ")



lista_juegos_que_coinciden = []

#    key          valor         in     diccionario
for juego , nivel_de_dificultad in diccionario_juegos_mesa.items():
    if(dificultad_ingresado == nivel_de_dificultad ):
        lista_juegos_que_coinciden.append(juego)
        
if(len(lista_juegos_que_coinciden) > 0):
    print("La dificultad ingresada es:{0}".format(dificultad_ingresado))
    for juegos_coincidentes in lista_juegos_que_coinciden:
        print(juegos_coincidentes)









'''chat gpt 
Creamos el diccionario con los juegos de mesa y su nivel de dificultad
juegos_mesa = {
"Risk": "Alto",
"Monopoly": "Medio",
"Scrabble": "Bajo",
"Catan": "Medio",
"Ajedrez": "Alto"
}

Pedimos al usuario el nivel de dificultad que desea buscar
nivel = input("Ingrese el nivel de dificultad que desea buscar: ")

Creamos una lista vacía para almacenar los juegos que coinciden con 
el nivel de dificultad

juegos_coincidentes = []

Recorremos el diccionario y buscamos los juegos que coinciden con el nivel de 
dificultad ingresado

for juego, dificultad in juegos_mesa.items():
if dificultad == nivel:
juegos_coincidentes.append(juego)

Imprimimos los juegos que coinciden con el nivel de dificultad ingresado
if len(juegos_coincidentes) > 0:
print("Los juegos de mesa con nivel de dificultad", nivel, "son:")
for juego in juegos_coincidentes:
print(juego)
else:
print("No se encontraron juegos de mesa con nivel de dificultad", nivel)'''