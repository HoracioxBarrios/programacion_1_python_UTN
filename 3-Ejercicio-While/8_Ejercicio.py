''' 8- Dada una cadena de texto,  imprimir la cantidad de vocales en la cadena.'''

Indice = 0
contador_vocales = 0

texto = input("INgrese una palabra")

while (Indice < len(texto)):
    letra = texto[Indice]
    
    if(letra == "a" or letra == "e" or letra == "i"
    or letra == "o" or letra == "u" or letra == "A"
    or letra == "E" or letra == "I" or letra == "O"
    or letra == "U"):
        contador_vocales += 1

    Indice +=1

print("cantidad de vocales: {0}".format(contador_vocales))


''' chat gpt
cadena = "Hola mundo"
contador = 0
i = 0

while i < len(cadena):
    letra = cadena[i]
    if letra in "aeiouAEIOU":
        contador += 1
    i += 1

print("La cantidad de vocales en la cadena es:", contador)
'''
