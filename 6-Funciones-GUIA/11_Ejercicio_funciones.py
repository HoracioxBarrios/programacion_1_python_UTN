'''
11- Crea una función que reciba como parámetro una cadena de 
texto y devuelva la cantidad de vocales que tiene.
'''
palabra_ingresada = input("Ingrese una palabra")

def contador_de_vocales(palabra):
    '''
    cuenta las vocales de una palabra
    recibe una caden de texto
    devuelve las cantidad de vocales que tiene.
    '''
    contador = 0
    for letra in palabra:
        if (letra in "aeiouAEIOU"):
            contador += 1
    return contador

cantidad_vocales = contador_de_vocales(palabra_ingresada)
print("La palabra ingresada es: {0} y la cantidad de vocales es:{1}".format(
    palabra_ingresada, cantidad_vocales ))