from ..Minion import Minion
from ..Decorators import *

@Effect("CD")
def damageOn(self, ownPlayer, ownMinion):
	minion.AddDamage(1)

minion = Minion("Frothing Berserker", 3, 2, 4)
minion.abilities.append(damageOn)
