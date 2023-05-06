# TIPO DE DATOS, (COLECCIONES)
# Diccionarios

''' Un diccionario tiene "clave" : valor ,"clave" : valor,
"clave" : valor, "clave" : valor, "clave" : valor , etc..........
y puede tener muchas, todas las que se quieran.
'''
# con esto se puede crear algo mas complejo como podria ser 
#la entidad ALUMNO, que dentro puede tener nombre, edad, dni...


''' DATO
por ejemplo si tenemos un dccionario Alumno ,vamos a poder
guardar los datos de un alumno. UNO SOLO.


Despues podemos tener una LISTA de Alumnos y dentro 
elementos en cada indice que contengan DCCIONARIOS,
que cada uno va a tener los datos de CADA persona.
'''

#             {   CLAVE  :  VALOR , CLAVE : VALOR}
diccionario = { 'nombre' : 'Pepe', 'edad': 25}

print(diccionario['nombre']) # imprime Pepe

print(diccionario['edad']) #imprime 25

#ver tipo de datos
print(type(diccionario)) # <class 'dict'>

# para AGREGAR UN elemento ...................................
diccionario['nombre'] = "Lili"
diccionario['edad'] = 18

''' asi se asigna un valor como arriba, lo que queremoa cargarles, puede 
venir de un archivo, base de datos, web service. de cualquier lado.'''



