# Implement Decision Tree
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap
#Load the dataset
data=pd.read_csv("Record/Datasets/User_data.csv")
x=data.iloc[:,[2,3]].values
y=data.iloc[:,4].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)
classifier=DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
x1,x2=np.meshgrid(np.arange(start=x_train[:,0].min()-1,stop=x_train[:,0].max()+1,step=0.01),
 np.arange(x_train[:,1].min()-1,x_train[:,1].max()+1,step=0.01))
plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),
 alpha=0.75,cmap=ListedColormap(('red','green')))
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i, j in enumerate(np.unique(y_train)):
    plt.scatter(x_train[y_train==j,0],
    x_train[y_train==j,1],
    c=ListedColormap(('red','green'))(i),label=j)
plt.legend(loc='upper right')
plt.title("Decision Tree Classification (Training Set)")
plt.xlabel("Experience (scaled)")
plt.ylabel("Salary (scaled)")
plt.show()
