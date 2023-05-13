from data_prueba import lista_bzrp

def generar_csv(nombre_archivo : str, lista : list[dict]):
    '''
    Genera un archivo csv a partir de una lista de ddionarios
    Recibe: el path/nombre_archivo.csv. (Donde se va a guardar)
    Devuelve: no aplica
    '''
    with open(nombre_archivo, "w") as archivo: # "w" es ecritura
        for video in lista:
            # print(video)
            texto_mensaje = "{0},{1}\n".format(video["title"], video["views"]) #hay que darle separacion con coma y al final salto de linea \n (alt +92  n)
            archivo.write(texto_mensaje)

path_archivo = "9-Ejercicios-Trabajar_con_archivos_json_y_csv -GUIA-f\mi_data_prueba.csv"
generar_csv(path_archivo, lista_bzrp)