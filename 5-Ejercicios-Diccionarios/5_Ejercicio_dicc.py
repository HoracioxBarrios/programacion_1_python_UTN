'''
5- Crea un diccionario que represente los continentes, donde 
las claves son los nombres de los continentes y los valores 
son los números correspondientes (por ejemplo, {"América": 1, 
"Europa": 2, ...}). Imprime el valor correspondiente al continente 
"África".

'''
dicc_continentes = {"America" : 1, "Europa" : 2,"Asia": 3,
                    "Africa" : 4, "Oceania" : 5, "Antartida": 6 }


print(dicc_continentes["Africa"])

# print("El valor que le corresponde a {0} es {1}".format(
#     "Africa", dicc_continentes["Africa"]))







'''Cantidad de continentes al 2023
¿Cuántos continentes hay en el mundo?
Para cercar algo más el asunto de cuántos continentes hay en el mundo, 
se puede dar como respuestas más certeras seis (Asia, África, América, 
Europa, Oceanía y Antártida)

o siete (Asia, África, América del Norte, 
América del Sur, Antártida, Europa y Oceanía)




#Otros condideran 7
En la actualidad, "convencionalmente hay 7 continentes. Pero en esos 7
está incluido Europa, que en realidad es una península del continente 
asiático, el mayor del mundo. "Entonces están Asia, África, América del 
Norte, América del Sur, Antártida, Europa, Oceanía"
'''

#Ejemplo de mostrar el nombre de la key: 
'''
Para mostrar el nombre de una clave (key) de un diccionario en Python 3,
simplemente se debe acceder a la clave y luego imprimir su nombre. 
Por ejemplo:

diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Bogotá"}

print("La clave es:", "nombre")

'''

#Si se quiere imprimir el valor

'''
diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Bogotá"}

print("El valor es: {0}".format(diccionario["nombre"]))
'''