''' Findall() retorna una lista con (todo) lo que coincide con el patron'''


import re

texto = " uno 1 dos 2 tres 3 cuatro"

print(re.findall(" ", texto)) #[' ', ' ', ' ', ' ', ' ', ' ', ' ']

''' separado por los numeros '''
print(re.findall("[0-9]+", texto))# ['1', '2', '3']

''' separado por las letras '''
print(re.findall("[a-z]+",texto))#['uno', 'dos', 'tres', 'cuatro']

'''
se utiliza para encontrar todas las ocurrencias de un patrón en una 
cadena y devuelve una lista con todas las coincidencias encontradas.

'''
