'''
El método read permite extraer un string que 
contenga todos los carácteres del archivo.
Leer un archivo: read


'''
# # Abrimos el archivo en modo lectura y escritura
# archivo = open('archivo.txt', 'r+')
# texto = archivo.read()
# print('El contenido del archivo es: ' + texto)
# # Cerramos el archivo
# archivo.close()



'''

Es posible limitar al método read a que lea cierta 
cantidad de bytes read(cantidad)
Leer un archivo: read
'''
# Abrimos el archivo en modo lectura y escritura
archivo = open('archivo.txt', 'r+')
archivo.seek(100)
texto = archivo.read(10)
print('El contenido del archivo es: ' + texto)
# Cerramos el archivo
archivo.close()