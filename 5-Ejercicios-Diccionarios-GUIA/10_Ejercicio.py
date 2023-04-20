'''
10- Crea un diccionario que represente las notas de un examen 
de varios estudiantes, donde las claves son los nombres de los 
estudiantes y los valores son sus notas. Imprime el promedio de 
las notas.
'''
# Uso metodo keys() para obtener los nombres y abajo llamo a su valor
dicc_estudiantes_programacion = {"Kloe" : 9, "Fulano": 7, "Rufo" : 5,
                                "Pirulo" : 5, "Ada" : 8, "Soro" : 7}


cant_estudiantes = len(dicc_estudiantes_programacion)
acum_notas = 0

for clave in dicc_estudiantes_programacion.keys(): # me traigo las claves y lo uso como indice abajo
    valor = dicc_estudiantes_programacion[clave]
    acum_notas += valor

promedio = acum_notas / cant_estudiantes

print("El promedio de notas es: {0}".format(promedio))