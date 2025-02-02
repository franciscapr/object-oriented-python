# Programa de prueba interactivo que crea un diccionario de cuentas
# Versión 4, con un menú interactivo

from Account import *

accountsDict = {}
nextAccountNumber = 0

# Crear algunas cuentas iniciales para pruebas
oAccount = Account('Joe', 100, 'JoesPassword')
accountsDict[nextAccountNumber] = oAccount
print('El número de cuenta de Joe es:', nextAccountNumber)
# Incrementar el número de cuenta después de la asignación
nextAccountNumber = nextAccountNumber + 1

oAccount = Account('Mary', 12345, 'MarysPassword')
accountsDict[nextAccountNumber] = oAccount
print('El número de cuenta de Mary es:', nextAccountNumber)
nextAccountNumber = nextAccountNumber + 1

while True:
    print()
    print('Presione b para obtener el saldo')
    print('Presione d para hacer un depósito')
    print('Presione o para abrir una nueva cuenta')
    print('Presione w para hacer un retiro')
    print('Presione s para mostrar todas las cuentas')
    print('Presione q para salir')
    print()

    action = input('¿Qué desea hacer? ')
    action = action.lower()
    action = action[0]  # Tomar la primera letra
    print()
    
    if action == 'b':
        print('*** Obtener Saldo ***')
        userAccountNumber = input('Por favor, ingrese su número de cuenta: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Por favor, ingrese la contraseña: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Su saldo es:', theBalance)

    elif action == 'd':
        print('*** Depósito ***')
        userAccountNumber = input('Por favor, ingrese el número de cuenta: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Por favor, ingrese el monto a depositar: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Por favor, ingrese la contraseña: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.deposit(userDepositAmount, userPassword)
        if theBalance is not None:
            print('Su nuevo saldo es:', theBalance)
        
    elif action == 'o':
        print('*** Abrir Cuenta ***')
        userName = input('¿Cuál es el nombre del titular de la nueva cuenta? ')
        userStartingAmount = input('¿Cuál es el saldo inicial para esta cuenta? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('¿Cuál es la contraseña que desea usar para esta cuenta? ')
        oAccount = Account(userName, userStartingAmount, userPassword)
        accountsDict[nextAccountNumber] = oAccount
        print('Su nuevo número de cuenta es:', nextAccountNumber)
        nextAccountNumber = nextAccountNumber + 1
        print()

    elif action == 's':
        print('Mostrar:')
        for userAccountNumber in accountsDict:
            oAccount = accountsDict[userAccountNumber]
            print('   Número de cuenta:', userAccountNumber)
            oAccount.show()

    elif action == 'q':
        break

    elif action == 'w':
        print('*** Retiro ***')
        userAccountNumber = input('Por favor, ingrese su número de cuenta: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawalAmount = input('Por favor, ingrese el monto a retirar: ')
        userWithdrawalAmount = int(userWithdrawalAmount)
        userPassword = input('Por favor, ingrese la contraseña: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithdrawalAmount, userPassword)
        if theBalance is not None:
            print('Retirado:', userWithdrawalAmount)
            print('Su nuevo saldo es:', theBalance)

    else:
        print('Lo siento, esa no es una acción válida. Inténtelo de nuevo.')

print('Finalizado')
