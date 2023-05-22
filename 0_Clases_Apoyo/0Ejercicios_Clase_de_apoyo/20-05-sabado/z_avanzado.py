from functools import reduce
from copy import deepcopy
import copy

#Lambda ---> anonimas
# 

suma = lambda numeroUno,numeroDos : numeroUno + numeroDos 

mayor = lambda numeroUno,numeroDos : numeroUno > numeroDos

print("Estamos usando la suma")
print(suma(2,3))
print("Estamos consultando si es mayor o menor")
print(mayor(3,10)) #boolean

#operadores ternarios : ?

mayor_edad = lambda numeroUno,numeroDos : numeroUno if numeroUno > numeroDos else numeroDos
#            lambda variable,variable : resultado_si_if_es_true if condicion else resultado_si_if_es_false
print("Operador ternario")
print(mayor_edad(3,10))


#map, filter, reduce

#map ----> a una lista le tenemos que aplicar algo

personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Juan", "edad": 30},
    {"nombre": "María", "edad": 35}
]

print(map(lambda persona : persona["edad"]+2,personas))
print(personas)

lista_nombres= list(map(lambda persona : persona["nombre"],personas[1:]))

print(lista_nombres)


#filter
lista_filtrada = list(filter(lambda persona: persona["edad"]>20,personas))
print("Lista filtrada")
print(lista_filtrada)
print(id(lista_filtrada))
print("Lista sin filtro")
print(personas)
print(id(personas))

#reduce
print(reduce(lambda acumulador,persona:acumulador + persona["edad"],personas,0))

#shallow copy
#deep copy

#shallow copy
lista_a = [[1,2,3],[4,5,6],[7,8,9]]

lista_b = list(lista_a)

#print(lista_a)
#print(lista_b)

lista_a.append(['nueva lista'])

#print(lista_a)
#print(lista_b)

lista_a[1][0]= 'A'

#print(lista_a)
#print(lista_b)


lista_c = [1,2,3,4,[0,5,6]]

lista_d = list(lista_c)


lista_c[1]=10
#print(lista_c)
#print(lista_d)
lista_c[4][0]='C'
#print(lista_c)
#print(lista_d)

def sumar(a,b):
    a = a +b
    return a

numero_uno = 2
numero_dos = 3
valor_uno = sumar(numero_uno,numero_dos)

print(numero_uno)



#deep copy
lista_a = [[1,2,3],[4,5,6],[7,8,9]]

lista_b = deepcopy(lista_a)

#print(lista_a)
#print(lista_b)

lista_a.append(['nueva lista'])

#print(lista_a)
#print(lista_b)

lista_a[1][0]= 'A'

print(lista_a)
print(lista_b)
'''
shallow copy en diccionarios
diccionario_original = {"a": 1, "b": 2, "c": [3, 4]} 
copia_diccionario = copy.copy(diccionario_original)

print(diccionario_original)
print(copia_diccionario)

copia_diccionario["c"][0] = 'A'
print(diccionario_original)
print(copia_diccionario)

copia_diccionario["a"] = 'A'
print(diccionario_original)
print(copia_diccionario)
'''

diccionario_original = {"a": 1, "b": 2, "c": [3, 4]} 
copia_diccionario = copy.deepcopy(diccionario_original)

print(diccionario_original)
print(copia_diccionario)

copia_diccionario["c"][0] = 'A'
print(diccionario_original)
print(copia_diccionario)

copia_diccionario["a"] = 'A'
print(diccionario_original)
print(copia_diccionario)


persona =  {"nombre": "María", "edad": 35, "altura": 1.60}

#devuelve el valor de la clave pasada por parametro
print(persona.get("nombre"))
print(persona.get("dni","No existe el campo ingresado"))

#keys devuelve todas las claves
print(list(persona.keys()))

#values devuelve todos los valores
print(list(persona.values()))

#items 
print(list(persona.items()))

#pop  
print(persona.pop("altura"))
print(persona)

try:
    numero = int(input("ingrese un numero"))
    array_numero = [1,2]
    print(array_numero[numero])
except ValueError:
    print("Lo que ingresaste no es un numero")
except Exception as e:
    print("Error: ", str(e))







#https://www.onlinegdb.com/2HvDGsbkZ