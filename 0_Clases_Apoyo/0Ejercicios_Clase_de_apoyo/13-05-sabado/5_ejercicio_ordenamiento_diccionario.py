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




frutas_ordenadas = ordenar_frutas_por_precio_kilo(diccionario_frutas)
print(frutas_ordenadas)





'''
comprension de diccionario es uno de los temas que vienen.

'''

