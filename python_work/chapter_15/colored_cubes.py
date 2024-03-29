import matplotlib.pyplot as plt

x_values = range(1, 5000)
y_values = [x ** 3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis)

ax.set_title('Cubes', fontsize=14)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Cubes', fontsize=14)

ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')
plt.show()