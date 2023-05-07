'''
11.Escribir una función que tome una lista de palabras y devuelva 
un string que contenga todas las palabras concatenadas con 
comas y "y" antes de la última palabra. Por ejemplo, si la lista 
es ["manzanas", "naranjas", "bananas"], el string resultante 
debería ser "manzanas, naranjas y bananas"..

'''
listado_de_frutas = ["manzanas", "naranjas", "bananas"]

def crear_cadena_concatenada(lista_de_frutas):
    '''
    concatena las frutas con "," y antes de la ultima fruta agrega "y"
    recibe una lista de frutas
    devuelve una cadena concatenada
    '''
    primero_separador = ", "
    ultimo_separador = " y "
    if len(lista_de_frutas) == 0:
        return ""
    elif len(lista_de_frutas) == 1:
        return lista_de_frutas[0]
    else:
        primeras_frutas = primero_separador.join(lista_de_frutas[:-1])#va de 0 hasta el anteultimo
        ultima_fruta = lista_de_frutas[-1]
        nueva_cadena = "{0} {1} {2}".format(
            primeras_frutas,ultimo_separador, ultima_fruta)
        return nueva_cadena


print(crear_cadena_concatenada(listado_de_frutas))