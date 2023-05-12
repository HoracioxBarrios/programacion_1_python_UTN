'''
Permite obtener una lista con todas las líneas que 
contiene el archivo.
Leer un archivo: readlines

'''

archivo = open('archivo.txt', 'r+')
for linea in archivo.readlines():
 print(linea, end="")
# Cerramos el archivo
archivo.close()