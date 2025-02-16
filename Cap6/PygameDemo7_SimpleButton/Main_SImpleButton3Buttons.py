# pygame demo 7 - Prueba de 3 botones

# 1 - Importar paquetes
import pygame
from pygame.locals import *
from SimpleButton import *
import sys

# Definir constantes
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

# 2 - Inicializar el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Cargar recursos: imágenes, sonidos, etc.

# 5 - Inicializar variables
# Crear instancias de SimpleButton
oButtonA = SimpleButton(window, (25, 30),
                        'Cap6/PygameDemo7_SimpleButton/images/buttonAUp.png',
                        'Cap6/PygameDemo7_SimpleButton/images/buttonADown.png')
oButtonB = SimpleButton(window, (150, 30),
                        'Cap6/PygameDemo7_SimpleButton/images/buttonBUp.png',
                        'Cap6/PygameDemo7_SimpleButton/images/buttonBDown.png')
oButtonC = SimpleButton(window, (275, 30),
                        'Cap6/PygameDemo7_SimpleButton/images/buttonCUp.png',
                        'Cap6/PygameDemo7_SimpleButton/images/buttonCDown.png')

# 6 - Bucle infinito
while True:

    # 7 - Comprobar y manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pasar el evento a cada botón para ver si se ha hecho clic en alguno
        if oButtonA.handleEvent(event):
            print('El usuario hizo clic en el botón A.')
        elif oButtonB.handleEvent(event):
            print('El usuario hizo clic en el botón B.')
        elif oButtonC.handleEvent(event):
            print('El usuario hizo clic en el botón C.')

    # 8 - Realizar acciones "por fotograma"
    
    # 9 - Limpiar la ventana
    window.fill(GRAY)
    
    # 10 - Dibujar todos los elementos de la ventana
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    # 11 - Actualizar la ventana
    pygame.display.update()

    # 12 - Reducir la velocidad del bucle
    clock.tick(FRAMES_PER_SECOND)  # Hacer que pygame espere
