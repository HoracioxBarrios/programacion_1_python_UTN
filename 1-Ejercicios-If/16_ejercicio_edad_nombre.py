'''
16- Escribir un programa que le pida al usuario que ingrese su 
nombre y su edad, y luego imprima "Eres adolescente" si la edad 
está entre 13 y 17 inclusive, "Eres adulto" si la edad está entre 
18 y 64 inclusive, o "Eres adulto mayor" si la edad es mayor o igual a 65 .
'''

nombre_ingresado = input("INgrese nombre")
edad_ingresada_str = input("Ingrese edad")
#casteamos la edad de str a int
edad_ingresada_int = int(edad_ingresada_str)

if(edad_ingresada_int > 12 and edad_ingresada_int < 18):
    print("Eres aolecente")
elif(edad_ingresada_int > 17 and edad_ingresada_int < 65):
    print("Eres adulto")
elif(edad_ingresada_int > 65):
    print("Eres adulto mayor")
else:
    print("Edad invalida o no abordada en el enunciado") # ver si es considerado Ok