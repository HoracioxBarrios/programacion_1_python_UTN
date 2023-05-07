'''               slice                 '''
'''
Cuando  se  crea  una slice  (rebanada),  el  primer número es donde 
comienza (inclusivo), y el segundo número de índice es donde termina (exclusivo).
'''
# cadena = "Hola Mundo"
# print(cadena[5:10]) # Mundo
# print(cadena[6:]) # Mundo
# print(cadena[:5]) # Hola





'''               Métodos de string                 '''

'''              El método count()              '''
'''
El método count permite contar las veces que otra cadena se 
encuentra dentro de la primera.
'''
# cadena = "Hola Mundo Hola"
# print(cadena.count("la")) # 2




'''              El  método isalnum()              '''
'''
devuelve  True  si  todos  los caracteres 
son alfanuméricos, False de lo contrario.
el espacio entre otros no se considera alfanumerico
'''

# cadena = "Hola Mundo 123"
# print(cadena.isalnum())# False -> por el espacio
# cadena = "HolaMundo123"
# print(cadena.isalnum())# True



'''              El  método isalpha()              '''
'''
devuelve  True  si  todos  los caracteres son alfabéticos, 
False de lo contrario.
el espacio entre otros no se considera alfanumerico

'''
# cadena = "Hola Mundo"
# print(cadena.isalpha())
# # False -> por el espacio
# cadena = "HolaMundo"
# print(cadena.isalpha())# True


'''              El método join()              '''

'''
devuelve la primera cadena , unida a cada uno de los elementos 
de la 
lista que se le pasa como parámetro.
'''
lista = ["A", "B", "C"]
cadena = " + "
cadena = cadena.join(lista)
print(cadena) # A+B+C


'''              El  método  strip()              '''
''' 
El  método  strip  eliminará  todos 
los  caracteres  vacíos  que  pueda  contener  la variable
No quita los espacios intermedios
ej: variable_str.strip():  
'''
variable_str = " Hola Mundo "
variable_corregida_str = variable_str.strip()
print(variable_str)



'''              El método split()              '''
'''
divide una cadena en subcadenas y las devuelve almacenadas en una lista
le indicas el caracter separador
'''
cadena = "Python,Java,C"
print(cadena.split(","))#['Python', 'Java', 'C']

'''              método replace()              '''
'''
* El  método replace()
remplazará  un  conjunto  de caracteres por otro
'''
# cadena = "Hola Mundo"
# cadena = cadena.replace("la","@")
# print(cadena) # Ho@ Mundo



'''*El método zfill()
rellena la cadena con ceros a la izquierda hasta llegar a 
la longitud pasada como parámetro.
'''
# cadena = "314"
# print(cadena.zfill(6))#000314


'''*El método lower()
convertirá a las letras en minúsculas.
ej: variable_str.lower()
'''
# variable_str = "HOLA MUNDO"
# variable_corregida = variable_str.lower()
# print(variable_corregida)



'''* El método upper()
convierte de minuscula a  mayuscula
ej: variable_str.upper()
'''
# variable_str = "hola mundo"
# variable_corregida = variable_str.upper()
# print(variable_corregida)


'''* El método capitalize()
convertirá a la primera letra de  la  Strings  en  mayúscula  
y  el  resto  en minúscula
ej: variable_str.capitalize()
'''

# variable_str = "hola mundo"
# variable_corregida = variable_str.capitalize()
# print(variable_corregida)



'''              En el método format()              '''

'''
En el método format las llaves, llamadas campos de formato, son 
reemplazadas con los valores de las variables pasadas.
'''
# nombre_usuario="JUAN"
# edad_usuario=35
# cadena = "Nombre: {1}, Edad: {0}"
# print(cadena.format(edad_usuario,nombre_usuario))#Nombre: JUAN, Edad: 35

# print("Nombre: {0}, Edad: {1}".format(nombre_usuario, edad_usuario))#Nombre: JUAN, Edad: 35


'''              f-strings              '''



'''
Las cadenas literales o f-strings, permiten incrustar expresiones dentro de cadenas.
'''
# n_usuario="JUAN"
# e_usuario=35
# cadena = f"Nombre: {n_usuario}, Edad: {e_usuario}"
# print(cadena)#Nombre: JUAN, Edad: 35





'''              El metodo len()              '''

'''
indica la longitud de la cadena de texto dentro de la variable en ese momento.

'''
# cadena = "Hola Mundo"
# print(len(cadena)) # 10




#-------------------------------------------------------------------

# BASICO

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
