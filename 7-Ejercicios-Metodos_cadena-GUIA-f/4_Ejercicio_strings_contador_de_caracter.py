'''
4. Escribir una función que tome un string y devuelva el número de caracteres
que tiene el string.

'''
palabra_a = "escribir"

def len_cadena(palabra : str)-> int:
    '''
    cuenta la cantidad de caracteres
    recibe una palabra
    devuelve el numero de letras
    '''
    return len(palabra)

print(len_cadena(palabra_a))















''' otra manera es usar un contador'''

# palabra_a = "escribir"

# def len_cadena(palabra : str)-> int:
#     contador_caracteres = 0
#     for letra in palabra:
#         contador_caracteres += 1
#     return contador_caracteres

# print(len_cadena(palabra_a))