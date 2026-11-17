# Data Visualization using python
# 01.Barchart
import matplotlib.pyplot as plt
import pandas as pd
x = ['Grocery', 'Rent', 'Education of Children', 'Medicine', 'Fuel', 'Entertainment','Miscellaneous']
y = [4, 5, 5, 2, 2, 1, 1]
plt.bar(x, y, color='green', edgecolor='blue', linewidth=2)
plt.title("Family Monthly plan")
plt.xlabel('Heads')
plt.ylabel('Expenditure (in thousand rupees)')
plt.show()

# 02.Histogram
import matplotlib.pyplot as plt
x=(22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27)
plt.hist(x, bins=[0,20,40,60,80,100],
color='green', edgecolor='red', linestyle='--')
plt.title("Dataset")
plt.ylabel('Frequency')
plt.xlabel('Total Bill')
plt.show()

# 03. Pie Chart
import matplotlib.pyplot as plt
cars=['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR']
data=[23,13,35,15,12]
explode=[0.1,0.5,0,0,0]
colors=("orange", "cyan", "yellow", "grey","green",)
plt.pie(data, labels=cars, explode=explode, autopct='%.2f%%', colors=colors,
shadow=True)
plt.show()

# 04. Scatter Plot
import matplotlib.pyplot as plt
price = [2.50, 1.23, 4.02, 3.25, 5.00, 4.40]
sales = [34, 62, 49, 22, 13, 19]
plt.scatter(price, sales, c='RED', s=60, marker='D', alpha=1)
plt.title("Dataset")
plt.ylabel('price')
plt.xlabel('sales')
plt.show()

# 05. Line Graph
import matplotlib.pyplot as plt
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]
# First Figure
plt.title('LINE CHART')
fig = plt.figure(figsize=(7, 5), facecolor='g',
 edgecolor='b', linewidth=7)
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y)
plt.xticks(x, labels=["one", "two", "three", "four"])
plt.plot(x, y, color='green', linewidth=3,
 marker='o', markersize=10, linestyle='--')
plt.legend(["GFG"])
# Second Figure
fig = plt.figure(figsize=(12, 4))
ax1 = fig.add_axes([0.05, 0.1, 0.28, 0.8])
ax2 = fig.add_axes([0.36, 0.1, 0.28, 0.8])
ax3 = fig.add_axes([0.67, 0.1, 0.28, 0.8])
# First Graph
ax1.plot(x, y)
# Second Graph
ax2.plot(y, x)
# Third Graph
ax3.plot(y, x)
ax3.set_ylabel('Y-Axis')
ax3.set_xlabel('X-Axis')
ax3.set_ylim(0, 80)
plt.show()
