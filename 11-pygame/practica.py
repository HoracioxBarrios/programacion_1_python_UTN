import pygame
from pygame.locals import *
pygame.init() #Se inicializa pygame

screen = pygame.display.set_mode([800, 800]) #Se crea una ventana
titulo = pygame.display.set_caption("Mi juego")
tick_s1 = pygame.USEREVENT + 0
tick_s2 = pygame.USEREVENT + 1
pygame.time.set_timer(tick_s1, 1000)
pygame.time.set_timer(tick_s2, 2000)

imagen = pygame.image.load("11-pygame\pokemon.png")
font = pygame.font.SysFont("Arial Narrow", 50)
text = font.render("HOLA MUNDO", True, (255, 0, 0))
running = True
while running:
   # Se verifica si el usuario cerro la ventana
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       
    #    if event.type == tick_s1:
    #         print("Ya paso un segundo")
    #    if event.type == tick_s1:
    #         print("Ya paso dos segundos")
       if event.type == pygame.KEYDOWN:# No soporta presionado
            if event.key == pygame.K_w:
                print("Se presiono la tecla w")

       variable_tecla = pygame.key.get_pressed() # No soporta presionado
       if True in variable_tecla:
            if variable_tecla[K_a]:
                print("presiono la tecla a")
       if True in variable_tecla:
            if variable_tecla[K_d]:
                print("presiono la tecla d")
       if True in variable_tecla:
            if variable_tecla[K_s]:
                print("presiono la tecla s")
       
       screen.blit(text,(400,400))
       screen.blit(imagen, (220, 600))
       pygame.display.flip()
#    print(type(imagen)) # <class 'pygame.Surface'>
        


   screen.fill((255, 255, 255))# Se pinta el fondo de la ventana
   # Se dibuja un círculo azul en el centro
#    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
#    pygame.display.flip()# Muestra los cambios en  la pantalla
   
pygame.quit() # Fin
