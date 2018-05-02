from die import Die

#create a six sided die D6
die = Die()

#store the rolling cases in a results list
results = []

for roll_num in range(1000):
	result = die.roll()
	results.append(result)
	
#analyze the result.
#create an empt list to store the values.
frequencies=[]

for value in range(1,die.num_sides+1):
	'''here we loop through the values 1 to 6 in results and count how many times
		each number comes in and then append it to frequency lisy'''
	frequency = results.count(value)
	frequencies.append(frequency)
	
print(results)
print(frequencies)
