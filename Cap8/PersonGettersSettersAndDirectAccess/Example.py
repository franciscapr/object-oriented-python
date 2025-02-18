class Example():
    def __init__(self, startingValue):
        self._x = startingValue

    @property
    def x(self):    # Este es el método getter decorado
        return self._x
    
    @x.setter
    def x(self, value):    # Este es el método setter decorado
        self._x = value


oExample = Example(10)
print(oExample.x)
oExample.x = 20