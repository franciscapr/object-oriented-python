# pygame demo6(a) - usando la clase Ball, hacer rebotar una bola

# 1 - Importar paquetes

import pygame
from pygame.locals import *
import sys
import random
from Ball import *   # Importar el código de la clase Ball

# 2 - Definir constantes
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 300

# 3 - Inicializar el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Cargar recursos: imágenes, sonidos, etc.

# 5 - Inicializar variables
ballList = []

for oBall in range(0, N_BALLS):
    # Cada vez que se ejecuta el bucle, crear un objeto Ball
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)    # Agregar la nueva bola a la lista de bolas

# 6 - Bucle infinito
while True:
    # 7 - Comprobar y manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Realizar acciones "por fotograma"
    for oBall in ballList:
        oBall.update()    # Decirle a cada bola que se actualice
    
    # 9 - Limpiar la ventana antes de volver a dibujarla
    window.fill(BLACK)

    # 10 - Dibujar los elementos de la ventana
    for oBall in ballList:
        oBall.draw()    # Decirle a cada bola que se dibuje

    # 11 - Actualizar la ventana
    pygame.display.update()

    # 12 - Reducir la velocidad de ejecución
    clock.tick(FRAMES_PER_SECOND)
