# Clase DimmerSwitch

class DimmerSwitch():
    def __init__(self, lebel):
        self.lebel = lebel
        self.swithIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.swithIsOn = True  # Encender el interruptor

    def turnOff(self):
        self.swithIsOn = False  # Apagar el interruptor

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1  # Aumentar el nivel de brillo

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1  # Disminuir el nivel de brillo

    # Método extra para depuración
    def show(self):
        print('¿El interruptor está encendido?', self.swithIsOn)
        print('El nivel de brillo es:', self.brightness)


oDimmer1 = DimmerSwitch('Dimmer1')
oDimmer2 = DimmerSwitch('Dimmer2')

oDimmer1.raiseLevel()
oDimmer2.raiseLevel()
oDimmer1.show()
oDimmer2.show()