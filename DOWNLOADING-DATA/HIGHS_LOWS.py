import csv

#get high temperatures from the file
#open the file as file object
filename = "sitka_weather_07-2014.csv"

with open(filename) as f:
	#reader processes the first line of comma-separated values in the file and stores each as an item in a list
	reader = csv.reader(f)
	#next() function returns the next line in the file
	header_row = next(reader)
	
	#read the row one temperatures data.
	highs = []
	for row in reader:
		#convert the extraceted data into int form from the string format by using int() function.
		#we are converting it into int() to read the data for visualization of matplotlib.
		high = int(row[1])
		highs.append(high)
	print(highs)	

	#we use enumerate() function to read the index as well as values in the list.
	for index, column_header in enumerate(header_row):
		print(index, column_header)
		
