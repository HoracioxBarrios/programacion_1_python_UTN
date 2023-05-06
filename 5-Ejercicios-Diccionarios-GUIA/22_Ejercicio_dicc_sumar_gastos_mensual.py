'''
22.Crea un diccionario que represente los gastos de una persona en diferentes
categorías, donde las claves son los nombres de las categorías y los valores
son los gastos correspondientes. Calcula el total de gastos de la persona en
el mes.
'''
diccionario_gastos = {
    'comida': 200,
    'transporte': 100,
    'entretenimiento': 50,
    'ropa': 150,
    'otros': 75
}

cantidad_de_dias = 30
acumulador_gastos = 0
for gasto in diccionario_gastos:
    acumulador_gastos += diccionario_gastos[gasto]

total_gasto_mensual = acumulador_gastos * cantidad_de_dias

print("El total de gastos en el mes es : {0}".format(total_gasto_mensual))