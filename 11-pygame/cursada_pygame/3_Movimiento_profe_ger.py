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
# pygame.display.set_icon() # creo que es para poner el logito arriba

FPS = 30
Relog = pygame.time.Clock() 

imagen_vertical = pygame.Surface((100, 100))
imagen_vertical.fill(VERDE)# pinta
rectangulo_vertical = imagen_vertical.get_rect()
rectangulo_vertical.center = (ANCHO_PANTALLA/2 ,ALTO_PANTALLA/2) # center es una propiedad, No un metodo

imagen_horizontal = pygame.Surface((100, 100))
imagen_horizontal.fill(AZUL_CLARO)
rectangulo_horizontal = imagen_horizontal.get_rect()
rectangulo_horizontal.center = (ANCHO_PANTALLA -100, ALTO_PANTALLA/2)# centramos

while(True):
    Relog.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    PANTALLA.fill(NEGRO)# pinta la pantalla o la superficie de pantalla mejor dicho 
    PANTALLA.blit(imagen_vertical, rectangulo_vertical) #blit: superpone la imagen en la pantalla    
    PANTALLA.blit(imagen_horizontal, rectangulo_horizontal)
    
    #movimiento
    rectangulo_vertical.y += 10 # para mover en y
    if rectangulo_vertical.top > ALTO_PANTALLA: # cuando desaparece por abajo, aparece arriba
        rectangulo_vertical.bottom = 0
    rectangulo_horizontal.x += 10 # para mover en x
    if rectangulo_horizontal.left > ANCHO_PANTALLA:# cuando desaparece por la derecha, aparece en la izq
        rectangulo_horizontal.left = 0
    
    
    
    
    #1:10:05 / 3:30:20    https://www.youtube.com/watch?v=HuA3CNvEVl8&list=PLE9qW09sJEPQBZx_WJM46jkrtlY9FFlxb&index=15
    
    pygame.draw.line(PANTALLA, AZUL, (400, 0), (400, 800), 1)
    pygame.draw.line(PANTALLA, AZUL, (0, 250), (800, 250), 1)
    
    # pygame.display.update()# esta función se utiliza para actualizar una parte específica de la pantalla.
    pygame.display.flip()# se utiliza para actualizar toda la pantalla
    
    
    
