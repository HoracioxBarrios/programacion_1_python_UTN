#Ejercicios_ Cadenas 22-04-2023
'''
1.Contar letras: Crea una función que tome una cadena de texto como argumento y 
cuente el número de letras que contiene.
'''
palabra_ingresada = input("Ingrese una Palabra\n")

def contar_letra(cadena : str)-> int:
    '''
    cuenta una cadena de caracteres
    recibe una cadena
    devuelve la cantidad de caracteres
    '''
    largo_de_cadena = len(cadena)
    return largo_de_cadena

largo_de_la_palabra = contar_letra(palabra_ingresada)

print("La Cantidad de caracteres es: {0}".format(largo_de_la_palabra))




'''
2.Eliminar caracteres: Crea una función que tome una cadena de texto y un carácter 
como argumentos, y elimine todas las ocurrencias de ese carácter en la cadena.
'''
palabra_ingresada = input("Ingrese una Palabra\n")
letra_a_borrar = input("Que letra queres borrar?\n")

def borrar_str(cadena : str, caracter : str)-> str:
    '''
    De una cadena de texto, borra caracteres segun el caracter ingresado
    recibe arg(1) una cadena a comprobar, y arg(2) el caracter buscado
    devuelve una nueva cadena
    '''
    nueva_cadena = cadena.replace(caracter, "")
    
    return nueva_cadena

nueva_palabra = borrar_str(palabra_ingresada, letra_a_borrar)

print("La nueva palabra es: {0}".format(nueva_palabra))





'''
3.Contar palabras: Crea una función que tome una cadena de texto como argumento y 
cuente el número de palabras que contiene. 
Suponga que las palabras están separadas por un espacio.
'''
palabras = input("Ingrese una Palabra\n")

def contar_letras(cadena : str)-> int:
    '''
    cuenta una cadena de caracteres
    recibe una cadena
    devuelve la cantidad de caracteres
    '''
    contador_de_caracteres = 0
    for letra in cadena:
        if(letra != " "):
            contador_de_caracteres += 1
        
    return contador_de_caracteres

largo_de_cadena = contar_letras(palabras)


print("La Cantidad de caracteres es: {0}".format(largo_de_cadena))


''' 
4.Reemplazar palabras: Crea una función que tome una cadena de texto, 
una palabra y otra palabra como argumentos, y reemplace todas las 
ocurrencias de la primera palabra por la segunda en la cadena.
'''

frase = "Hola, le traje el Perro"
palabra_buscada = "Perro"
palabra_a_reemplazar = "Gato"

def reemplazar_palabras(frase, palabra_origen, palabra_destino):
    '''
    reemplaza una palabra por otra 
    recibe un cadena de texto: ej: una frase
    devuelve una cadena con la palabra reemplazada
    '''
    frase.replace(palabra_origen, palabra_destino)
    return frase


nueva_frase = reemplazar_palabras(frase, palabra_buscada, palabra_a_reemplazar)
print(nueva_frase)

'''
5.Buscar patrón: Crea una función que tome dos cadenas de texto como argumentos
: una cadena principal y un patrón. La función debe encontrar todas las 
ocurrencias del patrón en la cadena principal y devolver una lista con las
posiciones donde se encontró el patrón.

'''
frase = "Hola, aca le traje el perro"
patron = "perro"

def buscar_patron(cadena, patron):
    '''
    busca un patron, en una cadena de texto
    recibe dos argunmentos: una cadena principal, y una cadena secundaria que se va a buscar
    returna una lista con la posicion en donde se encontro un patron o igualdad.
    '''
    posiciones = []
    indice = 0
    while indice < len(cadena):
        subindice = cadena.find(patron, indice)
        if subindice == -1:
            break
        posiciones.append(subindice)
        indice = subindice + len(patron)
    return posiciones

resultado = buscar_patron(frase, patron)
print(resultado)


