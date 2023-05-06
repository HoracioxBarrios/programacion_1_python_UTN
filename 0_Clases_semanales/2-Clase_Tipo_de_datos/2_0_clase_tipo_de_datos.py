# TIPOS DE DATOS repaso

''' Todos los datos que aparecen en un programa tienen un tipo.

Cada tipo de dato tiene un uso distinto.

En python no estamos obligados a declarar el tipo de dato, ya que eso
pasa automaticamente en el momento que le asignamos un valor a una variable (Esa 
carpteristica se llama TIPADO DINAMICO).
cuando se le da un valor a una viarible en ese momento pasa a 
tener un tipo de datos.
'''
#Tipo de dato Int (Entero)
'''permite representar un numero entero positivo o negativo. (NO DECIMAL)'''
numero_int = 23
print(numero_int)# 23
print(type(numero_int)) # <class 'int'>

# en python una viariable es una etiqueta. aca la etiqueta numero_int guarda el numero 23

#Tipo de dato Float (fltante o decimal)
numero_float = 15.2
print(numero_float)# 15.2
print(type(numero_float)) # <class 'float'>
'''permite representar un numero flotante positivo o negativo. (NO ENTERO)'''

#Otro tipo es: complex (complejoos)

'''los numeros complejos tienen dos partes: una real y otra imaginaria.
'''
c = 3 + 5j
print(c) # (3+5j)
print(c.real) #3.0    
print(c.imag)# 5.0
print(type(c))# <class 'complex'>

#tipo de dato STRING (cadena de caracteres)

''' 
los string son un tipo inmutable que permite almacenar cadena de capacteres.
Para crear una hay que incluir el texto entre comillas

'''
nombre = "pepe" # escrito con comillas dobles
apellido = 'Velez' # escrito con comillas simples
print(type(nombre))#<class 'str'>
print(type(apellido))#<class 'str'>

'''una cadena de caracteres , en el fondo son un caracter al lado de otro.
Se puede recorrer como si fuera una Lista'''


