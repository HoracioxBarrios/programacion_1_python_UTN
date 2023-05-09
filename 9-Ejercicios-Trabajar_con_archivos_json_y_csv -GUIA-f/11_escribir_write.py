'''
Escribe una cadena de caracteres dentro del 
archivo.
Escribir: write

'''
archivo = open('archivo.txt', 'w')
archivo.write('Primer linea de texto\n')
archivo.write('segunda linea\n')
archivo.write('tercera linea\n')
archivo.close()