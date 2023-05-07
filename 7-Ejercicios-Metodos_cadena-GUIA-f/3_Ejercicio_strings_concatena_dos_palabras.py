'''
3. Escribir una función que tome dos strings y devuelva un 
nuevo string que contenga ambos strings concatenados, separados 
por un espacio.
'''


primera_palabra = "buenos"
segunda_palabra = "dias"

def concatenar_palabras(palabra_a :str, palabra_b :str)-> str:
    '''
    concatena dos palabras con un espacio entre ellos.
    recibe dos cadenas por parametro.
    devuelve una cadena
    '''
    return " ".join([palabra_a, palabra_b]) #join() espera una lista, por eso puse los parametros juntos encerrados en []
   



print(concatenar_palabras(primera_palabra, segunda_palabra))