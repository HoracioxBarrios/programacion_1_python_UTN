#Tipo de datos Set
#Conjuntos SET

'''
1- los elementos de un Set son unicos, no contiene duplicados.
2- los Set no respetan el orden que tenian al ser declarados.
3- sus elementos son inmutables.

4 una llaves, no hay que confundirse con un diccionario. y a diferencia de 
estos , un set solo tiene VALOR (PYTHON no encuentra los dos puntos : 
y por eso entiende que es un set)


un set tiene ELEMENTOS  INMUTABLES
'''
s = {1, 2, 5, 10, 100}
print(s)#{1, 2, 100, 5, 10}

print(type(s)) # <class 'set'>

''' HAY soluciones que por ejemplo de una lista se construye 
un set. por lo tanto es una forma de obtener un conjuntos 
de elementos NO REPETIDOS.


sI EL USUARIO pide que le muestre todas las letras de una lista 
sin repetir, puede cosntruir un SET y mostrarlo 


--------------para eso HAY QUE RECORRERLO CON UN FOR---------------

por lo tanto si tenes una bolsa de palabras con set te traes una 
de cada sin repetir, y se puede mostar con un for .

puede ser usado como filtro, para obtener cada elemento una sola vez.

en el set no contamos con el orden.
'''

