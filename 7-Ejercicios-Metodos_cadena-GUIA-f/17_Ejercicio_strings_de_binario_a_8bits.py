'''
17.Escribir una función que tome un número binario y lo 
convierta en una cadena de 8 bits, rellenando con ceros a 
la izquierda si es necesario, por ejemplo:
"101" -> "00000101".

'''
numero_binario_str = "101"

def de_numero_binario_a_ocho_bits(numero_binario: str) -> str:
    '''
    toma un número binario y lo convierte en una cadena de 8 bits
    recibe un numero binario en str
    devuelve un numero de 8 bits en str
    '''
    ocho_bits = numero_binario.zfill(8)
    return ocho_bits


print(de_numero_binario_a_ocho_bits(numero_binario_str))#00000101