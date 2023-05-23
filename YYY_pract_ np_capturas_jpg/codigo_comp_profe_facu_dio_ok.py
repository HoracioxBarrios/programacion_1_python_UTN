
from Menu_biblioteca import *

salida = True
while salida == True:
    
    respuesta_txt = input("\n        Menu: \n1.Cargar lista de animales\n2.Imprimir la lista completa de animales por tipo\n3.Mostrar el porcentaje de animales por tipo\n4.Mayor cantidad de animales por tipo\n5.Menor cantidad de animales por tipo\n6.Verificar si un animal esta en lista\n7.Validar si un animal esta en la lista y muestra posición\n8.Cantidad de animales por cada tipo\n9.Vaciar la lista\n10.Salir\n\n")
    respuesta_int = int(respuesta_txt)


    match(respuesta_int):
        case 1:
            lista_de_animales = []
            # 1 Cargar una lista con 10 nombres de animales (perro, gato, león, etc,) y de que tipo son
            lista_de_animales = cargar_animales()
        case 2:
            # 2 Imprimir la lista completa de animales con su tipo.
            imprimir_lista(lista_de_animales)
        case 3:
            # 3 Mostrar el porcentaje de animales por tipo.
            calcular_porcentaje_por_tipo(lista_de_animales)
            pass
        case 4:
            # 4 Mayor cantidad de animales por tipo.
            mayor_cantidad_por_tipo(lista_de_animales)
            pass
        case 5:
            # 5 Menor cantidad de animales por tipo.
            menor_cantidad_por_tipo(lista_de_animales)
            pass
        case 6:
            # 6 Pedir un animal e informar si está en la lista y sus datos correspondientes si efectivamente está en la lista.
            informar_existencia(lista_de_animales)
            pass
        case 7:
            # 7 Pedir un animal e informar la primer ocurrencia de ese animal en la lista si es que existe.
            informar_ocurrencia(lista_de_animales)
            pass
        case 8:
            # 8 Informar la cantidad de animales por cada tipo de animal.
            informar_cantidad_por_tipo(lista_de_animales)
            pass
        case 9:
            vaciar_lista(lista_de_animales)
            # 9 Vaciar la lista.
            pass
        case 10:
            #10 Salir.
            print("Saliste del programa")
            salida = False
            pass


#-----------------------------------------------------------------------------------------------------------------
#BIBLIOTECA 


def cargar_animales()-> list[dict]:
    
    lista = []
    
    while len(lista) < 4:
                
        nombre = input("Ingrese nombre del animal: ")
        especie = input("Ingrese tipo de animal: ")
        
        diccionario_animales = {'animal': nombre, 'tipo': especie}
        
        lista.append(diccionario_animales)
        
    return lista
        

def imprimir_lista(lista:list):
        print(lista)


def calcular_porcentaje_por_tipo(lista:list):

    dir_contador_por_tipo = {}

    for element in lista:
            
        clave = element['tipo']

        if clave in dir_contador_por_tipo:
            dir_contador_por_tipo[clave] = dir_contador_por_tipo[clave] + 1
        else:
            dir_contador_por_tipo[clave] = 1

    for clave in dir_contador_por_tipo:
        
        cantidad = dir_contador_por_tipo[clave]
        tipo = clave
        
        print("Del tipo {} hay un {}%".format(tipo,(cantidad * 100 / len(lista))))
        
        
def mayor_cantidad_por_tipo(lista:list):

    dir_contador_por_tipo = {}
    flag = True
    for element in lista:
            
        clave = element['tipo']

        if clave in dir_contador_por_tipo:
            dir_contador_por_tipo[clave] = dir_contador_por_tipo[clave] + 1
        else:
            dir_contador_por_tipo[clave] = 1


    for clave in dir_contador_por_tipo:
        
        cantidad = dir_contador_por_tipo[clave]
       
        if flag == True or int(cantidad) > maximo: 
            maximo = cantidad
            tipo = clave
            flag = False
    
    print("El tipo que tiene mayor cantidad es '{}' con {} cantidad de animales".format(tipo,maximo))      
    

def menor_cantidad_por_tipo(lista:list):

    dir_contador_por_tipo = {}
    flag = True
    for element in lista:
            
        clave = element['tipo']

        if clave in dir_contador_por_tipo:
            dir_contador_por_tipo[clave] = dir_contador_por_tipo[clave] + 1
        else:
            dir_contador_por_tipo[clave] = 1


    for clave in dir_contador_por_tipo:
        
        cantidad = dir_contador_por_tipo[clave]
       
        if flag == True or int(cantidad) < minimo: 
            minimo = cantidad
            tipo = clave
            flag = False
    
    print("El tipo que tiene menor cantidad es '{}' con {} cantidad de animales".format(tipo,minimo))      
    
    
def informar_existencia(lista:list):
    
    animal_buscado = input("Ingrese el animal que desea consultar: ")
    encontrado = False

    for valor in lista:
        if valor['animal'] == animal_buscado:
            print("El animal {}, esta en a lista y es {}".format(valor['animal'],valor['tipo']))
            encontrado = True
        
    if encontrado == False:
        print("El animal no fue encontrado")
        
        
def informar_ocurrencia(lista:list):
    
    animal_buscado = input("Ingrese el animal que desea consultar: ")
    encontrado = False
    
    for indice in range(len(lista)):
        if lista[indice]['animal'] == animal_buscado:
            
            print("El animal buscado es {} y está en la posición {}".format(animal_buscado,indice))
            encontrado = True
        
    if encontrado == False:
        print("El animal no fue encontrado")            
    
def informar_cantidad_por_tipo(lista:list):

    dir_tipo = {}

    for animal in lista:
        clave = animal['tipo']
        
        if clave in dir_tipo:
            dir_tipo[clave] = dir_tipo[clave] + 1
        else:
            dir_tipo[clave] = 1

    print(dir_tipo)
    
    

def vaciar_lista(lista:list):
    
    lista.clear()
    print("Se vació la lista")

