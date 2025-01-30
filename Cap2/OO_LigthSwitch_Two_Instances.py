# OO_LightSwitch

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # Encender el interruptor
        self.switchIsOn = True

    def turnOff(self):
        # Apagar el interruptor
        self.switchIsOn = False

    def show(self):  # Agregado para pruebas
        print(self.switchIsOn)

# Código principal
oLightSwitch1 = LightSwitch()  # Crear un objeto LightSwitch
oLightSwitch2 = LightSwitch()  # Crear otro objeto LightSwitch

# Código de prueba
oLightSwitch1.show()
oLightSwitch2.show()
oLightSwitch1.turnOn()  # Encender el interruptor 1
# El interruptor 2 debería estar apagado al inicio, pero esto lo hace más claro
oLightSwitch2.turnOff()
oLightSwitch1.show()
oLightSwitch2.show()
