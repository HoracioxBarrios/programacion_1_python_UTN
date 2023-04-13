'''
8- Crea un diccionario que represente las edades de varias personas,
donde las claves son los nombres de las personas y los valores son 
sus edades. Imprime la edad de la persona más joven.

'''
dicc_personas = {"Cristian" : 20, "Lili" : 25, "Gustav" : 24}
flag_edad = True

for nombre, edad in dicc_personas.items(): # usar el metodo .items() par obtener clave y valor
    if(flag_edad):# minimo
        edad_min = edad
        nombre_min = nombre
        flag_edad = False
    else:
        if(edad < edad_min):
            edad_min = edad
            nombre_min = nombre
            

print("El mas joven es: {0} con {1} años".format(
    nombre,edad))

'''Al iterar sobre un diccionario en Python, debes 
utilizar el método .items() para obtener tanto la clave como el valor.'''