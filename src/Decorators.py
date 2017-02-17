def DeathRattle(f):
	setattr(f, "abilityType", "DeathRattle")
	return f

# INFO:
# Effect run 7 situations
# 1. beginning of game - BG
# 2. when draw new card - DC
# 3. when start new turn - NT
# 4. when kill minion - KM
# 5. when summon new card - SC
# 6. always while card alive - CA
# 7. when card damaged - CD

def Effect(type):
	def _effect(f):
		setattr(f, "abilityType", "Effect")
		setattr(f, "EffectSituation", type)
		return f

	return _effect

def EffectOn(f):
	setattr(f, "abilityRunType", "EffectOn")
	return f

def EffectOff(f):
	setattr(f, "abilityRunType", "EffectOff")
	return f

def BattleCry(f):
	setattr(f, "abilityType", "BattleCry")
	return f

def EffectCheck(*args):

	def _effectCheck(f):
		pass

	return _effectCheck
