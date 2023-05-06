#Ejercicios Regex clase de apoyo
import re
'''
1.Verificar correo electrónico: Crea una función que tome una cadena de 
texto como argumento y verifique si se trata de una dirección de correo 
electrónico válida.  Una dirección de correo electrónico válida debe 
tener un formato como "usuario@dominio.com".
'''
''''
[a-zA-Z0-9._%+-]+    @   [a-zA-Z0-9.-]+   \. [a-zA-Z]{2,}
usuario                @   dominio          .     com
1er grupo               2do grupo                 3er grupo
  

'''
#ejemplo :   "usuario@dominio.com"

correo = 'LordVamp_35@gmail.com'
def verificar_correo(correo : str):
    patron = re.findall('[a-zA-Z0-9_-]+@[a-zA-Z]+\.[a-zA-Z]{2,}', correo)
    if(patron):
        print(patron)
        return "Correo Valido"
    else:
        return "Correo invalido"

# verificar_correo(correo)





# def validar_correo(correo):
#     patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#     coincidencias = re.findall(patron, correo)
#     if len(coincidencias) == 1 and coincidencias[0] == correo:
#         return True
#     else:
#         return False

# print(validar_correo('usuario@dominio.com'))  # devuelve True
# print(validar_correo('usuario1@dominio-1.com'))  # devuelve True
# print(validar_correo('usuario@dominio.co.uk'))  # devuelve True
# print(validar_correo('usuario@dominio'))  # devuelve False
# print(validar_correo('usuario@dominio.'))  # devuelve False
# print(validar_correo('usuario@dominio..com'))  # devuelve False


'''
2.Eliminar dígitos: Crea una función que tome una cadena de texto y 
elimine todos los dígitos que contiene.
'''
palabra = "computadora64"
def eliminar_digitos(palabra):
    nueva_palabra = re.sub("\d", "" ,palabra)
    print(nueva_palabra)

# eliminar_digitos(palabra)
    
'''
3.Validar formato de fecha: Crea una función que tome una cadena de 
texto como argumento y verifique si se trata de una fecha válida en 
formato "dd/mm/aaaa".
'''
fecha_a_verificar = "300/04/2023"
def validar_formato_fecha(fecha : str):
    formato_fecha_valida = re.findall("[0-9]{2}\/[0-9]{2}\/[0-9]{4}",fecha)
    if formato_fecha_valida:
        print(formato_fecha_valida)
    else:
        print("Invalido")    

# validar_formato_fecha(fecha_a_verificar)

'''
4.Reemplazar formato de fecha: Crea una función que tome una cadena 
de texto que contiene una fecha en formato "dd/mm/aaaa" y  la reemplace 
por la misma fecha en formato "mm/dd/aaaa".

'''

fecha_original = "30/04/2023"
def cambiar_formato_fecha(fecha):
    patron = r'(\d{2})/(\d{2})/(\d{4})'
    nueva_fecha = re.sub(patron, r'\2/\1/\3', fecha)
    return nueva_fecha



print(nueva_fecha = cambiar_formato_fecha(fecha_original)) # "04/30/2023"
  



'''
5.Validar número de teléfono: Escribe una expresión regular que valide 
un número de teléfono con el siguiente formato: "+54 9 11 1234-5678". La expresión 
regular debe aceptar números de teléfono con el código de país "+54", seguido de 
un espacio, el dígito 9, otro espacio, el código de área de dos dígitos, un 
espacio, el número de teléfono de ocho dígitos separado por un guión en la mitad.

'''

numero = "+54 9 11 1234-5678"

def validar_telefono(numero):
    patron = r'^\+54 9 [1-9][0-9] [0-9]{4}-[0-9]{4}$'
    es_valido = re.match(patron, numero)
    return es_valido != None



print(es_valido = validar_telefono(numero)) # True
  





'''

6.Validar CUIL: Escribe una expresión regular que valide un CUIL con el s
iguiente formato: "20-12345678-1". La expresión regular debe aceptar CUILS 
que comiencen con "20" seguido de un guión, ocho dígitos y otro guión, 
seguido del último dígito que es un verificador.


'''


cuil = "20-12345678-1"

def validar_cuil(cuil):
    patron = r'^20-\d{8}-\d$'
    es_valido = re.match(patron, cuil)
    return es_valido != None



print(es_valido = validar_cuil(cuil)) # True
  







#https://www.onlinegdb.com/xXNKzNoHe
#https://docs.python.org/3/library/re.html?highlight=regul