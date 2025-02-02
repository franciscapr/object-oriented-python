# Programa de prueba usando cuentas
# Versión 2, usando una lista de cuentas

# Importar todo el código desde el archivo de la clase Account
from Account import *

# Comenzamos con una lista vacía de cuentas
accountsList = []    # 1.Creamos una lista vacía de cuentas

# Crear dos cuentas
oAccount = Account('Joe', 100, 'JoesPassword')    # 2.Creamos una objeto de cuenta para Joe
accountsList.append(oAccount)    # 3.Agregamos el objeto de cuenta de Joe a la lista mediante el mètodo append()
print('La cuenta de Joe tiene el número de cuenta 0')

oAccount = Account('Mary', 12345, 'MarysPassword')
accountsList.append(oAccount)
print('La cuenta de Mary tiene el número de cuenta 1')

accountsList[0].show()    # Visualizamos la cuenta con el índice 0
accountsList[1].show()    # Visualizamos la cuenta con el índice 1
print()

# Llamar algunos métodos en las diferentes cuentas
print('Llamando métodos de las dos cuentas...')
accountsList[0].deposit(50, 'JoesPassword')
accountsList[1].withdraw(345, 'MarysPassword')

# Mostrar las cuentas
accountsList[0].show()
accountsList[1].show()

# Crear otra cuenta con información ingresada por el usuario
print()
userName = input('¿Cuál es el nombre para la nueva cuenta de usuario? ')
userBalance = input('¿Cuál es el saldo inicial para esta cuenta? ')
userBalance = int(userBalance)
userPassword = input('¿Qué contraseña deseas usar para esta cuenta? ')
oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount)    # Agregar a la lista de cuentas

# Mostrar la cuenta de usuario recién creada
print('Cuenta creada, el número de cuenta es 2')
accountsList[2].show()

# Depositar 100 en la nueva cuenta
accountsList[2].deposit(100, userPassword)
userBalance = accountsList[2].getBalance(userPassword)
print()
print('Después de depositar 100, el saldo del usuario es:', userBalance)

# Mostrar la nueva cuenta
accountsList[2].show()
