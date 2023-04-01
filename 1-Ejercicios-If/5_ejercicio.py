'''
5- Escribir un programa que le pida al usuario que ingrese su nombre,
y luego imprima "Hola [nombre]" si el nombre ingresado es "Juan", "María" 
o "Pedro", o "Hola desconocido" si el nombre ingresado no es uno de esos tres .
'''

nombre_ingresado = input("Ingrese nombre")

if(nombre_ingresado == "Juan" or nombre_ingresado == "Maria" 
or nombre_ingresado == "Pedro"):
    print("Hola {0}".format(nombre_ingresado))# forma de concatenar 
else:
    print("Hola desconocido")








# Es una aberracion concatenar con + aca!!!
# nombre_ingresado = input("Ingrese un nombre")

# if(nombre_ingresado != "Juan" and nombre_ingresado != "Maria" 
#    and nombre_ingresado != "Pedro"):
#     print("Hola desconocido")
# else:
#     print("Hola " + nombre_ingresado)