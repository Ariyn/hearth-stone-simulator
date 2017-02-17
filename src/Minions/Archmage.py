from ..Minion import Minion
from ..Decorators import *

@EffectOn
def spellPower(self, ownPlayer, ownMinion):
	ownPlayer.AddSpellDamage(1, minion)

@EffectOff
def spellPowerDown(self, ownPlayer, ownMinion):
	ownPlayer.RemoveSpellDamage(1, minion)

minion = Minion("Archmage", 6, 4, 7)
minion.abilities.append(spellPower)
minion.abilities.append(spellPowerDown)