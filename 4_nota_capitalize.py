# nombre_nuevo_miembro_input = ""
# nombre_nuevo_miembro =nombre_nuevo_miembro_input.capitalize()
# print(nombre_nuevo_miembro)

# list_de_diccionario_miembros = [
#     {"id": "1", "nombre": "Lucas", "edad": 21, "membresia": "mensual"},
#     {"id": "2", "nombre": "Lili", "edad": 35, "membresia": "mensual"},
#     {"id": "3", "nombre": "Jorge", "edad": 36, "membresia": "anual"}]

# flag_id_validador = True
# flag_id_aceptada = False
# while (flag_id_validador):
#     id_nuevo_miembro_str = input("Ingrese numero id ")
#     while (len(id_nuevo_miembro_str) == 0):  # valido que no sea str vacio
#             id_nuevo_miembro_str = input(
#                     "Uste no ingreso nada! Ingrese numero id valido ")
#     for miembro in list_de_diccionario_miembros:  # corroboro si existe id
#         if (miembro["id"] == id_nuevo_miembro_str):
#             id_nuevo_miembro_str = input(
#                         "id existente! Ingrese numero id valido ")
#         else:  # si no existe en el dict, esta disponible la id y se acepta.
#                     flag_id_aceptada = True
#     if (flag_id_aceptada):
#                 flag_id_validador = False


# list_de_diccionario_miembros = [
#     {"id": "1", "nombre": "Lucas", "edad": 21, "membresia": "mensual"},
#     {"id": "2", "nombre": "Lili", "edad": 35, "membresia": "mensual"},
#     {"id": "3", "nombre": "Jorge", "edad": 36, "membresia": "anual"}]

# # ----------------valido nueva id ingresada
# flag_id_validador = True

# while (flag_id_validador):
#     flag_id_aceptada = False
#     id_nuevo_miembro_str = input("Ingrese numero id ")
#     while(len(id_nuevo_miembro_str) == 0):# valido que no sea str vacio
#         id_nuevo_miembro_str = input("Uste no ingreso nada! Ingrese numero id valido ")
#         for miembro in list_de_diccionario_miembros: #corroboro si existe id
#             if(miembro["id"] == id_nuevo_miembro_str):   
#                 id_nuevo_miembro_str = input(
#                     "id existente! Ingrese numero id valido ")
#             else:
#                 flag_id_aceptada = True
#     if(flag_id_aceptada):
#             flag_id_validador = False
            
# list_de_diccionario_miembros = [
#     {"id": "1", "nombre": "Lucas", "edad": 21, "membresia": "mensual"},
#     {"id": "2", "nombre": "Lili", "edad": 35, "membresia": "mensual"},
#     {"id": "3", "nombre": "Jorge", "edad": 36, "membresia": "anual"}]

# # ----------------valido nueva id ingresada
# flag_id_validador = True
# while (flag_id_validador):
#     id_nuevo_miembro_str = input("Ingrese numero id ")
#     while(len(id_nuevo_miembro_str) == 0):# valido que no sea str vacio
#         id_nuevo_miembro_str = input("Usted no ingresó nada! Ingrese un número de id válido: ")
#     for miembro in list_de_diccionario_miembros: #corroboro si existe id
#         if(miembro["id"] == id_nuevo_miembro_str):   
#             id_nuevo_miembro_str = input("Id existente! Ingrese un número de id válido: ")
#             break
#     else:
#         flag_id_aceptada = True
#         break
# else:
#     flag_id_aceptada = False

# if(flag_id_aceptada):
    # flag_id_validador = False
    
    
list_de_diccionario_miembros = [
    {"id": "1", "nombre": "Lucas", "edad": 21, "membresia": "mensual"},
    {"id": "2", "nombre": "Lili", "edad": 35, "membresia": "mensual"},
    {"id": "3", "nombre": "Jorge", "edad": 36, "membresia": "anual"}]

for miembro in list_de_diccionario_miembros:
    print("ID: {0} Nombre: {1} Edad {2} Membresia {3}".format(
        miembro["id"],miembro["nombre"],
        miembro["edad"],miembro["membresia"]))




# flag_id_validador = True
# while (flag_id_validador):
#     id_nuevo_miembro_str = input("Ingrese numero id ")
#     while(len(id_nuevo_miembro_str) == 0):# valido que no sea str vacio
#             id_nuevo_miembro_str = input("Uste no ingreso nada! Ingrese numero id valido ")
#     for miembro in list_de_diccionario_miembros: 
#         if(id_nuevo_miembro_str != miembro["id"]):#corroboro si no existe id, estaria Ok   
#             break
#         else:# pero si existe en lista, aviso y pido de nuevo
#             id_nuevo_miembro_str = input(
#             "id existente! Ingrese numero id valido ")