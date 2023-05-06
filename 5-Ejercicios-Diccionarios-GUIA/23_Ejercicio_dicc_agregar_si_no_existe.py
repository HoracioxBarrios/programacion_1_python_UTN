'''
23.Crea un diccionario que represente los contactos de un teléfono, donde las
claves son los nombres de las personas y los valores son los números de
teléfono correspondientes. Solicitar al usuario el nombre de un contacto:
agregarlo al diccionario en caso de que no exista. En caso de que exista
modificar el número de teléfono del contacto
'''

diccionario_contactos = {
    "Juan": "15787478",
    "María": "15555678",
    "Pedro": "15559012",
    "Lucía": "15553456"
}

nombre_ingresado = input("Ingrese nombre de contacto ").capitalize()
numero_ingresado = input("Ingrese numero de telefono ")

if(nombre_ingresado in diccionario_contactos):
    diccionario_contactos[nombre_ingresado] = numero_ingresado
    print("Se modifico el numero")
else:
    diccionario_contactos[nombre_ingresado] = numero_ingresado
    print("Se agregó el contacto y numero")
    
print(diccionario_contactos)