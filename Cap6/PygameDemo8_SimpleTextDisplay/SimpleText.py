# Clase SimpleText

import pygame
from pygame.locals import *

class SimpleText():

    def __init__(self, window, loc, value, textColor):
        pygame.font.init()
        self.window = window
        self.loc = loc
        self.font = pygame.font.SysFont(None, 30)
        self.textColor = textColor
        self.text = None    # Para que la llamada a setText abajo
        # obligue a la creación de la imagen del texto
        self.setValue(value)    # Establecer el texto inicial para dibujarlo

    def setValue(self, newText):
        if self.text == newText:
            return    # No hay nada que cambiar
        self.text = newText    # Guardar el nuevo texto
        self.textSurface = self.font.render(self.text, True, self.textColor)

    def draw(self):
        self.window.blit(self.textSurface, self.loc)
