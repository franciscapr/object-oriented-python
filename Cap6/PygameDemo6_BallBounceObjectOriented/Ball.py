import pygame
from pygame.locals import *
import random


# Clase ball
class Ball():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window    # remember the windown, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load('Cap6/PygameDemo6_BallBounceObjectOriented/images/ball.png')
        # A rect is made uo of [x, y, width, height]
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        # Pick a random starting position
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # CHooise a random speed between -4 and 4, but not zero, in both the x and y directions
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        # Check for hitting a wall. If so, change that diretion.
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed

        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed

        # Update the ball's x and y, using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

