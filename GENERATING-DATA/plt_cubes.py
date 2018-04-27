import matplotlib.pyplot as plt

x_values = list(range(1,5001))
cubes = [x**3 for x in x_values]

plt.scatter(x_values, cubes, c=cubes, cmap=plt.cm.Blues, edgecolor='none',s=40)

plt.title("CUBES OF NUMBERS",fontsize=24)
plt.xlabel("VALUES",fontsize=14)
plt.ylabel("CUBES OF VALUES",fontsize=14)

plt.savefig('figure_11.png')

