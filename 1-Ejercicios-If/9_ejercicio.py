'''
9- Escribir un programa que le pida al usuario que ingrese una letra, 
y luego imprima "Es una vocal" si la letra es una vocal (a, e, i, o, u), 
o "Es una consonante" si la letra es una consonante.
'''

letra_ingresada = input("Ingrese una letra")

if(letra_ingresada != "a" and letra_ingresada != "e"
and letra_ingresada != "i" and letra_ingresada != "o"
and letra_ingresada != "u"):
    print("Es una consonante")
else:
    print("Es una vocal")