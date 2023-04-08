'''13- Dada una lista de palabras, imprimir las palabras que tienen 
una longitud impar.'''

lista_de_palabras = ["Hola", "Saludos", "Chau", "Adios", "Bye"]

for palabra in lista_de_palabras:
    if(len(palabra) % 2 != 0):
        print(palabra)