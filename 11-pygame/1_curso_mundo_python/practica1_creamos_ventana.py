import pygame
import sys

#Inicializamos Pygame
pygame.init()

#definimos y creamos la ventana del juego
ANCHO = 800
ALTO = 500
screen = pygame.display.set_mode((ANCHO, ALTO))



while(True):
    for evento in pygame.event.get():
        # print(evento)
        if evento.type == pygame.QUIT:# si el usuario toca la cruz de arriba de la ventana ,cierra.
            sys.exit()
            
