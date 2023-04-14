'''EJEMPLO DICCIONARIOS'''

dicc_alumno = {"legajo" : 205664, "nombre" : "Wilson", "apellido" : "Pelota"}

print("el nombre es: {0} apellido: {1} legajo: {2}".format(
    dicc_alumno["nombre"],
    dicc_alumno["apellido"],
    dicc_alumno["legajo"]))

# #para agregar aca no se usa el append() como en las listas, sino que se agrega un elemento de esta forma:
# ''' si la key cuit ya existe, estarimos re- asignndo
# y si no existe estarimaos agregando esta nuev key y su valor'''
dicc_alumno["cuit"] = "7-31455244-3"

print(dicc_alumno)


# como AVERIGUAR LAS CLAVES
claves = dicc_alumno.keys()
print(claves)

# RECORRER EL DICCIONARIO
'''1 manera'''
for clave in dicc_alumno.keys():
    print(clave) #imprime las KEY ´--- el for ya me guarda la key aca en la variable clave
    print(dicc_alumno[clave]) #Inprime los VALORES --ESTO GENERA EL VALOR : dicc_alumno[clave]




'''simplificado''' # este y el de abajo son equivalentes
for clave in dicc_alumno.keys():
    print("la clave es: {0} y su valor es: {1}".format(clave, dicc_alumno[clave]))
    
'''2 manera-------- pra acceder a la KEY y VALOR al mismo tiempo:'''

for clave,valor in dicc_alumno.items():
    print("la clave es: {0} y su valor es: {1}".format(clave, valor))





