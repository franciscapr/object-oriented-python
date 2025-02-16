# pygame demo 8 - SimpleText, SimpleButton y Ball

# 1 - Importar paquetes
import pygame
from pygame.locals import *
import sys
import random

from Ball import *    # Importar el código de la clase Ball
from SimpleText import *
from SimpleButton import *

# 2 - Definir constantes
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Inicializar el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Cargar recursos: imágenes, sonidos, etc.

# 5 - Inicializar variables
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oFrameCountLabel = SimpleText(window, (10, 20),
                              'El programa ha ejecutado esta cantidad de ciclos: ', WHITE)
oFrameCountDisplay = SimpleText(window, (520, 20), '', WHITE)
oRestartButton = SimpleButton(window, (280, 60), 'Cap6/PygameDemo8_SimpleTextDisplay/images/restartUp.png',
                              'Cap6/PygameDemo8_SimpleTextDisplay/images/restartDown.png')
frameCounter = 0

# 6 - Bucle infinito
while True:
    # 7 - Comprobar y manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oRestartButton.handleEvent(event):
            frameCounter = 0    # Se hizo clic en el botón, reiniciar el contador

    # 8 - Realizar acciones "por fotograma"
    oBall.update()    # Indicar a la pelota que se actualice
    frameCounter = frameCounter + 1    # Incrementar en cada fotograma
    oFrameCountDisplay.setValue(str(frameCounter))

    # 9 - Limpiar la ventana antes de volver a dibujarla
    window.fill(BLACK)

    # 10 - Dibujar los elementos de la ventana
    oBall.draw()    # Indicar a la pelota que se dibuje
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    # 11 - Actualizar la ventana
    pygame.display.update()

    # 12 - Reducir la velocidad del bucle
    clock.tick(FRAMES_PER_SECOND)
