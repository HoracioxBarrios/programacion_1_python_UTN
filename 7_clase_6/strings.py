
'''
1- Escribir una función que reciba un string y devuelva el mismo 
string todo en mayúsculas.

'''
# cadena = "hola mundo"

# def de_mayuscula_a_minuscula(cadena : str)-> str:
#     '''
#     conbierte una cadena en minuscula, a mayuscula
#     recibe un string
#     devuelve un nuevo string
#     '''
#     nueva_cadena = cadena.upper()
#     return nueva_cadena

# nueva_cadena_minuscula = de_mayuscula_a_minuscula(cadena)
# print(nueva_cadena_minuscula)


'''
2-Escribir una función que reciba un string y devuelva el mismo string 
todo en minúsculas.
'''
# cadena = "HOLA MUNDO"

# def de_mayuscula_a_minuscula(cadena : str)-> str:
#     '''
#     conbierte una cadena en mayuscula a minuscula 
#     recibe un string
#     devuelve un nuevo string
#     '''
#     nueva_cadena = cadena.lower()
#     return nueva_cadena

# nueva_cadena_minuscula = de_mayuscula_a_minuscula(cadena)
# print(nueva_cadena_minuscula)

'''
3-Escribir una función que tome dos strings y devuelva un nuevo string 
que contenga ambos strings concatenados, separados por un espacio.

'''
# palabra_primera = input("Ingrese una palabra")
# palabra_segunda = input("Ingrese una palabra")
# def concatenar_cadenas(cadena_uno : str , cadena_dos : str, separador : str) -> str:
#     '''
#     concatena dos cadenas
#     pide por input dos cadenas
#     devuelve una nueva cadena
#     '''
    
#     nueva_cadena = separador.join([cadena_uno , cadena_dos])
#     return nueva_cadena

# nueva_cadena = concatenar_cadenas(palabra_primera, palabra_segunda, separador= " ")
# print(nueva_cadena)

'''
4- Escribir una función que tome un string y devuelva 
el número de caracteres que tiene el string.

'''
# palabra_primera = "Pelota"

# def contador_de_cadena(cadena : str)-> int:
#     '''
#     contador de strings
#     recibe un string
#     devuelve la cantidad de letras
    
#     '''

#     return len(cadena)


# palabra_contada = contador_de_cadena(palabra_primera)
# print(palabra_contada)

'''
5-Escribir una función que tome un string y un carácter y devuelva 
el número de veces que aparece ese carácter en el string.
'''

# palabra = "Hola, todo bien?"
# letra = "o"

# def contar_repetidos(palabra : str, letra : str)-> int:
#     '''
#     cuenta la cantidad de veces que se repite una palabra en una cadena
#     recibe una cadena , y un caracter a evaluar
#     devuelve la cantidad de veces que se repite el carapter
#     '''
#     return palabra.count(letra)

# cantidad_veces_repetido = contar_repetidos(palabra, letra)
# print(cantidad_veces_repetido)


'''
6- Escribir una función que tome un string y un carácter y devuelva una 
lista con todas las palabras en el string que contienen ese carácter.
'''
# palabra = "pepe juega a la pelota"
# letra = "e"

# def contiene_caracter(palabra : str, letra_a_evaluar : str)-> list:
#     '''
#     tome un string y un carácter y devuelva una 
#     lista con todas las palabras en el string que contienen ese carácte
#     recibe una plabra y una letra.
#     devuelve una lista
    
#     '''
#     lista_nueva = palabra.split(" ")
#     nueva_lista_sresultados = []
#     for palabra in lista_nueva:
#         for letra in palabra:
#             if (letra == letra_a_evaluar ):
#                 nueva_lista_sresultados.append(palabra)
#     return nueva_lista_sresultados

# print(contiene_caracter(palabra, letra))

'''
7- Escribir una función que tome un string y devuelva 
el mismo string con los espacios eliminados

'''
# frase = "pepe no quiere prueba"

def eliminar_espacios(cadena : str)-> str:
    '''
    elimina los espacios de una cadena
    recibe una cadena
    devuelve una nueva cadena
    '''
    return cadena.replace(" ", "")

# print(eliminar_espacios(frase))


'''
8- Escribir una función que reciba dos string (nombre y apellido) 
y devuelva un diccionario con el nombre y apellido, eliminando los 
espacios del comienzo y el final y colocando la primer letra en mayúscula
'''
# nombre = " pepe   "
# apellido =  "    pangosta "

# def corregir_nombre_apellido(cadena_uno : str, cadena_dos : str)-> dict:
#     '''
#     elimina los espacios del comienzo y el final y coloca la primer letra en
#     mayúscula
#     recibe dos cadenas
#     devuelve un dict
#     '''
#     nuevo_dicc = {}
#     nombre_corregido = cadena_uno.strip()
#     apellido_corregido = cadena_dos.strip()
#     nombre_corregido = nombre_corregido.capitalize()
#     apellido_corregido = apellido_corregido.capitalize()
#     nuevo_dicc["nombre"] = nombre_corregido
#     nuevo_dicc["apellido"] = apellido_corregido

#     return(nuevo_dicc)

# print(corregir_nombre_apellido(nombre, apellido))


'''
9-Escribir una función que tome una lista de nombres y los una en una sola 
cadena separada por un salto de línea, por ejemplo: 
["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".

'''
# lista_de_nombres = ["Pedro", "Mar", "Lilia"]
# separador = "\n"
# def convertir_de_lista_a_cadena(lista : list, separador)-> str:
#     '''
#     toma una lista de cadenas y las  separada por un salto de línea
#     recibe una lista, y el caracter separador
#     devuelve una cadena
#     '''
#     if(separador != ","):
#         cadena = separador.join(lista)
#     else:
#          cadena = separador.join(lista)+ ".."
#     return cadena

# print(convertir_de_lista_a_cadena(lista_de_nombres, separador))

'''
10- Escribir una función que tome un nombre y un apellido y 
devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".

'''
# nombre = "Pepe"
# apellido = "Mangosta"

# def creador_mail(cadena_uno :str,cadena_dos : str )-> str:
#     '''
#     crea un mail 
#     recibe dos cadenas nombre y apellido
#     devuelve un nuevo mail
#     '''
#     mail_base = "inicial_nombre.apellido@utn-fra.com.ar"
#     mail_nuevo = mail_base.replace("nombre", cadena_uno).replace(
#         "apellido", cadena_dos)
#     return mail_nuevo

# print(creador_mail(nombre, apellido))


'''
11- Escribir una función que tome una lista de palabras y devuelva un string 
que contenga todas las palabras concatenadas con comas y "y" antes de la última 
palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], 
el string resultante debería ser "manzanas, naranjas y bananas"..
'''
# lista_de_nombres = ["Pedro", "Mar", "Lilia"]
# separador = ","

# def convertir_de_lista_a_cadena(lista : list, separador)-> str:
#     '''
#     toma una lista de cadenas y las  separada por un separador
#     recibe una lista
#     devuelve una cadena
#     '''
#     if(separador != ","):
#         cadena = separador.join(lista)
#     else:
#          cadena = separador.join(lista)+ ".."
#     return cadena

# print(convertir_de_lista_a_cadena(lista_de_nombres, separador))

'''
12- Escribir una función que tome un número de tarjeta de crédito como 
input, verificar que todos los caracteres sean numéricos y devolver los 
últimos cuatro dígitos y los primeros dígitos como asteriscos, por 
ejemplo: "**** **** **** 1234". 

'''

numero_card = "1111 4444 5555 1234"

def verificar_tarjeta(numero_str : str)-> str:
    numero_card = eliminar_espacios(numero_str)
    str_card = []
    if(numero_card.isalnum()):
        for i in range(12):
           numero_card.replace(numero_card[i], "*")
           print(numero_card)

        


verificar_tarjeta(numero_card)