import matplotlib.pyplot as plt

from random_walk import RandomWalk

#make a random walk and plot the points
#keep making a new walk as long as the program is active
while True:
	rw = RandomWalk()
	rw.fill_walk()
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
	
	#emphasize the first and the last walk
	plt.scatter(0, 0, c='green', edgecolor='none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)
	
	#remove the axes
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()
	
	keep_running = input("MAKE ANOTHER WALK?(y/n)")
	if keep_running == 'n':
		break
