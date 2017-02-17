import unittest
from src.Minions import *
from src.GameEngine import GameEngine
from src.Player import Player, TempDeckCreator

class test_Player(unittest.TestCase):
	def setUp(self):
		self.t = TempDeckCreator()
		self.deck = []
		
	def test_tdc(self):
		for i in range(0, 30):
			self.deck.append(MagmaRager)
		
		print(len(self.deck), self.deck)
		
	def tearDown(self):
		pass
		
# if __name__ == '__main__':
# 	unittest.main()