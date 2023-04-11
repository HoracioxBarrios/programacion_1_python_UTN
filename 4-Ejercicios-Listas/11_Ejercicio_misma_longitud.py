'''
11- Crea una lista de palabras y pide al usuario que ingrese una palabra. Luego,
muestra todas las palabras de la lista que tienen la misma longitud que la
palabraingresada
'''

lista_de_palabras = ["vaso", "jugo", "cervilleta", "cuchara","tenedor"]

nueva_palabra = input("Ingrese una palabra")

for palabra in lista_de_palabras:
    if(len(nueva_palabra) == len(palabra)): #la longitud me la da len() y comparamos
        print(palabra)