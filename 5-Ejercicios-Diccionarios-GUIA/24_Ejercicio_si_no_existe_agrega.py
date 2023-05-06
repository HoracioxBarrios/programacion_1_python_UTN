'''
en python 3 si tengo un diccionario, con claves que son equipos 
de futbol y valores que son sus puntos, y al ingresar por input 
un equipo y tambien por input sus puntos.
como veo si existe en el diccionario?, si existe modifico 
sus puntos, y si no existe lo creo  y le asigno sus puntos. 

'''

# Creamos un diccionario vacío para guardar los equipos y sus puntos
equipos = {}

# Pedimos el nombre del equipo por input
nombre_equipo = input("Ingresa el nombre del equipo: ")

# Verificamos si el equipo ya existe en el diccionario
if nombre_equipo in equipos:
    # Si existe, pedimos los nuevos puntos por input y los sumamos a los puntos actuales
    puntos = int(input("Ingresa los nuevos puntos: "))
    equipos[nombre_equipo] += puntos
    print(
        "Los puntos del equipo", nombre_equipo, "han sido actualizados a", 
        equipos[nombre_equipo])
else:
    # Si no existe, pedimos los puntos por input y lo añadimos al diccionario
    puntos = int(input("Ingresa los puntos: "))
    equipos[nombre_equipo] = puntos
    print(
        "El equipo", nombre_equipo, "ha sido añadido al diccionario con", 
        puntos, "puntos.")

# Imprimimos el diccionario actualizado
print("Diccionario de equipos:", equipos)
