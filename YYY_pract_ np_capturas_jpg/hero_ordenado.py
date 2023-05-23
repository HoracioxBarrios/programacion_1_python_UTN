                
lista = lista_personajes
lista_auxiliar = []
bandera_swap = True
ordenada = True

for i in range(len(lista)-1):
    if lista[i]["altura"] > lista[i+1]["altura"]:
        print("ya esta ordenada")
        ordenada = False
        break
if not ordenada:
    
    for i in range(len(lista)-1):
        
        for j in range(i+1, len(lista)):
            
            if(lista[i]['altura'] > lista[j]['altura']):
                
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                print("se ordeno")

print("Lista ordenada:")
for heroe in lista:
    print(heroe['nombre'],heroe['altura'], "\n\n")

