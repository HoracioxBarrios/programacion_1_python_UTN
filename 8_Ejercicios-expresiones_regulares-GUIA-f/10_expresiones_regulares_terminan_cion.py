import re
'''
10.Crear una función que reciba un texto y devuelva una lista de todas las
palabras que terminan con "ción".
'''

texto = "La tecnología de la información ha revolucionado la comunicación en todas sus formas. La digitalización y la automatización de procesos han permitido la optimización de los recursos y la mejora en la eficiencia de los sistemas. La cibernética, la robótica y la inteligencia artificial son algunas de las áreas de la informática que se han desarrollado en las últimas décadas y han transformado la forma en que vivimos y trabajamos. La interconexión de dispositivos y la transmisión de datos en tiempo real han permitido la creación de nuevas industrias y modelos de negocio que antes eran impensables. La educación, la salud, el transporte y la logística son algunos de los sectores que han sido beneficiados por la innovación tecnológica. En conclusión, la tecnología ha generado una revolución en nuestra sociedad que ha llevado a la transformación y evolución de la misma."



def encontrar_palabras_cion(texto):
    '''
    de una cadena busca y lista todas las que terminan en cion
    recibe una cadena
    devuelve una lista de palabras
    '''
    palabras_cion = re.findall(r'[a-zA-ZáéíóúñÁÉÍÓÚÑ]+ción\b', texto)
    return palabras_cion

print(encontrar_palabras_cion(texto))

'''
En general, \b es el símbolo más comúnmente utilizado para buscar una 
frontera de palabra en una expresión regular y se considera la forma 
más precisa y confiable de hacerlo.
'''