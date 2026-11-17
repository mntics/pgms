# Implement polynomial regression
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
ds=pd.read_csv("Salary.csv")
x=ds.iloc[:,:-1].values
y=ds.iloc[:,1].values
from sklearn.linear_model import LinearRegression
lin_regs=LinearRegression()
lin_regs.fit(x,y)
from sklearn.preprocessing import PolynomialFeatures
poly_regs=PolynomialFeatures(degree=2)
x_poly=poly_regs.fit_transform(x)
lin_regs2=LinearRegression()
lin_regs2.fit(x_poly,y)
plt.scatter(x,y,color='blue')
plt.plot(x,lin_regs.predict(x),color='red')
plt.title("Bluff Detection (Linear Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()
plt.scatter(x,y,color='orange')
plt.plot(x,lin_regs2.predict(poly_regs.fit_transform(x)),color='green')
plt.title("Bluff Detection (Polynomial Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()
