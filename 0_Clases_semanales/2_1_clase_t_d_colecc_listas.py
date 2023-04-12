# TIPO DE DATOS, (COLECCIONES)
# List (LISTAS): en otro lenguaje como Javascript array

'''permite almacenar un conjunto arbitrario de datos. donde 
cada elemento ocupa un lugar, llamado indice. Estos indices comienzan 
en 0, 1, 2, 3, 4, etc '''

lista = [1, "Hola", 15.3]
print(type(lista)) # el tipo es:  <class 'list'>

#si queremsos mostar el elemento 2, esta en el indice 1
print(lista[1]) #Hola

#si queremos asignar otro valor nuevo, esto reescribe lo que hay en esa posicion
lista[1] = "chau"
print(lista[1])

# para ACCEDER AL ELEMENTO CONTAMOS CON EL INDICE, desde el indice 0 en adelante

''' NO ES UNA BUENA PRACTICA: que una lista tenga distintos tipos de datos.
No esta bien ya que eso deja un codigo engorroso y dificil de seguir.
EN PYTHON se puede tener una lista con distintos tipos de datos, pero 
no se debe hacer.'''

# el nombre de la lista debe decir o expresar que contiene
'''
ejemplos: lista_de_edad    lista_de_nombres    lista_de_empleados   etc...'''

#por lo tanto una lista debe tener siempre un mismo tipo de elementos

# ACCEDER A UN ELEMENTO
''' hay que poner el nombre de la lista y entre corchetes pasarle el indice'''
#para leer lo que tiene
lista_num = [1, 2, 3, 4, 5]
print(lista_num[0]) # imprime el 1

#para escribir
lista_num[0] = 10
print(lista_num[0]) # imprime el 10


''' a que indices no se pueden acceder? respuesta:  los que no existen'''

#para agregar un elemento al final de una lista .append()  y
# pasar como arg el dato a agregar

lista_nombres_ejemplo = ["pepe", "fito"]
nombre = "Rufo"

lista_nombres_ejemplo.append(nombre)
print(lista_nombres_ejemplo)




