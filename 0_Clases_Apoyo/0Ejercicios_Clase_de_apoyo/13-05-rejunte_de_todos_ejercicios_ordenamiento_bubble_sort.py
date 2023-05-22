import copy

'''
1. Crea una función que ordene una lista de números enteros 
de menor a mayor. Puedes utilizar cualquier método de 
ordenamiento que conozcas
'''
lista_de_numeros = [5, 10, 30, 50, 100, 150, 600]

lista_de_numeros_2 = copy.copy(lista_de_numeros)

lista_de_numeros_3 = lista_de_numeros[:]


'''
Hice unas copias para probar las 3 funciones, porque sino me 
estaria ordenando la que ya esta ordenada por que la lista al
tener los mimos valores va y busca en la posicion de memoria
existente. Por lo tanto al crear las copias con esas dos maneras,
libreria copy y slice. con esto me crea dos nuevos 
espacios en memoria para las dos nuevas listas 2 y 3
'''

# bubble sort con indice en decremento
def ordenar_numeros_bubble_sort(lista : list):
    len_de_lista = len(lista) -1
    for indice in range(len_de_lista):
        if(lista[indice] > lista[indice + 1]):
            aux = lista[indice]
            lista[indice] = lista[indice + 1]
            lista[indice + 1] = aux
    print(lista)

# ordenar_numeros_bubble_sort(lista_de_numeros)
# print("id en memoria:{0}".format(id(lista_de_numeros)))



#con flag
def ordenar_numeros_bubble_sort_v2(lista : list):
    flag_swap = True
    while(flag_swap):
        flag_swap = False
    for indice in range(len(lista)-1):
        if(lista[indice] > lista[indice + 1]):
            aux = lista[indice]
            lista[indice] = lista[indice + 1]
            lista[indice + 1] = aux
            flag_swap = True
        
    print(lista)

# ordenar_numeros_bubble_sort_v2(lista_de_numeros_2)
# print("id en memoria:{0}".format(id(lista_de_numeros_2)))

#mas obtimizada combinando las dos de abajo.
def ordenar_numeros_bubble_sort_v3(lista: list):
    len_de_lista = len(lista) -1
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        for indice in range(len_de_lista):
            if(lista[indice] > lista[indice +1]):
                aux_backup_valor = lista[indice]
                lista[indice] = lista[indice +1]
                lista[indice +1] = aux_backup_valor
                flag_swap = True
        len_de_lista -= 1
        print(lista)      
                
ordenar_numeros_bubble_sort_v3(lista_de_numeros_3)
# print("id en memoria:{0}".format(id(lista_de_numeros_3)))


#-----------------------------------------------------------------
'''
2. Crea una función que ordene una lista de cadenas 
alfabéticamente de A a Z.
'''



lista_de_letras = ['B', 'G', 'V', 'S', 'N', 'E', 'X', 'M', 
                   'P', 'F', 'L', 'R', 'Q', 'A', 'T', 'C', 
                   'Z', 'Y', 'K', 'I', 'U', 'D', 'W', 'H', 
                   'O', 'J']

def ordenar_letras_bubble_sort(lista : list):
    len_de_lista = len(lista)-1
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        for indice in range(len_de_lista):
            if(lista[indice] > lista[indice +1]):
                aux = lista[indice]
                lista[indice] = lista[indice +1]
                lista[indice +1] = aux
                flag_swap = True
        len_de_lista -=1
    return lista

# print(ordenar_letras_bubble_sort(lista_de_letras))
#-----------------------------------------------------------------
'''
3. Crea una función que ordene un diccionario de estudiantes por 
calificación de mayor menor.
'''
estudiantes = {
    'Juan': 85,
    'María': 92,
    'Pedro': 78,
    'Laura': 95
}

def ordenar_estudiantes_por_calificacion(dicc_estudiantes : dict):
    
    claves = list(dicc_estudiantes.keys()) #al dicc lo meto dentro de una lista para tomar las claves
    # print(type(claves)) #<class 'list'>
    len_de_diccionario =  len(dicc_estudiantes) -1
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        for indice in range(len_de_diccionario):
            if(dicc_estudiantes[claves[indice]] < dicc_estudiantes[claves[indice +1]]):
                claves[indice], claves[indice +1] = claves[indice +1], claves[indice]
                flag_swap = True
        len_de_diccionario -= 1
        
    #creamos un nuevo dicc y con el for va acomodando clave y valor  en cada iteracion. esto usando comprension de diccionario
    estudiantes_ordenados = {i_clave : dicc_estudiantes[i_clave] for i_clave in claves}
    return estudiantes_ordenados
            
# print(ordenar_estudiantes_por_calificacion(estudiantes))   


'''
Se puede utilizar el método list() para obtener una lista de las claves 
del diccionario y luego acceder al valor correspondiente utilizando 
la indexación.
ejemplo:

diccionario = {'Juan': 85, 'María': 92, 'Pedro': 78, 'Laura': 95}

claves = list(diccionario.keys()) #obtenemos la clave
valor = diccionario[claves[0]]    # ingresando al valor

print(valor)


'''



'''
estudiantes_ordenados = {clave: dicc_estudiantes[clave] for clave in claves}
    return estudiantes_ordenados


Esta línea de código utiliza una expresión de comprensión de diccionario 
para crear un nuevo diccionario llamado estudiantes_ordenados. Permíteme 
explicar cómo funciona paso a paso:

{clave: dicc_estudiantes[clave]}: Esta es la sintaxis básica de una 
comprensión de diccionario. Indica que se va a crear un nuevo diccionario 
donde cada elemento tendrá una clave clave y un valor dicc_estudiantes[clave]. 
Esto se hace para cada clave en la lista claves.

for clave in claves: Esta parte indica que la comprensión de diccionario 
se va a ejecutar para cada clave presente en la lista claves. En cada 
iteración, se asigna el valor correspondiente dicc_estudiantes[clave] a la 
clave clave en el nuevo diccionario.

'''
#-----------------------------------------------------------------
'''
4. Crea una función que ordene una lista de diccionarios con información 
sobre libros (título, autor, año de publicación) por año de publicación 
de menor a mayor.
'''
libros = [
    {
        "título": "Harry Potter y la piedra filosofal",
        "autor": "J.K. Rowling",
        "año": 1997
    },
    {
        "título": "Crepúsculo",
        "autor": "Stephenie Meyer",
        "año": 2005
    },
    {
        "título": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año": 1605
    },
    {
        "título": "Los juegos del hambre",
        "autor": "Suzanne Collins",
        "año": 2008
    },
    {
        "título": "El código Da Vinci",
        "autor": "Dan Brown",
        "año": 2003
}]

def ordenar_libros_por_clave(
    lista_de_libros : list[dict], clave_buscada : str)-> list[dict]:
    len_de_lista = len(lista_de_libros)-1
    flag_swap = True
    
    while(flag_swap):
        flag_swap = False
        for indice in range(len_de_lista):
            if(lista_de_libros[indice][clave_buscada] > 
               lista_de_libros[indice +1 ][clave_buscada]):
                aux_valor = lista_de_libros[indice]
                lista_de_libros[indice] = lista_de_libros[indice +1]
                lista_de_libros[indice +1] = aux_valor
                flag_swap = True
        len_de_lista -= 1
    return lista_de_libros




# lista_de_libros_ordenada = ordenar_libros_por_clave(libros, clave_buscada= "título")
# print(lista_de_libros_ordenada)


# lista_de_libros_ordenada = ordenar_libros_por_clave(libros, clave_buscada= "autor")
# print(lista_de_libros_ordenada)


lista_de_libros_ordenada = ordenar_libros_por_clave(libros, clave_buscada= "año")
print(lista_de_libros_ordenada)

#-----------------------------------------------------------------

'''
5. Crea una función que ordene un diccionario que mapee nombres de 
frutas a su precio por kilogramo de menor a mayor.
'''
diccionario_frutas = {
    "manzana": 2.5,
    "banana": 3.0,
    "naranja": 2.0,
    "uva": 4.5,
    "mango": 5.0
}


def ordenar_frutas_por_precio_kilo(diccionario_de_frutas : dict)-> dict:
    
    claves = list(diccionario_de_frutas.keys()) # importante obtener las keys
    len_de_dccionario = len(diccionario_de_frutas)-1
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        for indice in range(len_de_dccionario):
            if(diccionario_de_frutas[claves[indice]] > diccionario_de_frutas[claves[indice +1]]):
                claves[indice], claves[indice + 1] = claves[indice + 1] , claves[indice]
                flag_swap = True
        len_de_dccionario -= 1
        
    #creamos un nuevo dicc y con el for va acomodando clave y valor  en cada iteracion. esto usando comprension de diccionario
    diccionario_ordenado_frutas = {i_clave : diccionario_de_frutas[i_clave] for i_clave in claves} 
    return diccionario_ordenado_frutas




# frutas_ordenadas = ordenar_frutas_por_precio_kilo(diccionario_frutas)
# print(frutas_ordenadas)





'''
comprension de diccionario es uno de los temas que vienen.

'''

#-----------------------------------------------------------------

'''
6. Crea una función que ordene una lista de tuplas (nombre, edad, 
altura) primero por edad de menor a mayor y luego por altura 
de menor a mayor.
'''
lista_tuplas = [("Juan", 25, 170),
                ("María", 30, 165),
                ("Pedro", 40, 180),
                ("Ana", 35, 160),
                ("Luis", 28, 175)]

# con lista no hay drama

def ordenar_lista_de_tupas(
    lista_tupla : list[tuple], dato_a_ordenar = "altura", orientacion ="min_a_max")-> list[tuple]:
    '''
    Ordena una lista de tuplas segun dato a ordenar
    Recibe:(arg 1) una lista de tuplas, (arg2 ) el dato a ordenar("altura" o "edad"),
    (arg3) la orientacion (por defecto de "min_a_max") o cambiar a "max_a_min".
    Devuelve: una lista, de tuplas ordenada.
    
    '''
    if(lista_tupla):
        
        len_lista = len(lista_tupla) -1
        flag_swap = True
    
        while(flag_swap):
            flag_swap = False
            for indice in range(len_lista):
                if(dato_a_ordenar == "edad"):
                    valor_actual = lista_tupla[indice +1][1]
                    valor_siguiente = lista_tupla[indice][1]
                elif(dato_a_ordenar == "altura"):
                    valor_actual = lista_tupla[indice +1][2]# cambia el indice de la tupla
                    valor_siguiente = lista_tupla[indice][2]
                
                if(orientacion == "min_a_max" and valor_actual < valor_siguiente):
                    lista_tuplas[indice], lista_tuplas[indice + 1] = lista_tuplas[indice + 1], lista_tuplas[indice]# cambio las posiciones entre las tuplas
                    flag_swap = True
                elif(orientacion == "max_a_min" and valor_actual > valor_siguiente):
                    lista_tuplas[indice], lista_tuplas[indice + 1] = lista_tuplas[indice + 1], lista_tuplas[indice]# cambio las posiciones entre las tuplas
                    flag_swap = True
            len_lista -= 1
        return lista_tupla
                
    else:
        return "La lista esta vacia"
    
# lista_tupla_ordenada = ordenar_lista_de_tupas(lista_tuplas)
# print(lista_tupla_ordenada)

'''
la idea es cambiar de lugar entre las tuplas, para evaluar nos guardamos los valores 
en las variables
'''







