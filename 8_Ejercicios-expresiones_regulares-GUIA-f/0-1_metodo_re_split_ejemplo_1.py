 #                       metodo split()
'''
Retorna una lista con las ocurrencias, se le tiene que pasar un separador. 
es parecido al split() de strings, pero el re.split() es mas potente al 
soportar rangos en lugar de un solo separador
'''
import re
 
texto = "uno 1 dos 2 tres 3 cuatro"
''' separado por espacio '''
print(re.split(" ", texto)) #['', 'uno', '1', 'dos', '2', 'tres', '3', 'cuatro']

''' separado por los numeros '''
print(re.split("[0-9]+", texto))#[' uno ', ' dos ', ' tres ', ' cuatro']

''' separado por las letras '''
print(re.split("[a-z]+",texto))#[' ', ' 1 ', ' 2 ', ' 3 ', '']

# ver abajo porque los espacios en la lista

'''La letra "r" que se coloca antes de una cadena de texto en Python 
se utiliza para indicar que la cadena es una expresión regular cruda 
("raw", en inglés)'''

texto = " uno 1 dos 2 tres 3 cuatro"
''' separado por espacio '''
print(re.split(r" ", texto)) #['', 'uno', '1', 'dos', '2', 'tres', '3', 'cuatro']

''' separado por los numeros '''
print(re.split(r"[0-9]+", texto))#[' uno ', ' dos ', ' tres ', ' cuatro']

''' separado por las letras '''
print(re.split(r"[a-z]+",texto))#[' ', ' 1 ', ' 2 ', ' 3 ', '']

'''
En el ejemplo que proporcionas, parece que la cadena de texto tiene espacios 
antes y después de cada número. Por lo tanto, cada número se divide en dos 
partes: una cadena vacía antes del espacio y otra cadena vacía después del 
espacio.


Si quieres eliminar estos espacios en blanco de la lista resultante, puedes 
utilizar el método strip()
'''
 
