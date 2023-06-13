
import pygame
import sys
from mi_class_Imagen import Imagen

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

PANTALLA = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))


pygame.display.set_caption(TITULO_JUEGO)


FPS = 30
Relog = pygame.time.Clock() 

#******** objeto creado con la class Imagen - VERSION POO
color_vertical = {"color_inicial" : VERDE, "color_colision" : ROJO}
color_horizontal = {"color_inicial" : AZUL_CLARO, "color_colision" : BLANCO}

imagen_vertical = Imagen((100, 100), color_vertical, (ANCHO_PANTALLA/2 ,ALTO_PANTALLA/2))
imagen_horizontal = Imagen((100, 100), color_horizontal, (ANCHO_PANTALLA -100, ALTO_PANTALLA/2))
#******************************************


while(True):
    Relog.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    PANTALLA.fill(NEGRO)
    PANTALLA.blit(imagen_vertical.superficie, imagen_vertical.rectangulo)    
    PANTALLA.blit(imagen_horizontal.superficie, imagen_horizontal.rectangulo)
    
    #**************** movimiento VERSION POO
    imagen_vertical.mover_imagen("vertical", 10, (ANCHO_PANTALLA, ALTO_PANTALLA))
    imagen_horizontal.mover_imagen("horizontal", 10, (ANCHO_PANTALLA, ALTO_PANTALLA))
    #***************************************
    
    #******************verificamos si un rectangulo colisiona con otro rectangulo- VERSION POO
    imagen_horizontal.detectar_colicion(imagen_vertical)
    #***************************************
    
   
    
    pygame.draw.line(PANTALLA, AZUL, (400, 0), (400, 800), 1)
    pygame.draw.line(PANTALLA, AZUL, (0, 250), (800, 250), 1)
    
    # pygame.display.update()# esta función se utiliza para actualizar una parte específica de la pantalla.
    pygame.display.flip()# se utiliza para actualizar toda la pantalla
    
    
    
