'''https://www.onlinegdb.com/qXnIYatNa
/*
3) Copa pistón!!!
Se deberá generar un programa para registrar las estadísticas de los 10 
integrantes de una carrera de autos.
Se pedirá el ingreso de:
nombre
edad (mayor a 18)
nacionalidad del piloto (argentino, inglés, francés, brasilero, estadounidense)
cantidad de carreras ganadas (no pueden ser números negativos)
número del vehículo (no puede ser un número negativo)

se necesita saber:
1*Nacionalidad del piloto más joven.
2*Cantidad de vehículos con número par.
3*Nombre del piloto con menos victorias y el número de auto impar.
4*Cantidad de pilotos mayores de 25 años con número de vehículo impar.
5*Nombre del piloto más joven con más victorias.
6*Nacionalidad del piloto más veterano con menos victorias.
7*Promedio de edad de los pilotos que tiene un vehículo con número par.
*/
'''
contador_integrantes = 0
flag_mas_joven_mas_veterano = True
flag_impar = True
contador_vehiculos_par = 0
contador_vehiculos_impar = 0
contador_pilotos_mayores_a_veinticinco_impar = 0
acumulador_edad_par = 0


while (contador_integrantes < 1):  # pido datos de 10 participantes
    nombre_ingresado = input("Ingrese nombre")
    
    edad_ingresada_str = input("Ingrese edad")
    edad_ingresada_int = int(edad_ingresada_str)
    while (edad_ingresada_int <= 0 or edad_ingresada_int < 18):
        edad_ingresada_str = input(
            "Edad incorrecta! Ingrese edad mayor a 18 años")
        edad_ingresada_int = int(edad_ingresada_str)

    nacionalidad_piloto = input("Ingrese nacionalidad")
    while (nacionalidad_piloto != "argentino" and nacionalidad_piloto != "ingles"
        and nacionalidad_piloto != "frances" and nacionalidad_piloto != "brasilero"
        and nacionalidad_piloto != "estadounidense"):
        nacionalidad_piloto = input(
            "Nacionalidad incorrecta! Ingrese nacionalidad valida")

    cantidad_carreras_ganadas_str = input(
        "Ingrese cantidad de carreras ganadas")
    cantidad_carreras_ganadas_int = int(cantidad_carreras_ganadas_str)
    while (cantidad_carreras_ganadas_int < 0):
        cantidad_carreras_ganadas_str = input(
            "Valor incorrecto! Ingrese cantidad de carreras ganadas")
        cantidad_carreras_ganadas_int = int(cantidad_carreras_ganadas_str)

    numero_del_vehiculo_str = input("Ingrese numero del vehiculo")
    numero_del_vehiculo_int = int(numero_del_vehiculo_str)
    while (numero_del_vehiculo_int < 0):
        numero_del_vehiculo_str = input(
            "Valor Incorrecto! Ingrese numero del vehiculo")
        numero_del_vehiculo_int = int(numero_del_vehiculo_str)

    contador_integrantes += 1

    if (flag_mas_joven_mas_veterano):  # 1 *Nacionalidad del piloto más joven.
        edad_mas_joven = edad_ingresada_int
        nacionalidad_piloto_mas_joven = nacionalidad_piloto
        nombre_mas_joven_mas_victorias = nombre_ingresado
        maxima_cantidad_victorias_mas_joven = cantidad_carreras_ganadas_int

        edad_mas_veterano = edad_ingresada_int
        nombre_mas_veterano_ = nombre_ingresado
        nacionalidad_del_mas_veterano = nacionalidad_piloto
        minima_cantidad_victorias_mas_veterano = cantidad_carreras_ganadas_int
        flag_mas_joven_mas_veterano = False
    else:
        if (edad_ingresada_int < edad_mas_joven):
            nacionalidad_piloto_mas_joven = nacionalidad_piloto

        if (cantidad_carreras_ganadas_int > maxima_cantidad_victorias_mas_joven  # 5*Nombre del piloto más joven con más victorias.
                and edad_ingresada_int < edad_mas_joven):
            nombre_mas_joven_mas_victorias = nombre_ingresado
            maxima_cantidad_victorias_mas_joven = cantidad_carreras_ganadas_int

        if (cantidad_carreras_ganadas_int < minima_cantidad_victorias_mas_veterano
                and edad_ingresada_int > edad_mas_veterano):  # 6*Nacionalidad del piloto más veterano con menos victorias.
            nacionalidad_del_mas_veterano = nacionalidad_piloto

    if (numero_del_vehiculo_int % 2 != 0):  # impar
        if (flag_impar == True):
            # 3*Nombre del piloto con menos victorias y el número de auto impar.
            menor_cant_ganadas_impar = cantidad_carreras_ganadas_int
            nombre_piloto_menos_vict_impar = nombre_ingresado
            flag_impar = False
        else:
            if (cantidad_carreras_ganadas_int < menor_cant_ganadas_impar):
                menor_cant_ganadas_impar = cantidad_carreras_ganadas_int
                nombre_piloto_menos_vict_impar = nombre_ingresado

        if (edad_ingresada_int > 25):
            # 4*Cantidad de pilotos mayores de 25 años con número de vehículo impar.
            contador_pilotos_mayores_a_veinticinco_impar += 1
        contador_vehiculos_impar += 1
    else:  # sino entonces es par
        # 7*Promedio de edad de los pilotos que tiene un vehículo con número par.
        acumulador_edad_par += edad_ingresada_int
        contador_vehiculos_par += 1  # 2*Cantidad de vehículos con número par.
# fin while


if (contador_vehiculos_par > 0):
    promedio_edad_par = acumulador_edad_par / contador_vehiculos_par
    
        # 2*Cantidad de vehículos con número par.
    print("cantidad de vehiculos con numero par: {0}".format(
    contador_vehiculos_par))
    
    # 7*Promedio de edad de los pilotos que tiene un vehículo con número par.
    print("El promedio de edad de los pilotos que tiene un vehículo con número par es: {0}".format(
    promedio_edad_par))

else:
    promedio_edad_par = 0
    
    print("cantidad de vehiculos con numero par: {0}".format(
    contador_vehiculos_par))
    
    print("El promedio de edad de los pilotos que tiene un vehículo con número par es: {0}".format(
    promedio_edad_par))
    
# 1*Nacionalidad del piloto más joven.
print("la nacionalidad del Piloto mas Joven es: {0}".format(
    nacionalidad_piloto_mas_joven))



if(contador_vehiculos_impar > 0): 
    # 3*Nombre del piloto con menos victorias y el número de auto impar.
    print("Nombre del piloto con menos victorias y número de auto impar es: {0}".format(
    nombre_piloto_menos_vict_impar))
    
    # 4*Cantidad de pilotos mayores de 25 años con número de vehículo impar.
    print("Cantidad de pilotos mayores de 25 años y num del vehiculo impar: {0}".format(
    contador_pilotos_mayores_a_veinticinco_impar))
else:
    print("Nombre del piloto con menos victorias y número de auto impar : No hay")
    
    print("Cantidad de pilotos mayores de 25 años y num del vehiculo impar: No hay")


# 5*Nombre del piloto más joven con más victorias.
print("Nombre del piloto más joven con más victorias es: {0}".format(
    nombre_mas_joven_mas_victorias))

# 6*Nacionalidad del piloto más veterano con menos victorias.
print("Nacionalidad del piloto más veterano con menos victorias es: {0}".format(
    nacionalidad_del_mas_veterano))
