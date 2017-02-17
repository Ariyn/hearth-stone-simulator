# card.py

class Card:
	name = ""
	position = "InDeck"
	
	attack, health, coast = 0, 0, 0
	race = None
	
	def __init__(self, name, coast, attack, health, race = "basic"):
		self.name = name
		self.coast, self.attack, self.health = coast, attack, health
		self.race = race
