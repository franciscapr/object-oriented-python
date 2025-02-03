# Banco que gestiona un diccionario de objetos Account

from Account import *

class Bank():

    def __init__(self):
        self.accountsDict = {}    # Variable de instancia
        self.nextAccountNumber = 0    # Variable de instancia

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        # Incrementar para preparar la creación de la siguiente cuenta
        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber
    
    def openAccount(self):
        print('*** Abrir Cuenta ***')
        userName = input('¿Cuál es el nombre del titular de la nueva cuenta? ')
        userStartingAmount = input('¿Cuál es el saldo inicial para esta cuenta? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('¿Cuál es la contraseña que desea usar para esta cuenta? ')
        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Su nuevo número de cuenta es:', userAccountNumber)
        print()

    def closeAccount(self):
        print('*** Cerrar Cuenta ***')
        userAccountNumber = input('¿Cuál es su número de cuenta? ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('¿Cuál es su contraseña? ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)
        if theBalance is not None:
            print('Tenía', theBalance, 'en su cuenta, que le será devuelto.')
            # Eliminar la cuenta del usuario del diccionario de cuentas
            del self.accountsDict[userAccountNumber]
            print('Su cuenta ha sido cerrada.')

    def balance(self):
        print('*** Obtener Saldo ***')
        userAccountNumber = input('Por favor, ingrese su número de cuenta: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Por favor, ingrese la contraseña: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Su saldo es:', theBalance)

    def deposit(self):
        print('*** Depósito ***')
        accountNum = input('Por favor, ingrese el número de cuenta: ')
        accountNum = int(accountNum)
        depositAmount = input('Por favor, ingrese el monto a depositar: ')
        depositAmount = int(depositAmount)
        userAccountPassword = input('Por favor, ingrese la contraseña: ')
        oAccount = self.accountsDict[accountNum]        
        theBalance = oAccount.deposit(depositAmount, userAccountPassword)
        if theBalance is not None:
            print('Su nuevo saldo es:', theBalance)

    def show(self):
        print('*** Mostrar ***')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('   Número de cuenta:', userAccountNumber)
            oAccount.show()

    def withdraw(self):
        print('*** Retiro ***')
        userAccountNumber = input('Por favor, ingrese su número de cuenta: ')
        userAccountNumber = int(userAccountNumber)
        userAmount = input('Por favor, ingrese el monto a retirar: ')
        userAmount = int(userAmount)
        userAccountPassword = input('Por favor, ingrese la contraseña: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userAmount, userAccountPassword)
        if theBalance is not None:
            print('Retirado:', userAmount)
            print('Su nuevo saldo es:', theBalance)

    def bankInfo(self):
        print('Horario: 9 a 5')
        print('Dirección: 123 Main Street, Anytown, USA')
        print('Teléfono: (650) 555-1212')
        print('Actualmente tenemos', len(self.accountsDict), 'cuenta(s) abierta(s).')
