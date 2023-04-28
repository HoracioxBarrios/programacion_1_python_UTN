for personaje in lista:
        for clave, valor in personaje.items():
            if(valor.replace(".", "").isdecimal()): #Verifica si es decimal
                print(type(valor))
                valor = float(valor)
                print(type(valor))