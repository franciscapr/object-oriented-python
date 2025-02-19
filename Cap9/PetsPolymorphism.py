# Polimorfismo de mascotas
# Tres clases, cada una con un método "speak" (hablar) diferente

class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'dice bark, bark, bark!')

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'dice meeeoooow')

class Bird():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'dice tweet')


oDog1 = Dog('Rover')
oDog2 = Dog('Fido')
oCat1 = Cat('Fluffly')
oCat2 = Cat('Spike')
oBird = Bird('Big Bird')

petsList = [oDog1, oDog2, oCat1, oCat2, oBird]

# Enviar el mismo mensaje (llamar al mismo método) a todas las mascotas
for oPet in petsList:
    oPet.speak()