# pygame demo 0 - window only

# 1 - Importamos los paquetes
import pygame
from pygame.locals import *
import sys    # sys lo utilizaremos para cerra el programa

# 2 - Definimos algunas constantes
BLACK = (0, 0, 0)    # Definimos negro para el fondo de nuestra ventana
WINDOW_WIDTH = 640    # Constante para el ancho
WINDOW_HEIGHT = 480    # Constante para la altura
FRAMES_PER_SECOND = 30    # Constante para la tasa de refrezco --> Define el nùmero de veces que el programa harà el bucle

# 3 - Inicializamos pygame
pygame.init()    # Llamamos la mètodo inicializador
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))    # Pedimos a pygame que cree una ventana para nuestro programa con esta funciòn --> pasamos el ancho y la altura deseados de la ventana como argumentos
clock = pygame.time.Clock()    # Esta funciòn crea un objeto clock que se usa en la parte inferiro de nuestro buble principal para mantener nuestra tasa màxima de fotogramas.

# 4 - Cargar recursos: image(s), sound(s), etc.
# 5 - Inicializar variables
# 6 - Loop forever

# Podemos pensar en cada iteraciòn del bucle como un fotograma en una animaciòn
while True:
    # 7 - Verificamos y manejamos eventos
    for event in pygame.event.get():    # Obtenemos una lista de eventos que ocurrieron
        # iteramos a traves de la lista de eventos
        # cada eventos informado al programa es una objeto
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    # 9 - Clear the window
    window.fill(BLACK)
    # 10 - Draw all window elements
    # 11 - Update the windown
    pygame.display.update()
    # 12 - Show things down a bit
    clock.tick(FRAMES_PER_SECOND)