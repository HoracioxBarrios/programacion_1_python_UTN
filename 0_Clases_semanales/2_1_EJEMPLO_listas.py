#LISTAS
#Lista vacia - en general se declara vacia para agregarle luego los elementos
lista_valores = []
print(lista_valores) # Print []

#lista con elementos harcodeados
lista_valores = [1, 22, 33, 12, -12]
print(lista_valores) # [1, 22, 33, 12, -12]

# para ver el valor de un elemento, tenemos que ver en que indice está y entre corchetes pasarle ese indice
print(lista_valores[1]) # 22

# para AGREGAR usamos el metodo append() y dentro del parentesis hay que pasarle por parametro el valor o la variable que tiene el valor. append() agrega al final de la lista.
lista_valores.append(55)
print(lista_valores)# [1, 22, 33, 12, -12, 55]


'''-------------------------------------------------------'''
''' # 1ra forma de recorrer la lista'''
# FORMAS DE RECORRER LOS EMEMETOS
#imprimir TODOS - usamos for asi como en el ej:
for valor in lista_valores:
    print(valor)

''' # 2da forma de recorrer la lista'''
#Podemos Generar un indice para ir accediendo a cada elemento de la lista usando range()
for indice in range(len(lista_valores)):
    print(lista_valores[indice])

'''la 2da forma pero en modo "Dysney": len() nos devuelve la cnt de elem, y eso lu guardamos en la variable. (son semejantes)'''
cantidad_de_elementos_lista = len(lista_valores)
for indice in range(cantidad_de_elementos_lista):
    print(lista_valores[indice])





#Podemos Generar un indice usando range(), este funcion se le puede pasar por parametro dentro de
#los parentesis range(inicio, fin, incremento). o bien otro ejemplo es range(len(lista_ejemplo))- aca va a empezar en 0 por defecto, y va a ir hasta el ultimo elemento
#range genera una secuencia de valores desde 0 predeterminado hasta el numero que le pasemos o hasta len()



''' https://www.youtube.com/watch?v=upkPetk60K4  CLASE_02-PL01_PYTHON  minuto 47:00'''