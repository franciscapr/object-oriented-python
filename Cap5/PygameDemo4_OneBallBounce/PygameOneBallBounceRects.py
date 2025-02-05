# Pygame Demo 4 (b) - Una imagen que rebota dentro de la ventana usando rectángulos

# 1 - Importar librerías
import pygame
from pygame.locals import *
import sys
import random

# 2 - Definir constantes
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELES_PER_FRAME = 3

# 3 - Inicializar el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Cargar recursos: imagen(es), sonido(s), etc.
ballImage = pygame.image.load('Cap5/PygameDemo4_OneBallBounce/images/ball.png')
bounceSound = pygame.mixer.Sound('Cap5/PygameDemo4_OneBallBounce/sounds/boing.wav')    # Importamos el sonido

# 5 - Inicializar variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELES_PER_FRAME
ySpeed = N_PIXELES_PER_FRAME

# 6 - Bucle infinito
while True:
    # 7 - Verificar y manejar eventos
    for event in pygame.event.get():
        # ¿Se hizo clic en el botón de cerrar? Salir de pygame y terminar el programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Realizar acciones por cada fotograma
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed  # Invertir dirección en X
        bounceSound.play()    # Reproducimos el sonido

    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed  # Invertir dirección en Y
        bounceSound.play()    # Reproducimos el sonido

    # Actualizar el rectángulo de la pelota usando la velocidad en dos direcciones
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

    # 9 - Limpiar la ventana antes de volver a dibujar
    window.fill(BLACK)

    # 10 - Dibujar los elementos en la ventana
    window.blit(ballImage, ballRect)

    # 11 - Actualizar la ventana
    pygame.display.update()

    # 12 - Reducir la velocidad del bucle
    clock.tick(FRAMES_PER_SECOND)
