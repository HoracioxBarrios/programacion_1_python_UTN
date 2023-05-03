'''El método re.split() devuelve una lista de cadenas 
que se han separado utilizando la expresión regular.
Se utiliza para dividir una cadena en varias partes utilizando una expresión 
regular como separador.'''

import re

texto = "Hola, cómo estás? Yo estoy bien."
palabras = re.split('\W+', texto)

print(palabras) #['Hola', 'cómo', 'estás', 'Yo', 'estoy', 'bien', '']

'''re.findall() devuelve una lista de todas las coincidencias encontradas en la 
cadena, en el orden en que aparecen. Si no se encuentran coincidencias, la 
función devuelve una lista vacía.

re.findall() es una función de la biblioteca estándar re que se utiliza 
para buscar todas las ocurrencias de una expresión regular en una cadena y 
devolver una lista con todas las coincidencias encontradas.

En una expresión regular, el asterisco (*) es un metacaracter que representa 
cero o más ocurrencias del elemento que lo precede. En otras palabras, el 
asterisco indica que el elemento anterior puede aparecer cero veces, una vez 
o varias veces en la cadena y aún así hacer una coincidencia exitosa.
'''
import re

texto = "La casa está en la playa, y hay arena por todas partes."
palabras_con_a = re.findall(r'\b\w*a\w*\b', texto)

print(palabras_con_a) # ['casa', 'playa', 'arena', 'todas']


'''La función re.sub() en Python 3 es utilizada para reemplazar todas las 
ocurrencias de una expresión regular en una cadena con un texto especificado.'''

import re

texto = "La gata come galletas"
nuevo_texto = re.sub("gata", "perro", texto)

print(nuevo_texto)  # Output: "La perro come galletas"

'''La función re.match() en Python 3 se utiliza para buscar un patrón específico 
al principio de una cadena dada. Devuelve un objeto Match si se encuentra el 
patrón y None si no se encuentra.'''

import re

cadena = "Hola mundo"
patron = "Hola"

resultado = re.match(patron, cadena)

if resultado:
    print("Se encontró el patrón.")
else:
    print("No se encontró el patrón.")





