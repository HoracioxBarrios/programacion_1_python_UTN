import pygame

pygame.init() #se inicializa pygame
screen = pygame.display.set_mode((500, 500))# se crea una ventana
running = True

while(running):
    #se verifica si el usuario cerró la ventana
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
    screen.fill