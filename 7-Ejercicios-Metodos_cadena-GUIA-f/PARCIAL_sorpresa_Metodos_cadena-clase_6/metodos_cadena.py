'''
Las  cadenas  en  Python  o  strings  son  un  tipo 
inmutable que permite almacenar secuencias de 
caracteres.  Para crear una, es necesario incluir el 
texto entre comillas. simples o dobles.
'''
#-declaracion

# texto = 'Hola " " Mundo'
# print(texto)       #Hola " " Mundo
# print(type(texto)) #<class 'str'>

'''
Para  incluir  un  salto  de  línea  dentro  de  una 
cadena.
Caracteres especiales 
'''

# texto = 'Hola \n Mundo'
# print(texto)       
# #Hola
# # Mundo

'''               Métodos de string              '''
'''
* El  método  strip() 
El  método  strip  eliminará  todos 
los  caracteres  vacíos  que  pueda  contener  la 
variable
No quita los espacios intermedios
ej: variable_str.strip():  
'''
# variable_str = " Hola Mundo     "
# variable_corregida_str = variable_str.strip()
# print(variable_str)

'''
variable.lower(): El método lower convertirá a las 
letras en minúsculas.
'''
variable_str = "HOLA MUNDO"
variable_corregida = variable_str.lower()
print(variable_corregida)