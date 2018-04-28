import matplotlib.pyplot as plt

#to plot a single point use the scatter function by passing the x,y values in the parameter
#s parameter is used to set the size of the dots.
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
#c parameter gives the color.RGB values from 0 to 1,Colors closer to 0 produce dark color and close to 1 produce light color.
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none', s=10)

#set the chart title and labels axes.
plt.title("SQUARE NUMBERS",fontsize=24)
plt.xlabel("VALUES",fontsize=14)
plt.ylabel("SQUARES OF VALUES",fontsize=14)

#set the range for each axis.Here axis()function takes 2 parameters min and max points of x&y-axis.
plt.axis([0,1100,0,1100000])

#set size of tick labels.
plt.tick_params(axis='both',which='major',labelsize=14)

#savefig()function will directly save the image .first parameter is the name of the file and second parameter trims the extra whitespace from the plot.
plt.savefig('figure_10.png',bbox_inches='tight')
