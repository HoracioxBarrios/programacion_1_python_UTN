lista_bzrp=[{'title': 'QUEVEDO || BZRP Music Sessions #52', 'views': 227192970, 'length': 204, 'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg', 'url': 'https://youtube.com/watch?v=A_g3lMcWVy0', 'date': '2022-07-06 00:00:00'},
            {'title': 'VILLANO ANTILLANO || BZRP Music Sessions #51', 'views': 112947399, 'length': 188, 'img_url': 'https://i.ytimg.com/vi/wvz97-lNPH8/sddefault.jpg', 'url': 'https://youtube.com/watch?v=wvz97-lNPH8', 'date': '2022-06-08 00:00:00'}]

#Funcion para mostrar
def print_tema(tema): #Recibe un diccionario que reprecenta un tema, generado en el for de abajo
    '''
    Mustra un tema por terminal
    recibe el diccionario del tema a mostrar
    retorna - no aplica
    '''
    print("\n Titulo: {0} - Views: {1} - Length: {2}".format(
        tema["title"],
        tema["title"],
        tema["title"]))

#definicion de la funcion
def mostrar_lista_de_temas(lista_de_temas): # espera una LISTA DE TEMAS, recorre la lista con for
    '''
    Mustra una lista de temas por terminal
    recibe la lista de temas
    retorna - no aplica
    '''
    for tema in lista_de_temas:
        print_tema(tema)


#Llamada a la funcion
mostrar_lista_de_temas(lista_bzrp) #Le pasamos una lista de temas, en la definicion se puso que espera un arg