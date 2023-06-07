import pygame
import sys

#Inicializamos Pygame
pygame.init()

#definimos y creamos la ventana del juego
ANCHO = 800
ALTO = 500
screen = pygame.display.set_mode((ANCHO, ALTO))

#Definimos los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)



while(True):
    for evento in pygame.event.get():
        # print(evento)
        if evento.type == pygame.QUIT:# si el usuario toca la cruz de arriba de la ventana ,cierra.
            sys.exit()


    screen.fill(BLANCO) # pintamos la pantalla, en este caso 1ro el fondo.
    #Zona de dibujo ---------
    pygame.draw.line(screen, VERDE, (0, 100),(300, 300), 5) # recibe arg1 la superficie, arg2 coordenada comienzo(x, y), arg3 corrdenada donde termina, arg 4 el grosor de la linea
    pygame.draw.rect(screen, NEGRO, (100, 100, 80, 80)) #recibe la tupla con la posicion en x, y el ancho y el alto del rectangulo.
    pygame.draw.circle(screen, NEGRO, (200, 200),30)
    #-----------------------
    pygame.display.flip()# actualiza la pantalla