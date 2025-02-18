# Programa principal de ejemplo de un club

from Club import *

# Crear un club con un máximo de 5 miembros

oProgrammingClub = Club('Programming', 5)

oProgrammingClub.addMember('Joe Schmoe')
oProgrammingClub.addMember('Cindy Lou Hoo')
oProgrammingClub.addMember('Dino Richmond')
oProgrammingClub.addMember('Susie Sweetness')
oProgrammingClub.addMember('Fred Farkle')
oProgrammingClub.report()


# Intento de agregar un miembro adicional
oProgrammingClub.addMember('Iwanna Join')