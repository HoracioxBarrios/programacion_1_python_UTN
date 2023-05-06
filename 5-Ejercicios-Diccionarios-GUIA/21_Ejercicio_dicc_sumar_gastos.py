'''
21.Crea un diccionario que represente los gastos de una persona en diferentes
categorías, donde las claves son los nombres de las categorías y los valores
son los gastos correspondientes. Calcula el total de gastos de la persona.

'''
diccionario_gastos = {
    'comida': 200,
    'transporte': 100,
    'entretenimiento': 50,
    'ropa': 150,
    'otros': 75
}
acumulador_gastos = 0
for gasto in diccionario_gastos:
    acumulador_gastos += diccionario_gastos[gasto]



print("El total de gastos es: {0}".format(acumulador_gastos))





'''Otra forma'''

# # Definir el diccionario con los gastos
# gastos = {
#     'comida': 200,
#     'transporte': 100,
#     'entretenimiento': 50,
#     'ropa': 150,
#     'otros': 75
# }

# # Calcular el total de gastos
# total = sum(gastos.values())

# # Imprimir el resultado
# print("El total de gastos es:", total)
