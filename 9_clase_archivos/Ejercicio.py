# 1.2
def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    respuesta = input('Ingrese una opción: ').upper()
    if re.match('^[A-OZ]{1}$', respuesta):
        return respuesta
    return -1
# 1.4
def leer_archivo(path_completo: str) -> list[dict]:
    # with open(path_completo, 'r') as archivo:
    #     archivo_json = json.load(archivo)
    #     archivo_dict = dict(archivo_json)
    #     archivo_lista_dict = archivo_dict['heroes']
    #     return archivo_lista_dict
    with open(path_completo, 'r') as archivo:
        return list[dict](json.load(archivo)['heroes'])
    
    
