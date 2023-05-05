'''
7- Crear una función que calcule el máximo común divisor 
de dos números. Recibe dos parámetros (números) y devuelve 
el máximo común divisor.

'''
numero_uno_str = input("Ingrese un numero") 
numero_uno_int = int(numero_uno_str) # 24

numero_dos_str = input("Ingrese otro numero")
numero_dos_int = int(numero_dos_str) # 36

def euclides_maximo_comun_divisor(numero_a, numero_b):
    '''
    Calcula el Maximo comun divisor entre dos numeros.
    Recibe dos numeros por arg.
    devuelve el MCD
    '''
    while(numero_b != 0):
        numero_temporal = numero_b # 36 /// 24 /// 12 
        numero_b = numero_a % numero_b # 24 % 36 = 24 /// 36 % 24 = 12 ///  24 % 12 = 0 :  el MCD es 12
        numero_a = numero_temporal # 36 ///24 ///  
    return numero_a




numero_comun_divisor = euclides_maximo_comun_divisor(
    numero_uno_int, numero_dos_int)

print("El maximo comun divisor entre {0} y {1} es: {2}".format(
    numero_uno_int, numero_dos_int, numero_comun_divisor))

















# # Definimos los dos números para calcular el MCD
# num1 = 24
# num2 = 36

# # Definimos una función para calcular el MCD utilizando el algoritmo de Euclides
# def euclides(num1, num2):
#     while num2 != 0:
#         temp = num2
#         num2 = num1 % num2
#         num1 = temp
#     return num1

# # Llamamos a la función para calcular el MCD de los dos números
# mcd = euclides(num1, num2)

# # Imprimimos el resultado
# print("El MCD de", num1, "y", num2, "es:", mcd)

