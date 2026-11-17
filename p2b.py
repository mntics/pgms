#Program to demonstrate Pandas aggregate functions
import pandas as pd
df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=["maths","java","python"])
print(df)
print("the sum of df is:\n",df.sum())
print("the aggregation of df is:\n",df.agg(['min','max','mean','sum',
'count','std','var']))
print("the description of df is:\n",df.describe())
print("the groupby of df is:\n",df.groupby('java').first())
