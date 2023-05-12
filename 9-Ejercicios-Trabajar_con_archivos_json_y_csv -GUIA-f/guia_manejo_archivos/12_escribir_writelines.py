'''
Escribe una lista de cadena de caracteres dentro 
del archivo. El parámetro que recibe el método 
podrá ser cualquier iterable.
Escribir: writelines

'''

archivo = open('archivo.txt', 'w')

lineas_texto = ['Primer linea de texto\n','segunda linea\n',
'tercera linea\n']

archivo.writelines(lineas_texto)
archivo.close()