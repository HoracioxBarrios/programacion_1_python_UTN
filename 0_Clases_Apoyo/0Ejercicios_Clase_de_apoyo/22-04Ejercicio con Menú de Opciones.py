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

# 6 Pedir un animal e informar si está en la lista y sus datos correspondientes si efectivamente está en la lista. 

# 7 Pedir un animal e informar la primer ocurrencia de ese animal en la lista si es que existe. 

# 8 Vaciar la lista. 
# 9 Informar la cantidad de animales por cada tipo de animal. 
# 10 Salir.

'''
# lista_de_animales = [
#     {"animal": "leon", "tipo": "terrestre"},
#     {"animal": "tortuga", "tipo": "terrestre"},
#     {"animal": "ballena", "tipo": "acuatico"},
#     {"animal": "delfin", "tipo": "acuatico"},
#     {"animal": "rana", "tipo": "anfibio"},
#     {"animal": "aguila", "tipo": "volador"},
#     {"animal": "tigre", "tipo": "terrestre"},
#     {"animal": "gato", "tipo": "terrestre"},
#     {"animal": "perro", "tipo": "terrestre"},
#     {"animal": "paloma", "tipo": "volador"},]

cantidad_a_ingresar = 2
lista_de_animales = []
def agregar_a_lista(cantidad :int)-> list[dict]:
    ''' 
    toma nombres y tipos de animal por input y crea una lista de dicc animales.
    recibe cantidad a ingresar.
    devuelve una lista de dicc
    '''
    lista = []
    contador = cantidad
    while(contador > 0):
        nombre = input("Ingrese animal ")
        tipo = input("Ingrese tipo de animal ")
        dicc_animal = {}
        if(nombre not in dicc_animal):
            dicc_animal["animal"] = nombre
            dicc_animal["tipo"] = tipo
            lista.append(dicc_animal)
        contador -= 1
    return lista


def print_animal(lista : list):
    for elem in lista:
        print("Animal: {0} su tipo: {1}".format(elem["animal"], elem["tipo"]))
        
        
        
while (True):
    respuesta_str = input(
        "Elija una opcion:\n 1-Ingreser animal\n 2-ver lista completa\n 3-ver porcentaje por tipo\n 4-Mayor cantidad de animales por tipo\n 5-Menor cantidad de animales por tipo \n 6-Buscar informacion\n 7-Buscar si existe\n 8-vaciar lista\n 9-cantidad Animales por tipo\n 10-Salir\n")
    respuesta_int = int(respuesta_str)
    match(respuesta_int):
        case 1:
                lista_de_animales = agregar_a_lista(cantidad_a_ingresar)
                print_animal(lista_de_animales)
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            break
    input("Enter para continuar ")
        
