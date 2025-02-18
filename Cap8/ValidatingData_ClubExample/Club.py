# Clase Club

class Club():

    def __init__(self, clubName, maxMembers):
        self.clubName = clubName
        self.maxMembers = maxMembers
        self.membersList = []

    def addMember(self, name):
        # Asegurarse de que haya suficiente espacio disponible
        if len(self.membersList) < self.maxMembers:
            self.membersList.append(name)
            print('OK.', name, 'ha sido añadido al club', self.clubName, 'club')
        else:
            print('Lo siento, pero no podemos agregar a', name, 'al club', self.clubName + '.')
            print('Este club ya alcanzó el máximo de', self.maxMembers, 'miembros.')

    def report(self):
        print()
        print('Estos son los', len(self.membersList), 'miembros del club', self.clubName + ':')
        for name in self.membersList:
            print(' ' + name)
        print()
