from random import randint

class Die():
	'''Create a class representing a single die'''
	
	def __init__(self,num_sides=6):
		'''lets assume it to be a six sided die D6'''
		self.num_sides = num_sides
		
	def roll(self):
		'''return a random value between 1 and the number of sides of a die'''
		return randint(1,self.num_sides)
