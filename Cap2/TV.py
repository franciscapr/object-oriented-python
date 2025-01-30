# Clase TV

class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        # Lista de algunos canales predeterminados
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0    # constante
        self.VOLUME_MAXIMUM = 10    # constante
        self.volume = self.VOLUME_MAXIMUM // 2  # división entera

    def power(self):
        self.isOn = not self.isOn    # alternar estado de encendido

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False    # cambiar el volumen mientras está silenciado desactiva el silencio
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False    # cambiar el volumen mientras está silenciado desactiva el silencio
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1

    def channelUp(self):
        if not self.isOn:
            return 
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex == self.nChannels:
            self.channelIndex = 0    # volver al primer canal cuando se llega al final

    def chanelDown(self):  # (Nota: hay un error tipográfico en el nombre de este método)
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1    # volver al último canal si se retrocede desde el primer canal

    def channelDown(self):  # (Este método está repetido, lo correcto es tener solo uno)
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1    # volver al último canal si se retrocede desde el primer canal

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted  # alternar el estado de silencio

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
        # si el nuevo canal no está en nuestra lista de canales, no hacer nada

    def showInfo(self):
        print()
        print('Estado de la TV:')
        if self.isOn:
            print('    La TV está: Encendida')
            print('    Canal actual:', self.channelList[self.channelIndex])
            if self.isMuted:
                print('    Volumen:', self.volume, '(sonido silenciado)')
            else:
                print('    Volumen:', self.volume)
        else:
            print('    La TV está: Apagada')


# Código de prueba
oTV = TV()  # crear el objeto TV

# Encender la TV y mostrar el estado
oTV.power()
oTV.showInfo()

# Subir el canal dos veces y aumentar el volumen dos veces, luego mostrar el estado
oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

# Apagar la TV, mostrar el estado, encenderla nuevamente y mostrar el estado
oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

# Bajar el volumen, silenciar el sonido y mostrar el estado
oTV.volumeDown()
oTV.mute()
oTV.showInfo()

# Cambiar al canal 11
oTV.setChannel(11)
oTV.mute()
oTV.showInfo()
