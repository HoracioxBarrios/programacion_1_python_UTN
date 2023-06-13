import pygame


class Imagen:
    #Constructor
    #Atributos(setter y getters)
    #Metodos
    def __init__(self, tamaño : tuple, colores : dict, origen : tuple)-> None:
        '''
        crea una duperficie, obtiene un rectangulo, lo posiciona en 
        la pantalla-
        Recibe: 
        arg 1 el tamaño en una tupla(ancho : int, alto : int), 
        arg 2 los colores inicial y colision  en un dicc. ej 
        {"color_inicial" : azul, "color_colicion" : blanco}.
        
        arg 3 el origen en una tupla ej: (800 /2, 500 /2).
        retorna : None
        '''
        self.superficie = pygame.Surface(tamaño)
        self.color = colores["color_inicial"]
        self.color_colision = colores["color_colision"]
        self.superficie.fill(self.color)
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.center = (origen)
     
    def mover_imagen(self, sentido : str, desplazamiento : int, medidas_pantalla : tuple):
        '''
        mueve una imagen en pantalla
        recibe:
        arg 1 el sentido ej:(vertical), arg 2 el desplazamiento (es la velocidad de mov), 
        arg 3 las medidas de la pnatalla en una tupla (ancho : int, alto : int)
        
        '''
        if sentido == "vertical":
            self.rectangulo.y += desplazamiento
            if self.rectangulo.top > medidas_pantalla[1]:
                self.rectangulo.bottom = 0
        else:
            self.rectangulo.x += desplazamiento
            if self.rectangulo.left > medidas_pantalla[0]:
                self.rectangulo.left = 0

    def detectar_colicion(self, otra_imagen):
        '''
        Detecta la colicion entre dos superficies
        Recibe la otra imagen
        devuelve: None
        '''
        if self.rectangulo.colliderect(otra_imagen.rectangulo): # self represernta nuestra superficie(nuestra imagen): (nuestra superfie.rectangulo seria)
            self.superficie.fill(self.color_colision)
            otra_imagen.superficie.fill(otra_imagen.color_colision)
        else:
            self.superficie.fill(self.color)# el color seteado riginalmente
            otra_imagen.superficie.fill(otra_imagen.color)# el color seteado riginalmente de la otra imagen

#-------------------------