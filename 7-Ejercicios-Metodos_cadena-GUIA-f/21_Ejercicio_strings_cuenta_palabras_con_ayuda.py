'''
21.Crear una función que reciba como parámetro un string y 
devuelva un diccionario donde cada clave es una palabra y 
cada valor es un entero que indica cuántas veces aparece 
esa palabra dentro del string.
'''
palabras = "Quisiera saber si es posible aprobar si esto con 10"
def contar_palabras(texto):
    # Convertir todo el texto a minúsculas para evitar errores de distinción entre mayúsculas y minúsculas
    texto = texto.lower()
    
    # Separar el texto en palabras individuales
    palabras = texto.split()
    
    # Crear un diccionario vacío para almacenar el recuento de cada palabra
    recuento_palabras = {}
    
    # Recorrer cada palabra en la lista de palabras
    for palabra in palabras:
        # Si la palabra ya está en el diccionario, incrementar su contador
        if palabra in recuento_palabras:
            recuento_palabras[palabra] += 1
        # Si no, agregarla al diccionario con un contador inicial de 1
        else:
            recuento_palabras[palabra] = 1
    
    # Devolver el diccionario resultante
    return recuento_palabras

print(contar_palabras(palabras))
