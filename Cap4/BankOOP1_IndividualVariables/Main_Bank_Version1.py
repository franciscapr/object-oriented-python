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
