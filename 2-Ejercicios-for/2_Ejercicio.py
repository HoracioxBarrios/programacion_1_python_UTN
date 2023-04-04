''' STRING MAS LARGO
2-Dada una lista de palabras,imprimir la palabra más larga de la lista.
'''
#lista_de_nombres = ["Pepe, Carlos, Osvaldo, Lilia, Ricardiho"] cometi el errpr de no encerrar con doble comillas cada nombre
lista_de_nombres = ["Pepe", "Carlos", "Osvaldo", "Lilia", "Ricardinho"]
nombre_mas_largo = ""

for nombre in lista_de_nombres:
    if len(nombre) > len(nombre_mas_largo):
        nombre_mas_largo = nombre

print(nombre_mas_largo)


#ver







'''ejemplo de chat gtp

lista = ["hola", "bienvenido", "python", "programacion"]

palabra_mas_larga = ""

for palabra in lista:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

print("La palabra más larga de la lista es:", palabra_mas_larga)
'''