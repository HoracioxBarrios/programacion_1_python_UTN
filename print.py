lista_heroes =\
[
{
"nombre": "Howard the Duck",
"identidad": "Howard (Last name unrevealed)",
"empresa": "Marvel Comics",
"altura": "79.349999999999994",
"peso": "18.449999999999999",
"genero": "M",
"color_ojos": "Brown",
"color_pelo": "Yellow",
"fuerza": "2",
"inteligencia": "average"
},
{
"nombre": "Rocket Raccoon",
"identidad": "Rocket Raccoon",
"empresa": "Marvel Comics",
"altura": "122.77",
"peso": "25.73",
"genero": "M",
"color_ojos": "Brown",
"color_pelo": "Brown",
"fuerza": "5",
"inteligencia": "average"
},
{
"nombre": "Pepe",
"identidad": "Howard (Last name unrevealed)",
"empresa": "Marvel Comics",
"altura": "795.349999999999994",
"peso": "18.449999999999999",
"genero": "M",
"color_ojos": "Brown",
"color_pelo": "Yellow",
"fuerza": "2",
"inteligencia": "average"
},
{
"nombre": "Dalia",
"identidad": "Rocket Raccoon",
"empresa": "Marvel Comics",
"altura": "122.77",
"peso": "25.73",
"genero": "F",
"color_ojos": "Azul",
"color_pelo": "Brown",
"fuerza": "5",
"inteligencia": ""
},
{
"nombre": "Pricila",
"identidad": "Rocket Raccoon",
"empresa": "Marvel Comics",
"altura": "155.77",
"peso": "25.73",
"genero": "F",
"color_ojos": "Green",
"color_pelo": "Brown",
"fuerza": "5",
"inteligencia": ""
}
]

def print_dicc(diccionario):
    '''
    muestra un diccionario
    Recibe un diccionario
    devuelve, no aplica
    '''
    print("------------ Resultado ------------")
    for clave, valor in diccionario.items():
        print("------------")
        print("{0} : {1} ".format(clave, valor))

def contar_por_tipo(lista: list, clave_tipo: str) -> dict:
    '''
    separa por tipo y los contabiliza
    recibe una list de dict
    retorna - una lista de dict con los tipos y cantidades correspondientes
    '''
    nuevo_dicc_contador = {}
    for diccionario in lista:
        valor_tipo = diccionario.get(clave_tipo)
        if valor_tipo == '': # evalua si es "", reasigna 
            valor_tipo = 'Notiene'

        if valor_tipo in nuevo_dicc_contador: 
            nuevo_dicc_contador[valor_tipo] += 1
        else:
            nuevo_dicc_contador[valor_tipo] = 1
    return nuevo_dicc_contador



tipos_de_ojos = contar_por_tipo(lista_heroes, clave_tipo="color_ojos")
print_dicc(tipos_de_ojos)


