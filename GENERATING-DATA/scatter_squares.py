import matplotlib.pyplot as plt

#to plot a single point use the scatter function by passing the x,y values in the parameter
#s parameter is used to set the size of the dots.
x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.scatter(x, y, s=100)

#set the chart title and labels axes.
plt.title("SQUARE NUMBERS",fontsize=24)
plt.xlabel("VALUES",fontsize=14)
plt.ylabel("SQUARES OF VALUES",fontsize=14)

#set size of tick labels.
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()
