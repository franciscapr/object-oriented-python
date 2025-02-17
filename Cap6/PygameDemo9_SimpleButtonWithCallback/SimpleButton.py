# Clase SimpleButton
#
# Utiliza un enfoque de "máquina de estados"
#

import pygame
from pygame.locals import *

class SimpleButton():
    # Se usa para rastrear el estado del botón
    STATE_IDLE = 'idle'  # El botón está arriba, el mouse no está sobre él
    STATE_ARMED = 'armed'  # El botón está presionado, el mouse está sobre él
    STATE_DISARMED = 'disarmed'  # Se hizo clic en el botón, pero el mouse salió de él
        
    def __init__(self, window, loc, up, down, callBack=None):
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)
        self.callBack = callBack

        # Obtener el rectángulo del botón (usado para verificar si el mouse está sobre él)
        self.rect = self.surfaceUp.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = SimpleButton.STATE_IDLE

    def handleEvent(self, eventObj):
        # Este método devolverá True si el usuario hace clic en el botón.
        # Normalmente devuelve False.

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            # El botón solo se preocupa por eventos relacionados con el mouse
            return False

        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        if self.state == SimpleButton.STATE_IDLE:
            if (eventObj.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED

        elif self.state == SimpleButton.STATE_ARMED:
            if (eventObj.type == MOUSEBUTTONUP) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_IDLE
                # Si se especificó una función de callback, llamarla
                if self.callBack != None:
                    self.callBack()
                return True  # ¡Clic realizado!

            if (eventObj.type == MOUSEMOTION) and (not eventPointInButtonRect):
                self.state = SimpleButton.STATE_DISARMED

        elif self.state == SimpleButton.STATE_DISARMED:
            if eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE

        return False

    def draw(self):
        # Dibujar la apariencia actual del botón en la ventana
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown, self.loc)

        else:  # IDLE o DISARMED
            self.window.blit(self.surfaceUp, self.loc)
