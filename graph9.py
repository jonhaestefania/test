import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Deliveries By Company')
ax.set_xlabel('Company')
ax.set_ylabel('Shipments')

names = ['Aurrera', 'Soriana', 'Chedraui']
values = [1900, 5000, 2900]
values_2 = [2700, 1500, 3400]

plt.bar(names, values)
plt.show()
