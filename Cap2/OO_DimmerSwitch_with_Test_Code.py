from DimmerSwitch import DimmerSwitch

# Código principal
oDimmer = DimmerSwitch()

# Encender el interruptor y aumentar el nivel 5 veces
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()


# Disminuir el nivel 2 veces y apagar el interruptor
oDimmer.lowerLevel()
oDimmer.lowerLevel()
oDimmer.turnOff()
oDimmer.show()


# Encender el interruptor y aumentar el nivel 3 veces
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()
