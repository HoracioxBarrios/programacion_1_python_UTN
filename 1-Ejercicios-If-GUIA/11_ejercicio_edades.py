'''
11- Escribir un programa que le pida al usuario que ingrese su edad,
y luego imprima "Eres un niño" si la edad es menor a 12, "Eres un 
adolescente" si la edad está entre 12 y 17 inclusive, "Eres un adulto" 
si la edad está entre 18 y 64 .

'''

edad_ingresada_str = input("Ingrese edad")
edad_ingresada_int = int(edad_ingresada_str)

if(edad_ingresada_int < 12 and edad_ingresada_int > 0):
    print("eres niño")
elif(edad_ingresada_int > 11 and edad_ingresada_int < 18):
    print("eres adolecente")
elif(edad_ingresada_int > 17 and edad_ingresada_int < 65):
    print("eres adulto")
else:
    print("edad fuera de rango")

# se tiene en cuenta los datos invalidos osea 64+ ?




