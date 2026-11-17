# Functions on Iris Dataset
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r"iris.csv")
data.columns=['sepal_length','sepal_width','petal_length','petal_width','species']

#First 5 rows of the data
print(data.head())

from pandas.api.types import is_numeric_dtype
#Check if the column is numeric
for column in data.columns:
    if is_numeric_dtype(data[column]):
        print('%s' % column)
        print('\t Mean: %0.3f' %data[column].mean())
        print('\t Standard Deviation: %0.3f' %data[column].std())
        print('\t Minimum: %0.3f' %data[column].min())
        print('\t Maximum: %0.3f' %data[column].max())

#numeric columns selection and covariance matrix calculation
numeric_columns = data.select_dtypes(include=['number']).columns
covariance_matrix = data[numeric_columns].cov()
print(covariance_matrix)
data['sepal_length'].hist(bins=8)
data.boxplot()
plt.show()
