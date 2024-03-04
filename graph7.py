import matplotlib.pyplot as plt

names = ['A', 'B', 'C']
values = [19, 50, 29]
values_2 = [48, 19, 41]

fig = plt.figure(figsize=(8.0, 6.0))

# adds subplot on position 1
ax = fig.add_subplot(121)
# adds subplot on position 2
ax2 = fig.add_subplot(122)

ax.bar(names, values)
ax2.bar(names, values_2)
plt.show()

