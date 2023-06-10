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
PANTALLA.fill(BLANCO) #pinta la pantalla

pygame.display.set_caption(TITULO_JUEGO)#Titulo arriba de la ventana




#dibujamos un rectangulo aca afuera del loop
#                           SUPERFICIE, COLOR,(COORD X, COORD Y, ANCHO, ALTO),ANCHO DE BORDE. TAMBIEN EXISTE BORDER RADIUS 
pygame.draw.rect(PANTALLA, VERDE, (200, 200, 100, 400), 2)

#dibujamos una linea
#               superficie, color, (pos x DONDE COMIENZA, inclinacion o eje y), (pos x donde termina, inclinacion) ,ANCHO DE BORDE
pygame.draw.line(PANTALLA, ROJO, (100, 100), (400, 100), 2)

#dibujamos un circulo
#                  SUPERFICIE, COLOR, (pos x, pos y), radio, grosor de la linea
pygame.draw.circle(PANTALLA, AZUL_CLARO, (125, 250), 25, 2)

# dibujamos una elipse
#
pygame.draw.ellipse(PANTALLA, AMARILLO, (350, 200, 40, 80), 0)
while(True):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
    
    

