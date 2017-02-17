from ..Minion import Minion
from ..Decorators import *

@BattleCry
def summonMD(self, ownPlayer, ownMinion):
	self.Summon(ownPlayer, md, effect = True)

minion = Minion("Dragonling Mechanic", 4, 2, 4)
minion.abilities.append(summonMD)
md = Minion("Mechanical Dragonling", 1, 2, 1, "Mech")