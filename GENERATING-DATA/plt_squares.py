#just provide matplot with a number and it will do the rest.

import matplotlib.pyplot as plt
#pyplot contains a number of functions that help generate charts and plots.

#store the numbers in a list.
squares = [1,4,9,16,25]

#linewidth parameter controls the thickness fo the line
plt.plot(squares,linewidth=5)

#set chart labels and labels axes
plt.title("SQUARE NUMBERS",fontsize=24)
plt.xlabel("VALUES",fontsize=14)
plt.ylabel("SQUARE OF VALUES",fontsize=14)

#set size of tick labels.
plt.tick_params(axis='both',labelsize=14)

plt.show()
