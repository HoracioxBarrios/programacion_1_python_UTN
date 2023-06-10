import pygame, sys

pygame.init()
#constantes
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 500
TITULO_JUEGO = "Mi Juego Pygame"

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (0, 150, 255)
AMARILLO = (255, 255, 0)

PANTALLA = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))#seteo la ventana
# PANTALLA.fill(BLANCO) #pinta la pantalla. por default: negro

pygame.display.set_caption(TITULO_JUEGO)

FPS = 30
Relog = pygame.time.Clock() 

imagen_vertical = pygame.Surface((100, 100))
imagen_vertical.fill(VERDE)# pinta
rectangulo_vertical = imagen_vertical.get_rect()
rectangulo_vertical.center= (ANCHO_PANTALLA/2 ,ALTO_PANTALLA/2) # ceneter es una propiedad, No un metodo

while(True):
    Relog.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
    PANTALLA.blit(imagen_vertical, rectangulo_vertical) #blit: superpone la imagen en la pantalla    
    # pygame.display.update()# esta función se utiliza para actualizar una parte específica de la pantalla.
    pygame.display.flip()# se utiliza para actualizar toda la pantalla
    
    
    
