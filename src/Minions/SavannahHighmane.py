from ..Minion import Minion
from ..Decorators import *

@DeathRattle
def summon2Hyenas(self, ownPlayer, ownMinion):
	self.Summon(ownPlayer, hyena, effect = True)
	self.Summon(ownPlayer, hyena, effect = True)

minion = Minion("Savannah Highmane", 6, 6, 5, "Beast")
minion.abilities.append(summon2Hyenas)
hyena = Minion("Hyena", 2, 2, 2, "Beast")