'''
14.Crea un diccionario que contenga el nombre como clave y el 
puntaje como valor de varios jugadores en un juego. Luego, 
pedirle al usuario el nombre del jugador y nuevo puntaje y 
actualizar el valor correspondiente en el diccionario

'''
diccionario_jugadores = {"Carlos" : 100, "Rulo" : 85, "Eli" : 50}

jugador_buscado = input("Ingrese nombre del jugador").capitalize()

nuevo_puntaje_str = input("Ingrese nuevo puntaje")
nuevo_puntaje_int = int(nuevo_puntaje_str)
for clave in diccionario_jugadores.keys():
    if(clave == jugador_buscado):
        diccionario_jugadores[clave] = nuevo_puntaje_int

print(diccionario_jugadores)