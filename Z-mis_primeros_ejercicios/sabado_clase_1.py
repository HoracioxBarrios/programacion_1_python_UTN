'''
dos variables tienen el mismo valor, se usa la referencia o direccion,
en memoria de la primera variable, a diferencia de c que nosostros obtimizamos 
la memoria, aca se hce dinamicamente
'''



# numero_uno = 5
# numero_dos = 5

# print(id(numero_uno))
# print(id(numero_dos))


#**************************************************
'''usa dos direciones distintas'''
# numero_uno = 5
# numero_dos = 10
# print(id(numero_uno))
# print(id(numero_dos))

#*************************************************
''' para ver la direccion en exa hay que castearlo'''

'''usa dos direciones distintas'''
# numero_uno = 5
# numero_dos = 10
# print(exa(id(numero_uno)))
# print(exa(id(numero_dos)))


# edad = 18

# if (edad > 18):
#     print("Es mayor de edad")

# print("Fuera del if")

# lo mismo sin parentesis y es valido
# edad = 18

# if edad > 18:
#     print("Es mayor de edad")

# print("Fuera del if")


# otro ejemplo

# edad = 18

# if(edad > 18):
#     print("Es mayor")
# elif(edad > 0 and edad < 13 ):
#     print("Es niño")
# else:
#     print("Es adolecente")


#-while en python
numero_ejemplo = 5
contador = 0
while(contador < numero_ejemplo ):
    print(contador)
    contador += 1



# for en python
# for i in range(5): # la funcion range devuelve un iterable
#     print(i)

'''
en js y c:
let i;

for(i = 0; i < 5; i++){
    alert(i);
}


'''


# no se puede concatenar un int y un str con +
# hay 3 formas de concatenar o combiertiendo un numero a str y concatenarlo 
# con otro string
# o usando format

'''concatenar casteando a str un numero y concatenando (Davila no avaló)'''
# edad_int = 55
# edad_str = str(edad_int)
# print("Su edad es: "+ edad_str)

'''concatenar usando format ( davila dio Ok para usar este en lugar de los otros)'''
# edad = 25

# print("Su edad es {0}".format(edad))

''' 3ra forma'''

edad = 99

print("Su edad es: ",edad)
