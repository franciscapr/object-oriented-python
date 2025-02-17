# pygame demo 9 - Prueba de 3 botones con callbacks

# 1 - Importar paquetes
import pygame
from pygame.locals import *
from SimpleButton import *
import sys

# 2 - Definir constantes
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

# Definir una función para usar como "callback"
def myCallBackFunction():
    print('El usuario presionó el Botón B, se llamó a myCallBackFunction')

# Definir una clase con un método para usar como "callback"
class CallBackTest():
    def __init__(self):
        pass

    def myMethod(self):
        print('El usuario presionó el Botón C, se llamó a myMethod del objeto CallBackTest')

# 3 - Inicializar el entorno
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Cargar recursos: imágenes, sonidos, etc.

# 5 - Inicializar variables

oCallBackTest = CallBackTest()
# Crear instancias de SimpleButton
# Sin callback

oButtonA = SimpleButton(window, (25, 30), 'Cap6/PygameDemo9_SimpleButtonWithCallback/images/buttonAUp.png',
                        'Cap6/PygameDemo9_SimpleButtonWithCallback/images/buttonADown.png')

# Especificar una función para callback
oButtonB = SimpleButton(window, (150, 30), 
                        'Cap6/PygameDemo9_SimpleButtonWithCallback/images/buttonBUp.png',
                        'Cap6/PygameDemo9_SimpleButtonWithCallback/images/buttonBDown.png',
                        callBack=myCallBackFunction)

# Especificar un método de un objeto para callback
oButtonC = SimpleButton(window, (275, 30),
                        'Cap6/PygameDemo9_SimpleButtonWithCallback/images/buttonCUp.png',
                        'Cap6/PygameDemo9_SimpleButtonWithCallback/images/buttonCDown.png',
                        callBack=oCallBackTest.myMethod)

counter = 0

# 6 - Bucle infinito
while True:
    # 7 - Verificar y manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pasar el evento al botón y verificar si ha sido presionado
        if oButtonA.handleEvent(event):
            print('El usuario presionó el Botón A, manejado en el bucle principal')

    # oButtonB y oButtonC tienen callbacks, no es necesario verificar el resultado de estas llamadas
    oButtonB.handleEvent(event)
    
    oButtonC.handleEvent(event)
        
    # 8 - Realizar acciones "por cuadro"
    counter = counter + 1

    # 9 - Limpiar la ventana
    window.fill(GRAY)

    # 10 - Dibujar todos los elementos de la ventana
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    # 11 - Actualizar la ventana
    pygame.display.update()

    # 12 - Ralentizar un poco el programa
    clock.tick(FRAMES_PER_SECOND)  # Hacer que pygame espere
