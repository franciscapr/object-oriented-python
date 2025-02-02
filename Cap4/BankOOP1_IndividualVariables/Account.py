# Clase Account

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        
        if amountToDeposit < 0:
            print('You cannot deposit a negative amount')
            return None
        
        self.balance = self.balance + amountToDeposit
        return self.balance
    
    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Incorrect password for this account')
            return None
        
        if amountToWithdraw > self.balance:
            return self.balance
        
    def getBalance(self, password):
        if password != self.password:
            print('SOrry, incorrect password')
            return None
        return self.balance
    
    # Added for debugging
    def show(self):
        print('     Name:', self.name)
        print('     Balance:', self.balance)
        print('     Password:', self.password)
        print()

# Instanciaciòn
oAccount = Account('Joe Schmoe', 1000, 'magic')
oAccount.show()

newBalance = oAccount.deposit(500, 'magic')
oAccount.show()

oAccount.withdraw(250, 'magic')
oAccount.show()

currentBalance = oAccount.getBalance('magic')
oAccount.show()
