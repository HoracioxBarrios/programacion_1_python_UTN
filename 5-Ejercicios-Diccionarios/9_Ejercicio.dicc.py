'''
9- Crea un diccionario que contenga las capitales de los países 
de América del Sur. Luego, pide al usuario que ingrese el nombre 
de un país y muestra su capital correspondiente.
'''

dicc_paises_de_america = {"Argentina": "Buenos Aires",
                        "Uruguay": "Montevideo",
                        "Chile": "Santiago de Chile",
                        "Paraguay": "Asuncion"}

nombre_pais_ingresado = input(
    "Ingrese nombre de Pais de America del Sur")

for pais, capital in dicc_paises_de_america.items():
    if(pais == nombre_pais_ingresado):
        print("El pais ingresado es:{0} su Capital es: {1}".format(
            pais,capital))
        
