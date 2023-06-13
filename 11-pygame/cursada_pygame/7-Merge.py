
import pygame
import sys
from mi_class_Personaje import Personaje

pygame.init()
#constantes
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 500
TITULO_JUEGO = "Mi Juego Pygame"

# BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
# ROJO = (255, 0, 0)
# VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
# AZUL_CLARO = (0, 150, 255)
# AMARILLO = (255, 255, 0)

PANTALLA = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))


pygame.display.set_caption(TITULO_JUEGO)


FPS = 30
Relog = pygame.time.Clock() 

# #******** objeto creado con la class Imagen - VERSION POO # --------------------no va mas
# color_vertical = {"color_inicial" : VERDE, "color_colision" : ROJO}
# color_horizontal = {"color_inicial" : AZUL_CLARO, "color_colision" : BLANCO}

# imagen_vertical = Imagen((100, 100), color_vertical, (ANCHO_PANTALLA/2 ,ALTO_PANTALLA/2))
# imagen_horizontal = Imagen((100, 100), color_horizontal, (ANCHO_PANTALLA -100, ALTO_PANTALLA/2))
# #******************************************

homero = Personaje((200, 200),(ANCHO_PANTALLA /2, ALTO_PANTALLA /2 ), "11-pygame\cursada_pygame\homero.png")
dona = Personaje((50, 50), (ANCHO_PANTALLA/2, ALTO_PANTALLA), "11-pygame\cursada_pygame\dona.png")    



fondo = pygame.image.load("11-pygame\cursada_pygame/fondo.jpg")
fondo_escalado = pygame.transform.scale(fondo, (ANCHO_PANTALLA, ALTO_PANTALLA))


while(True):
    Relog.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # PANTALLA.fill(NEGRO)
    PANTALLA.blit(fondo_escalado, (0, 0))
    PANTALLA.blit(dona.superficie, dona.rectangulo)    
    PANTALLA.blit(homero.superficie, homero.rectangulo)
    
    #**************** movimiento VERSION POO
    dona.mover_imagen("vertical", 10, (ANCHO_PANTALLA, ALTO_PANTALLA))
    homero.mover_imagen("horizontal", 10, (ANCHO_PANTALLA, ALTO_PANTALLA))
    #***************************************
    
    #******************verificamos si un rectangulo colisiona con otro rectangulo- VERSION POO
    homero.detectar_colicion(dona)
    #***************************************
    
   
    
    # pygame.draw.line(PANTALLA, AZUL, (400, 0), (400, 800), 1)  # lineas para guia ejes cartesiano
    # pygame.draw.line(PANTALLA, AZUL, (0, 250), (800, 250), 1)
    
    # pygame.display.update()# esta función se utiliza para actualizar una parte específica de la pantalla.
    pygame.display.flip()# se utiliza para actualizar toda la pantalla
    
    
    



