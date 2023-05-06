#'''Lenguaje Python creado por Guido van Rossum lanzado en 1991'''
#'''A la fecha 2023 esta en la version 3.11.3 (https://www.python.org )'''

''' Se puede usar para hacer software multiplataforma.
Python no es compilado.(no requiere ser preparado par un 
sistema operativo en particular)
Es un lenguaje Interpretado, va a correr dentro de otro programa que se 
llama interprete, y ese interprete puede correr en varios sistemas operativos
Que se puede hacer?
*Software multiplataforma
*VideoJuegos
*Aplicaciones web
*Aplicaciones Big Data
*Inteligencia Artificial
'''

'''Sintaxis'''
nombre = "Juan"
numero_str = "15"
numero_int = 15
numero_Float = 15.5
boolean = True

'''Ejemplo If'''
if(numero_int > 0):
    print(numero_int)
    
'''Ejemplo for( aca un for recorre listas, es parecido a un for each, 
recorre cada elemento, for in recorre cada elemento y lo guarda in una variable )'''

lista = [1, 2, 3, 4, 5]# una lista es como un array, inicia en el endice 0 y continua 1, 2, 3, 4 ...

for elemento in lista: # en cada iteracion un valor  de lista se va  guardar en elemento
    print(elemento)


'''Ejemplo while'''

contador = 0
while(contador < numero_int):
    contador = contador +1
    
''' una funcion aca es una definicion
ejemplo:'''
def sumar(parametro):
    pass # codigo a ejecutar. aca el ej pass, seria como un Not operation(no haga nada)

'''Segun Guido van rossum el codigo es leido mas veces, que escrito, por 
eso es importante que ademas de funcionar ,sea tambien legible.

que es PEP8 ? 
un conjunto de recomendaciones a seguir por la comunidad python, par que
todo sea mas legible.
por ejemplo: un codigo no debe superar los 79 caracteres por linea'''

'''ejemplos multilinea'''
def mi_funcion(primer_parametro, segundo_parametro, tercer_parametro,
            cuarto_parametro, quinto_prametro):
        pass
    
variable_a = 10
variable_b = 10
variable_c = 10
variable_d = 10
variable_e = 10
variable_f = 10

resultado = (variable_a + variable_b + (variable_c 
            - variable_d) - variable_d  - variable_f)


'''Mas de la Sintaxis!!!'''
#Variables ( se declaran usando snake_case) letras minusculas separadas de guion bajo. 
# NO se usa camelCase como en js
'''# una variable debe describir que es lo que contiene'''
variable_numero = 100

#funcion aca es una definicion y se definen en snake_case, 
'''# el nombre de la definicion debe dejar claro que hace.'''
a = 5
b = 5

def sumar(parametro):
    resultado = a + b 

'''clases'''
#una Clase se escribe en CamelCase pero la primera letra tambien es mayuscula.
# sin barra baja ejemplo MiClase , ClaseDePrueba
'''Metodos'''
#son funciones que estan dentro de las clases
# al igual que las variables y las definiciones(funciones), usar snake_case
'''CONSTANTES'''
# una constante se escribe en mayusculas, ejemplo MI_CONSTANTE

'''modulos'''
#al igual que las funciones mi_modulo.py  , modulo.py

'''                   encoding                     '''
# en python 2 se usaba la codificacion ascii
'''#en python 3 se usa utf-8; se puede usar los carpteres que usamos en español, 
como texto ,no para variables'''