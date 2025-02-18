# Clase Stack (Pila)

class Stack():
    """La clase Stack implementa un algoritmo LIFO (último en entrar, primero en salir)"""
    
    def __init__(self, startingStackAsList=None):
        if startingStackAsList is None:
            self.dataList = []
        else:
            self.dataList = startingStackAsList[:]  # hacer una copia

    def push(self, item):
        self.dataList.append(item)

    def pop(self):
        if len(self.dataList) == 0:
            raise IndexError
        element = self.dataList.pop()
        return element
    
    def peek(self):
        # Obtener el elemento superior sin eliminarlo
        item = self.dataList[-1]
        return item
    
    def getSize(self):
        nElements = len(self.dataList)
        return nElements
    
    def show(self):
        # Mostrar la pila en una orientación vertical
        print('La pila es:')
        for value in reversed(self.dataList):
            print(' ', value)
