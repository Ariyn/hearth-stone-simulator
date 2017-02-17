def DeathRattle(f):
	setattr(f, "abilityType", "DeathRattle")
	return f

def EffectOn(f):
	setattr(f, "abilityType", "EffectOn")
	return f

def EffectOff(f):
	setattr(f, "abilityType", "EffectOff")
	return f

def BattleCry(f):
	setattr(f, "abilityType", "BattleCry")
	return f
	
def EffectCheck(*args):
	
	def _effectCheck(f):
		pass
	
	return _effectCheck
	