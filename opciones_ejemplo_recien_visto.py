def app():
    SOURCE = "./RUTA/archivo.json"
    DESTINY = "./RUTA/archivo.csv"
    lista_heroes = func.cargar_json(SOURCE)
    normalizar_lista(lista_videos)
    while(True):
        print("Aca se imprime el menú")
        # Tomar datos de usuario validando con regex
        respuesta = input("elegir opcion:")
        if(respuesta==1):            
            lista_obtenida = obtener_algunos(lista_heroes)
        elif(respuesta==2):
            lista_obtenida = ordenar_por_algo(
              lista_heroes,"alguna_clave","asc")
            mostrar(lista_heroes)
        elif(respuesta==3):
            lista_obtenida = ordenar_por_algo(
              lista_heroes,"alguna_clave","desc")
            mostrar(lista_heroes)
        elif(respuesta==4):
            print(calcular_promedio(lista))
        elif(respuesta==5):
            dato = input("Buscar: ")
            buscar(lista_heroes, dato)
        elif(respuesta==6):
            # Si no paso AL MENOS por una de las opciones 1, 2 o 3...
            # YOU SHALL NOT PASS!
            exportar_csv(lista_obtenida, DESTINY)
        elif(respuesta==7):
            break
        else: print('mensaje de error')