'''
14.Escribir una función que tome una URL y devuelva solo el 
nombre de dominio, por ejemplo: 
"https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..

'''
url = "https://www.ejemplo.com.ar/pagina1" 
def tomar_dominio(enlace_url :str)-> str:
    '''
    de una url toma el dominio
    recibe una url :str
    devuelve el dominio :str
    '''
    lista = enlace_url.split(".")
    return lista[1]

print(tomar_dominio(url)) # ejemplo