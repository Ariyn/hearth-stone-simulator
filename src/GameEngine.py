from copy import copy
import random

from .Minions import *
from .Player import Player

class GameEngine:
	def __init__(self, player1, player2):
		self.players = [player1, player2] # [first attack, late attack]
		self.field = {
			player1.name : [player1.selfCard],
			player2.name : [player2.selfCard]
		}
		self.__initForGame__()
		
		self.turn = 1
		# odd = first attack
		# even = last attack
	
	def __initForGame__(self):
		for p in self.players:
			random.shuffle(p.deck)
			
	def EndTurn(self):
		self.turn += 1
	
	def DrawCard(self, player, amount = 1):
		if self.activeTurn(player):
			for i in range(0,amount):
				card = player.deck.pop()
				player.hand.append(card)
	
	def activeTurn(self, player):
		order = self.players.index(player)
		if self.turn % 2 == order:
			return False
		else:
			return True
		
	def Summon(self, player, minion, location=None, effect=False):
		if self.activeTurn(player) or effect:
			if not location:
				location = len(self.field[player.name])
			cMinion = copy(minion)
			
			cMinion.summonTurn = self.turn
			
			player.Add(cMinion)
			
			self.field[player.name].insert(location, cMinion)
			cMinion.RunBattleCry(self, player, cMinion)
			cMinion.RunEffectOn(self, player, cMinion)
			
			return cMinion
		else:
			return False
	
	def Attack(self, aPlayer, aMinion, dPlayer, dMinion):
		if (aMinion.summonTurn == self.turn and not aMinion.charge) or not self.activeTurn(aPlayer) or aMinion.attack <= 0:
			# can't attack
			pass
		else:
			if dPlayer.taunt == False or (dPlayer.taunt and dMinion.taunt == True):
				# self.Damage(aPlayer, aMinion, dPlayer, dMinion)
				
				dMinion.Damage(aMinion)
				aMinion.Damage(dMinion)
				# result = aMinion.Attack(dMinion)
				
				if aMinion.dead:
					self.Kill(aPlayer, aMinion)
				
				if dMinion.dead:
					self.Kill(dPlayer, dMinion)
		
	def Kill(self, ownPlayer, minion):
		minion.RunDeathRattles(self, ownPlayer, minion)
		minion.RunEffectOff(self, ownPlayer, minion)
		self.field[ownPlayer.name].remove(minion)
	
	def Select(self, ownPlayer, location):
		return self.field[ownPlayer.name][location]
	
	def PrintField(self):
		retVal = []
		for p in self.players:
			strs = "%s(%d/%d) : %s"%(p.name, p.selfCard.attack, p.selfCard.health, " ".join([str(minion) for minion in self.field[p.name][1:]]))
			retVal.append(strs)
		
		return "\n".join(retVal)
	
	def Opponent(self, player):
		return self.players[(self.players.index(player) + 1)%2]
