import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
names = ['A', 'B', 'C']
values = [19, 50, 29]
ax.bar(names, values)
plt.show()

