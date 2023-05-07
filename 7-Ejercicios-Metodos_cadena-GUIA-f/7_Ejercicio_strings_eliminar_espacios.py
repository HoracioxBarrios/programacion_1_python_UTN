'''
7. Escribir una función que tome un string y devuelva el mismo string 
con los espacios eliminados
'''

palabra_con_espacio = "    buscar "

def eliminar_espacios(palabra : str)-> str:
    '''
    elimina los espacios de una palabra
    recibe una palabra
    devuelve la palabra corregida
    '''
    return palabra.strip()

print(eliminar_espacios(palabra_con_espacio))
    