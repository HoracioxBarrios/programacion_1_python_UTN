''' Metodo search() retorna un objeto match si encuentra 
al menos una ocurrencia o None si no.'''

import re

texto = " uno 1 dos 2 tres 3 cuatro"

print(re.search(" ", texto)) #<re.Match object; span=(0, 1), match=' '>

''' separado por los numeros '''
print(re.search("[0-9]+", texto))#<re.Match object; span=(5, 6), match='1'>   

''' separado por las letras '''
print(re.search("[a-z]+",texto))#<re.Match object; span=(1, 4), match='uno'>

''' La función re.search() es una función del módulo re de Python que 
se utiliza para encontrar la primera ocurrencia de un patrón en 
una cadena. 

A diferencia de re.match(), re.search() busca la 
coincidencia en toda la cadena, no solo al principio....'''