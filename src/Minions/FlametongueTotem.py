#FlametongueTotem

from ..Minion import Minion
from ..Decorators import *

@EffectOn
def spellPower(self, ownPlayer, ownMinion):
	ownPlayer.AddSpellDamage(1, minion)

@EffectOff
def spellPowerDown(self, ownPlayer, ownMinion):
	ownPlayer.RemoveSpellDamage(1, minion)

minion = Minion("Flametongue Totem", 2, 0, 3)
minion.abilities.append(spellPower)
minion.abilities.append(spellPowerDown)