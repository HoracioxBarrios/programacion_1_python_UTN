'''
2. Escribir una función que reciba un string y devuelva el mismo string todo en
minúsculas
'''
palabra_ejemplo = "COMPUTADORA"
def convetir_a_mayuscula(palabra :str)-> str:
    '''
    convierte de mayuscula a minuscula 
    recibe una cadena -un texto
    devuelve el texto en minuscula 
    '''
    palabra_resultado = palabra.lower()
    return palabra_resultado


print(convetir_a_mayuscula(palabra_ejemplo))