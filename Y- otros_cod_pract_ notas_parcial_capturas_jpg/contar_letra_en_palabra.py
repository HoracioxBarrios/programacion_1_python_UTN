

listado_de_palabras = ["hierba", "veneno", "fuego", "volador", "agua"]
letra = "a"

def contar_elementos(lista_palabras:list, caracter_buscado :str)->int:
    '''
    Cuenta la cantidad de veces que aparece una letra en una lista

    Parametros:
    lista de palabras:list
    letra:str

    retorna
    Contador de letras:int o mensaje de error
    '''
    contador_caracter = 0
    
    if(caracter_buscado.isalpha() and len(caracter_buscado)==1):# si es letra y si es una sola
        for palabra in lista_palabras: #recorremos la lista
            for caracter in palabra: #si el caracter buscado esta en la palabra
                if(caracter == caracter_buscado): # si la letra es la misma, la contamos
                    contador_caracter += 1

        if(contador_caracter > 0): #condicion para mostrar el contador sino muestra 0 
            return contador_caracter
        else: # si no se contó un caracter es lo mismo que si no estuviera en la lista y avisamos
            return "La letra {0} no está en la lista de palabras".format(caracter)
    else:
        return "Ingrese una letra válida" # si fuera otra cosa que no sea una letra

print(contar_elementos(listado_de_palabras, letra))

 
        






