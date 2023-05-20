def stark_normalizar_datos(lista:list):
    flag_normalizar = False
    if(len(lista) == 0 ):
        print("-1")
    else:
        for superheroes in lista:
            for clave,valor in superheroes.items():
                if (clave == "fuerza" and type(valor) != int and valor.isnumeric()):
                        superheroes[clave] = int(valor)
                        flag_normalizar = True
                if((clave == "altura" or clave == "peso") and type(valor) != float and valor.replace(".","").isnumeric()):
                        superheroes[clave] = float(valor)
                        flag_normalizar = True
    if(flag_normalizar == True):
        print("1")
        
'''Medio Pelo'''