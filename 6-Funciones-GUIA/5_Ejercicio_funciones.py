'''
5- Crear una función que determine si un número es primo o no. 
Recibe un parámetro (número) y devuelve True si es primo y 
False si no lo es.
'''
numero_ingresado_str = input("Ingrese un numero")
numero_ingresado_int = int(numero_ingresado_str)

def es_primo(numero : int)-> bool:
    '''
    determina si un numero es primo
    recibe un numero int
    devuelve True o False
    '''
    if(numero < 2):
        return False
    contador_de_divisores = 0
    
    for posible_divisor in range(1, numero + 1):
        if(numero % posible_divisor == 0):
            contador_de_divisores += 1
            if contador_de_divisores > 2:
                return False
    return True

numero_evaluado = es_primo(numero_ingresado_int)
print(numero_evaluado)
