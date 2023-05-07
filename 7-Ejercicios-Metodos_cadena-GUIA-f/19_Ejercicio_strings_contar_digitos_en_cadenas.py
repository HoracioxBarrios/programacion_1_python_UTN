'''
19.Escribir una función que tome una cadena de caracteres y 
cuente la cantidad de dígitos que contiene, por 
ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.
'''
cadena = "1234 Hola Mundo" 
def contar_digitos_en_cadenas(cadena_de_caracteres : str)-> int:
    '''
    En una cadena si hay un digito(un numero) lo cuenta
    recibe una cadena
    devuelve 
    '''
    contador_de_digitos = 0
    for caracter in cadena_de_caracteres:
        if(caracter.isdigit()):
            contador_de_digitos += 1
    if(contador_de_digitos > 0):
        return contador_de_digitos
    else:
        return "No hay digitos en la cadena"

print(contar_digitos_en_cadenas(cadena))