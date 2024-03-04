import matplotlib.pyplot as plt

sales = [350, 380, 402, 434, 460, 492, 501, 529, 543, 600, 650, 719]

plt.plot(sales)
plt.yscale('log')
plt.show()
