# Implement Multiple Regression
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
ds=pd.read_csv("Startups.csv")
x=ds.iloc[:,:-1].values
y=ds.iloc[:,-1].values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
le=LabelEncoder()
x[:,2]=le.fit_transform(x[:,2])
onehotencoder=OneHotEncoder()
x=onehotencoder.fit_transform(x).toarray()
print(x)
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(train_x,train_y)
y_pred=regressor.predict(test_x)
print("Training Score:",regressor.score(train_x,train_y))
print("Testing Score:",regressor.score(test_x,test_y))
fig=plt.figure(figsize=(10,5))
plt.scatter(test_y,y_pred)
plt.xlabel("Position Levels")
plt.ylabel("Predicted Values")
plt.title("Linear Regression Model")
plt.plot([min(test_y),max(test_y)],[min(test_y),max(test_y)],linestyle='--',color='blue')
plt.show()
