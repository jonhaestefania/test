import matplotlib.pyplot as plt

fig = plt.figure()

names = ['A', 'B', 'C']
values = [19, 50, 29]
values_2 = [48, 19, 41]

ax = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax.bar(names, values)
ax2.bar(names, values_2)
plt.show()
