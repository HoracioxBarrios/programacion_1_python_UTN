'''                         for en python'''
''' funcion range:
range() genera una secuencia de numeros que van desde 0 (por defecto
)hasta el numero que le pasemos MENOS UNO , hay que pasarlo por parametro'''

#lista_de_numeros = list(range(5))    #aca creamos una lista y usamos range para definir los elementos numericos
# lista_de_numeros = range(5)
# #aca devuelve un iterable que se guarda en list de numeros

# for numero in lista_de_numeros:
#     print(numero)# 1 2 3 4 

''' range devuelve un iterable, no una lista. si queremos una lista
tenemos que creala nosotros'''


#Dato ***********************************************************
'''* Si quiero recorrer una lista que estoy fabricando, el for viene bien para eso.
y si necesito emular el for de otro lenguaje, usando range()  para generar ese Iterable,
para tener esos numeros para definir cuando terminar el bucle'''
#****************************************************************


''' el for en python no se hace incrementando una variable como en javascript
sino que aca recorre un iterable, ejemplo: listas o lo que en js es un array.
Ej Javascript :
for(i = 0; i < 10; i++){
    }
    
'''
#Aca es Distinto a js
#Dato ***********************************************************
'''* Si quiero recorrer una lista que estoy fabricando, el for viene bien para eso.
y si necesito emular el for de otro lenguaje, usando range()  para generar ese Iterable,
para tener esos numeros para definir cuando terminar el bucle'''
#****************************************************************
# variable_ver_que_hace_range = range(5)
# print(variable_ver_que_hace_range)#range(0, 5)
# '''genera un objeto iterable'''

# '''para convertirlo a lista, hacemos un casting'''
# lista_nueva = list(variable_ver_que_hace_range)#me arma la lista con el iterable de 5 "indices"
# print(lista_nueva)# [0, 1, 2, 3, 4]


'''CUANDO TENEMOS UNA LISTA, Y QUIERO RECORRERLA AHI USAMOS for'''
#DATO
#EN EL WHILE NO SABES CUANTAS ITERACIONES VA A HACER
#EN CAMBIO SI SABES QUE VAS A ITERAR 10 VECES, 15 VECES O QUE RECORRA LA
#TOTALIDAD DE LA LISTA, USARIAMOS FOR 

# lista_de_numeros = [1, 2, 3, 4, 15, -1]

# for numero in lista_de_numeros:
#     print(numero, end=" ") #salida 1 2 3 4 15 -1
    #end = " " es un terminador para que imprima uno al lado del otro, si no 
    # lo tiene, el print() agrega un salto de linea he imprime uno bajo el otro
    
'''En la primera iteracion, la variable numero (es una variable que existe 
en el for localmente )va a tomar el valor 1 del primer elemento
de lista_de_numeros; en la segunda iteracion va a contener el 2; en la tercera 
va a tener el 3 y asi sucesivamente ...'''

# si quiero una lista de 20 numeros, no combienehacerlo a mano
# lista_numeros = [0, 1, 2, 3,] #hecho a mano
# para hacerlo mas facil usamos la funcion range()
# lista_numeros = range(4) # aca indicamos 4 elementos pra que imprima desde 0 hasta 3
'''si queremos que el iterable se una lista:'''
# lista_numeros = list(range(4)) #usando range()
# print(lista_numeros)

''' ESTOS SON EQUIVALENTES
lista_numeros = [0, 1, 2, 3,] #hecho a mano
print(lista_numeros)

lista_numeros = list(range(4)) #hecho usando range()
print(lista_numeros)

'''
#-------- equivalentes ------------------------------
# lista_de_numeros = [0, 1, 2, 3]

# for numero in lista_de_numeros:
#     print(numero, end=" ")


# lista_de_numeros = list(range(4))

# for numero in lista_de_numeros:
#     print(numero, end=" ")
    
#---------------------------------------------------

lista_de_nombres = ["PEPE", "ROLO", "FER", "LUCAS"]

for nombre in lista_de_nombres:
    print(nombre)