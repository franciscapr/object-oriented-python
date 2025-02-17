# Demostración de Pygame con texto y botones

# 1 - Importar paquetes
import pygame
from pygame.locals import *
import sys
import random
import pygwidgets

# 2 - Definir constantes
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3
BALL_WIDTH_HEIGHT = 100

# 3 - Inicializar el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Cargar recursos: imágenes, sonidos, etc.

# 5 - Inicializar variables
oBall = pygwidgets.Image(window, (0, 0), 'Cap7/PygameDemo10_ImageTextButtonBall/images/ball.png')  # Se crea el objeto
ballLeft = 0
ballTop = 0

MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

oBackground = pygwidgets.Image(window, (0, 0), 'Cap7/PygameDemo10_ImageTextButtonBall/images/background.jpg')

oRestartButton = pygwidgets.CustomButton(window, (500, 430), 
                                        up='Cap7/PygameDemo10_ImageTextButtonBall/images/restartUp.png', 
                                        down='Cap7/PygameDemo10_ImageTextButtonBall/images/restartDown.png', 
                                        over='Cap7/PygameDemo10_ImageTextButtonBall/images/restartOver.png', 
                                        disabled= 'Cap7/PygameDemo10_ImageTextButtonBall/images/restartDisabled.png')

oHitMeButton = pygwidgets.TextButton(window, (500, 370), 'Golpéame')

oMessageTextA = pygwidgets.DisplayText(window, (20, 50), 'Aquí hay un texto', 
                                    fontSize=36, textColor=WHITE)

oMessageTextB = pygwidgets.DisplayText(window, (20, 150),
                                       'Aquí hay más texto\nY más texto\nE incluso más texto', 
                                       fontSize=36, textColor=WHITE, justified='center')

oUserInputA = pygwidgets.InputText(window, (20, 350), '', 
                                  fontSize=24, textColor=BLACK, backgroundColor=WHITE)

oUserInputB= pygwidgets.InputText(window, (20, 430), '', width = 400, 
                                  fontSize=24, textColor=WHITE, backgroundColor=BLACK)

counter = 0

# 6 - Bucle infinito
while True:

    # 7 - Comprobar y manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if  oRestartButton.handleEvent(event):
                counter = 0

        if  oHitMeButton.handleEvent(event):
                print('No me golpees')

        if oUserInputA.handleEvent(event):
            userText = oUserInputA.getText()
            print('En el primer campo, el usuario ingresó:', userText)

        if oUserInputB.handleEvent(event):
            userText = oUserInputB.getText()
            print('En el segundo campo, el usuario ingresó:', userText)


    # 8 - Acciones por fotograma
    counter = counter + 1
    oMessageTextA.setValue('Aquí hay un texto. Contador de bucle: ' + str(counter))

    ballLeft, ballRight = oBall.getLoc()

    if (ballLeft < 0) or (ballLeft + BALL_WIDTH_HEIGHT >= WINDOW_WIDTH):
        xSpeed = -xSpeed  # Invertir dirección en X

    if (ballTop < 0) or (ballTop + BALL_WIDTH_HEIGHT >= WINDOW_HEIGHT):
        ySpeed = -ySpeed  # Invertir dirección en Y

    # Actualizar la posición de la pelota en función de la velocidad en ambas direcciones
    ballLeft = ballLeft + xSpeed
    ballTop = ballTop + ySpeed
    oBall.setLoc( (ballLeft, ballTop ))


    # 9 - Limpiar la ventana antes de volver a dibujar
    oBackground.draw()  # Dibujar la imagen de fondo
                          
    # 10 - Dibujar los elementos en la ventana
    oBall.draw()

    oRestartButton.draw()
    oHitMeButton.draw()

    oMessageTextA.draw()
    oMessageTextB.draw()

    oUserInputA.draw()
    oUserInputB.draw()

    # 11 - Actualizar la ventana
    pygame.display.update()

    # 12 - Ralentizar la ejecución
    clock.tick(FRAMES_PER_SECOND)  # Hacer que pygame espere
