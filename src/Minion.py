from .Card import Card

class Minion(Card):
	def __init__(self, name, coast, attack, health, race="normal",
				charge = False, taunt = False):
		self.abilities = []

		self.name = name
		self.attack, self.health, self.coast = attack, health, coast
		self.additionalAttack, self.additionalHealth, self.additionalCoast = 0, 0, 0
		self.race = race,
		self.summonTurn = 0

		self.dead = False
		self.taunt = taunt
		self.charge = charge

	def __str__(self):
		return "%s(%d|%d/%d)"%(self.name, self.coast, self.attack, self.health)

	def __repr__(self):
		return self.__str__()

	def Attack(self):
		return self.attack + self.additionalAttack

	def Health(self):
		return self.health + self.additionalHealth

	def Coast(self):
		return self.coast + self.additionalCoast

	def Damage(self, opCard):
		self.health -= opCard.Attack()

		if self.health <= 0:
			self.dead = True

	def AddDamage(self, amount):
		self.additionalAttack += amount

	# TODO:
	# change this try state to pre compile to set ability type to all abilityies which doesnot have type
	def GetEffects(self, situation=None):
		eff = []
		for i in self.abilities:
			try:
				at = getattr(i, "abilityType")
				if at == "Effect":
					if situation and getattr(i, "EffectSituation") == situation:
						eff.append(i)
					elif not situation:
						eff.append(i)
			except:
				pass
		return eff

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
				at = getattr(func, "abilityRunType")
				if at == "EffectOn":
					func(gameEngine, ownPlayer, ownMinion)
			except AttributeError as e:
				pass

	def RunEffectOff(self, gameEngine, ownPlayer, ownMinion):
		for func in self.abilities:
			try:
				at = getattr(func, "abilityRunType")
				if at == "EffectOff":
					func(gameEngine, ownPlayer, ownMinion)
			except AttributeError as e:
				pass

	def RunDeathRattles(self, gameEngine, ownPlayer, ownMinion):
		for func in self.abilities:
			at = getattr(func, "abilityType")

			if at == "DeathRattle":
				func(gameEngine, ownPlayer, ownMinion)
