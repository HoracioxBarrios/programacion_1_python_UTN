'''
15.Crea un diccionario que contenga el nombre y el sueldo de 
varios empleados.Luego, permite al usuario aumentar el sueldo 
de un empleado y actualizar el valor correspondiente en el 
diccionario

'''
diccionario_empleados = {"Carlos" : 100000, "Rulo" : 85000, "Eli" : 50000}

empleado_buscado = input("Ingrese nombre del Empleado").capitalize()

nuevo_sueldo_str = input("Ingrese nuevo Sueldo")
nuevo_sueldo_int = int(nuevo_sueldo_str)
for clave in diccionario_empleados.keys():
    if(clave == empleado_buscado):
        diccionario_empleados[clave] = nuevo_sueldo_int

print(diccionario_empleados)