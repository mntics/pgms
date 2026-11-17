# NumPy Functions on Datasets (Aggregate functions)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
iris=pd.read_csv("iris.csv")
print(iris)
#Plot scatter by comparing
fig=iris[iris['species']=='setosa'].plot.scatter(
 x='petal_length',
 y='petal_width',
 color='orange',
 label='Setosa'
)
iris[iris['species']=='versicolor'].plot.scatter(
 x='petal_length',
 y='petal_width',
 color='blue',
 label='Versicolor',
 ax=fig
)
iris[iris['species']=='virginica'].plot.scatter(
 x='petal_length',
 y='petal_width',
 color='green',
 label='Virginica',
 ax=fig
)
fig.set_xlabel("petal_length")
fig.set_ylabel("petal_width")
fig.set_title("petal length and width")
fig=plt.gcf()
fig.set_size_inches(8,8)
plt.show()
#To display all data whose values ==1.4
petal_width=iris[iris['petal_length']==1.4]
print("Rows where petal_length == 1.4:\n", petal_width)

#To known the how many times each value in petal length is given
count=iris.groupby('petal_length')['petal_length'].count()
print("Count of each petal_length value:\n", count)

#To find the sum of petal length column
sum=iris['petal_length'].sum()
print("Sum of petal_length column:\n", sum)

#To known the max size of sepal width column
max=iris['sepal_width'].max()
print("Maximum sepal width:\n", max)

#To add 1.0 to all the inputs in sepal length column
add=iris['sepal_length']+1.0
print("Added 1.0 to sepal_length:\n", add)
