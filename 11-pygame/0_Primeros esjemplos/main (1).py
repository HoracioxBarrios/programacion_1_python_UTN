
import pygame as pg


# link video https://www.youtube.com/watch?v=PhbIJPnP1EQ
'''
1- instalar biblioteca pygame:
En una terminal escribir (o copiar y pegar) este comando:
pip install -U pygame
2- Probar pygame:
Una vez que termine la instalación ingresar el siguiente comando:
python -m pygame.examples.aliens


'''





def gestionar_eventos(event: pg.event.Event, flag_run: bool, segundero: int):

    match event.type:
        case pg.QUIT:
            flag_run = False
            print('Estamos cerrando el juego y la ventana va a desaparecer')
        case pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print('Estamos presionando la tecla espacio')
                segundero += 2
            
    return flag_run, segundero
    


ANCHO_VENTANA = 800
ALTO_VENTANA = 500
COLOR_CELESTE = (5, 239, 250, 0.5)
CENTRO_CIRCULO = (250, 250) # Eje X = 250 , Eje Y = 250

pg.init()
# Seteamos la variable que representara el objeto de la ventana principal de nuestro juego
# Le ponemos el tamaño que tendra dicha ventana
ventana_ppal = pg.display.set_mode(size=(ANCHO_VENTANA, ALTO_VENTANA))
pg.display.set_caption("Prueba de jueguito")

nuestro_circulo = pg.draw.circle(
    ventana_ppal, COLOR_CELESTE, CENTRO_CIRCULO, 50
)

tick_1s = pg.USEREVENT + 0 #32866
tick_2s = pg.USEREVENT + 100 #32966

pg.time.set_timer(tick_1s, 1000)

segundero = 7
flag_run = True
while flag_run:
    lista_eventos = pg.event.get()
    for event in lista_eventos:
        flag_run, segundero = gestionar_eventos(
            event, flag_run, segundero
        )

        if event.type == tick_1s:
            segundero -= 1
            print(f'Restan {segundero} segundo/s')
            if segundero == 0:
                flag_run = False
                print('Tiempo finalizado, perdiste prro!')

pg.quit()
