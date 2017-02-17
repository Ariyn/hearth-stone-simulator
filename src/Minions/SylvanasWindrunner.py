#! SylvanasWindrunner
from ..Minion import Minion
from ..Decorators import *
import random

@DeathRattle
def callEnemy(self, ownPlayer, ownMinion):
	opPlayer = self.Opponent(ownPlayer)
	
	aliveMinions = [i for i in self.field[opPlayer.name] if i and i.health > 0]
	length = len(aliveMinions)
	target = random.sample(aliveMinions, 1)[0]
	
	index = self.field[ownPlayer.name].index(ownMinion)

	self.field[opPlayer.name].remove(target)
	self.field[ownPlayer.name].insert(index, target)

minion = Minion("Sylvanas Windrunner", 6, 6, 5)
minion.abilities.append(callEnemy)