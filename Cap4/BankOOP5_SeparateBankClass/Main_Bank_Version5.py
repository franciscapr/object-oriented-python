# Programa principal para controlar un Banco compuesto por Cuentas

# Importar todo el código de la clase Bank
from Bank import *

# Crear una instancia del Banco
oBank = Bank()

# Código principal
# Crear dos cuentas de prueba
joesAccountNumber = oBank.createAccount('Joe', 100, 'JoesPassword')
print("El número de cuenta de Joe es:", joesAccountNumber)

marysAccountNumber = oBank.createAccount('Mary', 12345, 'MarysPassword')
print("El número de cuenta de Mary es:", marysAccountNumber)

while True:    # 1.Pedimos al usuario la acciòn
    print()
    print('Para obtener el saldo de una cuenta, presione b')
    print('Para cerrar una cuenta, presione c')
    print('Para hacer un depósito, presione d')
    print('Para obtener información del banco, presione i')
    print('Para abrir una nueva cuenta, presione o')
    print('Para salir, presione q')
    print('Para mostrar todas las cuentas, presione s')
    print('Para hacer un retiro, presione w')
    print()

    action = input('¿Qué desea hacer? ')
    action = action.lower()
    action = action[0]  # Tomar la primera letra
    print()
    
    # Llamamos al mètodo apropiado en el objeto bank para realizar el trabajo
    if action == 'b':
        oBank.balance()

    # Solicirud de cierre --> se elimina la cuenta
    elif action == 'c':
        oBank.closeAccount()

    elif action == 'd':
        oBank.deposit()

    elif action == 'i':
        oBank.bankInfo()

    elif action == 'o':
        oBank.openAccount()

    elif action == 's':
        oBank.show()

    elif action == 'q':
        break

    elif action == 'w':
        oBank.withdraw()

    else:
        print('Lo siento, esa no fue una acción válida. Inténtelo de nuevo.')
        
print('Finalizado')
