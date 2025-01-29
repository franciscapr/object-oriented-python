# OO_LightSwitch

class LightSwitch():
    def __init__(self):
        self.switchIsON = False

    def turnOn(self):
        # turn the switch on
        self.switchIsON = True

    def turnOff(self):
        # turn the switch off
        self.switchIsON = False


# Busca la clase LightSwitch, crea un objeto LightSwitch a partir de la clase y asigna el objeto resultante a la variable oLightSwitch
oLightSwitch = LightSwitch()