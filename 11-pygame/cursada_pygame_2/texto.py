import pygame, sys
pygame.init()

#https://www.youtube.com/watch?v=5dOa-xXXvDY&list=PLE9qW09sJEPQBZx_WJM46jkrtlY9FFlxb&index=14
BLANCO = (255, 255, 255)
NEGRO = (0 , 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (0, 150, 255)

ANCHO = 800
ALTO = 500
VENTANA =pygame.display.set_mode((ANCHO, ALTO))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
