'''
14- Dada una cadena de texto, imprimir la cantidad de veces que aparece una
letra específica en la cadena
'''

cadena_de_texto = "El Salvador"
indice = 0
letra = "a"
contador_letra_especifica = 0
while(indice < len(cadena_de_texto)):
    if(cadena_de_texto[indice] == letra):
        contador_letra_especifica += 1
    indice += 1
print(contador_letra_especifica)