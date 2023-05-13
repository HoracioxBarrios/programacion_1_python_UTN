


def parse_csv_a_lista_dicc(nombre_archivo : str):
    '''
    Genera una lista de dicc a partir de un archivo csv
    Recibe: el path/nombre_archivo.csv. - (Desde donde toma los datos.)
    Devuelve la lista de diccionario generada.
    '''
    lista = []
    with open(nombre_archivo, "r") as archivo: #archivo es iterable
        for linea in archivo:
            lista_de_campos = linea.split(",")#hay que quitarle el separador "," que tiene el archivo csv
            video = {} #hay que contriur la lista de diccionario desde aca
            video["title"] = lista_de_campos[0] 
            video["views"] = int(lista_de_campos[1])
            lista.append(video) #agregamos cada dciionario a la lista en cada iteracion
    return lista      





lista_generada = parse_csv_a_lista_dicc("9-Ejercicios-Trabajar_con_archivos_json_y_csv -GUIA-f\mi_data_prueba.csv")

print(lista_generada)