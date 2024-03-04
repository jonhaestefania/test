import matplotlib.pyplot as plt

names = ['Aurrera', 'Soriana', 'Chedraui']
values = [1900, 5000, 29]
values_2 = [2700, 1500, 3400]

plt.xlabel("Company")
plt.ylabel("Shipments")
plt.bar(names, values)
plt.suptitle('Total deliveries by Company')
plt.show()
