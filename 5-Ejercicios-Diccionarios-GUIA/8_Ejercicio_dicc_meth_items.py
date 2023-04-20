'''
8- Crea un diccionario que represente las edades de varias personas,
donde las claves son los nombres de las personas y los valores son 
sus edades. Imprime la edad de la persona más joven.

'''

dicc_personas = {"Cristian" : 20, "Lili" : 25, "Gustav" : 24, "juli" : 15}
flag_min = True
for edad in dicc_personas.values():
    if(flag_min or edad < edad_min):
        edad_min = edad
        flag_min = False

print("La edad minima es: {0}".format(edad_min))


''''''


'''Al iterar sobre un diccionario en Python, debes 
utilizar el método .items() para obtener tanto la clave como el valor.'''