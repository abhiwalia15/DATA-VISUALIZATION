import csv
from datetime import datetime
from matplotlib import pyplot as plt

#get dates, high and low temperatures from the file
#open the file as file object
filename = "death_valley_2014.csv"

with open(filename) as f:
	#reader processes the first line of comma-separated values in the file and stores each as an item in a list
	reader = csv.reader(f)
	#next() function returns the next line in the file
	header_row = next(reader)
	
	#read the row one temperatures data.
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			#convert the extraceted data into int form from the string format by using int() function.
			#we are converting it into int() to read the data for visualization of matplotlib.
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			low=int(row[3])
			high = int(row[1])

		except ValueError:
			print(current_date,'missing data')
			
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

	#we use enumerate() function to read the index as well as values in the list.
	for index, column_header in enumerate(header_row):
		print(index, column_header)
		
#plot data
'''set pixels using dpi'''
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
#fill_between() function is used to fill the space between.it takes a series  of x-values and 2 y-values to fill them
#aplha controls the transparecy of the colors(alpha=0 is transparent and aplha=1 is completly opaque)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

#format plot
plt.title("DAILY HIGH AND LOW TEMPERATURES, 2014\nDEATH VALLEY",fontsize=20)
plt.xlabel(' ', fontsize=16)
#this draws the date labels diagonally so that they dont overlap
fig.autofmt_xdate()
plt.ylabel("TEMPERATURE(F)",fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

