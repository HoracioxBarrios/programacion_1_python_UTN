'''
5- Dado un número entero n,  imprimir si el número es primo o no.
'''
numero_ingresado_str = input("Ingrese un numero") #"10"
#validar
numero_ingresado_int = int(numero_ingresado_str) # 10
contador_divisor = 2
flag_es_primo = True

#           2          <         10
while(contador_divisor < numero_ingresado_int):
    #           10                      2       == 0
    if( numero_ingresado_int % contador_divisor == 0):
        flag_es_primo = False
    contador_divisor += 1


if flag_es_primo and numero_ingresado_int > 1:
    print("{0} es un número primo ".format(numero_ingresado_int))
else:
    print("{0} no es un número primo".format(numero_ingresado_int))    


'''
chat gpt4
Para determinar si un número entero n es primo o no,
se puede utilizar un bucle while para comprobar si n 
es divisible por cualquier número entre 2 y n-1. Si n 
es divisible por algún número en ese rango, entonces no
es primo. Si no es divisible por ninguno, entonces es primo.

Aquí está el código en Python:
python Copy code:

n = int(input("Ingrese un número entero: "))
es_primo = True
i = 2

while i < n and es_primo:
    if n % i == 0:
        es_primo = False
    i += 1

if es_primo and n > 1:
    print(n, "es un número primo")
else:
    print(n, "no es un número primo")





'''









# similar al debugger de js
# import pdb
# pdb.set_trace()
# corroborar con el profe

# numero_ingresado_str = input("Ingrese un numero")
# numero_ingresado_int = int(numero_ingresado_str)

# es_numero_primo = True
# iterador_divisor = 2

# while(iterador_divisor < numero_ingresado_int and es_numero_primo):
#     if(numero_ingresado_int % iterador_divisor == 0):
#         es_numero_primo = False
#     iterador_divisor = iterador_divisor + 1

# if(es_numero_primo and numero_ingresado_int > 1):
#     print("Es numero Primo")
# else:
#     print("No es numero Primo")




#ver


