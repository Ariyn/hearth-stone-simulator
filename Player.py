class Player:
	def __init__(self, name):
		self.name = name
		self.spellPower, self.spellPowerList = 0, []
		self.deck = []
		self.character = 0
		
	def AddSpellDamage(self, amount, minion):
		self.spellPower += amount
		self.spellPowerList.append(minion)
	
	def RemoveSpellDamage(self, amount, minion):
		self.spellPower -= amount
		self.spellPowerList.remove(minion)
		
		