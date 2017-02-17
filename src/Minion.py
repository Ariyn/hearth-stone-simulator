from .Card import Card

class Minion(Card):
	def __init__(self, name, coast, attack, health, race="normal",
				charge = False, taunt = False):
		self.abilities = []
		
		self.name = name
		self.attack, self.health, self.coast = attack, health, coast
		self.race = race,
		self.summonTurn = 0
		
		self.dead = False
		self.taunt = taunt
		self.charge = charge
	
	def __str__(self):
		return "%s(%d|%d/%d)"%(self.name, self.coast, self.attack, self.health)
	
	def __repr__(self):
		return self.__str__()
	
	def Damage(self, opCard):
		self.health -= opCard.attack
		if self.health <= 0:
			self.dead = True
	
	# TODO:
	# change this to decorator
	def RunBattleCry(self, gameEngine, ownPlayer, ownMinion):
		for func in self.abilities:
			try:
				at = getattr(func, "abilityType")
				if at == "BattleCry":
					func(gameEngine, ownPlayer, ownMinion)
			except AttributeError as e:
				pass

	def RunEffectOn(self, gameEngine, ownPlayer, ownMinion):
		for func in self.abilities:
			try:
				at = getattr(func, "abilityType")
				if at == "EffectOn":
					func(gameEngine, ownPlayer, ownMinion)
			except AttributeError as e:
				pass
				
	def RunEffectOff(self, gameEngine, ownPlayer, ownMinion):
		for func in self.abilities:
			try:
				at = getattr(func, "abilityType")
				if at == "EffectOff":
					func(gameEngine, ownPlayer, ownMinion)
			except AttributeError as e:
				pass

	def RunDeathRattles(self, gameEngine, ownPlayer, ownMinion):
		for func in self.abilities:
			at = getattr(func, "abilityType")

			if at == "DeathRattle":
				func(gameEngine, ownPlayer, ownMinion)