from die import Die
import pygal

#create a six sided die D6
die = Die()

#store the rolling cases in a results list
results = []

for roll_num in range(1000):
	result = die.roll()
	results.append(result)
	
#analyze the result.
#create an empty list to store the values.
frequencies=[]

for value in range(1,die.num_sides+1):
	'''here we loop through the values 1 to 6 in results and count how many times
		each number comes in and then append it to frequency lisy'''
	frequency = results.count(value)
	frequencies.append(frequency)
	
print(results)
print(frequencies)

#visualize the result
hist = pygal.Bar()
hist.title = "Results of rolling a D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Results"
hist.y_title = "Frequeny of results"

'''We use add() to add a series of values to the chart(passing it a label for 
the set of values to be added and a list of the values to appear on the chart)'''
hist.add('D6',frequencies)
hist.render_to_file('die_visuals.svg')
