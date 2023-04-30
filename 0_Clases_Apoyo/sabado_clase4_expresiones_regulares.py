import re




#https://www.onlinegdb.com/xXNKzNoHe
#https://docs.python.org/3/library/re.html?highlight=regul
'''
1.Verificar correo electrónico: Crea una función que tome una cadena de 
texto como argumento y verifique si se trata de una dirección de correo 
electrónico válida.  Una dirección de correo electrónico válida debe 
tener un formato como "usuario@dominio.com".
'''
''''
[a-zA-Z0-9._%+-]      +@   [a-zA-Z0-9.-]   +\. [a-zA-Z]{2,}
usuario                @   dominio          .     com
1er grupo               2do grupo                 3er grupo
  

'''


def validar_correo(correo):
    patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    coincidencias = re.findall(patron, correo)
    if len(coincidencias) == 1 and coincidencias[0] == correo:
        return True
    else:
        return False

print(validar_correo('usuario@dominio.com'))  # devuelve True
print(validar_correo('usuario1@dominio-1.com'))  # devuelve True
print(validar_correo('usuario@dominio.co.uk'))  # devuelve True
print(validar_correo('usuario@dominio'))  # devuelve False
print(validar_correo('usuario@dominio.'))  # devuelve False
print(validar_correo('usuario@dominio..com'))  # devuelve False


'''
2.Eliminar dígitos: Crea una función que tome una cadena de texto y 
elimine todos los dígitos que contiene.
'''
def eliminar_digitos():
    pass
'''
3.Validar formato de fecha: Crea una función que tome una cadena de 
texto como argumento y verifique si se trata de una fecha válida en 
formato "dd/mm/aaaa".
'''






'''
4.Reemplazar formato de fecha: Crea una función que tome una cadena 
de texto que contiene una fecha en formato "dd/mm/aaaa" y  la reemplace 
por la misma fecha en formato "mm/dd/aaaa".

'''




'''
5.Validar número de teléfono: Escribe una expresión regular que valide 
un número de teléfono con el siguiente formato: "+54 9 11 1234-5678". La expresión 
regular debe aceptar números de teléfono con el código de país "+54", seguido de 
un espacio, el dígito 9, otro espacio, el código de área de dos dígitos, un 
espacio, el número de teléfono de ocho dígitos separado por un guión en la mitad.

'''





'''

6.Validar CUIL: Escribe una expresión regular que valide un CUIL con el s
iguiente formato: "20-12345678-1". La expresión regular debe aceptar CUILS 
que comiencen con "20" seguido de un guión, ocho dígitos y otro guión, 
seguido del último dígito que es un verificador.


'''