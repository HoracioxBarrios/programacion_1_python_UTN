''' 
4- Crea un diccionario que contenga la información de una dirección: 
nombre de la calle, altura, localidad, código postal, partido y 
provincia. Luego, imprime el nombre de la calle, seguido de su altura.

'''
diccionario_direccion = {"Calle" : "Avenida Mitre", "Altura" : 750 ,
                        "Localidad" : "Avellaneda","Codigo Postal" : 1870,
                        "Partido" : "Avellaneda", 
                        "Provincia" : "Buenos Aires"}


print("Nombre de la calle: {0} {1}".format(
    diccionario_direccion["Calle"],
    diccionario_direccion["Altura"]))

