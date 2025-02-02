# Programa de prueba usando cuentas
# Versión 3, usando un diccionario de cuentas

# Importar todo el código desde el archivo de la clase Account
from Account import *

accountsDict = {}    # Creamos un diccionario vacío
nextAccountNumber = 0

# Crear dos cuentas:
oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = oAccount
print('El número de cuenta de Joe es:', joesAccountNumber)
nextAccountNumber = nextAccountNumber + 1

oAccount = Account('Mary', 12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber
accountsDict[marysAccountNumber] = oAccount
print('El número de cuenta de Mary es:', marysAccountNumber)
nextAccountNumber = nextAccountNumber + 1  # Se corrigió que no se incrementaba correctamente

accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
print()

# Llamar algunos métodos en las diferentes cuentas
print('Llamando métodos en las dos cuentas ...')

accountsDict[joesAccountNumber].deposit(50, 'JoesPassword')
accountsDict[marysAccountNumber].withdraw(345, 'MarysPassword')
accountsDict[marysAccountNumber].deposit(100, 'MarysPassword')

# Mostrar las cuentas
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()

# Crear otra cuenta con información ingresada por el usuario
print()
userName = input('¿Cuál es el nombre para la nueva cuenta de usuario? ')
userBalance = input('¿Cuál es el saldo inicial para esta cuenta? ')
userBalance = int(userBalance)
userPassword = input('¿Qué contraseña deseas usar para esta cuenta? ')
oAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = oAccount
print('El número de cuenta de la nueva cuenta es:', newAccountNumber)
nextAccountNumber = nextAccountNumber + 1

# Mostrar la cuenta recién creada
accountsDict[newAccountNumber].show()

# Depositar 100 en la nueva cuenta
accountsDict[newAccountNumber].deposit(100, userPassword)
userBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print()
print('Después de depositar 100, el saldo del usuario es:', userBalance)

# Mostrar la nueva cuenta
accountsDict[newAccountNumber].show()
