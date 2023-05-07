'''
13.Escribir una función que tome un correo electrónico y elimine 
cualquier carácter después del símbolo @, por ejemplo: 
"usuario@gmail.com" -> 
"usuario".

'''

correo = "usuario@gmail.com"


def eliminar_despues_arroba(correo):
    '''
    elimina lo que esta despues del arroba
    recibe un correo electronico
    devuelve el dato antes del arroba
    '''
  
    nueva_lista = correo.split("@")
    # print(nueva_lista)
    
    return nueva_lista[0] #nos quedamos con el primero de la lista

print(eliminar_despues_arroba(correo))