'''
3- Crear una función que calcule el descuento aplicado a un producto.
Recibe dos parámetros (precio original y precio con descuento) y
devuelve el porcentaje de descuento aplicado.
'''
precio_producto = 100
precio_descuento = 80

def calcular_decuento_en_procentaje(precio_original, precio_descuento):
    '''
    calcula el descuento aplicado a un producto
    recibe el precio original, y el precio descuento
    devuelve el porcentaje del descuento aplicado
    '''
    porcentaje_descuento_local = (precio_original - precio_descuento) / precio_original * 100
    return porcentaje_descuento_local




porcentaje_descuento = calcular_decuento_en_procentaje(precio_producto, precio_descuento)

print(porcentaje_descuento)















# # Ejemplo de uso de la función
# def calcular_descuento(precio_original, precio_descuento):
#     descuento = ((precio_original - precio_descuento) / precio_original) * 100
#     return descuento

# # Ejemplo de uso de la función
# precio_original = 100
# precio_descuento = 80
# descuento = calcular_descuento(precio_original, precio_descuento)
# print("El descuento aplicado es del", descuento, "%")

