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
    "fuerza": "35",
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

def obtener_nombre(heroe : dict)-> str:
    '''
    obtiene nombre de un dicc
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
palabra = "Programacion"


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
    '''
    imprime los nombres de heroes
    recibe una lista de diccionarios
    devuelve en caso de error -1
    '''
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
clave_a_calcular = "fuerza"

def obtener_nombre_y_dato(diccionario_heroe :dict, clave_buscada : str)-> str:
    '''
    obtiene nombre de heroe y dato
    recibe un diccionario, y una clave ejemplo: "altura", "fuerza", "peso"
    devuelve una cadena
    '''
    for clave in diccionario_heroe.keys():
        if clave == clave_buscada:
            return "{0} | {1} : {2}".format(
                diccionario_heroe["nombre"], clave, diccionario_heroe[clave])


# nombre__dato_buscado = obtener_nombre_y_dato(heroe, clave_buscada)
# print(nombre__dato_buscado)

'''
3. Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por
parámetro la lista de héroes, la cual deberá iterar e imprimir sus nombres y
alturas USANDO la función creada en el punto 2. Validar que la lista de héroes
no esté vacía para realizar sus acciones, caso contrario no hará nada y
retornara -1.
'''

def stark_imprimir_nombres_alturas(lista_heroes : list[dict]):
    '''
    imprime nombres y alturas de los heroes
    recibe una list[dict] de heroes
    retorna -1 en caso de error
    '''
    if(lista_heroes):
        clave_buscada = "altura"
        for dicc_heroe in lista_heroes:
            print(obtener_nombre_y_dato(dicc_heroe, clave_buscada))
    else:
        return -1

# stark_imprimir_nombres_alturas(lista_personajes)

'''
4.1. Crear la función 'calcular_max' la cual recibirá por parámetro la lista de
héroes y una key (string) la cual representará el dato que deberá ser evaluado
a efectos de determinar cuál es el máximo de la lista. Por ejemplo la función
deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
que tenga el dato más alto.
Ejemplo de llamada:
calcular_max(lista,'edad')
'''
clave_a_calcular="fuerza"

def calcular_max(lista_heroes :list[dict], clave_buscada : str)-> dict:
    '''
    calcula el maximo de una lista de heroes segun clave
    recibe una list[dict] y una clave, por ejemplo clave_buscada = "altura"
    devuelve el maximo
    '''
    lista_heroes_normalizada = stark_normalizar_datos(lista_heroes)
    for indice in range(len(lista_heroes_normalizada)):
        if(indice == 0 or 
           lista_heroes_normalizada[indice][clave_buscada] >
           lista_heroes_normalizada[max_indice][clave_buscada]):
            
            max_indice = indice
    return lista_heroes_normalizada[max_indice]
            
    
# heroe_maximo = calcular_max(lista_personajes, clave_buscada)
# print(heroe_maximo)


'''
4.2. Crear la función 'calcular_min' la cual recibirá por parámetro la lista de
héroes y una key (string) la cual representará el dato que deberá ser evaluado
a efectos de determinar cuál es el mínimo de la lista. Por ejemplo la función
deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
que tenga el dato más bajo.
correspondientes
Ejemplo de llamada:
calcular_min(lista,'edad')
'''
clave_a_calcular="fuerza"

def calcular_min(lista_heroes :list[dict], clave_buscada : str)-> dict:
    '''
    calcula el minimo de una lista de heroes segun clave
    recibe una list[dict] y una clave, por ejemplo clave_buscada = "altura"
    devuelve el maximo
    '''
    lista_heroes_normalizada = stark_normalizar_datos(lista_heroes)
    for indice in range(len(lista_heroes_normalizada)):
        if(indice == 0 or 
           lista_heroes_normalizada[indice][clave_buscada] <
           lista_heroes_normalizada[mim_indice][clave_buscada]):
            
            mim_indice = indice
    return lista_heroes_normalizada[mim_indice]
            
    
# heroe_minimo = calcular_min(lista_personajes, clave_buscada)
# print(heroe_minimo)


'''
4.3. Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros:
●La lista de héroes
●El tipo de cálculo a realizar: es un valor string que puede tomar los
valores maximo o minimo
●Un string que representa la key del dato a calcular, por ejemplo: altura,
peso, edad, etc.
La función deberá retornar el héroe que cumpla con la condición pedida.
Reutilizar las funciones hechas en los puntos 4.1 y 4.2
Ejemplo de llamada:
calcular_max_min_dato(lista,"maximo","edad")
'''
tipo_de_calculo = "minimo" # o "maximo"
clave_a_calcular = "altura"  # o "fuerza", "peso"

def calcular_max_min_dato(
    lista_heroes :list[dict], tipo_de_calculo : str,clave_buscada :str )-> dict:
    if(tipo_de_calculo == "maximo"):
        return calcular_max(lista_heroes, clave_buscada)
    elif(tipo_de_calculo == "minimo"):
        return calcular_min(lista_heroes, clave_buscada)
    else:
        return "Error :Ingrese clave 'maximo' o 'minimo'"

# resultado_max_o_min_por_clave = calcular_max_min_dato(
#     lista_personajes, tipo_de_calculo, clave_buscada)

# print(resultado_max_o_min_por_clave)


'''
4.4. Crear la función 'stark_calcular_imprimir_heroe' la cual recibirá tres
parámetros:
●La lista de héroes
●El tipo de cálculo a realizar: es un valor string que puede tomar los
valores maximo o minimo
●Un string que representa la key del dato a calcular, por ejemplo: altura,
peso, edad, etc.
Con este se resuelve el Ej3, Ej4, Ej6 y Ej7 del desafío #00
La función deberá obtener el héroe que cumpla dichas condiciones, imprimir
su nombre y el valor calculado. Reutilizar las funciones de los puntos:
punto 1.2, punto: 2 y punto 4.3
Validar que la lista de héroes no esté vacía para realizar sus acciones, caso
contrario no hará nada y retornara -1.
Ejemplo de llamada:
stark_calcular_imprimir_heroe(lista,"maximo","edad")
Ejemplo de salida:
Mayoraltura:Nombre:HowardtheDuck|altura:79.34
correspondientes
'''
tipo_de_calculo = "maximo"
clave_a_calcular = "altura"

def stark_calcular_imprimir_heroe(
    lista_heroes :list[dict], tipo_de_calculo : str, clave_buscada : str):
    '''
    de una List[dict] el héroe que cumpla dichas condiciones, 
    imprime su nombre y el valor calculado.
    recibe una lista de dicc heroes list[dict]
    devuelve -1 en caso de error
    '''
    if(lista_heroes):
        heroe_dicc_max_o_min= calcular_max_min_dato(
            lista_heroes, tipo_de_calculo,clave_buscada)#4.3
    
        nombre_y_dato = obtener_nombre_y_dato(
            heroe_dicc_max_o_min, clave_buscada)#2
    
        print_dato("Mayor {0} Nombre {1}".format(clave_buscada, nombre_y_dato))#1.2
    else:
        return -1
    
# stark_calcular_imprimir_heroe(lista_personajes, tipo_de_calculo, clave_buscada)

'''
5.1. Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una
lista de héroes y un string que representara el dato/key de los héroes que se
requiere sumar. Validar que cada héroe sea tipo diccionario y que no sea un
diccionario vacío antes de hacer la suma. La función deberá retorna la suma
de todos los datos según la key pasada por parámetro
'''
clave_a_calcular = "altura"

#normalizo los datos de la lista dentro de esta funcion
def sumar_dato_heroe(lista_heroes : list[dict], clave_a_calcular : str):
    '''
    de una list[dicc] acumula(suma) segun clave
    recibe una lista de dicc heroes
    retorna la suma de lo buscado - si la lista esta vacia da -1
    '''
    if(lista_heroes):
        lista_heroes_normalizada = stark_normalizar_datos(lista_heroes)
        acumulador_de_dato = 0
        for dicc_heroe in lista_heroes_normalizada:
            if (clave_a_calcular in dicc_heroe and 
                bool(dicc_heroe) and type(dicc_heroe) is dict):
                
                acumulador_de_dato += dicc_heroe[clave_a_calcular]
        return acumulador_de_dato
                
    else:
        return -1

# print(sumar_dato_heroe(lista_personajes, clave_a_calcular))

'''
5.2. Crear la función dividir la cual recibirá como parámetro dos números
(dividendo y divisor). Se debe verificar si el divisor es 0, en caso de serlo,
retornar 0, caso contrario realizar la división entre los parámetros y retornar el
resultado
'''
ejemplo_dividendo = "30"
ejemplo_divisor = 2

def dividir(dividendo, divisor )-> float:
    '''
    realiza la division entre dos numeros
    recibe un dividendo Int o Float, y un divisor int o float
    devuelve el resultado (float) o en caso de error 0
    '''
    if divisor != 0 and isinstance(dividendo, (int, float)) and isinstance(divisor, (int, float)):
        return dividendo / divisor
    else:
        return 0

# print(dividir(ejemplo_dividendo, ejemplo_divisor))


#Nota: no sirve esta validacion: if(divisor != 0 and type[dividendo] is not str or type[divisor] is not str):     ya que si entra un str vuelva todo,
#isinstance() comprueba en este caso si el valor es una instancia de la clase Int o la clase Float

'''
5.3. Crear la función calcular_promedio la cual recibirá como parámetro una
lista de héroes y un string que representa el dato del héroe que se requiere
calcular el promedio. La función debe retornar el promedio del dato pasado
por parámetro
'''
clave_a_calcular = "altura"

#uso la funcion normalizar datos, en la funcion sumar_dato_heroe
def calcular_promedio(
    lista_heroes : list[dict], clave_a_calcular : str)-> float:
    '''
    calcula el promedio total segun necesidad en base a una lista de heroes
    recibe una lista de dicc heroes y una clave a calcular (ej: clave = "altura")
    devuelve el promedio
    '''
    resultado_acumulado = sumar_dato_heroe(lista_heroes, clave_a_calcular)
    cantidad_de_heroes = len(lista_heroes)
    promedio = dividir(resultado_acumulado, cantidad_de_heroes)
    return promedio

# resultado_promedio = calcular_promedio(lista_personajes, clave_a_calcular)
# print(resultado_promedio)

'''
5.4. Crear la función 'stark_calcular_imprimir_promedio_altura' la cual recibirá
una lista de héroes y utilizando la función del punto 5.3 calcula y mostrará la
altura promedio. Validar que la lista de héroes no esté vacía para realizar sus
acciones, caso contrario no hará nada y retornara -1.
IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y
5.3
Con este se resuelve el Ej 5 del desafío #00
'''

def stark_calcular_imprimir_promedio_altura(lista_heroes : list[dict]):
    '''
    calcula el promedio total de alturas de los heroes  y lo muestra.
    recibe una lista de heroes
    devuelve el resultado y en caso de error -1
    
    '''
    if(lista_heroes):
        clave_a_calcular = "altura"
        resultado_promedio = calcular_promedio(lista_heroes, clave_a_calcular) #5.3 incluye al 5.1
        return resultado_promedio
    else:
        return -1

# print_dato(stark_calcular_imprimir_promedio_altura(lista_personajes)) #1.2

'''
6.1. Crear la función "imprimir_menu" que imprima el menú de opciones por
pantalla, el cual permite utilizar toda la funcionalidad ya programada. Se
deberá reutilizar la función antes creada encargada de imprimir un string (1.2)
'''
def imprimir_menu():
    lista_menu = ["Opciones:", "Mostrar el nombre de los superheroes", 
                  "Mostrar el nombre y la altura de cada superheore", 
                  "Mostrar el superheroe mas alto", 
                  "Mostrar la altura promedio del total de superheroes",
                  "Mostrar superheroe mas alto", "Mostrar superheroe mas bajo", 
                  "Mostrar el superheroe mas pesado", "Mostrar el superheroe menos pesado",
                  "Salir"]
    for indice in range(len(lista_menu)):
        menu = menu = '\n\n1{0}\n2- .\n3- .\n4- .\n5- .\n6-  \n7- .\n8- . \n9- .\n10-salir \ningrese la opcion deseada: '
        print_dato(menu)

# imprimir_menu()

'''
6.2.Crear la función “validar_entero” la cual recibirá por parámetro un string de
número el cual deberá verificar que sea sea un string conformado únicamente
por dígitos. Retornara True en caso de serlo, False caso contrario
'''
numero = "15"
# numero = "1.5"
# numero = "15abc"
def validar_entero(numero_str: str) -> bool:
    numero_str.isdigit()
    numero_int = int(numero_str)
    return numero_int


# print(validar_entero(numero))


'''
6.3. Crear la función 'stark_menu_principal' la cual se encargará de imprimir el
menú de opciones y le pedirá al usuario que ingrese el número de una de las
opciones elegidas y deberá validarlo. En caso de ser correcto dicho número,
lo retornara casteado a entero, caso contrario retorna -1. Reutilizar las
funciones del ejercicio 6.1 y 6.2
'''
def stark_menu_principal():
    pass



