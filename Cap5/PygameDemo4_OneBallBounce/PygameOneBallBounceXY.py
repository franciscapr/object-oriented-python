# pygame demo 4(a) - one image, bounce around the windown using (x, y) coords

# 1 - Importaciòn de librerias
import pygame
from pygame.locals import *
import sys
import random

# 2 - Definimos las constantes
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3

# 3 - Inicializamos
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
ballImage = pygame.image.load('PygameDemo4_OneBallBounce/images/ball.png')

# 5 - INitialize variables
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Aquit pygame and end the programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    if(ballX < 0) or (ballX >= MAX_WIDTH):
        xSpeed = -xSpeed    # reverse X direction
    
    if(ballY < 0) or (ballY >= MAX_HEIGHT):
        ySpeed = -ySpeed    # reverse Y direction

    # Update the ball`s location, using the speed in two directions
    ballX = ballX + xSpeed
    ballY = ballY + ySpeed

    # 9 - Clear the windowbefore drawing it again
    window.fill(BLACK)

    # 10 - Draw the window elements
    window.blit(ballImage, (ballX, ballY))

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)