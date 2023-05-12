'''
El nombre es un acrónimo de las siglas en inglés de JavaScript 
Object Notation.
JSON es un formato para el intercambio de datos basado en texto. 
Por lo que es fácil de leer tanto para una persona como para una máquina. '''
'''                  JSON (Escritura)

El paquete json permite traducir un diccionario a 
formato JSON utilizando el método dump.

'''
import json

data = {}
data['clientes'] = []
data['clientes'].append({ 'nombre': 'Juan', 'edad': 27})
data['clientes'].append({ 'nombre': 'Ana', 'edad': 26})
with open('data.json', 'w') as file:
 json.dump(data, file, indent=4, ensure_ascii=False )
 
 
 '''               JSON (Lectura)
 La lectura es similar al proceso de escritura, se 
debe abrir un archivo y procesar esté utilizando el 
método load.
'''
 
import json

with open('data.json') as file:
 data = json.load(file)