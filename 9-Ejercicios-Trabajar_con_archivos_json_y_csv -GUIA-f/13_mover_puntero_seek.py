'''
El método seek permite modificar la posición 
actual del puntero.
Mover puntero: seek

'''

archivo = open('archivo.txt', 'r+')
archivo.seek(11)
print(archivo.tell()) #Esta en el byte 11
linea = archivo.readline()
print(linea,end="") # Hola mundo
archivo.close()