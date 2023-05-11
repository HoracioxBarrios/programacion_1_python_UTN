from biblioteca import leer_archivo_json, stark_marvel_app_5 # las dos que usamos abajo

def main():
    ruta_del_archivo_json = "Desafio_Stark_03-Archivos\data_stark.json"
    lista_de_personajes = leer_archivo_json(ruta_del_archivo_json)
    stark_marvel_app_5(lista_de_personajes) #Ejecucion del programa


main()
