'''
15- Crear una función que recibe una lista de diccionarios 
con información de películas (título, género, director) y 
devuelve un diccionario con la cantidad de películas por género.
'''

lista_de_peliculas = [
{"titulo": "El Señor de los anillos", "genero": "Fantasia", "Director": "Peter Jackson"},
{"titulo": "Harry potter","genero": "Aventura", "Director": "Chris Colombus"},
{"titulo": "Terminator","genero": "Ciencia Ficcion", "Director": "James Cameron"},
{"titulo": "El Señor de los anillos 2 ", "genero": "Fantasia", "Director": "Peter Jackson"}]

def calcular_por_genero(lista,clave):
    '''
    de una lista cuenta, cuenta los elementos que se repiten
    recibe una lista
    retorna un diccionario con los elementos contabilizados
    '''
    dicc_contador_peliculas = {}

    for elemento in lista:
        
        if elemento[clave] in dicc_contador_peliculas:
            dicc_contador_peliculas[elemento[clave]] += 1
        else:
            dicc_contador_peliculas[elemento[clave]] = 1
    return dicc_contador_peliculas

resultado = calcular_por_genero(lista_de_peliculas,"genero")
print(resultado)











# def calcular_peliculas_por_genero(lista_peliculas):
#     dicc_contador_peliculas = {}

#     for pelicula in lista_peliculas:
#         clave = pelicula["genero"]
#         if clave in dicc_contador_peliculas:
#             dicc_contador_peliculas[clave] += 1
#         else:
#             dicc_contador_peliculas[clave] = 1
#     return dicc_contador_peliculas

# resultado = calcular_peliculas_por_genero(lista_de_peliculas)
# print(resultado)














# def buscar_peliculas_por_genero(lista):
#     '''
#     contabiliza peliculas segun su genero
#     recibe una lista de diccionario peliculas
#     retorna un nuevo diccionario con los generos y su cantidad
#     '''
#     contador_Fantasia = 0
#     contador_ciencia_ficcion = 0
#     contador_aventura = 0
#     dicc_conteo_pelicula_por_generos = {}
    
#     for pelicula in lista:
#         if(pelicula["genero"] == "Fantasia"):
#             contador_Fantasia += 1
#             dicc_conteo_pelicula_por_generos["Fantasia"] = contador_Fantasia
            
#         if(pelicula["genero"] == "Aventura"):
#             contador_aventura += 1
#             dicc_conteo_pelicula_por_generos["Aventura"] = contador_aventura
            
#         if(pelicula["genero"] == "Ciencia Ficcion"):
#             contador_ciencia_ficcion += 1
#             dicc_conteo_pelicula_por_generos["Ciencia Ficcion"] = contador_ciencia_ficcion
            
#     return dicc_conteo_pelicula_por_generos

# print("Las peliculas por genero son: {0}".format(
#     buscar_peliculas_por_genero(lista_de_peliculas)))