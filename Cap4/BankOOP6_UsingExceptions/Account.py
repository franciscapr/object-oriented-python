# Clase Account
# Error indicated by 'raise' statemnets

# Definimos nuestra excepciòn personalizada
class AbortTransaction(Exception):
    """raise this exception to abort a bank transaction"""
    pass




class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    # Verificamos que el saldo inicial sea valido
    def validateAmount(self, amount):
        # Usamos try/except para asegurarnos de que le monto inicial pued convertise en un numero entero
        try:
            amount = int(amount)
            # Si falla lanza una excepciòn ValueError genèrico 
        except ValueError:
            # Se ejecuta la sentencia raise lanzando la excepciòn AbortTransaction
            raise AbortTransaction('Amount must be an integer')
        if amount <= 0:
            raise AbortTransaction('Amount mus be positive')
        return amount
    
    def checkPasswordMatch(self, password):
        if password != self.password:
            raise AbortTransaction('Incorrect password for this account')
        

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
