import unittest

from src.Minions import *
from src.GameEngine import GameEngine
from src.Player import Player

sampleDeck1 = [MagmaRager for i in range(0, 30)]
sampleDeck2 = [MagmaRager for i in range(0, 30)]

class test_GE(unittest.TestCase):
	def setUp(self):
		self.p1 = Player("test1")
		self.p1.deck = sampleDeck1
		
		self.p2 = Player("test2")
		self.p2.deck = sampleDeck2
		
		self.ge = GameEngine(self.p1, self.p2)
		
		print("\n\n",self._testMethodName)
	
	def test_drawhand(self):
		self.ge.DrawCard(self.p1, amount=3)
		print(self.p1.hand)
		
	def test_summon(self):
		self.ge.Summon(self.p1, MagmaRager)
		self.ge.EndTurn()
		
		self.ge.Summon(self.p2, MagmaRager)
		self.ge.Summon(self.p2, SavannahHighmane)
		
		str = self.ge.PrintField()
		self.assertEqual("test1(0/30) : MagmaRager(3|5/1)\ntest2(0/30) : MagmaRager(3|5/1) Savannah Highmane(6|6/5)", str)
	
	def test_kill(self):
		mr = self.ge.Summon(self.p1, MagmaRager)
		self.ge.EndTurn()
		self.ge.Summon(self.p2, MagmaRager)
		
		sh = self.ge.Summon(self.p2, SavannahHighmane)
		self.ge.EndTurn()
		
		# print(self.turn)
		self.ge.Attack(self.p1, mr, self.p2, sh)
		
		str = self.ge.PrintField()
		self.assertEqual("test1(0/30) : \ntest2(0/30) : MagmaRager(3|5/1) Hyena(2|2/2) Hyena(2|2/2)", str)
		
	def test_spell(self):
		b_before = self.p1.spellPower
		
		ar = self.ge.Summon(self.p1, Archmage)
		self.ge.EndTurn()
		
		mr1 = self.ge.Summon(self.p2, MagmaRager)
		mr2 = self.ge.Summon(self.p2, MagmaRager)
		
		self.ge.EndTurn()
		self.ge.EndTurn()
		
		before = self.p1.spellPower
		
		self.ge.Attack(self.p2, mr1, self.p1, ar)
		self.ge.Attack(self.p2, mr2, self.p1, ar)
		
		after = self.p1.spellPower
		self.assertEqual((b_before, before, after), (0, 1, 0))
	
	def test_charge(self):
		mr = self.ge.Summon(self.p1, MagmaRager)
		
		str = self.ge.PrintField()
		print(str,"\n")
		
		self.ge.EndTurn()
		bw = self.ge.Summon(self.p2, BluegillWarrior)

		str = self.ge.PrintField()
		print(str,"\n")
		
		self.ge.Attack(self.p2, bw, self.p1, mr)
		
		str = self.ge.PrintField()
		# self.assertEqual("test1 : \ntest2 : MagmaRager(3|5/1) Hyena(2|2/2) Hyena(2|2/2)", str)
	
	def test_attackheart(self):
		mr = self.ge.Summon(self.p1, MagmaRager)
		self.ge.EndTurn()
		self.ge.EndTurn()
		self.ge.Attack(self.p1, mr, self.p2, self.p2.selfCard)
	
	def test_summondragon(self):
		self.ge.Summon(self.p1, DragonlingMechanic)
		
	def test_sylbanas(self):
		sw = self.ge.Summon(self.p1, SylvanasWindrunner)
		self.ge.EndTurn()
		
		mr = self.ge.Summon(self.p2, MagmaRager)
		self.ge.Summon(self.p2, MagmaRager)
		self.ge.EndTurn()
		
		d = self.ge.PrintField()
		print(d, "\n")
		
		self.ge.Attack(self.p1, sw, self.p2, mr)
	
	def test_voidwalker(self):
		vw = self.ge.Summon(self.p1, Voidwalker)
		mr1= self.ge.Summon(self.p1, MagmaRager)
		self.ge.EndTurn()
		
		mr = self.ge.Summon(self.p2, MagmaRager)
		self.ge.EndTurn()
		self.ge.EndTurn()
		
		self.ge.Attack(self.p2, mr, self.p1, mr1)
		self.tearDown()
		
		self.ge.Attack(self.p2, mr, self.p1, vw)
		# self.assertEqual(self.p1.taunt, True)
		
	def tearDown(self):
		d = self.ge.PrintField()
		print(d)
		
# if __name__ == '__main__':
# 	unittest.main()