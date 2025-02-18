# Programa principal de ejemplo de la clase Person utilizando getters y setters

from Person import *

oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('Jane Smith', 99000)

# Obtener los salarios usando el getter y mostrarlos
print(oPerson1.getSalary())
print(oPerson2.getSalary())

# Cambiar los salarios usando el setter
oPerson1.setSalary(100000)
oPerson2.setSalary(111111)

# Obtener los salarios y mostrarlos nuevamente
print(oPerson1.getSalary())
print(oPerson2.getSalary())
