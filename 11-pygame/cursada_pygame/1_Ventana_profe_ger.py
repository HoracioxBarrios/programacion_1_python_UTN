import pygame, sys

pygame.init()
#constantes
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 500
TITULO_JUEGO = "Mi Juego Pygame"

PANTALLA = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))#seteo la ventana
pygame.display.set_caption(TITULO_JUEGO)#Titulo arriba de la ventana


while(True):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()








