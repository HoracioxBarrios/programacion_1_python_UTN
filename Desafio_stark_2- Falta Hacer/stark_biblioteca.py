# from data_stark import lista_personajes


lista_personajes =\
[
  {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "F",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  },
  {
    "nombre": "Rocket Raccoon",
    "identidad": "Rocket Raccoon",
    "empresa": "Marvel Comics",
    "altura": "122.77",
    "peso": "25.73",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Brown",
    "fuerza": "5",
    "inteligencia": "average"
  },
  {
    "nombre": "Wolverine",
    "identidad": "Logan",
    "empresa": "Marvel Comics",
    "altura": "160.69999999999999",
    "peso": "135.21000000000001",
    "genero": "F",
    "color_ojos": "Blue",
    "color_pelo": "Black",
    "fuerza": 35,
    "inteligencia": "good"
  }]
#Ejemplo de dicc heroe
heroe = {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "F",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
}
'''
Desafío #02: (con biblioteca propia: stark_biblioteca)
En base a lo resuelto en el desafío #00, deberás mejorar la calidad de tus funciones.
Es por ello que te proponemos lo siguiente:

IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas
escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista,
un string, etc y que contendrá) y que es lo que retorna la función!

0. Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista
de héroes. La función deberá:

● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con
las keys que representan datos numéricos)

● Validar primero que el tipo de dato no sea del tipo al cual será
casteado. Por ejemplo si una key debería ser entero (ejemplo edad)
verificar antes que no se encuentre ya en ese tipo de dato.

● Si al menos un dato fue modificado, la función deberá imprimir como
mensaje ‘Datos normalizados’, caso contrario no imprimirá nada.

● Validar que la lista de héroes no esté vacía para realizar sus acciones,
caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”


'''


def stark_normalizar_datos(heroes: list[dict]) -> list[dict]:
    '''
    normaliza los datos
    recibe una list[dict] personajes
    devuelve una nueva lista de dicc con datos normalizados    
    '''
    result_nueva_lista = []
    if heroes:
        for heroe in heroes:
            keys = list(heroe.keys())
            for key in keys:
                if type(heroe[key]) is str:
                    valor_reemplazado: str = heroe[key].replace('.', '')
                    if valor_reemplazado.isnumeric() and type(heroe[key]) is str:
                        if '.' in heroe[key] and heroe[key].count('.') == 1:
                            heroe[key] = float(heroe[key])
                        else:
                            heroe[key] = int(heroe[key])
                        print(
                            "El dato {0}fue modificado en el heroe {1}".format(key, heroe["nombre"]))
            result_nueva_lista.append(heroe)
        return result_nueva_lista
    else:
        return "La lista esta Vacia"
    
    

# print(stark_normalizar_datos(lista_personajes))


'''
1.1 Crear la función 'obtener_nombre' la cual recibirá por parámetro un
diccionario el cual representara a un héroe y devolverá un string el cual
contenga su nombre formateado de la siguiente manera:
Nombre:Howard theDuck
'''
# heroe = {
#     "nombre": "Rocket Raccoon",
#     "identidad": "Rocket Raccoon",
#     "empresa": "Marvel Comics",
#     "altura": "122.77",
#     "peso": "25.73",
#     "genero": "M",
#     "color_ojos": "Brown",
#     "color_pelo": "Brown",
#     "fuerza": "5",
#     "inteligencia": "average"
# }


def obtener_nombre(heroe : dict):
    '''
    obtiene nombre
    recibe un diccionario
    devuelve una cadena
    '''
    for nombre in heroe:
        if(nombre == "nombre"):
            return "{0} : {1}".format(nombre, heroe[nombre])

# print(obtener_nombre(heroe))

'''
1.2 Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y
deberá imprimirlo en la consola. La función no tendrá retorno.
'''
palabra = "Pelota"


def print_dato(palabra : str):
    '''
    imprime un dato
    recibe una cadena str
    devuelve - no aplica
    '''
    print("{0}".format(palabra))

# print_dato(palabra)

'''
1.3 Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por
parámetro la lista de héroes y deberá imprimirla en la consola. Reutilizar las
funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía
correspondientes
para realizar sus acciones, caso contrario no hará nada y retornara -1.

'''

def stark_imprimir_nombres_heroes(lista_heroes : list[dict]):
    if(lista_heroes):
        for heroe in lista_heroes:
            nombre = obtener_nombre(heroe)# esta funcion recorre el dicc heroe
            print_dato(nombre)# esta funcion Imprime el nombre del heroe
    else:
        return -1
        
# stark_imprimir_nombres_heroes(lista_personajes)


'''
2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un
diccionario el cual representara a un héroe y una key (string) la cual
representará el dato que se desea obtener.
●La función deberá devolver un string el cual contenga el nombre y dato
(key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O
CUALQUIER OTRO DATO.
●El string resultante debe estar formateado de la siguiente manera:
(suponiendo que la key es fuerza)
Nombre:Venom|fuerza:500
'''


def obtener_nombre_y_dato(diccionario_heroe :dict, clave_buscada : str)-> str:
    for clave in diccionario_heroe.keys():
        if clave == clave_buscada:
            return "{0} | {1} : {2}".format(
                diccionario_heroe["nombre"], clave, diccionario_heroe[clave])

nombre__dato_buscado = obtener_nombre_y_dato(heroe,clave_buscada = "altura")
print(nombre__dato_buscado)

'''
3. Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por
parámetro la lista de héroes, la cual deberá iterar e imprimir sus nombres y
alturas USANDO la función creada en el punto 2. Validar que la lista de héroes
no esté vacía para realizar sus acciones, caso contrario no hará nada y
retornara -1.
'''

