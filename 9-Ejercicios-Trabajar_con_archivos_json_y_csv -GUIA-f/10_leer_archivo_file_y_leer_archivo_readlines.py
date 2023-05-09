'''
Si solamente requerimos recorrer el archivo línea 
por línea, el objeto file es iterable.
Leer un archivo: file

'''

archivo = open('archivo.txt', 'r+')
for linea in archivo:
 print(linea, end="")
# Cerramos el archivo
archivo.close()

'''-----------------------------------------------------------------'''

'''
Utilizando la función readline() es posible leer desde 
la posición actual del puntero del archivo hasta el 
final de la línea y luego posicionar el puntero al 
comienzo de la siguiente línea.

'''

archivo = open('archivo.txt', 'r+')
print(archivo.tell()) #Indica en que byte esta el puntero 0
linea = archivo.readline()
print(linea,end="") # Hola mundo
print(archivo.tell()) #Indica en que byte esta el puntero 11
# Cerramos el archivo
archivo.close()