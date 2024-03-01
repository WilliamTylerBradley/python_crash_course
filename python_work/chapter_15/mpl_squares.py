import matplotlib.pyplot as plt

input
squares = [x ** 2 for x in range(1, 6)]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()