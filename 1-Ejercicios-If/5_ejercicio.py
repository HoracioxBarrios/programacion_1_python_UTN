'''
5- Escribir un programa que le pida al usuario que ingrese su nombre,
 y luego imprima "Hola [nombre]" si el nombre ingresado es "Juan", "María" 
 o "Pedro", o "Hola desconocido" si el nombre ingresado no es uno de esos tres.
'''
nombre_ingresado = input("Ingrese un nombre")

if(nombre_ingresado != "Juan" and nombre_ingresado != "Maria" 
   and nombre_ingresado != "Pedro"):
    print("Hola desconocido")
else:
    print("Hola " + nombre_ingresado)