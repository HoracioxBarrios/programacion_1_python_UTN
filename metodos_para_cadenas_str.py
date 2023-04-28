# isdigit(), verifica que sea un numero str
'''La función isdigit() devuelve True si todos los caracteres 
en la cadena son dígitos y hay al menos un carácter, de lo contrario,
 devuelve False.'''
 
dato = "1234.5"
if dato.isdigit():
    dato_int = int(dato)
    dato_float = float(dato)
    print("El dato como entero:", dato_int)
    print("El dato como número decimal:", dato_float)
else:
    print("El dato no es un número.")






#isdecimal() 
'''isdecimal() es un método de cadenas en Python que permite verificar 
si una cadena representa un número decimal válido. Retorna True si todos 
los caracteres en la cadena son dígitos decimales (0-9) y False si la 
cadena contiene algún otro carácter, como letras, signos de puntuación 
o espacios en blanco.'''
# cadena1 = "1234"    # contiene solo dígitos decimales
# cadena2 = "12.34"   # no es un número decimal válido

# if cadena1.isdecimal():
#     print("cadena1 es un número decimal válido")
# else:
#     print("cadena1 no es un número decimal válido")

# if cadena2.isdecimal():
#     print("cadena2 es un número decimal válido")
# else:
#     print("cadena2 no es un número decimal válido")

