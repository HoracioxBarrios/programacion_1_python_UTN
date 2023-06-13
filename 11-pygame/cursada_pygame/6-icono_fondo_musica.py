import pygame, sys

pygame.init()
#constantes
ANCHO_PANTALLA = 1000
ALTO_PANTALLA = 500
SCREEN_SIZE = (ANCHO_PANTALLA, ALTO_PANTALLA)
TITULO_JUEGO = "Mi Juego Pygame"

PANTALLA = pygame.display.set_mode(SCREEN_SIZE)#seteo la ventana
pygame.display.set_caption(TITULO_JUEGO)#Titulo arriba de la ventana
#ICONO
icono = pygame.image.load("11-pygame\cursada_pygame\icono_homero.png")
pygame.display.set_icon(icono)
# FONDO
fondo = pygame.image.load("11-pygame\cursada_pygame/fondo.jpg")
fondo_escalado = pygame.transform.scale(fondo,SCREEN_SIZE)
PANTALLA.blit(fondo_escalado, (0, 0))
#MUSICA
pygame.mixer.music.load("11-pygame\cursada_pygame\musica_l2.mp3")
pygame.mixer.music.play(-1)# -1 se repite indefinidamente, o nada para una sola vez.
pygame.mixer.music.set_volume(0.5)# volimen rango de 0 a 1 que es el maximo


while(True):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()


