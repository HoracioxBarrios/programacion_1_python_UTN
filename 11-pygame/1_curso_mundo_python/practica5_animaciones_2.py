import pygame, sys, random

pygame.init()

BLANCO = (255, 255, 255)
CELESTE = (14, 150, 255)
size = (800, 500)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

lista_coordenadas = []
for i in range(60):
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        lista_coordenadas.append([x, y])


while(True):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(BLANCO)
    for coordenada in lista_coordenadas:
        x = coordenada[0]
        y = coordenada[1]
        coordenada[1] += 1
        pygame.draw.circle(screen, CELESTE, (x, y), 2)
        if coordenada[1] > 500:
             coordenada[1] = 0


    pygame.display.flip()
    clock.tick(30)


#https://www.youtube.com/watch?v=fJcXtfwhtD8&list=PLuB3bC9rWQAu6cGeRo_I6QV8cz1_2V6uM&index=5