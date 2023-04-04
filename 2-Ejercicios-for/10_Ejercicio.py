'''
10-Dada una lista de palabras,imprimir las palabras que comienzan y 
terminan con la misma letra.
'''
lista_de_palabras = ["argentina", "correo", "lionel", "pepe","ojo"]

for palabra in lista_de_palabras:
    if palabra[0] == palabra[-1]:# el indice 0 es el primer elemento, el indice -1 se refuere al ultimo elemento
        print(palabra)


#ver si esta bien

