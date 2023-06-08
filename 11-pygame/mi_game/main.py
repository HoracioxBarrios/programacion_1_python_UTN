import pygame
import sys
from pyvidplayer import Video

pygame.init()

#defino las dimenciones de la pantalla
WIDTH = 800
HEIGTH = 500
#se crea la ventana y el nombre que aparece arriba
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Super Dragon Ball Sprite")

#colores a usar
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
#Relog
clock = pygame.time.Clock()

#Fondo de pantalla
background = pygame.image.load("11-pygame\mi_game\shenlong.png")

#Referente al video de la intro
vid = Video("11-pygame\mi_game\Video1.mp4")
vid.set_size((800, 500))

def intro():
    while True:
        vid.draw(screen, (0, 0)) #donde corre el video
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                main_game()

# Loop game
def main_game():
    while (True):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()

        # -----------Logica

        # -----------Screen
        screen.fill(NEGRO)
        # -----------Dibujamos

        # ----------flip (mostramos)

        screen.blit(background, (110, -70))
        #actualizacion de mi pantalla
        pygame.display.flip()

        #Fps
        clock.tick(60)

intro()
