import csv

#open the file as file object
filename = "sitka_weather_07-2014.csv"

with open(filename) as f:
	#reader processes the first line of comma-separated values in the file and stores each as an item in a list
	reader = csv.reader(f)
	#next() function returns the next line in the file
	header_row = next(reader)
	print(header_row)
	
