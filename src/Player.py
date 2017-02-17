from .Minion import Minion

class Player:
	def __init__(self, name):
		self.name = name
		self.hand, self.deck = [], []
		self.spellPower, self.spellPowerList = 0, []
		self.taunt = False
		
		self.selfCard = Minion(name, 0, 0, 30, "player")
		
	def AddSpellDamage(self, amount, minion):
		self.spellPower += amount
		self.spellPowerList.append(minion)
	
	def RemoveSpellDamage(self, amount, minion):
		self.spellPower -= amount
		self.spellPowerList.remove(minion)
	
	def Add(self, minion):
		if minion.taunt:
			self.taunt = True

class TempDeckCreator:
	def __init__(self):
		from . import Minions
		self.minions = Minions
	
	def test(self):
		pass
