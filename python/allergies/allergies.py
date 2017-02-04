
class Allergies():
	"""docstring for Allergies"""
	allergies = {
		"eggs": 1,
		"peanuts": 2,
		"shellfish": 4,
		"strawberries": 8,
		"tomatoes": 16,
		"chocolate": 32,
		"pollen": 64,
		"cats": 128
	}

	def __init__(self, score):
		self.score = score
		self.lst = self.build_allergies()

	def is_allergic_to(self, item):
		return item in self.lst

	def build_allergies(self):
		allergic = []
		curr_score = self.score
		inv_allergies = {v: k for k, v in self.allergies.items()}
		while curr_score > 2*max(inv_allergies.keys()):
			curr_score -= 2*max(inv_allergies.keys())
		while curr_score > 0:
			for k in sorted(inv_allergies.items(), reverse=True):
				if curr_score >= k[0]:
					allergic.append(k[1])
					curr_score -= k[0]
		return allergic

