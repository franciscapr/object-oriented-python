# Programa principal de ejemplo de la clase Person utilizando acceso directo

from Person import *

oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('Jane Smith', 99000)

# Obtener los valores de la variable de salario directamente
print(oPerson1.salary)
print(oPerson2.salary)

# Cambiar la variable de salario directamente
oPerson1.salary = 100000
oPerson2.salary = 111111

# Obtener los salarios actualizados y mostrar nuevamente
print(oPerson1.salary)
print(oPerson2.salary)
