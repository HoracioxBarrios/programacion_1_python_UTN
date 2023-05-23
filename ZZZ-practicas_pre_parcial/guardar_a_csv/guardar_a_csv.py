lista_personajes =\
  [{
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": 79.349999999999994,
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  },
  {
    "nombre": "Rocket Raccoon",
    "identidad": "Rocket Raccoon",
    "empresa": "Marvel Comics",
    "altura": 122.77,
    "peso": "25.73",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Brown",
    "fuerza": "5",
    "inteligencia": "average"
  },
  {
    "nombre": "Wolverine",
    "identidad": "Logan",
    "empresa": "Marvel Comics",
    "altura": 160.69999999999999,
    "peso": "135.21000000000001",
    "genero": "M",
    "color_ojos": "Blue",
    "color_pelo": "Black",
    "fuerza": "35",
    "inteligencia": "good"
  },
  {
    "nombre": "Black Widow",
    "identidad": "Natasha Romanoff",
    "empresa": "Marvel Comics",
    "altura": 170.78999999999999,
    "peso": "59.340000000000003",
    "genero": "F",
    "color_ojos": "Green",
    "color_pelo": "Auburn",
    "fuerza": "15",
    "inteligencia": "good"
  }]

def crear_archivo_csv(nombre_path : str, lista_a_guardar :list[dict]):
  with open(nombre_path, "w") as archivo:
    for heroe in lista_a_guardar:
      mensaje = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}\n"
      mensaje = mensaje.format(heroe["nombre"],
                               heroe["identidad"],
                               heroe["empresa"],
                               heroe["altura"],
                               heroe["peso"],
                               heroe["genero"],
                               heroe["color_ojos"],
                               heroe["color_pelo"],
                               heroe["fuerza"],
                               heroe["inteligencia"])
      archivo.write(mensaje)

ruta_donde_se_va_a_guardar = "ZZZ-practicas_pre_parcial\guardar_a_csv\\nuevo_archivo.csv"
      
crear_archivo_csv(ruta_donde_se_va_a_guardar, lista_personajes)
      
    


'''
como tiene el valor str vacio "inteligencia": ""
en el csv va a quedar una coma al final. para corregir esto primero 
tenemos que, renombrar con nuetra funcion los str vacios y volver 
a generar el csv. con eso no va a quedar la coma al final.
'''







# def guardar_archivo(nombre_archivo : str, contenido_a_guardar : str):
#     '''
#     Genera un archivo con la extension requerida .
#     Recibe: (arg 1)El path/nombre_archivo.extencion (ejemplo: csv) el path:
#     (Donde se va a guardar).
#     (arg 2) El contenido a guardar (una cadena str).
#     Devuelve: un boolean para caso de exito True, sino False.
#     '''
#     retorno = False
#     try:
#         with open(nombre_archivo, "w+",newline='\n') as archivo:
#             archivo.write(contenido_a_guardar)
#             retorno = True
#             print("Se creó el archivo {0}".format(nombre_archivo))
#     except:
#         retorno = False
#         print("Error al crear el archivo {0}".format(nombre_archivo))
        
#     return retorno
  
  