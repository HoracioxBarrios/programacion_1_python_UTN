'''
Una vez que un archivo está abierto y se obtiene 
el objeto file permite no sólo operar con él sino 
también obtener mucha información relacionada 
con ese archivo.
'''
#el metodo open retorna un obj file, que tiene propiedades:

'''
archivo = open(ruta_y_nombre_y_extension, modo)


archivo.closed retorna True si el archivo está cerrado, 
si no, False.

archivo.mode retorna el modo de acceso con el que el 
archivo ha sido abierto.


archivo.name retorna el nombre del archivo.
'''

#archivo = open(nombre_archivo, modo)