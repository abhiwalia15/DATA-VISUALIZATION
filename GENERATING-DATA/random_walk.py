from random import choice

class RandomWalk():
	'''a calss to import random walks'''
	def __init__(self,num_points=5000):
		'''initialize attributes of a walk'''
		self.num_points = num_points
		
		#all walk starts at(0,0).
		self.x_values = [0]
		self.y_values = [0]
