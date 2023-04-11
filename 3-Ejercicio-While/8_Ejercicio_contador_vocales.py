''' 8- Dada una cadena de texto,  imprimir la cantidad de vocales en la cadena.'''


cadena_str = "Hola"
indice = 0
contador_vocales = 0

while(indice < len(cadena_str)):
    if(cadena_str[indice] == "a" or cadena_str[indice] == "e"
    or cadena_str[indice] == "i" or cadena_str[indice] == "o"
    or cadena_str[indice] == "u" or cadena_str[indice] == "A" 
    or cadena_str[indice] == "E"or cadena_str[indice] == "I" 
    or cadena_str[indice] == "O"or cadena_str[indice] == "U" ):
        contador_vocales = contador_vocales + 1
    indice += 1

print("La cantidad de vocales {0}".format(contador_vocales))













# Indice = 0
# contador_vocales = 0

# texto = input("INgrese una palabra")

# while (Indice < len(texto)):
#     letra = texto[Indice]
    
#     if(letra == "a" or letra == "e" or letra == "i"
#     or letra == "o" or letra == "u" or letra == "A"
#     or letra == "E" or letra == "I" or letra == "O"
#     or letra == "U"):
#         contador_vocales += 1

#     Indice +=1

# print("cantidad de vocales: {0}".format(contador_vocales))


#ver

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
