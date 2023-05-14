


lista_heroes_prueba =\
[
    {
      "nombre": "mystique",
      "identidad": "Raven Darkholme",
      "empresa": "Marvel Comics",
      "altura": 178.65000000000001,
      "peso": "54.960000000000001",
      "genero": "F",
      "color_ojos": "Yellow (without irises)",
      "color_pelo": "red / orange",
      "fuerza": "15",
      "inteligencia": "good"
    },
    {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": 79.349999999999994,
    "peso": "18.449999999999999",
    "genero": "F",
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
    "color_ojos": "",
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
    "genero": "F",
    "color_ojos": "Blue",
    "color_pelo": "Black",
    "fuerza": "35",
    "inteligencia": "good"
  }]

def capitalizar_palabras(cadena: str) -> str:
    '''
    capitaliza palabras
    Recibe una cadena str.
    devuelve dicho string en el cual todas y cada una de las palabras 
    que contenga, deberán estar capitalizadas.
    '''
    lista_palabras = cadena.split()
    lista_palabras_capitalizadas = []
    for palabra in lista_palabras:
        palabra_capitalizada = palabra.capitalize()
        lista_palabras_capitalizadas.append(palabra_capitalizada)
    return ' '.join(lista_palabras_capitalizadas)



def normalizar_dato(valor : str, valor_reemplazante= "N/A"):
    '''
    Normaliza un valor string.
    Recibe: (arg 1) valor (ejemplo: verde), (arg2) Opcional:valor 
    reemplazante en caaso de que el valor sea "", 
    por defaul reemplaza por "N/A".
    Retorna el valor modificado si fue necesario.
    '''
    if(valor == ""):
        valor = valor_reemplazante
    return valor


set_ejemplo = {'Brown', 'Red / Orange', 'Black', 'Yellow'}



def obtener_heroes_por_tipo(
    lista_heroes :list[dict], set_de_variedades : str, clave_a_evaluar : str)->dict:
    nuevo_diccionario_variedades = {}
    for tipo_variedad in set_de_variedades:
        if(tipo_variedad not in nuevo_diccionario_variedades):
            print(tipo_variedad)
            nueva_lista = []
            nuevo_diccionario_variedades[tipo_variedad] = nueva_lista
            for heroe in lista_heroes:
               valor_normalizado = normalizar_dato(heroe[clave_a_evaluar])
               heroe[clave_a_evaluar] = valor_normalizado
               heroe[clave_a_evaluar] = capitalizar_palabras(heroe[clave_a_evaluar])
               if(heroe[clave_a_evaluar] == tipo_variedad):
                   nueva_lista.append(heroe["nombre"])
    
              
            
    print(nuevo_diccionario_variedades)


obtener_heroes_por_tipo(lista_heroes_prueba, set_ejemplo, clave_a_evaluar="color_pelo")


''' si en la lista de el heroes tiene el colo re pelo en minusculas
la comprovacion de la claves no dara igual ya que el set si viene 
capitalizado. entoncers ha que capitalizar la clave buscada tambien 
de la lista para que nos de igualdad'''
