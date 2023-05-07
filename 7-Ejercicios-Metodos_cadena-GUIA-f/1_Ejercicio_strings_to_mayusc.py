'''
1. Escribir una función que reciba un string y devuelva el mismo 
string todo en mayúsculas

'''
palabra_ejemplo = "pelota"
def convetir_a_mayuscula(palabra :str)-> str:
    '''
    convierte de minuscula a mayuscula
    recibe una cadena -un texto
    devuelve el texto en mayuscula
    '''
    palabra_resultado = palabra.upper()
    return palabra_resultado


print(convetir_a_mayuscula(palabra_ejemplo))