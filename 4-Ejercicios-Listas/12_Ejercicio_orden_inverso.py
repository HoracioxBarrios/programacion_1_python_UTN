'''
12- Crea una lista con los nombres de tus 3 películas favoritas 
y luego imprime los elementos en orden inverso (sin utilizar
el método reverse())
'''

lista_de_peliculas = ["terminator", "harry potter", "jason bourne"]

for pelicula in range(len(lista_de_peliculas)-1, -1, -1):# comienza en len()-1 ,hasta -1(en lugar de poner 0, si pongo 0 va jasta "harry potter", y el 3er parametro es la secuencia que va a ir descontando de 1 en uno)
    print(lista_de_peliculas[pelicula])# imprime el elemento de la lista en esa posicion