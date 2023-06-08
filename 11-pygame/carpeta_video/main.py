import pygame
import sys
from pyvidplayer import Video

pygame.init()

WIDTH = 800
HEIGTH = 500

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Dragon Ball Sprite")
clock = pygame.time.Clock()
vid = Video("11-pygame\carpeta_video\Video1.mp4")
vid.set_size((800, 500))

def intro():
    while True:
        vid.draw(screen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                main()


def main():
    while (True):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()

        # -----------Logica

        # -----------Screen
        screen.fill(BLANCO)
        # -----------Dibujamos

        # ----------flip (mostramos)


        #actualizacion de mi pantalla
        pygame.display.flip()

        #Fps
        clock.tick(60)

intro()
