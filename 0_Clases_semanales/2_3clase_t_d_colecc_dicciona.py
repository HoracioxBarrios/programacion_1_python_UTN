# TIPO DE DATOS, (COLECCIONES)
# Diccionarios

''' UN Diccionario es una coleccion de elementos.

    0_ UN DICCIONARIO tiene los Elementos encerrados entre llaves {}
    
    
    1_Cada  elemento tiene una key (clave) IZQUIERDA y value (valor). DERECHA
    
    2_ la key va escrita entre comillas. simples o dobles
    
    
    3-Van separados entre key y valor por :  dos puntos, 
    y entre elementos por coma asi como los elementos en 
    una lista
    
'''
#             {   CLAVE  :  VALOR , CLAVE : VALOR}
diccionario = { 'nombre' : 'Pepe', 'edad': 25}

print(diccionario['nombre']) # imprime Pepe

print(diccionario['edad']) #imprime 25

#ver tipo de datos
print(type(diccionario)) # <class 'dict'>

''' 
Se puede poner un diccionario dentro de otro diccionario.

Se puede poner un diccionario dentro de un lista.

Se puede poner una Lista dentro de un diccionario.

Se puede tener un diccionario que dentro, tiene una lista, que 
a su vez tiene un diccionario, que a su vez tiene un lista,
y a su vez tiene un fccionario que adentro tiene otra lista. 
'''
# A diferencia de una Lista que para ACCEDER A UN ELEMENTO solo contabamos
# con el INDICE, 
# Aca con los diccionarios PARA ACCEDER al ELEMENTO contamos con 
# la CLAVE y VALOR

''' LAS CLAVES siempre van a estar definidas como cadena de carapteres.
    El VALOR puede ser cualquier tipo de datos (el profe dijo: puede tener
    cualquier cosa.)

'''
''' los primeros tipos de datos que vamos a implementar en dicc son'''
#Booleano
#Entero
#Flotante
#String