'''

La función re.match() es una función del módulo re de 
Python que se utiliza para encontrar la primera ocurrencia 
de un patrón en una cadena
'''

import re

cadena = "Hola, ¿cómo estás?"
patron = r"H"

coincidencia = re.match(patron, cadena)

if coincidencia:
    print("Se encontró una coincidencia en la posición", coincidencia.start())
else:
    print("No se encontró ninguna coincidencia")
    

'''
match busca la primera ocurrencia. al principio.

es similar a re.search(que busca en toda la cadena la primera courrencia)
'''
