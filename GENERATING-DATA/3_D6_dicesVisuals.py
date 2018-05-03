
from die import Die
import pygal

#create three D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

#store the rolling cases in a results list
results = []

for roll_num in range(5000):
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)
	
#analyze the result.
#create an empt list to store the values.
frequencies=[]
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides

for value in range(3,max_result+1):
	'''here we loop through the values 1 to 6 in results and count how many times
		each number comes in and then append it to frequency lisy'''
	frequency = results.count(value)
	frequencies.append(frequency)
	
print(frequencies)

#visualize the result
hist = pygal.Bar()

hist.title = "Results of rolling three D6 5000 times"
hist.x_labels = ['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
hist.x_title = "Results"
hist.y_title = "Frequeny of results"

'''We use add() to add a series of values to the chart(passing it a label for 
the set of values to be added and a list of the values to appear on the chart)'''
hist.add('D6+ D6+ D6',frequencies)
hist.render_to_file('three_D6.svg')


