'''
10.Escribir una función que tome un nombre y un apellido y devuelva un email en
formato "inicial_nombre.apellido@utn-fra.com.ar".
'''
nombre = "Pepe"
apellido = "Stiercol"

def generar_direccion_correo(nombre :str, apellido : str)-> str:
    '''
    genera una nueva direccion de correo electronico
    recibe un nombre y un apellido
    devuelve la nueva direccion de  correo electronico
    '''
    formato_mail = "inicial_nombre.apellido@utn-fra.com.ar"
    
    nuevo_mail_nombre_agregado = formato_mail.replace("nombre", nombre)
    nuevo_mail_nombre_y_apellido_Agregado = nuevo_mail_nombre_agregado.replace(
        "apellido", apellido)
    print(nuevo_mail_nombre_y_apellido_Agregado)

generar_direccion_correo(nombre, apellido)
    