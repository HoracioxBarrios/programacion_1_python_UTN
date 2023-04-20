'''
10- Crea una lista de palabras y muestra las palabras que 
tienen más de 5 letras.
'''

lista_de_palabras = ["libro", "paracaidas", "computadora", "lapiz", "sol"]

for palabra in lista_de_palabras:
    if(len(palabra) > 5):
        print(palabra)