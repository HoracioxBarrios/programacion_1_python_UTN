'''
20.Escribir una función que tome una lista de direcciones de 
correo electrónico y las una en una sola cadena separada por 
punto y coma, por ejemplo:
["juan@gmail.com", "maria@hotmail.com"] ->
"juan@gmail.com; maria@hotmail.com".

'''
correos = ["juan@gmail.com", "maria@hotmail.com"]

def unir_correos(correos):
    """
    Une una lista de correos electrónicos en una sola 
    cadena separada por punto y coma.
    recibe una lista de correos
    devuelve una cadena con los correos concatenados con "; "
    """
    return "; ".join(correos)# se le pasa la lista y el separador a join()


cadena_unida = unir_correos(correos)
print(cadena_unida)  # imprime "juan@gmail.com; maria@hotmail.com"

