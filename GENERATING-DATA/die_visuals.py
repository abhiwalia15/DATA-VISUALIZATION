from die import Die

#create a six sided die D6
die = Die()

#store the rolling cases in a results list
results = []

for roll_num in range(100):
	result = die.roll()
	results.append(result)
	
print(results)
