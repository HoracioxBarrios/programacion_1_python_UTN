'''
usando python 3 como seria esto? Integrador 2 : Gimnasio - Lista de diccionarios
Un gimnasio desea llevar el control de sus miembros. Cada miembro tiene 
un número de identificación, nombre, edad y tipo de membresía (por ejemplo,
mensual o anual). La información se encuentra almacenada en una lista de 
listas, donde cada sublista representa a un miembro y contiene los siguientes 
elementos: número de identificación, nombre, edad y tipo de membresía.


'''
'''
chat gtp 

En lugar de usar una lista de listas, se puede usar una lista de 
diccionarios para almacenar la información de los miembros. Cada 
diccionario contendría la información de un miembro, con las claves
'id', 'nombre', 'edad' y 'tipo_membresia'. Aquí está un ejemplo de 
cómo se puede implementar esto en Python 3:'''

miembros = [
    {'id': 1, 'nombre': 'Juan', 'edad': 30, 'tipo_membresia': 'mensual'},
    {'id': 2, 'nombre': 'Maria', 'edad': 25, 'tipo_membresia': 'anual'},
    {'id': 3, 'nombre': 'Pedro', 'edad': 40, 'tipo_membresia': 'mensual'}
]

# Agregar un nuevo miembro
nuevo_miembro = {'id': 4, 'nombre': 'Ana', 'edad': 20, 'tipo_membresia': 'anual'}
miembros.append(nuevo_miembro)

# Obtener la información de un miembro por su id
id_buscado = 2
for miembro in miembros:
    if miembro['id'] == id_buscado:
        print(miembro)
        break
else:
    print(f"No se encontró ningún miembro con id {id_buscado}")


'''
En este ejemplo, se define una lista llamada miembros que contiene tres 
diccionarios que representan a los miembros del gimnasio. Luego, se agrega 
un nuevo miembro a la lista utilizando el método append().

Para buscar un miembro por su id, se utiliza un bucle for que recorre 
cada elemento de la lista. Si se encuentra un miembro con el id buscado, 
se imprime su información y se detiene el bucle utilizando la sentencia 
break. Si el bucle termina sin encontrar un miembro con el id buscado, se
imprime un mensaje de error utilizando la sentencia else del bucle for.
'''