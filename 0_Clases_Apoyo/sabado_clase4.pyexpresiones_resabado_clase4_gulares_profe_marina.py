import re 



ingreso = input("Ingrese una edad: ")  #string str

if re.match('[0-9]{2}',ingreso):
    edad = int(ingreso)
    print(f"Le edad es: {edad}")
else:
    print("no es un numero lo ingresado")
'''
"""
    "Marina"
    "3434"
    ()  ---
    []  ---> CONJUNTO  [aeiou] [a-z] [0-9]
    {4} --->cuantas veces

    +
    ^
    $

    \d ---> todos los digitos
    \w ---> alfa numerico
    \s ---> todos los separadores
"""
'''

texto = "hola . mundo .. cruel"

print(re.split(' \.{2} ',texto)) #['hola . mundo', 'cruel']
print(re.split(' \.+ ',texto)) # ['hola', 'mundo', 'cruel']
print(re.split(' \.{1,2} ',texto)) #['hola', 'mundo', 'cruel']

name = "Marina anabella Cardozo"
print(re.sub('[0-9]','*',name))

texto = 'Chola 1234' #primera letra mayus  hola 4 4 digitos

print(re.match('([a-zA-Z]+) ([0-9]{4})',texto))

'''
if re.match('(^[A-Z][a-z]{4}) ([0-9]{4})',texto):
    print("se cumple")
else:
    print("no se cumple")
'''


saludo = "¡Holasssss! ¿como estas?"

print(re.match('¡[A-Za-z]+!',saludo))

fecha = "hoy es 2023/04/09 y son las 10:04:00, 12:04:00"

print(re.findall('[0-9]{4}',fecha))
print(re.findall('/[0-9]{2}/',fecha))
print(re.findall('[0-9]{4}/[0-9]{2}/[0-9]{2}',fecha))
print(re.findall('[0-9]{2}:[0-9]{2}:[0-9]{2}',fecha))







#continuar codigo 
