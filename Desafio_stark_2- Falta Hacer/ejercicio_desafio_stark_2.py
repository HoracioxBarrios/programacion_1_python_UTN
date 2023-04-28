from data_stark import lista_personajes

# lista_personajes = []

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


'''0. Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista
 de héroes. La función deberá:
 
 ● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con
 las keys que representan datos numéricos)
 ● Validar primero que el tipo de dato no sea del tipo al cual será
 casteado. Por ejemplo si una key debería ser entero (ejemplo edad)
 verificar antes que no se encuentre ya en ese tipo de dato.
 ● Si al menos un dato fue modificado, la función deberá imprimir como
 mensaje ‘Datos normalizados’, caso contrario no imprimirá nada.
 ● Validar que la lista de héroes no esté vacía para realizar sus acciones,
 caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía||

'''

def stark_normalizar_datos_1(heroes: list[dict]) -> None:

    if heroes:
        # Recorro cada diccionario de heroe de la lista
        for heroe in heroes:
            key_list = list(heroe.keys())
            # Recorro las claves que me interesan castear
            for key in key_list:
                if type(heroe[key]) is str:
                    valor_reemplazado: str = heroe[key].replace('.', '')
                    if valor_reemplazado.isnumeric() and type(heroe[key]) is str:
                        if '.' in heroe[key] and heroe[key].count('.') == 1:
                            heroe[key] = float(heroe[key])
                        else:
                            heroe[key] = int(heroe[key])
                        print(f'El dato {key} fue modificada para el heroe: {heroe["nombre"]}')
    else:
        print('Error La lista esta vacía.')

# stark_normalizar_datos_1(lista_personajes)

'''
1.1 Crear la función 'obtener_nombre' la cual recibirá por parámetro un
diccionario el cual representara a un héroe y devolverá un string el cual
contenga su nombre formateado de la siguiente manera:
Nombre:Howard theDuck
'''
heroe = {
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
}


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
1.2 Crear la función 'imprimir_dato' la cual recibirá por parámetro|| un string y
deberá imprimirlo en la consola. La función no tendrá retorno.
'''
palabra = "Pelota"
def print_dato(palabra : str):
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
    if (lista_heroes):
        return -1
    else:
        nombre = obtener_nombre(lista_heroes)
        print_dato(nombre)



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
def obtener_nombre_y_dato(heroe : dict, clave):
    nombre_formateado = obtener_nombre(heroe)
    return "{0} | {1} {2} ".format(nombre_formateado.capitalize(), clave.capitalize(), heroe[clave])

print(obtener_nombre_y_dato(heroe, clave ="fuerza"))


