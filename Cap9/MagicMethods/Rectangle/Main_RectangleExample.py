

import pygame
import sys
from pygame.locals import *
from Rectangle import *

# Definir las constantes
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_RECTANGLES = 10
FIRST_RECTANGLE = 'first'
SECOND_RECTANGLE = 'second'

# Configurar la ventana
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

rectanglesList = []
for i in range(0, N_RECTANGLES):
    oRectangle = Rectangle(window)
    rectanglesList.append(oRectangle)

whichRectangle = FIRST_RECTANGLE

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            for oRectangle in rectanglesList:
                if oRectangle.clickedInside(event.pos):
                    print('CLicked on', whichRectangle, 'rectangle.')

                    if whichRectangle ==  FIRST_RECTANGLE:
                        oFirstRectangle = oRectangle
                        whichRectangle = SECOND_RECTANGLE

                    elif whichRectangle == SECOND_RECTANGLE:
                        oSecondRectangle =  oRectangle
                        # El usuario ha seleccionado 2 rectángulos, comparemos
                        if oFirstRectangle == oSecondRectangle:
                            print('Los rectángulos tienen el mismo tamaño.')
                        elif oFirstRectangle < oSecondRectangle:
                            print('El primer rectángulo es más pequeño que el segundo rectángulo.')
                        else:    # must be larger
                            print('El primer rectángulo es más grande que el segundo rectángulo.')
                        whichRectangle = FIRST_RECTANGLE

    # Limpiar la ventana y dibujar todos los rectángulos    
    window.fill(WHITE)
    for oRectangle in rectanglesList:
        oRectangle.draw()
    
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)