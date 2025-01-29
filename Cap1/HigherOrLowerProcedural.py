import random

# Constantes de cartas
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')  # Palos: Espadas, Corazones, Tréboles, Diamantes
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')  # Rangos de cartas

NCARDS = 8  # Número de cartas a jugar por partida

# Recibe un mazo y devuelve una carta aleatoria del mazo
def getCard(deckListIn):
    thisCard = deckListIn.pop()  # Extrae una carta de la parte superior del mazo y la devuelve
    return thisCard

# Recibe un mazo y devuelve una copia barajada del mismo
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # Hace una copia del mazo original
    random.shuffle(deckListOut)  # Baraja las cartas
    return deckListOut

# Código principal
print('Bienvenido a Higher or Lower.')
print('Debes elegir si la siguiente carta que se mostrará será mayor o menor que la carta actual.')
print('Si aciertas, ganas 20 puntos; si te equivocas, pierdes 15 puntos.')
print('Empiezas con 50 puntos.')
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}  # Se asigna un valor numérico a cada carta
        startingDeckList.append(cardDict)

score = 50  # Puntaje inicial

while True:  # Permite jugar múltiples partidas
    print()
    gameDeckList = shuffle(startingDeckList)  # Baraja el mazo
    currentCardDict = getCard(gameDeckList)  # Extrae la primera carta
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('La carta inicial es:', currentCardRank + ' de ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):  # Juega una partida con este número de cartas
        answer = input('¿La siguiente carta será mayor o menor que ' + currentCardRank + ' de ' + currentCardSuit + '? (ingresa "h" o "l"): ')
        answer = answer.casefold()  # Convierte la respuesta a minúsculas
        nextCardDict = getCard(gameDeckList)  # Extrae la siguiente carta
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('La siguiente carta es: ' + nextCardRank + ' de ' + nextCardSuit)

        if answer == 'h':  # Si el jugador eligió "mayor"
            if nextCardValue > currentCardValue:
                print('¡Correcto, era mayor!')
                score = score + 20
            else:
                print('Lo siento, no era mayor.')
                score = score - 15
        elif answer == 'l':  # Si el jugador eligió "menor"
            if nextCardValue < currentCardValue:
                score = score + 20
                print('¡Correcto, era menor!')
            else:
                score = score - 15
                print('Lo siento, no era menor.')
        
        print('Tu puntaje es:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue  # No es necesario actualizar el palo actual

    goAgain = input('Para jugar de nuevo, presiona ENTER, o "q" para salir: ')
    if goAgain == 'q':
        break

print('¡Hasta luego!')
