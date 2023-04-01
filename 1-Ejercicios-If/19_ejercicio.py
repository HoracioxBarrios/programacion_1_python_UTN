'''
19- Escribir un programa que le pida al usuario que ingrese su edad,
y luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18, 
"Eres adolescente" si la edad está entre 13 y 17 inclusive, o 
"Eres menor de edad" si la edad es menor que 13.

'''

edad_ingresada_string = input("Ingrese edad")
edad_ingresada_integer = int(edad_ingresada_string)

if(edad_ingresada_integer >= 18):
    print("Eres mayor de edad")
elif(edad_ingresada_integer < 13):
    print("Eres menor de edad")
else:
    print("Eres adolecente")