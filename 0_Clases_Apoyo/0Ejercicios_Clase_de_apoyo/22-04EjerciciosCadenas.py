'''
1.Contar letras: Crea una función que tome una cadena de texto como argumento y 
cuente el número de letras que contiene.

2.Eliminar caracteres: Crea una función que tome una cadena de texto y un carácter como argumentos, y elimine todas las ocurrencias de ese carácter en la cadena.

3.Contar palabras: Crea una función que tome una cadena de texto como argumento y 
cuente el número de palabras que contiene. 
Suponga que las palabras están separadas por un espacio.

4.Reemplazar palabras: Crea una función que tome una cadena de texto, una palabra y otra palabra como argumentos, y reemplace todas las ocurrencias de la primera palabra por la segunda en la cadena.

5.Buscar patrón: Crea una función que tome dos cadenas de texto como argumentos: una cadena principal y un patrón. La función debe encontrar todas las ocurrencias del patrón en la cadena principal y devolver una lista con las posiciones donde se encontró el patrón.

'''





'''
1.Contar letras: Crea una función que tome una cadena de texto como argumento y 
cuente el número de letras que contiene.
'''
# palabra_ingresada = input("Ingrese una Palabra\n")

# def contar_letra(cadena : str)-> int:
#     '''
#     cuenta una cadena de caracteres
#     recibe una cadena
#     devuelve la cantidad de caracteres
#     '''
#     largo_de_cadena = len(cadena)
#     return largo_de_cadena

# largo_de_la_palabra = contar_str(palabra_ingresada)

# print("La Cantidad de caracteres es: {0}".format(largo_de_la_palabra))



'''
2.Eliminar caracteres: Crea una función que tome una cadena de texto y un carácter 
como argumentos, y elimine todas las ocurrencias de ese carácter en la cadena.
'''
# palabra_ingresada = input("Ingrese una Palabra\n")
# letra_a_borrar = input("Que letra queres borrar?\n")

# def borrar_str(cadena : str, caracter : str):
#     nueva_cadena = cadena.replace(caracter, "")
    
#     return nueva_cadena

# nueva_palabra = borrar_str(palabra_ingresada, letra_a_borrar)

# print("La nueva palabra es: {0}".format(nueva_palabra))

'''
3.Contar palabras: Crea una función que tome una cadena de texto como argumento y 
cuente el número de palabras que contiene. 
Suponga que las palabras están separadas por un espacio.
'''
# palabras = input("Ingrese una Palabra\n")

# def contar_letras(cadena : str)-> int:
#     '''
#     cuenta una cadena de caracteres
#     recibe una cadena
#     devuelve la cantidad de caracteres
#     '''
#     contador_de_caracteres = 0
#     for letra in cadena:
#         if(letra != " "):
#             contador_de_caracteres += 1
        
#     return contador_de_caracteres

# largo_de_cadena = contar_letras(palabras)


# print("La Cantidad de caracteres es: {0}".format(largo_de_cadena))


''' 
4.Reemplazar palabras: Crea una función que tome una cadena de texto, 
una palabra y otra palabra como argumentos, y reemplace todas las 
ocurrencias de la primera palabra por la segunda en la cadena.
'''

cadena = "Hola, le traje el Perro"
palabra_buscada = "Perro"
palabra_a_reemplazar = "Gato"


