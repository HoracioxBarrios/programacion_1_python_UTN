lista_heroes_prueba =\
[   {
      "nombre": "MystiqueChuo",
      "identidad": "Raven Darkholme",
      "empresa": "Marvel Comics",
      "altura": 120.65000000000001,
      "peso": 15.960000000000001,
      "genero": "F",
      "color_ojos": "Yellow (without irises)",
      "color_pelo": "red / orange",
      "fuerza": "15",
      "inteligencia": "good"
    },
    {
      "nombre": "Mystique",
      "identidad": "Raven Darkholme",
      "empresa": "Marvel Comics",
      "altura": 178.65000000000001,
      "peso": 54.960000000000001,
      "genero": "F",
      "color_ojos": "Yellow (without irises)",
      "color_pelo": "red / orange",
      "fuerza": "15",
      "inteligencia": ""
    },
    {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": 79.349999999999994,
    "peso": 180.449999999999999,
    "genero": "F",
    "color_ojos": "",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  }]





def normalizar_valores_str_vacios(
    lista_heroe : list[dict], valor_que_reemplaza = "N/A")-> list[dict]:
    '''
    verifica los str vacios y los renombra segun criterio
    Recibe:(arg 1)Una lista de heroes, (arg2)el valor str reemplazante("N/A").
    Devuelve la lista corregida.
    '''
    for heroe in lista_heroe:
        for clave in heroe.keys():
            if(heroe[clave] == ""):
                heroe[clave] = valor_que_reemplaza
    return lista_heroe
        
print(normalizar_valores_str_vacios(lista_heroes_prueba))


'''DATO.
para actualizar el valor de un diccionario hay qie trabajar con las
las claves usando el metodo keys(), luego para asignarle el nuevo 
valor usamos : heroe[clave] = valor_que_reemplaza


al principio probe con values() pero me dio error al querer
cambiar el valor. 
'''