'''
Ejercicio con Menú de Opciones 
Realizar un programa utilizando los conceptos de la clase: 
Opciones del menú: 

# 1 Cargar una lista con 10 nombres de animales (perro, gato, león, etc,) 
y de que tipo son (terrestre, anfibio, volador). 

# 2 Imprimir la lista completa de animales con su tipo. 

# 3 Mostrar el porcentaje de animales por tipo. 

# 4 Mayor cantidad de animales por tipo. 

# 5 Menor cantidad de animales por tipo. 

# 6 Pedir un animal e informar si está en la lista y sus datos correspondientes 
si efectivamente está en la lista. 

# 7 Pedir un animal e informar la primer ocurrencia de ese animal en la lista si es que existe. 

# 8 Vaciar la lista. 
# 9 Informar la cantidad de animales por cada tipo de animal. 
# 10 Salir.

'''
lista_de_animales = [
    {"animal": "leon", "tipo": "terrestre"},
    {"animal": "tortuga", "tipo": "terrestre"},
    {"animal": "ballena", "tipo": "acuatico"},
    {"animal": "delfin", "tipo": "acuatico"},
    {"animal": "rana", "tipo": "anfibio"},
    {"animal": "aguila", "tipo": "volador"},
    {"animal": "tigre", "tipo": "terrestre"},
    {"animal": "gato", "tipo": "terrestre"},
    {"animal": "perro", "tipo": "terrestre"},
    {"animal": "paloma", "tipo": "volador"},]


clave_nombre = "animal"
clave_tipo = "tipo"
cantidad_a_ingresar = 2

''' Funcion para agregar a la lista, me hice una lista harcodeada para prueba'''
# def agregar_a_lista(
#         cantidad :int,clave_nombre : str, clave_tipo : str)-> list[dict]:
#     ''' 
#     toma nombres y tipos de animal por input y crea una lista de dicc animales.
#     recibe cantidad a ingresar.
#     devuelve una lista de dicc
#     '''
#     lista = []
#     contador = cantidad
#     while(contador > 0):
#         nombre_ingresado = input("Ingrese {0} ".format(clave_nombre))
#         tipo_ingresado = input("Ingrese tipo de {0} ".format(clave_tipo))

#         nuevo_dicc_animal = {}
#         if(nombre_ingresado not in nuevo_dicc_animal):
#             nuevo_dicc_animal[clave_nombre] = nombre_ingresado
#             nuevo_dicc_animal[clave_tipo] = tipo_ingresado
#             lista.append(nuevo_dicc_animal)
#         contador -= 1
#     return lista



def separar_contar_por_tipo(lista : list)-> dict:
    '''
    separa por tipo y los contabiliza
    recibe una list de dict
    retorna - una lista de dict con los tipos y cantidades correspondientes
    '''
    nuevo_dicc_contador = {}
    for animal in lista:
        nueva_clave = animal[clave_tipo]
        if (animal[clave_tipo] in nuevo_dicc_contador):
            nuevo_dicc_contador[nueva_clave] += 1
        else:
            nuevo_dicc_contador[nueva_clave] = 1
    return nuevo_dicc_contador




def max_min(diccionario : dict, maximo = False, minimo = False)-> dict:
    '''
    busca el maximo, el minimo, o ambos
    recibe tres parametros: arg(1) diccionario, arg(2)(maximo = true) 
    por defecto da maximo. arg(3)(minimo = False) por defecto No da el minimo
    devuelve un diccionario
    '''
    flag_max = True
    flag_min = True
    nuevo_dicc = {}
    for clave, valor in diccionario.items():
        if(flag_max or valor > max_valor and maximo == True):
            max_valor = valor
            max_clave = clave
            flag_max = False
        if(flag_min or valor < min_valor and minimo == True):
            min_valor = valor
            min_clave = clave
            flag_min = False
    
    if(maximo == True):
        nuevo_dicc["max"] = [max_clave, max_valor]
    if(minimo == True):
        nuevo_dicc["min"] = [min_clave,min_valor]
    return nuevo_dicc




def sumar_elem_dic(diccionario : dict)-> dict:
    '''
    acumula valores (los suma)
    recibe un diccionario
    retorna un nuevo diccionario con la suma acumalada
    '''
    acumulador = 0
    for valor in diccionario.values():
        acumulador += valor
    return acumulador

def mostrar_porcentaje(diccionario : dict)-> None:
    '''
    muestra los porcentajes
    recibe un diccionario
    retorna - no plica
    '''
    valor_total = sumar_elem_dic(diccionario)

    for clave, valor in diccionario.items():
        porcentaje = (valor *100) / valor_total
        print("Tipo de animal: {0} porcentaje {1}".format(clave, porcentaje))

        

def print_Lista_anim(lista : list)-> None:
    '''
    imprime una lista de animales
    recibe una lista de dicc
    retorna - no aplica
    '''
    for elem in lista:
        print("nombre del animal: {0} y su tipo: {1}".format(
            elem[clave_nombre], elem[clave_tipo]))


def print_diccionario_anim(diccionario : dict) -> None: 
    '''
    muestra por consola, un dicc
    recibe un diccionario
    devuelve - no aplica
    '''
    for clave, valor in diccionario.items():
        print("{0}  {1}".format(clave, valor))    


def buscar(lista : list,palabra_a_buscar :str, clave_busqueda : str):
    '''
    busca en una lista el elemento segun palabra buscada y key
    recibe una arg(1)lista, arg(2)un str :palabra a buscar y arg(3)una clave str
    retorna el resultado, o -1 en caso de no encontrarse.
    '''
    aux_existe = -1
    for elem in lista:
         if(palabra_a_buscar == elem[clave_busqueda]):
             aux_existe = elem
    return aux_existe

     


while (True):
    respuesta_str = input(
        "Elija una opcion:\n 1-Ingreser animal\n 2-ver lista completa\n 3-ver porcentaje por tipo\n 4-Mayor cantidad de animales por tipo\n 5-Menor cantidad de animales por tipo \n 6-Buscar informacion\n 7-Buscar si existe\n 8-vaciar lista\n 9-cantidad Animales por tipo\n 10-Salir\n")
    respuesta_int = int(respuesta_str)
    match(respuesta_int):
        case 1:
            lista_de_animales = agregar_a_lista(
                    cantidad_a_ingresar, clave_nombre , clave_tipo)
        case 2:
            print_Lista_anim(lista_de_animales)
        case 3:
            lista_separada_por_tipo_y_cant = separar_contar_por_tipo(lista_de_animales)
            mostrar_porcentaje(lista_separada_por_tipo_y_cant)
        case 4:
            lista_separada_por_tipo_y_cant = separar_contar_por_tipo(lista_de_animales)
            maximo_a_mostrar = max_min(lista_separada_por_tipo_y_cant, maximo=True)
            print(maximo_a_mostrar)
        case 5:
            lista_separada_por_tipo_y_cant = separar_contar_por_tipo(lista_de_animales)
            minimo_amostrar = max_min(lista_separada_por_tipo_y_cant, minimo=True)
            print(minimo_amostrar)
        case 6:
            animal_a_buscar = input("Ingrese un animal, para ver si esta en la lista\n")
            resultado_busqueda = buscar(
                lista_de_animales,animal_a_buscar,clave_busqueda="animal")
            if(resultado_busqueda != -1):
                print(resultado_busqueda)
            else:
                print("No existe")
        case 7:
            pass
        case 8:
            lista_de_animales.clear()
            print(lista_de_animales)
        case 9:
            print_Lista_anim(lista_de_animales)
        case 10:
            break
    input("Enter para continuar ")
        
