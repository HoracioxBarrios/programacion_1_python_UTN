'''
Gimnasio - Lista de diccionarios
Un gimnasio desea llevar el control de sus miembros. Cada miembro tiene
un número de identificación, nombre, edad y tipo de membresía (por ejemplo,
mensual o anual). La información se encuentra almacenada en una lista de
listas, donde cada sublista representa a un miembro y contiene los siguientes
elementos: número de identificación, nombre, edad y tipo de membresía.

Escriba un programa que permita a los usuarios realizar las siguientes
operaciones:

1- Agregar un nuevo miembro: el programa debe pedir al usuario que
ingrese el número de identificación, nombre, edad y tipo de membresía
del nuevo miembro. La información debe ser agregada a la lista de diccionarios.


2- Mostrar toda la información de todos los miembros (número de identificación,
nombre, edad y tipo de membresía).

3- Actualizar el tipo de membresía de un miembro: el programa debe pedir
al usuario que ingrese el número de identificación del miembro y el
nuevo tipo de membresía. El programa debe buscar el miembro en la lista
de diccionario y actualizar el tipo de membresía correspondiente.

4- Buscar información de un miembro: el programa debe pedir al usuario que
ingrese el número de identificación del miembro. El programa debe buscar
el miembro en la lista de diccionarios y mostrar su nombre, edad y tipo
de membresía.

5- Calcular el promedio de edad de los miembros: el programa debe recorrer
la lista de diccionarios y calcular el promedio de edad de los miembros.

6- Buscar el miembro más joven y el más viejo: el programa debe buscar la
edad máxima y mínima en la lista de diccionarios y mostrar el nombre y
número de identificación correspondientes.

El programa debe permitir al usuario realizar estas operaciones
tantas veces como desee, hasta que decida salir del programa. El programa
debe mostrar un menú de opciones para que el usuario pueda elegir la
operación que desea realizar.

'''
'''Cada miembro tiene:
un número de identificación, nombre, edad y tipo de membresía
(por ejemplo,mensual o anual).'''

list_de_diccionario_miembros = [
    {"id": "1", "nombre": "Lucas", "edad": 21, "membresia": "Mensual"},
    {"id": "2", "nombre": "Lili", "edad": 35, "membresia": "Mensual"},
    {"id": "3", "nombre": "Jorge", "edad": 36, "membresia": "Anual"}]

dicc_nuevo_miembro = {}

while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")

    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        # ----------------valido nueva id ingresada
        flag_id_validador = True
        id_nuevo_miembro_str = input("Ingrese numero id ")

        while (flag_id_validador):
            while (len(id_nuevo_miembro_str) == 0):  # valido que no sea str vacio
                id_nuevo_miembro_str = input(
                    "Uste no ingreso nada! Ingrese numero id valido ")
            for miembro in list_de_diccionario_miembros:
                # corroboro si no existe id, estaria Ok
                if (id_nuevo_miembro_str != miembro["id"]):
                    flag_id_validador = False
                else:  # pero si existe en lista, aviso y pido de nuevo
                    id_nuevo_miembro_str = input(
                        "id existente! Ingrese numero id valido ")

        # ------------------valido nuevo nombre ingresado - que no sea vacio o (str numerico)
        nombre_nuevo_miembro_input = input("Ingrese Nombre ")
        nombre_nuevo_miembro = nombre_nuevo_miembro_input.capitalize()
        while (len(nombre_nuevo_miembro) == 0 or
               nombre_nuevo_miembro.isnumeric()):
            nombre_nuevo_miembro_input = input("Incorrecto! Ingrese nombre ")
            nombre_nuevo_miembro = nombre_nuevo_miembro_input.capitalize()

        # -------------------valido edad - falta ver que no ingrese (str numerico)
        edad_nuevo_miembro_str = input("Ingrese edad")
        edad_nuevo_miembro_int = int(edad_nuevo_miembro_str)
        while (edad_nuevo_miembro_int < 0):
            edad_nuevo_miembro_str = input("Ingrese edad valida")
            edad_nuevo_miembro_int = int(edad_nuevo_miembro_str)
        # -----------------valido miembro
        membresia_nuevo_miembro_input = input(
            "Ingrese membresia 'mensual/'anual")
        membresia_nuevo_miembro = membresia_nuevo_miembro_input.capitalize()
        while (len(membresia_nuevo_miembro) == 0 or
               membresia_nuevo_miembro.isnumeric()):
            membresia_nuevo_miembro_input = input(
                "Incorrecto! Ingrese nombre ")
            membresia_nuevo_miembro = membresia_nuevo_miembro_input.capitalize()

        # Carga al Diccionario
        for indice in range(4):
            dicc_nuevo_miembro["id"] = id_nuevo_miembro_str
            dicc_nuevo_miembro["nombre"] = nombre_nuevo_miembro
            dicc_nuevo_miembro["edad"] = edad_nuevo_miembro_int
            dicc_nuevo_miembro["membresia"] = membresia_nuevo_miembro

        # carga a la lista el diccionario nuevo
        list_de_diccionario_miembros.append(dicc_nuevo_miembro)
        print(list_de_diccionario_miembros)

    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        for miembro in list_de_diccionario_miembros:
            print("ID: {0} Nombre: {1} Edad {2} Membresia {3}".format(
                miembro["id"], miembro["nombre"],
                miembro["edad"], miembro["membresia"]))

    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        flag_busqueda_id_validador = True
        id_existe_ok = False
        id_busqueda = input("Busqueda de ID: Ingrese numero id ")

        while (flag_busqueda_id_validador):
            while (len(id_busqueda) == 0):  # valido que no sea str vacio
                id_busqueda = input(
                    "Busqueda de ID: Uste no ingreso nada. Ingrese numero id valido")
            for miembro in list_de_diccionario_miembros:
                # corroboro si existe id
                if (id_busqueda == miembro["id"]):
                    id_existe_ok = True
                    break

        if (id_existe_ok):
            actualiza_membresia_input = input(
                "Ingrese nueva membresia 'mensual/'anual")
            actualiza_membresia = actualiza_membresia_input.capitalize()
            while (len(actualiza_membresia) == 0 or
                actualiza_membresia.isnumeric()):  # true si es str numerico
                actualiza_membresia_input = input(
                    "Incorrecto! Ingrese nueva membresia 'mensual/'anual")
                actualiza_membresia = actualiza_membresia_input.capitalize()
                
        '''TENGO QUE AGREGAR EL CAMBIO '''

    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        pass

    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        pass

    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        pass

    # Opcion 0: Salir
    elif opcion == "0":
        break

    else:
        print("Opción inválida. Intente de nuevo.")
