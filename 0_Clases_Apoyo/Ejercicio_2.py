# #Lista

# lista_valores = [1 , 33, 12, -12]
# print(lista_valores[1])#33

# lista_valores[1] = 22
# print(lista_valores[1])# 22

# #agregar a la lista
# lista_valores.append(99)
# print(lista_valores(4))# 99

# # for
# # recorremos la lista
# for valor in lista_valores:
#     print(valor)

# #len se sabe cuantos elementos tiene una lista, o un str
# for indice in range(len(lista_valores)):# genero un indice a partir de la lista
#     print(lista_valores[indice])


# cant_elem_de_la_lista = len(lista_valores)
# for indice in range(cant_elem_de_la_lista):
#     print(lista_valores[indice])

#dicionarios
dict_alums = {"CLAVE" : "VALOR" , "legajo": 202145, 
            "nombre" : "Juan", "apellido" : "Mendez"}
#acceder
print("El legajo es: {0}, el nombre es {1}, el apellido es {2}".format(
    dict_alums["legajo"], 
    dict_alums["nombre"], 
    dict_alums["apellido"]))

#agregar un nuevo elem a un diccionario

dict_alums["cuit"] = "22-252252-9"

#recorrer las claves de un diccionario

claves = dict_alums.keys()
print(claves)

for clave in dict_alums.keys():   # con keys() que devuelve las keys y con iteramos entre las keys
    valor = dict_alums[clave]
    print("La clave es {0} y el item es {1}".format(clave,valor))

#otra forma - es una tupla implicita
for clave,valor in dict_alums.items(): # con items() ieteramos entre los items
    print("La clave es {0} y el item es {1}".format(clave, valor))