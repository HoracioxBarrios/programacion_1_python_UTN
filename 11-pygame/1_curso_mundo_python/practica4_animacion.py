import pygame
import sys

#Inicializamos Pygame
pygame.init()

#definimos y creamos la ventana del juego
ANCHO = 800
ALTO = 500
screen = pygame.display.set_mode((ANCHO, ALTO))
#controlar los FPS
relog = pygame.time.Clock()


# corrdenadas del rectangulo
coordenada_x = 400
coordenada_y = 200

#Velocidad a la que se moverá el rectangulo
velocidad_x = 3
velocidad_y = 3



#Definimos los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)



while(True):
    for evento in pygame.event.get():
        # print(evento)
        if evento.type == pygame.QUIT:# si el usuario toca la cruz de arriba de la ventana ,cierra.
            sys.exit()
    #logica ----------------
    if coordenada_x > 720 or coordenada_x < 0:
        velocidad_x *= -1
    if coordenada_y > 320 or coordenada_y < 0:
        velocidad_y *= -1
    #con esto se mueve el rectangulo
    coordenada_x += velocidad_x
    coordenada_y += velocidad_y
    #------------------------


    screen.fill(BLANCO) # pintamos la pantalla, en este caso 1ro el fondo.
    #Zona de dibujo ---------        x     y   ancho, alto
    pygame.draw.rect(screen, AZUL, (coordenada_x, coordenada_y, 80, 80))
    #-----------------------
    pygame.display.flip()# actualiza la pantalla
    relog.tick(60)





#https://www.youtube.com/watch?v=X9b-o57vC8Q&list=PLuB3bC9rWQAu6cGeRo_I6QV8cz1_2V6uM&index=4