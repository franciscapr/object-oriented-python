# Programa de prueba usando cuentas
# Versión 1, usando variables explícitas para cada objeto Account

# Importar todo el código desde el archivo de la clase Account
from Account import *

# Crear dos cuentas
oJoesAccount = Account('Joe', 100, 'JoePassword')
print('Se ha creado una cuenta para Joe')

oMarysAccount = Account('Mary', 12345, 'MarysPassword')
print('Se ha creado una cuenta para Mary')

oJoesAccount.show()
oMarysAccount.show()
print()

# Llamar algunos métodos en las diferentes cuentas
print('Llamando métodos de las dos cuentas ...')
oJoesAccount.deposit(50, 'JoePassword')
oMarysAccount.withdraw(345, 'MarysPassword')
oMarysAccount.deposit(100, 'MarysPassword')

# Mostrar las cuentas
oJoesAccount.show()
oMarysAccount.show()

# Crear otra cuenta con información ingresada por el usuario
print()

userName = input('¿Cuál es el nombre para la nueva cuenta de usuario? ')
userBalance = input('¿Cuál es el saldo inicial para esta cuenta? ')
userBalance = int(userBalance)
userPassword = input('¿Qué contraseña deseas usar para esta cuenta? ')
oNewAccount = Account(userName, userBalance, userPassword)

# Mostrar la cuenta de usuario recién creada
oNewAccount.show()

# Depositar 100 en la nueva cuenta
oNewAccount.deposit(100, userPassword)
userBalance = oNewAccount.getBalance(userPassword)
print()
print('Después de depositar 100, el saldo del usuario es:', userBalance)

# Mostrar la nueva cuenta
oNewAccount.show()
