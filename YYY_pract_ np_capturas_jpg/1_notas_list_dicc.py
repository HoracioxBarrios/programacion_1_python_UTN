'''
en pyton 3 como agrego una nueva key  y su valor a un diccionario vacio.



respuesta:

Para agregar una nueva key y su valor a un diccionario 
vacío en Python 3, puedes seguir los siguientes pasos:

Crea un diccionario vacío utilizando las llaves {} o la 
función dict().
Utiliza la sintaxis de corchetes [] para agregar una nueva 
clave y su valor al diccionario.
Aquí está el código que puedes utilizar:
'''
# Crea un diccionario vacío
mi_diccionario = {}

# Agrega una nueva clave y su valor
mi_diccionario["nueva_clave"] = "nuevo_valor"

# Imprime el diccionario para verificar que la clave y el valor se hayan agregado correctamente
print(mi_diccionario)


'''Este código creará un diccionario vacío llamado mi_diccionario, 
luego agrega una nueva clave llamada "nueva_clave" con el valor 
"nuevo_valor". Finalmente, imprime el diccionario para verificar 
que se haya agregado correctamente.'''

'''
Si necesitas pedir por input el valor que deseas agregar a tu 
diccionario en Python 3, puedes utilizar la función input() 
para leer el valor ingresado por el usuario y luego agregarlo 
al diccionario utilizando la sintaxis de corchetes [].

Aquí te muestro un ejemplo de cómo hacerlo:'''

# Crea un diccionario vacío
mi_diccionario = {}

# Pide al usuario que ingrese un valor
nuevo_valor = input("Ingrese un nuevo valor: ")

# Agrega una nueva clave y su valor al diccionario
mi_diccionario["nueva_clave"] = nuevo_valor

# Imprime el diccionario para verificar que se haya agregado correctamente
print(mi_diccionario)
