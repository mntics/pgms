# NumPy Functions on Datasets (Query)
import numpy as np
import pandas as pd
data=pd.read_csv("auto-mpg.csv")
print(data.head(),"\n")
print(data.tail(),"\n")
print(data.info(),"\n")
print(data.describe(),"\n")
print("Size of the dataset:", data.size)
print("Shape of the dataset:", data.shape)
