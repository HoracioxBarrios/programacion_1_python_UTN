'''
19.Crea un diccionario que represente las temperaturas de una ciudad durante
una semana, donde las claves son los días de la semana y los valores son las
temperaturas correspondientes. Calcula la temperatura promedio de la
semana.

'''
dicc_temperaturas = {
    "lunes": 25, "martes": 28, "miércoles": 31, "jueves": 29, 
    "viernes": 26, "sábado": 24, "domingo": 23}
cantidad_de_dias = len(dicc_temperaturas)
acum_temperaturas = 0
for valor_temp in dicc_temperaturas.values():
    acum_temperaturas += valor_temp

promedio_de_temperatura = acum_temperaturas / cantidad_de_dias
promedio_redondeado = round(promedio_de_temperatura, 2)

print(
    "El promedio de temperaturas de la semana es {0}".format(promedio_redondeado))












'''
en python 3 como muestro solo 2 decimales de un numero flotante?

ChatGPT
Puedes utilizar la función round() para redondear un número flotante a 
un número específico de decimales. Para mostrar solo 2 decimales, 
puedes pasar el número flotante y el número 2 como argumentos de la 
función round(). Luego, puedes imprimir el resultado utilizando la 
función print().

Aquí tienes un ejemplo:

python
Copy code
num = 3.14159265359
num_redondeado = round(num, 2)
print(num_redondeado)
'''
