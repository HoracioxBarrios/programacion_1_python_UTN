'''
●Métodos de manipulación de cadenas: hay varios métodos 
que se pueden usar para manipular los strings en Python. 
Algunos de ellos son 
upper()
lower()

strip()      # El método strip() se utiliza para eliminar los caracteres 
de espacio en blanco al principio y al final de una cadena de texto. 
No los intermedios


split()     # El metodo split() divide una cadena de texto en una lista de 
subcadenas, utilizando un separador especificado como argumento.


join()       #El método join() se utiliza para unir elementos de una lista 
en una cadena de texto con un separador específico.


replace()    #El  método  replace  remplazará  un  conjunto  de 
caracteres por otro.
'''
# isdigit() digitos: Los números del 0 al 9 pero de tipo str
# si le paso un int o float a isdigit() nos da error (AttributeError)
'''
Los números del 0 al 9: "0", "1", "2", "3", "4", "5", "6", "7", "8", "9".
Los dígitos numéricos Unicode que representan números en otros sistemas 
numéricos, como por ejemplo los caracteres árabes, chinos, japoneses, 
coreanos, entre otros.
Cualquier otro carácter que no sea un dígito numérico no será considerado 
como tal por la función isdigit(). Por ejemplo, las letras, los signos de 
puntuación, los espacios en blanco y los caracteres especiales no son 
dígitos numéricos.
'''

#isalnum()   alfanumerico:  letras y numeros
'''
Los números del 0 al 9: "0", "1", "2", "3", "4", "5", "6", "7", "8", "9".
Las letras del alfabeto inglés, tanto en mayúsculas como en minúsculas: 
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", 
"C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
"Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z".
Los dígitos y letras Unicode que representan números y letras en otros 
alfabetos, como por ejemplo los caracteres árabes, chinos, japoneses, 
coreanos, entre otros.
Cualquier otro carácter que no sea un número o una letra no será 
considerado alfanumérico por la función isalnum(). Por ejemplo, los 
signos de puntuación, los espacios en blanco y los caracteres especiales 
no son alfanuméricos.
'''

#isalpha()  solo letras

'''
Las letras del alfabeto inglés, tanto en mayúsculas como en minúsculas: 
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", 
"C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
"Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z".
Las letras Unicode en otros alfabetos, como por ejemplo los caracteres 
árabes, chinos, japoneses, coreanos, entre otros.
Cualquier otro carácter que no sea una letra no será considerado 
como tal por la función isalpha(). Por ejemplo, los números, los 
signos de puntuación, los espacios en blanco y los caracteres especiales 
no son letras.
'''