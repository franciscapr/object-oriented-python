# pygame demo 0 - window only

# 1 - Importamos los paquetes
import pygame
from pygame.locals import *
import sys    # sys lo utilizaremos para cerra el programa
import random    # Importamos random para generar los numeros aleatorios de las coordenadas

# 2 - Definimos algunas constantes
BLACK = (0, 0, 0)    # Definimos negro para el fondo de nuestra ventana
WINDOW_WIDTH = 640    # Constante para el ancho
WINDOW_HEIGHT = 480    # Constante para la altura
FRAMES_PER_SECOND = 30    # Constante para la tasa de refrezco --> Define el nùmero de veces que el programa harà el bucle
BALL_WIDTH_HEIGHT = 100    # Definimos la altura y ancho de la imagen
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT    # Limitamos las coordenadas en ancho
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT    # Limitamos las coordenadas en largo

# 3 - Inicializamos pygame
pygame.init()    # Llamamos la mètodo inicializador
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))    # Pedimos a pygame que cree una ventana para nuestro programa con esta funciòn --> pasamos el ancho y la altura deseados de la ventana como argumentos
clock = pygame.time.Clock()    # Esta funciòn crea un objeto clock que se usa en la parte inferiro de nuestro buble principal para mantener nuestra tasa màxima de fotogramas.

# 4 - Cargar recursos: image(s), sound(s), etc.
ballImage = pygame.image.load('PygameDemo1_OneImage/images/ball.png')

# 5 - Inicializar variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)    # Creamos una rectagulo

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

        # See if user clicked
        if event.type == pygame.MOUSEBUTTONUP:    # Buscamos el evento
            # mouseX, mouseY = event.pos # Could do this if we needed it
            # Check of the click was in the rect of the ball
            # If so, choose a random new location
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    # 8 - Do any "per frame" actions
    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    # draw ball at position 100 across (x) and 200 down (y)
    window.blit(ballImage, (ballX, ballY))

    # 11 - Update the windown
    pygame.display.update()
    
    # 12 - Show things down a bit
    clock.tick(FRAMES_PER_SECOND)    # make pygame wait