import matplotlib.pyplot as plt

company = ['Aurrera', 'Soriana', 'Chedraui']
sales = [900, 500, 350]
sales_2 = [270, 150, 430]

fig = plt.figure(figsize=(8.0, 6.0))

plt.xlabel("Company")
plt.ylabel("Sales")
plt.bar(company, sales)
plt.legend(['Sales'], loc="upper right")
plt.suptitle("Sales plot")
plt.show()
