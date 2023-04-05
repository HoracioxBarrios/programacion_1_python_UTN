'''Estructura de control while: permite ejecutar una seccion de codigo, 
mientras la condicion se cumpla (TRUE), y deja de iterar cuando la 
la condicion no se cumpla (FALSE)'''

#Ej 1
# respuesta = "s"

# while (respuesta == "s"):
#     respuesta = input("Desea continuar? (s/n)")

#---------------------------------------------------------

'''2-Dado un número entero n, imprimir todos los números desde 1 
hasta n en orden ascendente.'''
# numero_ingresado_str = input("Ingrese un numero")
# #validar
# numero_ingresado_int = int(numero_ingresado_str)
# contador = 0

# while(contador < numero_ingresado_int):
#     contador = contador + 1
#     print(contador)

'''version prof. davila'''
numero_ingresado_str = input("Ingrese un numero")
#validar
numero_ingresado_int = int(numero_ingresado_str)
contador = 1# inicia en 1 a diferencia

while(contador <= numero_ingresado_int):# se agrega igual a diferencia
    print(contador)
    contador = contador + 1# contador al final 
