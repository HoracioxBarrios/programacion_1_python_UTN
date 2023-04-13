'''
si quiero comprobar si una Id existe:

Puedes utilizar un bucle for para recorrer la lista de diccionarios y 
comparar el valor de la clave "id" con el valor ingresado por el usuario.
Si encuentras una coincidencia, significa que el id ya existe en la lista.
Aquí te dejo un ejemplo de cómo hacerlo:
'''
list_de_diccionario_miembros = [
    {"id": "1", "nombre": "lucas", "edad": 21, "membresia": "mensual"},
    {"id": "2", "nombre": "Lili", "edad": 35, "membresia": "mensual"},
    {"id": "3", "nombre": "Jorge", "edad": 36, "membresia": "anual"}]

dicc_nuevo_miembro = {}




# id_ingresado = input("Ingrese el ID a buscar: ")

# for miembro in list_de_diccionario_miembros:
#     if miembro["id"] == id_ingresado:
#         print("El ID ya existe en la lista.")
#         break
# else:
#     print("El ID no existe en la lista.")
    
'''siquiero validar
Si quieres validar que el ID ingresado por el usuario sea un valor válido 
(es decir, que sea un número entero y que no esté vacío), puedes utilizar
un bloque try-except para capturar posibles errores al convertir el valor 
ingresado a entero. Aquí te dejo un ejemplo de cómo hacerlo:
'''
# while True:
#     id_ingresado = input("Ingrese el ID a buscar: ")
#     if not id_ingresado:
#         print("El ID no puede estar vacío.")
#         continue
#     try:
#         id_ingresado = int(id_ingresado)
#     except ValueError:
#         print("El ID debe ser un número entero.")
#         continue
#     break

# for miembro in list_de_diccionario_miembros:
#     if miembro["id"] == id_ingresado:
#         print("El ID ya existe en la lista.")
#         break
# else:
#     print("El ID no existe en la lista.")

'''este codigo sin el not , y el try?

respuesta:
'''
while True:
    id_ingresado = input("Ingrese el ID a buscar: ")
    if id_ingresado == "":
        print("El ID no puede estar vacío.")
        continue
    if not id_ingresado.isdigit():
        print("El ID debe ser un número entero.")
        continue
    break

id_ingresado = int(id_ingresado)

for miembro in list_de_diccionario_miembros:
    if miembro["id"] == id_ingresado:
        print("El ID ya existe en la lista.")
        break
else:
    print("El ID no existe en la lista.")