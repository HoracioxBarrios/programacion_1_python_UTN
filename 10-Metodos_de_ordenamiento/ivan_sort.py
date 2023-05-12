
import random
import time

def ivan_sort_A(lista:list):
    rango_a = len(lista)
    flag_swap = True

    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        for indice_A in range(rango_a):
            if  lista[indice_A] < lista[indice_A+1]:
                lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                flag_swap = True


def ivan_sort_B(lista:list,flag_orden:bool):
    rango_a = len(lista) - 1
    flag_swap = True

    while(flag_swap):
        flag_swap = False

        for indice_A in range(rango_a):
            if  flag_orden == False and lista[indice_A] < lista[indice_A+1] \
             or flag_orden == True and lista[indice_A] > lista[indice_A+1]:
                lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                flag_swap = True

lista = list(range(10000))
random.shuffle(lista)

lista_A = lista[:]
lista_B = lista[:]
lista_C = lista[:]


inicio = time.time()
ivan_sort_A(lista_A)
fin = time.time()

print("IVAN_A {0}".format((fin-inicio)))


inicio = time.time()
ivan_sort_B(lista_B,True)
fin = time.time()

print("IVAN_B {0}".format((fin-inicio)))



inicio = time.time()
ivan_sort_A(lista_A)
fin = time.time()

print("IVAN_A_YA ORDENADO {0}".format((fin-inicio)))