''' Sintaxis
[] conjunto de caracteres    ejemplo:    "[a-z]"

\  permite determinar secuencias especiales y escapar caracteres    ejemplo: "\d"

.  hace referencia a cualquier caracter        ejemplo:   "HO.A"

^  "acento circunflexo" hace referemcia a cualquier caracter        ejemplo "^hola"

^  este mismo dentro de un conjunto se usa para negarlo, Por lo tanto, "[^0-9]" 
coincide con cualquier carácter que no sea un número del 0 al 9.

$ termina con          ejemplo "mundo$"

------------------------------ definimos las cantidades
* ninguna o mas ocurrencias              ejemplo "HO.*A" como el punto es cualquier caracter con el * decimos ninguna o o mas courrecias
+ una o mas ocurrencias                  "HO.+A" 
                  
? cero o una ocurrencia         "HO.?A"

----------- o podemos se especificos en las cantidades
{}     especifica el numero de ocurrencias          "HO.{1}A"    =  un caracter cualquiera

----------------


|     or        una o la otra                  "HOLA|CHAU"

() permite seleccionar un grupo 
'''