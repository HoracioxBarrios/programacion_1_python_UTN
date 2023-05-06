'''
20.Crea un diccionario que represente los asientos de un avión,donde las claves
son los números de asientos y los valores son "True" si están ocupados y
"False" si no lo están. Solicita al usuario un número de asiento y modifica su
valor para marcarlo como ocupado. Luego imprimí la lista de asientos libres

'''
diccionario_asientos_avion = {
    "1A": True,
    "1B": False,
    "1C": False,
    "1D": False,
    "1E": False,
    "1F": False,
    "2A": False,
    "2B": False,
    "2C": False,
    "2D": False,
    "2E": False,
    "2F": False,
    "3A": False,
    "3B": False,
    "3C": False,
    "3D": False,
    "3E": False,
    "3F": False,
    "4A": False,
    "4B": False,
    "4C": False,
    "4D": False,
    "4E": False,
    "4F": False,
    "5A": False,
    "5B": False,
    "5C": False,
    "5D": False,
    "5E": False,
    "5F": False,
    "6A": False,
    "6B": False,
    "6C": False,
    "6D": False,
    "6E": False,
    "6F": False,
    "7A": False,
    "7B": False,
    "7C": False,
    "7D": False,
    "7E": False,
    "7F": False,
    "8A": False,
    "8B": False,
    "8C": False,
    "8D": False,
    "8E": False,
    "8F": False,
}

numero_asiento_ingresado = input(
    "Ingresa una letra y un número de asiento. (ejemplo 1A)  ")

flag_encontrado = False
for numero_asiento in diccionario_asientos_avion.keys():
    if(numero_asiento_ingresado == numero_asiento):
        flag_encontrado = True
        if(diccionario_asientos_avion[numero_asiento] == False):
            diccionario_asientos_avion[numero_asiento] = True
            print("Has reservado este asiento")
        else:
            print("asiento no disponible")
        break

if not flag_encontrado:
    print("No existe ese asiento")

print(diccionario_asientos_avion)

