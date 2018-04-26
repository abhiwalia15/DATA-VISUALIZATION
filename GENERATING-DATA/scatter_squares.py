import matplotlib.pyplot as plt

#to plot a single point use the scatter function by passing the x,y values in the parameter
#s parameter is used to set the size of the dots.
plt.scatter(2, 4, s=200)

#set the chart title and labels axes.
plt.title("SQUARE NUMBERS",fontsize=24)
plt.xlabel("VALUES",fontsize=14)
plt.ylabel("SQUARES OF VALUES",fontsize=14)

#set size of tick labels.
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()
