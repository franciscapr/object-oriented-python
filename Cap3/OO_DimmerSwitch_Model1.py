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


# Create first DimmerSwicth, turn it on, and raise the level twice
oDimmer1 = DimmerSwitch('Dimmer1')
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()

# Create second DimmerSwitch, turn it on, and raise the level 3 times
oDimmer2 = DimmerSwitch('Dimmer2')
oDimmer2.turnOn()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()

# Craete third DimmerSwitch, using the default settings 
oDimmer3 = DimmerSwitch('Dimmer3')

# Ask each switch to show itself
oDimmer1.show()
oDimmer2.show()
oDimmer3.show()