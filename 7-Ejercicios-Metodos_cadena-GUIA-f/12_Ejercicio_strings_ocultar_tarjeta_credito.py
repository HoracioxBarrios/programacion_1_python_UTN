'''
12.Escribir una función que tome un número de tarjeta de crédito 
como input, verificar que todos los caracteres sean numéricos y 
devolver los últimos cuatro dígitos y los primeros dígitos como 
asteriscos, por ejemplo: "**** **** **** 1234"
'''

numero_de_tarjeta = "1111 3333 8888 9999"

def ocultar_tarjeta(numero_str :str)-> str:
    '''
    oculta los numeros de una tarjeta de credito a excecion de los ultimos
    4
    recibe 16 digitos separados de 4 en 4 por espacio
    devuelve los numeros ocultos a exceccion de los 4 ultimos
    '''
    
    numero_str = numero_str.replace(" ", "") # Elimina los espacios en blanco de la cadena
    if not numero_str.isdigit(): # Verifica si todos los caracteres son numéricos
        return "El número de tarjeta ingresado no es válido"
    # Si es válido, oculta los primeros dígitos con asteriscos
    numero_oculto = "**** **** **** {0}".format(numero_str[-4:]) #Solo nos interresa los ultimos 4 (-1 sera el ultimo digito, -2 el anteultimo, y asi de atras pra adelante)
    return numero_oculto


print(ocultar_tarjeta(numero_de_tarjeta))