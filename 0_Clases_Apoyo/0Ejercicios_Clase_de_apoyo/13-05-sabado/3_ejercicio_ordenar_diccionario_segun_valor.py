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
            
print(ordenar_estudiantes_por_calificacion(estudiantes))   

    




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






