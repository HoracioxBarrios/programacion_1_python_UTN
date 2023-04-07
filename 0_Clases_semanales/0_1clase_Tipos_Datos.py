# Tipos de Datos

#variables en otros lenguajes
'''En algunos lenguajes una variable es un "contenedor" en el cual
se puede guardar un Valor de un tipo especifico de datos, por ejemplo
un valor numerico
# variable_numerica = 14'''
#variables en python
'''en python una variable es una etiqueta que permite hacer una referencia
a los datos, que se guardan en "cajas' llamadas objetos 
# para cada dato que aparece, python crea un objeto para contenerlo
el nombre de ese objeto para que lo podamos encontrar se llama etiqueta
y es el nombre que le ponemos al declarar la variable,
'''
#cada objeto tiene:
'''un identificador unico, una ID que no se repite'''
'''un tipo de datos(entero, flotante, cadena de carapteres, etc)'''
variable_ejemplo = 10

'''Forma en que manja Python los tipos de DATOS'''
# en lenguajes como C, C++, Java ,ETC antes de utilizar una variable,
# exigen que se aclare el tipo de dato que va a guardar
'''Otros lenguajes como Python, PHP, Etc , no lo exigen.
sino que al momento de usar esa variable se asigna el tipo de datos
dinamicamente'''

# numero_texto = "25"
# print(type(numero_texto))# muestra str
# print(id(numero_texto))# muestra ej: 2505678617776
# #casteo
# numero_entero = int(numero_texto)

numero_entero = 25
print(type(numero_entero))
print(id(numero_entero))

#reescribo numero_entero con otro valor (ver como la id cambia. osea se destruye el
# objeto anterior y se crea uno nuevo para contener el valor)
numero_entero = 5
print(type(numero_entero))
print(id(numero_entero))

''' si declaro otra variable para contener el valor de 5 , redirecciona a la 
etiqueta que ya tiene ese valor. osea usa la id de una variable ya existente'''

numero_entero_nuevo_creado_mas_adelante = 5
print(type(numero_entero))
print(id(numero_entero))

'''000000000000000000000000000000000'''
#Tipos de datos
# numeros enteros = Int
#decimales o numeros flotantes = float
#cadena de caracteres ,String =  str
# boolean = True , False

''' que es hacer CASTING'''
# castear es convertir de un tipo de datos a otro, simpre que sea posible. Ej:
numero_prueba_str = "25"
numero_prueba_int = int(numero_prueba_str)
print(numero_prueba_int) 