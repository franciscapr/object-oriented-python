# Cuadrado

import pygame
import random

# Configurar los colores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Square():
    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.widthAndHeight = random.randrange(10, 100)
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)
        self.rect = pygame.Rect(self.x, self.y, self.widthAndHeight, self.widthAndHeight)
        self.shapeType = 'Square'

    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked
    
    def getType(self):
        return self.shapeType
    
    def getArea(self):
        theArea = self.widthAndHeight * self.widthAndHeight
        return theArea
    
    def __eq__(self, oOtherSquare):
        if not isinstance(oOtherSquare, Square):
            raise TypeError('Second object was not a Square')
        if self.widthAndHeight == oOtherSquare.widthAndHeight:
            return True    # math
        else:
            return False    # Not a match

    
    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.widthAndHeight, self.widthAndHeight))