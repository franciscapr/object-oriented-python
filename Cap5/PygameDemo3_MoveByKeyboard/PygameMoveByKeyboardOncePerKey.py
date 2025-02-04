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
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3


# 3 - Inicializamos pygame
pygame.init()    # Llamamos la mètodo inicializador
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))    # Pedimos a pygame que cree una ventana para nuestro programa con esta funciòn --> pasamos el ancho y la altura deseados de la ventana como argumentos
clock = pygame.time.Clock()    # Esta funciòn crea un objeto clock que se usa en la parte inferiro de nuestro buble principal para mantener nuestra tasa màxima de fotogramas.

# 4 - Cargar recursos: image(s), sound(s), etc.
ballImage = pygame.image.load('PygameDemo3_MoveByKeyboard/images/ball.png')
targetImage = pygame.image.load('PygameDemo3_MoveByKeyboard/images/target.jpg')

# 5 - Inicializar variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)    # Creamos una rectagulo

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

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballX = ballX - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ballX = ballX + N_PIXELS_TO_MOVE
            elif event.key == pygame.K_UP:
                ballY = ballY - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                ballY = ballY + N_PIXELS_TO_MOVE

    ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    if ballRect.colliderect(targetRect):
        print('Ball is touching the target')

    # 8 - Do any "per frame" actions
    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    # draw ball at position 100 across (x) and 200 down (y)
    window.blit(targetImage, (TARGET_X, TARGET_Y))
    window.blit(ballImage, (ballX, ballY))

    # 11 - Update the windown
    pygame.display.update()
    
    # 12 - Show things down a bit
    clock.tick(FRAMES_PER_SECOND)    # make pygame wait